#!/usr/bin/env python3
# Copyright (c) 2026 American Mathematical Society. All rights reserved.
"""Prepare native Verso HTML for reading, retaining alignment in a JSON sidecar.

This is a publishing step, not a replacement for Lean elaboration. Statements
come from Verso's checked docstring blocks; reviewed explanations are inserted
beside exact prose anchors. The transformation fails if those anchors drift.
"""

from __future__ import annotations

import argparse
import copy
from dataclasses import dataclass, field
from html import escape
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import shutil
import subprocess
from urllib.parse import quote


VOID = frozenset("area base br col embed hr img input link meta param source track wbr".split())
SCAN_BLANK_ITEMS = frozenset({"Frontmatter/BlankPage1", "Frontmatter/BlankPage2"})
CITATION = re.compile(r"book-ref=([^;\]\s]+); role=(primary|supporting)")
GENERIC = re.compile(
    r"\bauxiliary\b"
    r"|\b(?:associated|displayed) (?:predicate|type|value)\b", re.I
)


@dataclass
class Element:
    tag: str
    attrs: dict[str, str | None] = field(default_factory=dict)
    children: list[Element | str] = field(default_factory=list)

    def walk(self):
        yield self
        for child in self.children:
            if isinstance(child, Element):
                yield from child.walk()

    def has_class(self, name: str) -> bool:
        return name in (self.attrs.get("class") or "").split()

    def text(self) -> str:
        return "".join(child.text() if isinstance(child, Element) else child for child in self.children)

    def html(self) -> str:
        body = "".join(
            child.html() if isinstance(child, Element)
            else child if self.tag in {"script", "style"}
            else escape(child, quote=False)
            for child in self.children
        )
        if not self.tag:
            return body
        attrs = "".join(
            f" {key}" if value is None else f' {key}="{escape(value, quote=True)}"'
            for key, value in self.attrs.items()
        )
        return f"<{self.tag}{attrs}>" + ("" if self.tag in VOID else body + f"</{self.tag}>")


class DocumentParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = Element("")
        self.stack = [self.root]

    def handle_starttag(self, tag, attrs):
        node = Element(tag, dict(attrs))
        self.stack[-1].children.append(node)
        if tag not in VOID:
            self.stack.append(node)

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in VOID:
            self.handle_endtag(tag)

    def handle_endtag(self, tag):
        for index in range(len(self.stack) - 1, 0, -1):
            if self.stack[index].tag == tag:
                self.stack = self.stack[:index]
                break

    def handle_data(self, data):
        self.stack[-1].children.append(data)


def parse(value: str) -> Element:
    parser = DocumentParser()
    parser.feed(value)
    return parser.root


def el(tag: str, *children, **attrs) -> Element:
    return Element(tag, {key.rstrip("_").replace("_", "-"): str(value) for key, value in attrs.items()}, list(children))


def section_id(node: Element) -> str:
    if node.tag != "section":
        return ""
    return next((child.attrs.get("id") or "" for child in node.children
                 if isinstance(child, Element) and child.tag in {"h1", "h2", "h3", "h4", "h5", "h6"}), "")


def normalized(value: str) -> str:
    return " ".join(value.split())


def repeated_section_header_ids(xref: dict) -> set[str]:
    """Identify transcribed running headers that repeat an enclosing section.

    Require both a generated body-heading tag and an exact ancestor title;
    similarly numbered but genuinely different mathematical headings stay.
    The page transcription and generated Lean are not altered.
    """
    result = set()
    sections = xref.get("Verso.Genre.Manual.section", {}).get("contents", {})
    for entries in sections.values():
        for entry in entries:
            identifier = entry.get("id", "")
            data = entry.get("data") or {}
            title = normalized(data.get("title", ""))
            if not re.search(r"___heading-\d+$", identifier):
                continue
            if not re.match(r"\d+(?:\.\d+)*[.:]\s", title):
                continue
            if any(normalized(ancestor.get("title", "")) == title
                   for ancestor in data.get("context", [])[:-1]):
                result.add(identifier)
    return result


def suppress_repeated_section_headers(document: Element, identifiers: set[str]) -> int:
    main = next(node for node in document.walk() if node.tag == "main")
    before = reading_prose(document)
    count = 0
    for node in list(main.walk()):
        if node.tag in {"h1", "h2", "h3", "h4", "h5", "h6"} and node.attrs.get("id") in identifiers:
            replace(main, node, el("span", id=node.attrs["id"], aria_hidden="true"))
            count += 1
    if before != reading_prose(document):
        raise ValueError("running-header suppression changed book paragraphs")
    return count


def remove(root: Element, target: Element) -> bool:
    for node in root.walk():
        for index, child in enumerate(node.children):
            if child is target:
                del node.children[index]
                return True
    return False


def replace(root: Element, target: Element, replacement: Element):
    for node in root.walk():
        for index, child in enumerate(node.children):
            if child is target:
                node.children[index] = replacement
                return
    raise ValueError("element is not in the document")


def declaration_name(card: Element) -> str:
    signature = next(node for node in card.walk() if node.has_class("signature"))
    for node in signature.walk():
        binding = node.attrs.get("data-binding") or ""
        if binding.startswith("const-"):
            return binding.removeprefix("const-")
    return (card.attrs.get("id") or "").replace("___", ".")


def doc_prose(card: Element) -> str:
    text = next((node for node in card.walk() if node.has_class("text")), None)
    if text is None:
        return ""
    return " ".join(
        normalized(node.text()) for node in text.walk()
        if node.tag == "p" and not CITATION.search(node.text())
    )


def remove_citations(card: Element):
    for node in list(card.walk()):
        if node.tag == "li" and CITATION.search(node.text()):
            remove(card, node)
    for node in list(card.walk()):
        if node.tag in {"ul", "ol"} and not node.text().strip():
            remove(card, node)


def card_citations(card: Element) -> list[tuple[str, str]]:
    # Verso embeds constructor/field documentation inside a structure's card.
    # Those declarations have their own citations, not additional associations
    # on the enclosing structure. Their separate cards supply their records.
    def own_text(node: Element) -> str:
        if node is not card and node.has_class("docstring-section"):
            return ""
        return "".join(own_text(child) if isinstance(child, Element) else child
                       for child in node.children)
    return CITATION.findall(own_text(card))


def extract_alignment(document: Element) -> list[dict]:
    rows = []
    for card in document.walk():
        if card.has_class("namedocs"):
            for reference, role in card_citations(card):
                rows.append(dict(declaration=declaration_name(card), reference=reference, role=role, imported=False))
    imported_name = None
    for node in document.walk():
        if node.tag != "p":
            continue
        value = normalized(node.text())
        if value.startswith("Declaration: "):
            imported_name = value.removeprefix("Declaration: ")
        elif value.startswith("Alignment metadata:") and imported_name:
            for reference, role in CITATION.findall(value):
                rows.append(dict(declaration=imported_name, reference=reference, role=role, imported=True))
    return rows


def source_link(name: str, revision: str, sources: dict[str, str]) -> str:
    key = name if name in sources else next((key for key in sorted(sources, key=len, reverse=True)
                                             if name.startswith(key + ".")), None)
    if key is not None:
        module = sources[key].replace(".", "/") + ".lean"
        return f"https://github.com/mathlib-initiative/EtingofRepresentationTheory/blob/{revision}/{module}"
    if not name.startswith("RepresentationTheory."):
        # The bare query selects the finder's machine-data view, whose link
        # field can be absent. Human readers need its documentation view.
        return "https://leanprover-community.github.io/mathlib4_docs/find/?pattern=" + quote(name, safe="") + "#doc"
    return "https://github.com/mathlib-initiative/EtingofRepresentationTheory/search?q=" + quote(name, safe="")


