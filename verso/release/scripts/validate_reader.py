#!/usr/bin/env python3
"""Check that publication contains a reading edition, not alignment dumps."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from urllib.parse import urlsplit

from prepare_reader import parse, normalized


def is_machine_mathlib_find_link(address: str) -> bool:
    url = urlsplit(address)
    return (url.netloc == "leanprover-community.github.io"
            and url.path.rstrip("/") == "/mathlib4_docs/find"
            and url.fragment not in {"doc", "src"})


def validate(root: Path, require_complete: bool = False) -> dict:
    ledger = json.loads((root / "alignment.json").read_text(encoding="utf-8"))
    report = json.loads((root / "reader-report.json").read_text(encoding="utf-8"))
    errors = []
    if require_complete and report.get("editorial_review", {}).get("status") != "complete":
        errors.append("full-book editorial review is incomplete or absent")
    annotations = notes = redirects = 0
    retained_targets = set()
    for path in sorted(root.rglob("*.html")):
        value = path.read_text(encoding="utf-8")
        if "location.replace(" in value and "<title>Page moved</title>" in value:
            redirects += 1
            continue
        document = parse(value)
        main = next((node for node in document.walk() if node.tag == "main"), None)
        if main is None:
            errors.append(f"missing main content: {path.relative_to(root)}")
            continue
        if "book-ref=" in value or "Alignment metadata:" in value:
            errors.append(f"alignment records leaked into HTML: {path.relative_to(root)}")
        if "end IntroductionToRepresentationTheoryVerso." in value:
            errors.append(f"Lean command leaked into HTML: {path.relative_to(root)}")
        for node in document.walk():
            if node.tag == "a" and is_machine_mathlib_find_link(node.attrs.get("href") or ""):
                errors.append(f"Mathlib link selects machine data instead of documentation: {path.relative_to(root)}")
            if node.has_class("namedocs") and node.attrs.get("id"):
                retained_targets.add(("/" + path.relative_to(root).as_posix().removesuffix("index.html"),
                                      node.attrs["id"]))
            if node.tag == "a" and node.attrs.get("rel") in {"prev", "next"}:
                route = (node.attrs.get("href") or "").split("#")[0].removesuffix("index.html")
                current = path.relative_to(root).as_posix().removesuffix("index.html")
                if route == current or "Formalization/" in route:
                    errors.append(f"previous/next does not follow book prose: {path.relative_to(root)}")
            if node.has_class("lean-annotation"):
                annotations += 1
            if node.has_class("lean-statement") and any(
                    child.has_class("reader-footnotes") for child in node.walk()):
                errors.append(f"book footnotes hidden inside a Lean statement: {path.relative_to(root)}")
            if node.has_class("footnote-body"):
                notes += 1
            if node.tag == "details" and node.has_class("footnote"):
                errors.append(f"old invalid folding footnote: {path.relative_to(root)}")
            if node.tag == "a" and node.attrs.get("aria-label", "").startswith(("Footnote", "Return to text")):
                href = node.attrs.get("href") or ""
                route, anchor = href.split("#", 1)
                expected = path.relative_to(root).as_posix().removesuffix("index.html")
                if route != expected:
                    errors.append(f"footnote leaves its page: {path.relative_to(root)}")
                if not any(other.attrs.get("id") == anchor for other in document.walk()):
                    errors.append(f"footnote target is missing: {path.relative_to(root)}#{anchor}")
        toc = next((node for node in document.walk() if node.attrs.get("id") == "toc"), None)
        if toc is not None:
            for node in toc.walk():
                if node.tag == "a" and normalized(node.text()) in {"Formalization", "Primary declarations", "Supporting declarations"}:
                    errors.append(f"technical panel in navigation: {path.relative_to(root)}")
    keys = {(entry["declaration"], entry["reference"], entry["role"]) for entry in ledger}
    xref = json.loads((root / "xref.json").read_text(encoding="utf-8"))
    for name, entries in xref.get("Verso.Genre.Manual.doc", {}).get("contents", {}).items():
        for entry in entries:
            if entry["address"].startswith("https://"):
                if is_machine_mathlib_find_link(entry["address"]):
                    errors.append(f"external Mathlib definition selects machine data: {name}")
                if entry["id"]:
                    errors.append(f"external definition link has a phantom fragment: {name}")
            elif (entry["address"], entry["id"]) not in retained_targets:
                errors.append(f"definition link lacks a checked statement: {name}")
    if len(keys) != len(ledger) or len(ledger) != report["alignment_entries"]:
        errors.append("alignment ledger count or uniqueness mismatch")
    if (annotations, notes, redirects) != (report["reviewed_annotations"], report["footnotes"], report["redirects"]):
        errors.append("publication report does not match HTML")
    if annotations != report.get("editorial_review", {}).get("annotations"):
        errors.append("HTML omits or duplicates authored reader annotations")
    for error in errors:
        print(error)
    if errors:
        raise ValueError(f"reader validation failed: {len(errors)} errors")
    return dict(alignment_entries=len(ledger), annotations=annotations, footnotes=notes,
                redirects=redirects, errors=0)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("html_root", type=Path)
    parser.add_argument("--require-complete", action="store_true",
                        help="reject publication without the complete full-book editorial review")
    args = parser.parse_args()
    print(json.dumps(validate(args.html_root, args.require_complete), sort_keys=True))