def add_footnotes(document: Element) -> int:
    notes = [node for node in document.walk() if node.has_class("footnote") and node.tag == "details"]
    if not notes:
        return 0
    content = next(node for node in document.walk() if node.tag == "main")
    listing = el("ol")
    for number, note in enumerate(notes, 1):
        body = [child for child in note.children if not isinstance(child, Element) or child.tag != "summary"]
        note_id, ref_id = f"footnote-{number}", f"footnote-ref-{number}"
        reference = el("sup", el("a", str(number), href="#" + note_id, id=ref_id,
                                 aria_label=f"Footnote {number}"), class_="footnote-reference")
        replace(document, note, reference)
        listing.children.append(el("li", el("div", *body, class_="footnote-body"),
                                   el("a", "↩", href="#" + ref_id, aria_label="Return to text"), id=note_id))
    block = el("section", el("h2", "Notes"), listing, class_="reader-footnotes", aria_label="Footnotes")
    # The note body is outside all prose paragraphs, including on narrow screens.
    # A checked structure's fields are sections too. They are not book
    # sections: placing Notes after the last one would hide the footnotes
    # inside a collapsed Lean statement.
    book_sections = []
    def visit(node: Element):
        if any(node.has_class(name) for name in ("lean-annotation", "namedocs", "lean-reference")):
            return
        if node.tag == "section":
            book_sections.append(node)
        for child in node.children:
            if isinstance(child, Element):
                visit(child)
    visit(content)
    if not book_sections:
        content.children.append(block)
        return len(notes)
    last_section = book_sections[-1]
    for parent in content.walk():
        if any(child is last_section for child in parent.children):
            index = next(i for i, child in enumerate(parent.children) if child is last_section)
            parent.children.insert(index + 1, block)
            break
    return len(notes)


def reading_prose(document: Element) -> list[str]:
    """Book paragraphs, displayed mathematics, and tables, excluding navigation."""
    main = next(node for node in document.walk() if node.tag == "main")
    result = []
    def visit(node: Element):
        if node.tag == "nav" or any(node.has_class(name) for name in (
                "namedocs", "lean-annotation", "lean-reference", "reader-footnotes", "split-toc")):
            return
        if section_id(node).endswith("___formalization"):
            return
        if node.tag in {"p", "table"} or (node.has_class("math") and node.has_class("display")):
            # Footnotes are compared separately, so moving them cannot alter prose.
            value = copy.deepcopy(node)
            for note in list(value.walk()):
                if note.has_class("footnote") or note.has_class("footnote-reference"):
                    remove(value, note)
            result.append(normalized(value.text()))
            return
        for child in node.children:
            if isinstance(child, Element):
                visit(child)
    visit(main)
    return result


def printed_contents_key(text: str) -> str | None:
    chapter = re.match(r"Chapter (\d+)\.", text)
    if chapter:
        return f"chapter-{int(chapter[1]):02d}"
    section = re.match(r"§(\d+)\.(\d+)\.", text)
    if section:
        return f"chapter-{int(section[1]):02d}/section-{section[1]}-{section[2]}"
    for title, key in (("References for historical interludes", "Backmatter/ReferencesHistorical"),
                       ("Mathematical references", "Backmatter/MathematicalReferences")):
        if text.startswith(title + " —"):
            return key
    return None


def link_printed_contents(document: Element, destinations: dict[str, str]) -> int:
    """Make the original contents useful without changing labels or print folios."""
    before = reading_prose(document)
    main = next(node for node in document.walk() if node.tag == "main")
    linked = 0
    for node in list(main.walk()):
        if node.tag != "p":
            continue
        key = printed_contents_key(normalized(node.text()))
        if key is None:
            continue
        if key not in destinations:
            raise ValueError(f"printed contents has no reading destination: {key}")
        if any(child.tag == "a" for child in node.walk()):
            raise ValueError("printed contents entry already contains a link")
        node.children = [el("a", *node.children, href=destinations[key],
                            class_="reader-contents-link")]
        linked += 1
    if reading_prose(document) != before:
        raise ValueError("linking the printed contents changed its text")
    heading = next(node for node in main.walk() if node.tag == "h1")
    for parent in main.walk():
        if any(child is heading for child in parent.children):
            parent.children.insert(parent.children.index(heading) + 1,
                el("nav", el("p", "Choose a chapter or section below. Page numbers refer to the printed book."),
                   class_="reader-contents-note", aria_label="About the contents"))
            break
    return linked


def contents_reading_destinations(root: Path, sections: dict, items: list[dict]) -> dict[str, str]:
    """Use actual retained prose, including body-heading pages, not empty wrappers."""
    pages = {}
    result = {}
    keys = {item["node_id"] for item in items if item["node_id"].startswith("chapter-")}
    keys.update(key.split("/")[0] for key in list(keys))
    keys.update({"Backmatter/ReferencesHistorical", "Backmatter/MathematicalReferences"})
    for key in sorted(keys):
        candidates = [item for item in items if item["id"] == key or
                      item["node_id"] == key or item["node_id"].startswith(key + "/")]
        for item in sorted(candidates, key=lambda item: item["order"]):
            identifier = (item["node_id"] if item.get("verso_projection", {}).get("structure_only")
                          else item["id"]).replace("/", "___").replace(".", "___")
            references = [identifier] + sorted(k for k in sections if k.startswith(identifier + "___heading-"))
            for reference in references:
                for entry in sections.get(reference, []):
                    address = entry["address"].lstrip("/")
                    if address not in pages:
                        path = root / address / "index.html"
                        pages[address] = parse(path.read_text()) if path.exists() else None
                    page = pages[address]
                    if page is not None and reading_prose(page) and any(
                            node.attrs.get("id") == entry["id"] for node in page.walk()):
                        result[key] = address + "#" + entry["id"]
                        break
                if key in result:
                    break
            if key in result:
                break
    return result


def annotation_node(annotation: dict, cards: dict[str, Element], revision: str, sources: dict) -> Element:
    kicker = "FORMALIZATION STATUS" if annotation.get("kind") == "coverage_gap" else "IN LEAN"
    block = el("aside", el("p", kicker, class_="annotation-kicker"),
               el("h2", annotation["title"]), class_="lean-annotation")
    for paragraph in annotation["explanation"]:
        block.children.append(el("p", *parse(paragraph).children))
    if annotation.get("lean"):
        block.children.append(el("pre", el("code", annotation["lean"], class_="language-lean")))
    for selected in annotation.get("declarations", []):
        name = selected["name"]
        if name not in cards:
            raise ValueError(f"reviewed declaration not found in the rendered item: {name}")
        card = copy.deepcopy(cards[name])
        remove_citations(card)
        if selected.get("documentation"):
            text = next((node for node in card.walk() if node.has_class("text")), None)
            if text is not None:
                # Structure fields live inside the documentation container.
                # Rewording the parent description must not discard their
                # checked signatures or descriptions.
                fields = [child for child in text.children
                          if isinstance(child, Element) and child.has_class("docstring-section")]
                text.children = [el("p", selected["documentation"]), *fields]
        # The existing Lean identifier is retained in the exact signature, not
        # rewritten into a different constant that was never checked by Lean.
        for node in list(card.walk()):
            if node.has_class("permalink-widget"):
                remove(card, node)
        detail = el("details", el("summary", selected["label"]), card,
                    el("p", el("a", "Inspect definition or proof", href=source_link(name, revision, sources))),
                    class_="lean-statement")
        block.children.append(detail)
    for link in annotation.get("links", []):
        block.children.append(el("p", el("a", link["label"], href=source_link(link["name"], revision, sources))))
    return block


def insert_annotations(item_id: str, item: Element, annotations: list[dict],
                       cards: dict[str, Element], revision: str, sources: dict) -> int:
    last_inserted = {}
    for annotation in annotations:
        anchor = annotation["after"]
        anchor_kind = annotation.get("anchor_kind", "paragraph")
        if anchor_kind not in {"paragraph", "table", "list", "math"}:
            raise ValueError(f"unknown reader anchor kind: {anchor_kind!r}")
        anchor_tags = {"paragraph": {"p"}, "table": {"table"}, "list": {"ul", "ol"},
                       "math": set()}[anchor_kind]
        prose_nodes = []
        def visit(node: Element):
            if node.has_class("lean-annotation") or node.has_class("namedocs"):
                return
            if node.tag in anchor_tags or (anchor_kind == "math"
                    and node.has_class("math") and node.has_class("display")):
                prose_nodes.append(node)
            for child in node.children:
                if isinstance(child, Element):
                    visit(child)
        visit(item)
        matches = [node for node in prose_nodes
                   if normalized(node.text()).startswith(anchor)]
        if len(matches) != 1:
            raise ValueError(f"expected one prose anchor for {item_id}: {anchor!r}; found {len(matches)}")
        target = matches[0]
        if anchor_kind == "math":
            # Native Verso wraps a displayed formula in its own paragraph.
            # An aside inside that paragraph is invalid HTML and also changes
            # the paragraph's contents. Attach after the complete wrapper.
            parent = next(node for node in item.walk()
                          if any(child is target for child in node.children))
            if parent.tag == "p":
                displays = [node for node in parent.walk()
                            if node.has_class("math") and node.has_class("display")]
                if len(displays) != 1 or normalized(parent.text()) != normalized(target.text()):
                    raise ValueError(f"math anchor does not occupy a complete paragraph: {item_id}")
                target = parent
        insertion_target = last_inserted.get(id(target), target)
        for parent in item.walk():
            if any(child is insertion_target for child in parent.children):
                index = next(i for i, child in enumerate(parent.children) if child is insertion_target)
                block = annotation_node(annotation, cards, revision, sources)
                parent.children.insert(index + 1, block)
                last_inserted[id(target)] = block
                break
    return len(annotations)


def prepare_document(document: Element, annotations: dict, revision: str, sources: dict,
                     page_items: tuple[str, ...] = (),
                     book_prose_only: frozenset[str] = frozenset()) -> tuple[list[dict], int, int]:
    before = reading_prose(document)
    notes_before = [normalized(node.text().split("]", 1)[-1]) for node in document.walk()
                    if node.tag == "details" and node.has_class("footnote")]
    panel_nodes = [node for node in document.walk() if section_id(node).endswith("___formalization")]
    ledger = []
    inserted = 0
    processed = set()
    for panel in panel_nodes:
        panel_id = section_id(panel).removesuffix("___formalization")
        references = [ref for ref, _ in CITATION.findall(panel.text())]
        item_id = next((ref for ref in references if ref.replace("/", "___").replace(".", "___") == panel_id), None)
        if item_id is None:
            item_id = next((ref.rsplit("/", 1)[0] for ref in references
                            if ref.rsplit("/", 1)[0].replace("/", "___").replace(".", "___") == panel_id), None)
        if item_id is None:
            raise ValueError(f"cannot identify panel {panel_id}")
        item = next((node for node in document.walk() if section_id(node) == panel_id), None)
        if item is None:
            raise ValueError(f"formalization panel lacks an owning item: {item_id}")
        cards = {declaration_name(node): node for node in panel.walk() if node.has_class("namedocs")}
        for name, card in cards.items():
            for reference, role in card_citations(card):
                ledger.append(dict(declaration=name, reference=reference, role=role, imported=False))
        imported_name = None
        for node in panel.walk():
            if node.tag != "p":
                continue
            text = normalized(node.text())
            if text.startswith("Declaration: "):
                imported_name = text.removeprefix("Declaration: ")
            elif text.startswith("Alignment metadata:") and imported_name:
                for reference, role in CITATION.findall(text):
                    ledger.append(dict(declaration=imported_name, reference=reference, role=role, imported=True))
        reviewed = annotations.get(item_id, [])
        if reviewed:
            inserted += insert_annotations(item_id, item, reviewed, cards, revision, sources)
        processed.add(item_id)
        replacement = el("div", class_="lean-reference")
        if not reviewed and item_id not in book_prose_only:
            useful = []
            for name, card in cards.items():
                prose = doc_prose(card)
                primary = any(reference == item_id and role == "primary"
                              for reference, role in CITATION.findall(card.text()))
                if primary and prose and not GENERIC.search(prose) and "auxiliaryElided" not in name:
                    useful.append((name, card))
            if useful:
                replacement.children.append(el("h2", "Lean statements"))
                for name, card in useful:
                    remove_citations(card)
                    text = next(node for node in card.walk() if node.has_class("text"))
                    description = next(normalized(node.text()) for node in text.walk() if node.tag == "p")
                    if len(description) > 180:
                        description = description[:177].rsplit(" ", 1)[0] + "…"
                    replacement.children.append(el("details", el("summary", description), card,
                        el("p", el("a", "Inspect definition or proof", href=source_link(name, revision, sources))),
                        class_="lean-statement"))
        names = sorted(set(cards) | {row["declaration"] for row in ledger
                                    if row["reference"] == item_id or row["reference"].startswith(item_id + "/")})
        if names and item_id not in book_prose_only:
            listing = el("ul")
            for name in names:
                listing.children.append(el("li", el("a", el("code", name), href=source_link(name, revision, sources))))
            replacement.children.append(el("details", el("summary", f"Definitions and proof dependencies ({len(names)})"),
                                           listing, class_="implementation-references"))
        replace(item, panel, replacement)
    # Background discussions may have no alignment panel at all. Their explicit
    # coverage notes still belong beside the prose, without implying a proof.
    for item_id, reviewed in annotations.items():
        if item_id in processed:
            continue
        identifier = item_id.replace("/", "___").replace(".", "___")
        item = next((node for node in document.walk() if section_id(node) == identifier), None)
        if item is None and item_id in page_items:
            # Structure-only chapter introductions live directly in main.
            # Their route is established by the native xref, not a guessed
            # prose match on every page. Native split pages may omit the tag.
            item = next(node for node in document.walk() if node.tag == "main")
        if item is not None:
            inserted += insert_annotations(item_id, item, reviewed, {}, revision, sources)
    note_count = add_footnotes(document)
    after = reading_prose(document)
    # Book paragraphs are untouched; technical paragraphs are not book prose.
    def book_only(values):
        return [value for value in values if not value.startswith(("Inspect definition or proof", "Definitions and proof dependencies"))]
    if book_only(before) != book_only(after):
        raise ValueError("reader preparation changed original book paragraphs")
    notes_after = [normalized(node.text()) for node in document.walk() if node.has_class("footnote-body")]
    if notes_before != notes_after:
        raise ValueError("reader preparation changed a footnote body")
    head = next(node for node in document.walk() if node.tag == "head")
    head.children.append(el("link", rel="stylesheet", href="reader.css"))
    head.children.append(el("script", src="reader.js", defer=""))
    # A document title and its first content heading refer to the same item.
    main = next(node for node in document.walk() if node.tag == "main")
    headings = [node for node in main.walk() if node.tag in {"h1", "h2"}]
    if len(headings) > 1 and normalized(headings[0].text()) == normalized(headings[1].text()):
        # Keep the original content anchor on the visible title.
        if headings[1].attrs.get("id"):
            headings[0].attrs["id"] = headings[1].attrs["id"]
        remove(main, headings[1])
    return ledger, note_count, inserted


def flatten_routes(root: Path) -> dict[str, str]:
    # Old renders have a document title plus an identically titled subsection.
    # Merge the leaf into its wrapper; preserve old URLs as redirect pages.
    routes = {}
    for page in sorted(root.rglob("index.html")):
        if "Formalization" in page.relative_to(root).parts:
            parts = page.relative_to(root).parts
            index = parts.index("Formalization")
            routes[page.relative_to(root).as_posix().removesuffix("index.html")] = "/".join(parts[:index]) + "/"
            continue
        if page.parent.name == page.parent.parent.name:
            target = page.parent.parent / "index.html"
            if target.exists():
                old = page.relative_to(root).as_posix().removesuffix("index.html")
                new = target.relative_to(root).as_posix().removesuffix("index.html")
                routes[old] = new
    return routes


def join_reader_documents(head: Element, tail: Element, record: dict) -> None:
    """Reunite an explicitly reviewed page-break seam without rewriting prose."""
    before_head, before_tail = reading_prose(head), reading_prose(tail)
    if not before_head or not before_tail or not before_head[-1].endswith(record["head_ends"]) \
            or not before_tail[0].startswith(record["tail_starts"]):
        raise ValueError("reader continuation does not match its reviewed sentence boundary")
    head_id = record["head"].replace("/", "___").replace(".", "___")
    tail_id = record["tail"].replace("/", "___").replace(".", "___")
    head_main = next(node for node in head.walk() if node.tag == "main")
    tail_main = next(node for node in tail.walk() if node.tag == "main")
    head_section = next(node for node in head_main.walk() if section_id(node) == head_id)
    tail_section = next(node for node in tail_main.walk() if section_id(node) == tail_id)
    # Only original paragraphs qualify: never attach a continuation to a note.
    def paragraphs(section):
        result = []
        def visit(node):
            if any(node.has_class(cls) for cls in ("lean-annotation", "lean-reference", "namedocs")):
                return
            if node.tag == "p":
                result.append(node)
                return
            for child in node.children:
                if isinstance(child, Element):
                    visit(child)
        visit(section)
        return result
    last, first = paragraphs(head_section)[-1], paragraphs(tail_section)[0]
    if normalized(last.text()) != before_head[-1] or normalized(first.text()) != before_tail[0]:
        raise ValueError("reader continuation is not a pair of original paragraphs")
    last.children.extend([" ", *copy.deepcopy(first.children)])
    remove(tail_section, first)
    heading = next(node for node in tail_section.children
                   if isinstance(node, Element) and node.attrs.get("id") == tail_id)
    replace(tail_section, heading, el("span", id=tail_id, aria_hidden="true"))
    # A conversion panel at the page seam must not interrupt the reunited proof.
    references = [child for child in head_section.children
                  if isinstance(child, Element) and child.has_class("lean-reference")]
    for reference in references:
        head_section.children.remove(reference)
    head_section.children.append(tail_section)
    head_section.children.extend(references)
    # Retain the continuation's wrapper bookmarks and skip its former page in
    # previous/next navigation. The global route rewrite updates incoming links.
    for child in tail_main.children:
        if isinstance(child, Element) and child.tag == "span" and child.attrs.get("id"):
            head_main.children.append(copy.deepcopy(child))
    following = next((node for node in tail_main.walk() if node.tag == "a"
                      and node.attrs.get("rel") == "next"), None)
    for node in list(head_main.walk()):
        if node.tag == "a" and node.attrs.get("rel") == "next":
            if following is None:
                remove(head_main, node)
            else:
                node.attrs = dict(following.attrs)
                node.children = copy.deepcopy(following.children)
    expected = [*before_head[:-1], normalized(before_head[-1] + " " + before_tail[0]), *before_tail[1:]]
    if reading_prose(head) != expected:
        raise ValueError("joining reader pages changed or reordered original prose")


def consolidate_reader_references(section: Element) -> int:
    """Joined passages need one optional dependency list, not repeated footers."""
    references = []
    for node in section.walk():
        if not node.has_class("lean-reference"):
            continue
        content = [child for child in node.children
                   if (isinstance(child, Element)
                       and not (child.tag == "span" and child.attrs.get("aria-hidden") == "true"))
                   or (isinstance(child, str) and child.strip())]
        if len(content) == 1 and isinstance(content[0], Element) \
                and content[0].has_class("implementation-references"):
            references.append(node)
    if len(references) < 2:
        return 0
    before = reading_prose(parse("<main>" + section.html() + "</main>"))
    old_ids = {node.attrs["id"] for reference in references for node in reference.walk()
               if node.attrs.get("id")}
    entries = {}
    for reference in references:
        listing = next(node for node in reference.walk() if node.tag == "ul")
        for entry in listing.children:
            if not isinstance(entry, Element) or entry.tag != "li":
                continue
            links = tuple(node.attrs.get("href") for node in entry.walk() if node.tag == "a")
            entries.setdefault((normalized(entry.text()), links), entry)
    first = references[0]
    first.children = [el("details",
                         el("summary", f"Definitions and proof dependencies ({len(entries)})"),
                         el("ul", *entries.values()), class_="implementation-references")]
    for reference in references[1:]:
        remove(section, reference)
    retained_ids = {node.attrs["id"] for node in section.walk() if node.attrs.get("id")}
    for identifier in sorted(old_ids - retained_ids):
        first.children.append(el("span", id=identifier, aria_hidden="true"))
    if reading_prose(parse("<main>" + section.html() + "</main>")) != before:
        raise ValueError("dependency consolidation changed original reading prose")
    return len(references) - 1


def join_reader_blocks(head: Element, tail: Element, record: dict) -> None:
    """Restore a reviewed block/list continuation without rewriting sentences."""
    before_head, before_tail = reading_prose(head), reading_prose(tail)
    if not before_head or not before_tail or not before_head[-1].endswith(record["head_ends"]) \
            or not before_tail[0].startswith(record["tail_starts"]):
        raise ValueError("reader block continuation does not match its reviewed boundary")
    head_id = record["head"].replace("/", "___").replace(".", "___")
    tail_id = record["tail"].replace("/", "___").replace(".", "___")
    head_main = next(node for node in head.walk() if node.tag == "main")
    tail_main = next(node for node in tail.walk() if node.tag == "main")
    head_section = next(node for node in head_main.walk() if section_id(node) == head_id)
    tail_section = next(node for node in tail_main.walk() if section_id(node) == tail_id)
    heading = next(node for node in tail_section.children
                   if isinstance(node, Element) and node.attrs.get("id") == tail_id)
    bookmark = el("span", id=tail_id, aria_hidden="true")
    replace(tail_section, heading, bookmark)
    # Native nesting varies: a prepared Notes block can be inside the item
    # section or beside it. Detach both forms before moving the continuation,
    # then place the complete note after the reunited reading content.
    footnotes_to_move = []
    for main in (head_main, tail_main):
        notes = [node for node in main.walk() if node.has_class("reader-footnotes")]
        for footnotes in notes:
            remove(main, footnotes)
        footnotes_to_move.extend(notes)
    if record.get("merge_lists"):
        def original_lists(section):
            result = []
            def visit(node):
                if any(node.has_class(cls) for cls in (
                        "lean-annotation", "lean-reference", "namedocs", "reader-footnotes")):
                    return
                if node.tag in {"ul", "ol"}:
                    result.append(node)
                    return
                for child in node.children:
                    if isinstance(child, Element):
                        visit(child)
            visit(section)
            return result
        def labels(listing):
            return [normalized(next(node for node in child.walk() if node.tag == "p").text())
                    for child in listing.children if isinstance(child, Element) and child.tag == "li"]
        head_lists, tail_lists = original_lists(head_section), original_lists(tail_section)
        if not head_lists or not tail_lists:
            raise ValueError("reader list continuation lacks its original lists")
        first, second = head_lists[-1], tail_lists[0]
        if first.tag != second.tag or labels(first) != record["head_list"] \
                or labels(second) != record["tail_list"]:
            raise ValueError("reader list continuation differs from its reviewed labels")
        remove(tail_section, bookmark)
        first_tail_item = next(child for child in second.children
                               if isinstance(child, Element) and child.tag == "li")
        first_tail_item.children.insert(0, bookmark)
        first.children.extend(second.children)
        remove(tail_section, second)
    references = [node for node in head_section.walk() if node.has_class("lean-reference")]
    for reference in references:
        remove(head_section, reference)
    head_section.children.append(tail_section)
    head_section.children.extend(references)
    consolidate_reader_references(head_section)
    for child in tail_main.children:
        if isinstance(child, Element) and child.tag == "span" and child.attrs.get("id"):
            head_main.children.append(copy.deepcopy(child))
    # Carry the entire body and return link, not just the reference marker.
    container = next((node for node in head_main.walk() if node.has_class("content-wrapper")), head_main)
    for footnotes in footnotes_to_move:
        existing_ids = {node.attrs["id"] for node in head_main.walk() if node.attrs.get("id")}
        note_ids = {node.attrs["id"] for node in footnotes.walk() if node.attrs.get("id")}
        if existing_ids & note_ids:
            raise ValueError("reader block continuation would duplicate footnote bookmarks")
        # Verso has navigation both above and below the reading section.
        # Inserting before the first nav puts the note before the book itself.
        index = 1 + max((i for i, child in enumerate(container.children)
                         if isinstance(child, Element) and child.tag == "section"),
                        default=len(container.children) - 1)
        container.children.insert(index, copy.deepcopy(footnotes))
    following = next((node for node in tail_main.walk() if node.tag == "a"
                      and node.attrs.get("rel") == "next"), None)
    for node in list(head_main.walk()):
        if node.tag == "a" and node.attrs.get("rel") == "next":
            if following is None:
                remove(head_main, node)
            else:
                node.attrs = dict(following.attrs)
                node.children = copy.deepcopy(following.children)
    if reading_prose(head) != before_head + before_tail:
        raise ValueError("joining reader blocks changed or reordered original prose or mathematics")


def relocate_reader_footnote(head: Element, tail: Element, record: dict, route: str = "") -> None:
    """Restore a reviewed page-footer note, including its checked explanation."""
    before = reading_prose(head)
    tail_prose = reading_prose(tail)
    marker = record["marker"]
    if len(tail_prose) != 1 or not tail_prose[0].startswith(record["tail_starts"]):
        raise ValueError("reader footnote does not match its reviewed original body")
    references = [node for node in head.walk() if node.tag == "code"
                  and node.has_class("math") and normalized(node.text()) == marker]
    if len(references) != 1:
        raise ValueError("reader footnote lacks a unique reference marker")
    main = next(node for node in head.walk() if node.tag == "main")
    tail_main = next(node for node in tail.walk() if node.tag == "main")
    identifier = record["tail"].replace("/", "___").replace(".", "___")
    section = next(node for node in tail_main.walk() if section_id(node) == identifier)
    paragraph = next(node for node in section.walk() if node.tag == "p"
                     and normalized(node.text()) == tail_prose[0])
    prefix = next((node for node in paragraph.walk() if node.tag == "code"
                   and node.has_class("math") and normalized(node.text()) == marker), None)
    if prefix is None or not normalized(paragraph.text()).startswith(marker):
        raise ValueError("reader footnote lacks its original number prefix")
    remove(paragraph, prefix)
    original_body = normalized(tail_prose[0].removeprefix(marker))
    if normalized(paragraph.text()) != original_body:
        raise ValueError("reader footnote body changed during relocation")
    heading = next(node for node in section.children
                   if isinstance(node, Element) and node.attrs.get("id") == identifier)
    replace(section, heading, el("span", id=identifier, aria_hidden="true"))
    note_id, ref_id = "footnote-" + identifier, "footnote-ref-" + identifier
    reference = el("sup", el("a", record["number"], href=route + "#" + note_id,
                               id=ref_id, aria_label="Footnote " + record["number"]),
                   class_="footnote-reference")
    replace(head, references[0], reference)
    block = el("section", el("h2", "Notes"), el("ol", el("li",
        el("div", section, class_="footnote-body"),
        el("a", "↩", href=route + "#" + ref_id, aria_label="Return to text"),
        id=note_id, value=record["number"])),
        class_="reader-footnotes", aria_label="Footnotes")
    container = next((node for node in main.walk() if node.has_class("content-wrapper")), main)
    last_section = max((index for index, child in enumerate(container.children)
                        if isinstance(child, Element) and child.tag == "section"),
                       default=len(container.children) - 1)
    container.children.insert(last_section + 1, block)
    for child in tail_main.children:
        if isinstance(child, Element) and child.tag == "span" and child.attrs.get("id"):
            main.children.append(copy.deepcopy(child))
    expected = [normalized(text.replace(marker, "", 1)) for text in before]
    if sum(text.count(marker) for text in before) != 1 or reading_prose(head) != expected:
        raise ValueError("reader footnote relocation changed original body prose")


def join_reader_pages(root: Path, joins_file: Path, routes: dict[str, str]) -> dict[str, str]:
    if not joins_file.exists():
        return {}
    sections = json.loads((root / "xref.json").read_text())["Verso.Genre.Manual.section"]["contents"]
    redirects = {}
    used = set()
    used_heads = set()
    for record in json.loads(joins_file.read_text()):
        kind = record.get("kind")
        if kind not in {None, "footnote", "blocks"}:
            raise ValueError("unknown reader continuation kind")
        destinations = []
        for item in (record["head"], record["tail"]):
            repeat_head = (item == record["head"] and item in used_heads
                           and kind in {"footnote", "blocks"})
            if item in used and not repeat_head:
                raise ValueError("overlapping reader continuation records")
            used.add(item)
            key = item.replace("/", "___").replace(".", "___")
            values = {entry["address"].lstrip("/") for entry in sections[key]}
            if len(values) != 1:
                raise ValueError("reader continuation lacks a unique reading route")
            route = values.pop()
            destinations.append(routes.get(route, route))
        used_heads.add(record["head"])
        head_route, tail_route = destinations
        if head_route == tail_route:
            raise ValueError("reader continuation already shares a page")
        head_path, tail_path = (root / route / "index.html" for route in destinations)
        head, tail = parse(head_path.read_text()), parse(tail_path.read_text())
        if record.get("kind") == "footnote":
            relocate_reader_footnote(head, tail, record, head_route)
        elif record.get("kind") == "blocks":
            join_reader_blocks(head, tail, record)
        else:
            join_reader_documents(head, tail, record)
        head_path.write_text("<!DOCTYPE html>\n" + head.html(), encoding="utf-8")
        redirects[tail_route] = head_route
        for old, new in routes.items():
            if new == tail_route:
                redirects[old] = head_route
    return redirects


def preserve_legacy_routes(root: Path, legacy_file: Path) -> dict[str, str]:
    """Resolve saved reading URLs by stable section tags, not generated titles."""
    if not legacy_file.exists():
        return {}
    legacy = json.loads(legacy_file.read_text(encoding="utf-8"))
    sections = json.loads((root / "xref.json").read_text(encoding="utf-8"))["Verso.Genre.Manual.section"]["contents"]
    redirects = {}
    for old, record in legacy["routes"].items():
        entries = sections.get(record["key"], [])
        destinations = {entry["address"].lstrip("/") for entry in entries}
        if len(destinations) != 1:
            raise ValueError(f"legacy reading URL lacks a unique current section: {old}")
        new = destinations.pop()
        for route in (old, new):
            if route.startswith("/") or ".." in Path(route).parts:
                raise ValueError(f"unsafe legacy reading route: {route}")
        destination = root / new / "index.html"
        if not destination.is_file():
            raise ValueError(f"legacy reading URL's destination is missing: {old} -> {new}")
        document = parse(destination.read_text(encoding="utf-8"))
        main = next(node for node in document.walk() if node.tag == "main")
        ids = {node.attrs.get("id") for node in document.walk()}
        for anchor in sorted(set(record["anchors"]) - ids):
            main.children.insert(0, el("span", id=anchor, aria_hidden="true"))
        destination.write_text("<!DOCTYPE html>\n" + document.html(), encoding="utf-8")
        if old == new:
            continue
        previous = root / old / "index.html"
        if previous.is_file() and '<title>Page moved</title>' not in previous.read_text(encoding="utf-8"):
            raise ValueError(f"legacy URL would overwrite a current reading page: {old}")
        previous.parent.mkdir(parents=True, exist_ok=True)
        target = "../" * len(Path(old).parts) + new
        previous.write_text(
            '<!DOCTYPE html><html><head><meta charset="utf-8"><title>Page moved</title>'
            f'<script>location.replace({json.dumps(target)} + location.search + location.hash);</script>'
            f'<meta http-equiv="refresh" content="0;url={escape(target, quote=True)}"></head>'
            f'<body><a href="{escape(target, quote=True)}">Read this page</a></body></html>',
            encoding="utf-8")
        redirects[old] = new
    return redirects


def resolve_declaration_links(root: Path, xref: dict, revision: str, sources: dict) -> dict:
    """Link to real documentation, never an invisible substitute for a card.

    Editorial notes retain only selected checked statements. Native Verso links
    still refer to the removed inventory, including its embedded find-page map.
    Prefer a retained card anywhere in the book; otherwise use the definition's
    source. Section/bookmark aliases are handled separately.
    """
    pages = {}
    retained = {}
    for page in sorted(root.rglob("*.html")):
        value = page.read_text(encoding="utf-8")
        if '<title>Page moved</title>' in value:
            continue
        document = parse(value)
        pages[page] = document
        route = page.relative_to(root).as_posix().removesuffix("index.html")
        for node in document.walk():
            if node.has_class("namedocs") and node.attrs.get("id"):
                name = declaration_name(node)
                retained.setdefault(name, ("/" + route, node.attrs["id"]))
    contents = xref.get("Verso.Genre.Manual.doc", {}).get("contents", {})
    external = 0
    for name in list(contents):
        if name == "[anonymous]":
            # Anonymous constructor entries have no stable declaration name.
            # Do not advertise destinations for documentation we removed.
            contents[name] = [entry for entry in contents[name]
                              if any(address == entry["address"] and anchor == entry["id"]
                                     for address, anchor in retained.values())]
            if not contents[name]:
                del contents[name]
            continue
        if name in retained:
            address, anchor = retained[name]
            contents[name] = [dict(address=address, id=anchor, data=None)]
        else:
            contents[name] = [dict(address=source_link(name, revision, sources), id="", data=None)]
            external += 1
    rewritten = 0
    for page, document in pages.items():
        changed = False
        for node in document.walk():
            if node.tag != "a":
                continue
            href = node.attrs.get("href") or ""
            if href.startswith(("https:", "http:", "mailto:")):
                continue
            name = next(((child.attrs.get("data-binding") or "").removeprefix("const-")
                         for child in node.walk()
                         if (child.attrs.get("data-binding") or "").startswith("const-")), None)
            if name is None:
                continue
            if name in retained:
                address, anchor = retained[name]
                target = address.lstrip("/") + "#" + anchor
                title = "Checked statement for " + name
            else:
                target = source_link(name, revision, sources)
                title = "Definition or proof of " + name
            if href != target or node.attrs.get("title") != title:
                node.attrs.update(href=target, title=title)
                changed = True
                rewritten += 1
        # find/ embeds its own xref snapshot; changing xref.json alone leaves
        # saved permalinks and searches pointing at the discarded inventory.
        for node in document.walk():
            if node.tag != "script":
                continue
            script = node.text()
            match = re.search(r"window\.xref\s*=\s*", script)
            if match:
                _, end = json.JSONDecoder().raw_decode(script[match.end():])
                encoded = json.dumps(xref).replace("</", "<\\/")
                node.children = [script[:match.end()] + encoded + script[match.end() + end:]]
                changed = True
        if changed:
            page.write_text("<!DOCTYPE html>\n" + document.html(), encoding="utf-8")
    return dict(retained_declarations=len(retained), source_destinations=external,
                rewritten_declaration_links=rewritten)


def repair_search_link_resolution(root: Path):
    """Native semantic search assumes every destination is inside the book."""
    path = root / "-verso-search" / "search-box.js"
    if not path.exists():
        return
    value = path.read_text(encoding="utf-8")
    marker = "export const resolveAgainstBase = (dest) => {"
    if value.count(marker) != 1:
        raise ValueError("Verso search destination resolver changed")
    value = value.replace(marker, marker + '\n    if (/^https?:\\/\\//i.test(dest)) return dest;', 1)
    path.write_text(value, encoding="utf-8")


def prepare(root: Path, annotations_file: Path, revision: str, sources: dict[str, str]) -> dict:
    root = root.resolve()
    if (root / "reader-report.json").exists():
        raise ValueError("reader preparation requires fresh native HTML, not already prepared output")
    annotations = json.loads(annotations_file.read_text(encoding="utf-8"))
    from reader_review import audit
    editorial_review = audit(metadata=annotations_file.parent, emit=False)
    reviews = json.loads(annotations_file.with_name("reader-reviews.json").read_text(encoding="utf-8"))
    book_prose_only = frozenset(key for key, review in reviews.items()
                               if review["decision"] == "book_prose_only")
    xref_path = root / "xref.json"
    native_xref = json.loads(xref_path.read_text(encoding="utf-8")) if xref_path.exists() else {}
    structure_items = {}
    sections = native_xref.get("Verso.Genre.Manual.section", {}).get("contents", {})
    metadata_items = json.loads(annotations_file.with_name("items.json").read_text(encoding="utf-8"))["items"]
    for item in metadata_items:
        if not item.get("verso_projection", {}).get("structure_only"):
            continue
        identifier = item["node_id"].replace("/", "___").replace(".", "___")
        for entry in sections.get(identifier, []):
            route = entry["address"].lstrip("/")
            structure_items.setdefault(route, []).append(item["id"])
    running_headers = repeated_section_header_ids(native_xref)
    routes = flatten_routes(root)
    scan_routes = {entry["address"].lstrip("/") for item in SCAN_BLANK_ITEMS
                   for entry in sections.get(item.replace("/", "___"), [])}
    scan_routes.update(routes.get(route, route) for route in list(scan_routes))
    navigation = {}
    for page in root.rglob("index.html"):
        route = page.relative_to(root).as_posix().removesuffix("index.html")
        document = parse(page.read_text(encoding="utf-8"))
        navigation[route] = {direction: next((node for node in document.walk()
                                            if node.tag == "a" and node.attrs.get("rel") == direction), None)
                             for direction in ("prev", "next")}
    documents = {}
    ledger = {}
    notes = inserted = suppressed_headers = 0
    for page in sorted(root.rglob("*.html")):
        route = page.relative_to(root).as_posix().removesuffix("index.html")
        document = parse(page.read_text(encoding="utf-8"))
        for row in extract_alignment(document):
            ledger[(row["declaration"], row["reference"], row["role"])] = row
        if "Formalization" in page.relative_to(root).parts:
            continue  # Implementation records are not independent reading destinations.
        if route in {new for old, new in routes.items() if "Formalization/" not in old}:
            continue  # Empty title wrapper is replaced with the real item page.
        entries, n, a = prepare_document(document, annotations, revision, sources,
                                         tuple(structure_items.get(route, ())), book_prose_only)
        suppressed_headers += suppress_repeated_section_headers(document, running_headers)
        notes += n
        inserted += a
        for row in entries:
            key = (row["declaration"], row["reference"], row["role"])
            ledger[key] = row
        destination = root / (routes.get(route, route) + "index.html") if page.name == "index.html" else page
        destination_route = destination.relative_to(root).as_posix().removesuffix("index.html")
        # Previous/next should follow book prose, not the removed wrapper and
        # inventory pages (which otherwise create self-navigation loops).
        for node in list(document.walk()):
            direction = node.attrs.get("rel")
            if node.tag != "a" or direction not in {"prev", "next"}:
                continue
            seen = set()
            candidate = node
            while candidate is not None:
                target = (candidate.attrs.get("href") or "").split("#")[0].removesuffix("index.html")
                if routes.get(target, target) != destination_route and "Formalization/" not in target \
                        and target.lstrip("/") not in scan_routes:
                    break
                if target in seen:
                    candidate = None
                    break
                seen.add(target)
                candidate = navigation.get(target, {}).get(direction)
            if candidate is None:
                remove(document, node)
            elif candidate is not node:
                node.attrs = dict(candidate.attrs)
                node.children = copy.deepcopy(candidate.children)
        base = next((node for node in document.walk() if node.tag == "base"), None)
        if base:
            depth = len(destination.relative_to(root).parts) - 1
            base.attrs["href"] = "../" * depth or "./"
        # Remove technical destinations from all native navigation lists.
        technical_titles = {"Formalization", "Primary declarations", "Supporting declarations"}
        for node in list(document.walk()):
            if node.tag in {"li", "tr"}:
                links = [child for child in node.walk() if child.tag == "a"]
                if links and (normalized(links[0].text()) in technical_titles
                              or (links[0].attrs.get("href") or "").split("#")[0].lstrip("/") in scan_routes
                              or (links[0].attrs.get("href") or "").split("#")[-1] in running_headers):
                    remove(document, node)
            if node.has_class("split-toc"):
                title = next((child for child in node.children if isinstance(child, Element) and child.has_class("title")), None)
                links = [] if title is None else [child for child in title.walk() if child.tag == "a"]
                if links and (normalized(links[0].text()) in technical_titles or
                              (links[0].attrs.get("href") or "").split("#")[0].lstrip("/") in scan_routes):
                    remove(document, node)
        for node in document.walk():
            for attr in ("href", "src"):
                value = node.attrs.get(attr)
                if value and attr == "href" and value.startswith("#"):
                    prefix = "./" if node.attrs.get("rel") in {"prev", "next"} else destination_route
                    node.attrs[attr] = prefix + value
                    continue
                if not value or value.startswith(("https:", "http:", "mailto:", "data:")):
                    continue
                for old, new in routes.items():
                    if value == old or value.startswith(old + "#") or value == old + "index.html":
                        node.attrs[attr] = new + value[len(old):]
                        break
        navigation_tables = {id(child) for parent in document.walk() if parent.has_class("split-toc")
                             for child in parent.walk() if child.tag == "table"}
        for node in list(document.walk()):
            if node.has_class("split-toc"):
                title = next((child for child in node.children if isinstance(child, Element) and child.has_class("title")), None)
                links = [] if title is None else [child for child in title.walk() if child.tag == "a"]
                if links and (links[0].attrs.get("href") or "").split("#")[0] == destination_route:
                    remove(document, node)
            if node.tag == "table" and id(node) in navigation_tables:
                seen = set()
                for row in list(node.walk()):
                    if row.tag != "tr":
                        continue
                    link = next((child for child in row.walk() if child.tag == "a"), None)
                    if link is None:
                        continue
                    key = ((link.attrs.get("href") or "").split("#")[0], normalized(link.text()))
                    if key in seen:
                        remove(node, row)
                    seen.add(key)
        # Generated wrapper anchors still occur in saved links and xref.json.
        if route in routes:
            wrapper = parse((root / routes[route] / "index.html").read_text(encoding="utf-8"))
            wrapper_main = next(node for node in wrapper.walk() if node.tag == "main")
            from urllib.parse import parse_qs, urlparse
            wrapper_names = [parse_qs(urlparse(node.attrs.get("href") or "").query).get("name", [None])[0]
                             for node in wrapper_main.walk() if node.tag == "a" and node.attrs.get("title") == "Permalink"]
            main = next(node for node in document.walk() if node.tag == "main")
            for name in wrapper_names:
                if name:
                    main.children.insert(0, el("span", id=name, aria_hidden="true"))
        documents[destination] = "<!DOCTYPE html>\n" + document.html()
    expected_annotations = sum(len(notes) for notes in annotations.values())
    if inserted != expected_annotations:
        raise ValueError(f"reader preparation omitted or duplicated annotations: "
                         f"expected {expected_annotations}, inserted {inserted}")
    for destination, value in documents.items():
        destination.write_text(value, encoding="utf-8")
    joins_file = annotations_file.with_name("reader-joins.json")
    join_records = json.loads(joins_file.read_text()) if joins_file.exists() else []
    relocated_notes = [record for record in join_records if record.get("kind") == "footnote"]
    hidden_records = [record for record in join_records
                      if record.get("kind") == "footnote" or record.get("hide_navigation")]
    hidden_join_routes = set()
    for record in hidden_records:
        key = record["tail"].replace("/", "___").replace(".", "___")
        for entry in sections[key]:
            old = entry["address"].lstrip("/")
            hidden_join_routes.update((old, routes.get(old, old)))
    joined_routes = join_reader_pages(root, joins_file, routes)
    notes += len(relocated_notes)
    routes.update(joined_routes)
    # Joining happens after per-item integrity/annotation checks. Rewrite
    # incoming reading and navigation links as well as the xref/search maps.
    if joined_routes:
        for page in root.rglob("*.html"):
            document = parse(page.read_text(encoding="utf-8"))
            for toc in list(document.walk()):
                if toc.attrs.get("id") != "toc" and not toc.has_class("split-toc"):
                    continue
                for row in list(toc.walk()):
                    if row.tag == "tr" and any(node.tag == "a" and
                            (node.attrs.get("href") or "").split("#", 1)[0] in hidden_join_routes
                            for node in row.walk()):
                        remove(toc, row)
            for node in document.walk():
                value = node.attrs.get("href")
                if not value:
                    continue
                for old, new in joined_routes.items():
                    if value == old or value.startswith(old + "#") or value == old + "index.html":
                        node.attrs["href"] = new + value[len(old):]
                        break
            page.write_text("<!DOCTYPE html>\n" + document.html(), encoding="utf-8")
    for old, new in routes.items():
        depth = len(Path(old).parts)
        # Relative target keeps the Pages repository prefix and the old anchor.
        target = "../" * depth + new
        redirect = (
            '<!DOCTYPE html><html><head><meta charset="utf-8"><title>Page moved</title>'
            f'<script>location.replace({json.dumps(target)} + location.search + location.hash);</script>'
            f'<meta http-equiv="refresh" content="0;url={escape(target, quote=True)}"></head>'
            f'<body><a href="{escape(target, quote=True)}">Read this page</a></body></html>'
        )
        (root / old / "index.html").write_text(redirect, encoding="utf-8")
    # Native Verso search and cross-reference maps must use the corrected routes.
    for pattern in ("*.json", "*.js"):
        for path in root.rglob(pattern):
            value = path.read_text(encoding="utf-8")
            for old, new in sorted(routes.items(), key=lambda pair: -len(pair[0])):
                value = value.replace(old, new)
            path.write_text(value, encoding="utf-8")
    xref = root / "xref.json"
    contents_links = 0
    if xref.exists():
        data = json.loads(xref.read_text(encoding="utf-8"))
        aliases = {}
        for domain_name, domain in data.items():
            if domain_name == "Verso.Genre.Manual.doc":
                continue  # Removed declaration cards must not acquire ghost anchors.
            contents = domain.get("contents", {})
            for key in list(contents):
                for entry in contents[key]:
                    address = entry["address"].lstrip("/")
                    aliases.setdefault(address, set()).add(entry["id"])
        sections = data.get("Verso.Genre.Manual.section", {}).get("contents", {})
        for record in hidden_records:
            key = record["tail"].replace("/", "___").replace(".", "___")
            for entry in sections[key]:
                entry["data"]["readerHidden"] = True
        grouped = {}
        for key, values in sections.items():
            entry = values[0]
            if entry["address"].lstrip("/") in scan_routes:
                entry["data"].update(readerHidden=True, readerScanMarker=True)
            if entry["data"].get("title") in {"Formalization", "Primary declarations", "Supporting declarations"}:
                entry["data"]["readerHidden"] = True
            if entry["id"] in running_headers:
                entry["data"]["readerHidden"] = True
            group = (entry["address"], entry["data"].get("title"))
            grouped.setdefault(group, []).append((key, entry))
        for group in grouped.values():
            if len(group) > 1:
                preferred = next((key for key, entry in group if not key.startswith("Introduction-to-Representation-Theory--")), group[0][0])
                for key, entry in group:
                    if key != preferred:
                        entry["data"]["readerHidden"] = True
        definition_links = resolve_declaration_links(root, data, revision, sources)
        xref.write_text(json.dumps(data) + "\n", encoding="utf-8")
        # Native split pages omit some of their own section anchors. Retain
        # every published xref destination, including old title-wrapper links.
        for address, ids in aliases.items():
            page = root / address / "index.html"
            if not page.exists() or page not in documents:
                continue
            document = parse(page.read_text(encoding="utf-8"))
            existing = {node.attrs.get("id") for node in document.walk()}
            main = next(node for node in document.walk() if node.tag == "main")
            for anchor in sorted(ids - existing):
                main.children.insert(0, el("span", id=anchor, aria_hidden="true"))
            page.write_text("<!DOCTYPE html>\n" + document.html(), encoding="utf-8")
        contents_entries = sections.get("Frontmatter___TableOfContents", [])
        if contents_entries:
            page = root / contents_entries[0]["address"].lstrip("/") / "index.html"
            document = parse(page.read_text())
            destinations = contents_reading_destinations(root, sections, metadata_items)
            contents_links = link_printed_contents(document, destinations)
            if contents_links != 105:
                raise ValueError(f"expected 105 printed contents links, found {contents_links}")
            page.write_text("<!DOCTYPE html>\n" + document.html(), encoding="utf-8")
        else:
            contents_links = 0
    search = root / "-verso-search"
    repair_search_link_resolution(root)
    if (search / "searchIndex.js").exists():
        subprocess.run(["node", str(Path(__file__).with_name("prepare_reader_search.js")), str(search)], check=True)
    entries = sorted(ledger.values(), key=lambda row: (row["reference"], row["role"], row["declaration"]))
    (root / "alignment.json").write_text(json.dumps(entries, indent=2) + "\n", encoding="utf-8")
    shutil.copyfile(annotations_file.with_name("reader.css"), root / "reader.css")
    shutil.copyfile(annotations_file.with_name("reader.js"), root / "reader.js")
    legacy_routes = preserve_legacy_routes(root, annotations_file.with_name("reader-legacy-routes.json"))
    report = dict(redirects=len(set(routes) | set(legacy_routes)), legacy_title_redirects=len(legacy_routes),
                  joined_reading_pages=len(joined_routes),
                  suppressed_running_headers=suppressed_headers,
                  printed_contents_links=contents_links, skipped_scan_pages=len(SCAN_BLANK_ITEMS),
                  alignment_entries=len(entries), footnotes=notes,
                  reviewed_annotations=inserted, reviewed_items=editorial_review["reviewed_items"],
                  presentation_checks="passed", editorial_review=editorial_review,
                  definition_links=definition_links if xref.exists() else {},
                  status="passed" if editorial_review["status"] == "complete" else "editorial_review_incomplete")
    (root / "reader-report.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("html_root", type=Path)
    parser.add_argument("--formalization-revision", default="752fe269b3233f08f0795aa4bcdc5b4c84be7a50")
    parser.add_argument("--declarations", type=Path)
    parser.add_argument("--alignment-export", type=Path,
                        help="require the reader ledger to match the checked Lean export exactly")
    args = parser.parse_args()
    metadata = Path(__file__).resolve().parent.parent / "metadata"
    sources = json.loads((metadata / "declaration-sources.json").read_text(encoding="utf-8"))
    if args.declarations:
        for line in args.declarations.read_text(encoding="utf-8").splitlines():
            row = json.loads(line)
            sources[row["new_fqn"]] = row["new_module"]
    config = metadata / "reader-annotations.json"
    report = prepare(args.html_root, config, args.formalization_revision, sources)
    if args.alignment_export:
        expected = json.loads(args.alignment_export.read_text(encoding="utf-8"))
        actual = json.loads((args.html_root / "alignment.json").read_text(encoding="utf-8"))
        key = lambda row: (row["declaration"], row["reference"], row["role"], row["imported"])
        expected_keys, actual_keys = {key(row) for row in expected}, {key(row) for row in actual}
        if expected_keys != actual_keys:
            raise ValueError(f"rendered alignment differs from Lean: missing={sorted(expected_keys - actual_keys)}; "
                             f"extra={sorted(actual_keys - expected_keys)}")
    print(json.dumps(report, sort_keys=True))


if __name__ == "__main__":
    main()
