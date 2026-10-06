#!/usr/bin/env python3
"""Check annotated and reviewed reading pages at desktop and phone widths.

Run with Playwright installed and --chromium pointing to an available browser.
This exercises a mounted URL prefix, as used by GitHub Pages. Source destinations
are checked structurally here; publication still requires checking the deployed pin.
"""

import argparse
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import json
from pathlib import Path
import re
import sys
from threading import Thread
from urllib.parse import quote, urlsplit

from playwright.sync_api import sync_playwright

PROJECT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT / "verso/release/scripts"))
from prepare_reader import parse


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, *_):
        pass


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("html_root", type=Path)
    parser.add_argument("--chromium", required=True)
    parser.add_argument("--item", action="append", default=[],
                        help="Check only these reviewed items (repeatable); still audit all route coverage")
    parser.add_argument("--saved-bookmarks", action="store_true",
                        help="Also exercise captured public URLs and anchors for the selected items")
    parser.add_argument("--site-url",
                        help="Check this deployed HTTP(S) URL instead of serving html_root locally")
    args = parser.parse_args()
    if args.site_url:
        address = urlsplit(args.site_url)
        if address.scheme not in {"http", "https"} or not address.hostname or \
                address.query or address.fragment or address.username or address.password:
            parser.error("--site-url needs an HTTP(S) site root without credentials, query or fragment")
    root = args.html_root.resolve()
    annotations = json.loads((PROJECT / "verso/release/metadata/reader-annotations.json").read_text())
    reviews = json.loads((PROJECT / "verso/release/metadata/reader-reviews.json").read_text())
    item_anchors = {key: key.replace("/", "___").replace(".", "___")
                    for key in set(annotations) | set(reviews)}
    metadata = json.loads((PROJECT / "verso/release/metadata/items.json").read_text())
    joins = json.loads((PROJECT / "verso/release/metadata/reader-joins.json").read_text())
    hidden_titles = {item["title"] for item in metadata["items"]
                     if any(record.get("hide_navigation") and record["tail"] == item["id"]
                            for record in joins)}
    for item in metadata["items"]:
        if item["id"] in reviews and item.get("verso_projection", {}).get("structure_only"):
            item_anchors[item["id"]] = item["node_id"].replace("/", "___").replace(".", "___")
    identifiers = {anchor: item for item, anchor in item_anchors.items()}
    routes = {}
    for path in root.rglob("index.html"):
        document = parse(path.read_text())
        # Flattened prose-only pages retain their semantic tag on a bookmark
        # span, rather than a section heading. Exercise those pages as well.
        found = sorted({identifiers[node.attrs["id"]] for node in document.walk()
                        if node.attrs.get("id") in identifiers})
        if found:
            routes[path.relative_to(root).as_posix()] = found
    discovered = [item for items in routes.values() for item in items]
    assert sorted(item for item in discovered if item in annotations) == sorted(annotations), (
        "Every annotated item needs one reading page")
    assert len(discovered) == len(set(discovered)), "Reading items need unique routes"
    assert sorted(discovered) == sorted(reviews), "Every reviewed item needs a reading route"
    if args.item:
        selected = set(args.item)
        assert selected <= set(reviews), "Requested item has no review record"
        routes = {route: items for route, items in routes.items() if selected.intersection(items)}
        discovered = [item for items in routes.values() for item in items]
    legacy_routes = {}
    if args.saved_bookmarks:
        selected_keys = {item_anchors[item] for item in discovered}
        selected_keys.update(item["node_id"].replace("/", "___").replace(".", "___")
                             for item in metadata["items"] if item["id"] in discovered)
        legacy = json.loads((PROJECT / "verso/release/metadata/reader-legacy-routes.json").read_text())
        legacy_routes = {route: record for route, record in legacy["routes"].items()
                         if record["key"] in selected_keys or any(
                             record["key"].startswith(key + "___heading-") for key in selected_keys)}
    server = None
    if args.site_url:
        prefix = args.site_url.rstrip("/") + "/"
    else:
        server = ThreadingHTTPServer(("127.0.0.1", 0), partial(QuietHandler, directory=str(root.parent)))
        thread = Thread(target=server.serve_forever, daemon=True)
        thread.start()
        prefix = f"http://127.0.0.1:{server.server_port}/{quote(root.name)}/"
    errors = []
    cases = bookmarks = saved_bookmarks = card_actions = helper_links = 0
    try:
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(executable_path=args.chromium, args=["--no-sandbox"])
            for width in (1440, 390):
                page = browser.new_page(viewport={"width": width, "height": 1000})
                page.on("pageerror", lambda error: errors.append(str(error)))
                for route, items in sorted(routes.items()):
                    url = prefix + quote(route)
                    response = page.goto(url, wait_until="networkidle")
                    assert response.status == 200, url
                    assert page.locator('#toc a, .split-toc a, .prev-next-buttons a').evaluate_all(
                        "nodes => nodes.every(n => !/Blank-Page-[12]-___-Blank-page/.test(n.href))"), (
                            url, 'scan-only blank pages remain in reading navigation')
                    if 'Frontmatter/TableOfContents' in items:
                        assert page.locator('main .reader-contents-link').count() == 105, url
                        assert page.locator('main .reader-contents-note').count() == 1, url
                        page.screenshot(path=str(root.parent / f'reader-contents-{width}.png'))
                    if 'Backmatter/ReferencesHistorical' in items:
                        assert page.locator('main p').evaluate_all(
                            r"nodes => nodes.filter(n => /^\[\d+\]/.test(n.textContent.trim())).length") == 61, url
                        page.screenshot(path=str(root.parent / f'reader-historical-references-{width}.png'))
                    if 'Backmatter/MathematicalReferences' in items:
                        assert page.locator('main p').evaluate_all(
                            r"nodes => nodes.filter(n => /^\[[A-Za-z]+\]/.test(n.textContent.trim())).length") == 9, url
                        page.screenshot(path=str(root.parent / f'reader-mathematical-references-{width}.png'))
                    for title in hidden_titles:
                        assert page.locator("#toc, .split-toc").get_by_role(
                            "link", name=title, exact=True, include_hidden=True).count() == 0, (
                                url, title, "a folded proof tail remains in navigation")
                    assert page.locator("main .lean-statement[open]").count() == 0, url
                    if width == 390:
                        assert page.locator("main h1").evaluate_all(
                            "nodes => nodes.every(node => parseFloat(getComputedStyle(node).fontSize) <= 28)"), (
                            url, "mobile title dominates the reading area")
                        assert page.locator(".prev-next-buttons").evaluate_all(
                            "nodes => nodes.every(node => node.getBoundingClientRect().height <= 64)"), (
                            url, "mobile navigation obscures the reading area")
                    ordered_items = [item["id"] for item in metadata["items"] if item["id"] in items]
                    if 'Chapter9/Theorem9.2.1' in items:
                        assert page.locator('main p').evaluate_all("""nodes => {
                          const prose = nodes.filter(n => !n.closest(
                            '.lean-annotation, .lean-reference, .namedocs, .reader-footnotes'));
                          return ['(ii)', '(iii)'].every(part =>
                            prose.some(n => n.textContent.trim().startsWith(part)));
                        }"""), (url, 'projective classification parts are merged into the display')
                    if 'Chapter9/Proposition9.1.1' in items:
                        assert page.locator('main p').evaluate_all("""nodes => nodes.some(n =>
                          !n.closest('.lean-annotation, .lean-reference, .namedocs')
                          && n.textContent.trim().startsWith('so')
                          && !n.querySelector('.math.display'))
                        """), (url, 'the idempotent proof continuation is merged into its formula')
                    if 'Chapter9/Theorem9.6.4' in items:
                        assert page.locator('main p, main aside').evaluate_all("""nodes => {
                          const reading = nodes.filter(n => n.tagName === 'ASIDE'
                            || !n.closest('.lean-annotation, .lean-reference, .namedocs'));
                          const i = reading.findIndex(n => n.tagName === 'P'
                            && n.textContent.trim().startsWith('The proof of Theorem 9.6.4'));
                          return i >= 0 && reading[i+1]?.tagName === 'P'
                            && reading[i+1].textContent.trim().startsWith('Problem 9.6.5.');
                        }"""), (url, 'the proof transition is interrupted')
                    for item, filename in (('Chapter9/Theorem9.2.1', 'projective-covers'),
                                           ('Chapter9/Problem9.3.2', 'cartan-example'),
                                           ('Chapter9/Problem9.5.3', 'blocks'),
                                           ('Chapter9/Exercise9.6.3', 'generator'),
                                           ('Chapter9/Problem9.6.5', 'balanced-tensors'),
                                           ('Chapter9/Corollary9.7.3', 'morita')):
                        if item in items:
                            page.screenshot(path=str(root.parent / f'reader-chapter9-{filename}-{width}.png'))
                    if 'Chapter8/Theorem8.1.1' in items:
                        assert page.locator('main p').evaluate_all("""nodes => {
                          const prose = nodes.filter(n => !n.closest(
                            '.lean-annotation, .lean-reference, .namedocs, .reader-footnotes'));
                          return ['(i)', '(ii)', '(iii)', '(iv)'].every(part =>
                            prose.some(n => n.textContent.trim().startsWith(part)));
                        }"""), (url, 'projectivity needs four separate original conditions')
                    if 'Chapter8/Theorem8.1.5' in items:
                        assert page.locator('main p').evaluate_all("""nodes => {
                          const prose = nodes.filter(n => !n.closest(
                            '.lean-annotation, .lean-reference, .namedocs, .reader-footnotes'));
                          return ['(i)', '(ii)', '(iii)'].every(part =>
                            prose.some(n => n.textContent.trim().startsWith(part)));
                        }"""), (url, 'injectivity conditions (ii) and (iii) are merged')
                    if 'Chapter8/Problem8.2.5' in items:
                        assert page.locator('main p').evaluate_all("""nodes => nodes.some(n =>
                          !n.closest('.lean-annotation, .lean-reference, .namedocs')
                          && n.textContent.trim().startsWith('The collection of homomorphisms'))
                        """), (url, 'comparison-map definition is joined to question (ii)')
                    if 'Chapter8/Problem8.2.10' in items:
                        assert page.locator('main .lean-annotation').count() == 5, url
                        assert '[Blank page]' not in page.locator('main').inner_text(), url
                        assert page.locator('main p').evaluate_all("""nodes => {
                          const prose = nodes.filter(n => !n.closest(
                            '.lean-annotation, .lean-reference, .namedocs, .reader-footnotes'));
                          return ['(i)', '(ii)', '(iii)', '(iv)', '(v)'].every(part =>
                            prose.some(n => n.textContent.trim().startsWith(part)));
                        }"""), (url, 'a Koszul exercise part is missing or merged')
                    if 'Chapter8/Problem8.2.8' in items:
                        assert page.locator('main p, main aside').evaluate_all("""nodes => {
                          const reading = nodes.filter(n => n.tagName === 'ASIDE'
                            || !n.closest('.lean-annotation, .lean-reference, .namedocs'));
                          const i = reading.findIndex(n => n.tagName === 'P'
                            && n.textContent.trim() === 'Similarly,');
                          return i >= 0 && reading[i+1]?.tagName === 'P'
                            && reading[i+1].querySelector('.math.display');
                        }"""), (url, 'the Tor explanation interrupts the Ext transition')
                    for item, filename in (('Chapter8/Theorem8.1.1', 'projectivity'),
                                           ('Chapter8/Example8.1.7', 'injectivity'),
                                           ('Chapter8/Problem8.2.6', 'exact-sequences'),
                                           ('Chapter8/Problem8.2.8', 'tensor-algebras'),
                                           ('Chapter8/Problem8.2.10', 'koszul')):
                        if item in items:
                            page.screenshot(path=str(root.parent / f'reader-chapter8-{filename}-{width}.png'),
                                            full_page=True)
                    if 'Chapter7/Definition7.8.1' in items:
                        assert page.locator('main p').evaluate_all("""nodes => {
                          const p = nodes.find(n => !n.closest('.lean-annotation, .reader-footnotes, .namedocs')
                            && n.textContent.trim().startsWith('Definition 7.8.1.'));
                          const foot = document.querySelector('main .reader-footnotes');
                          const continuation = nodes.find(n => !n.closest('.lean-annotation, .reader-footnotes, .namedocs')
                            && n.textContent.trim().startsWith('Often one considers complexes'));
                          return p && p.textContent.includes('The cohomology of this complex is')
                            && p.textContent.includes('The complex is said to be')
                            && p.textContent.includes('exact in all terms.')
                            && p.querySelector('.math') && foot
                            && foot.textContent.includes('de Rham complex')
                            && foot.textContent.includes('This explains the term')
                            && !foot.textContent.includes('The complex is said to be')
                            && continuation
                            && !!(continuation.compareDocumentPosition(foot) & Node.DOCUMENT_POSITION_FOLLOWING);
                        }"""), (url, 'the de Rham footnote has swallowed the cohomology definition')
                    if 'Chapter7/Problem7.8.7' in items:
                        assert page.locator('main .lean-annotation').count() == 4, (
                            url, 'the four tensor-complex questions need locally placed explanations')
                        assert page.locator('main .lean-annotation').first.evaluate("""note =>
                          note.previousElementSibling?.tagName === 'P'
                          && note.previousElementSibling.textContent.trim().startsWith('(i) Show')
                          && !note.previousElementSibling.querySelector('.math.display')
                        """), (url, 'the first tensor question remains attached to the differential display')
                    if 'Chapter7/Example7.9.6' in items:
                        assert page.locator('main .lean-annotation').count() == 3, (
                            url, 'the three exactness examples need their own explanations')
                    for item, filename in (('Chapter7/Definition7.8.1', 'cohomology'),
                                           ('Chapter7/Problem7.8.7', 'kunneth'),
                                           ('Chapter7/Example7.9.6', 'exactness')):
                        if item in items:
                            page.screenshot(path=str(root.parent / f'reader-chapter7-{filename}-{width}.png'))
                    if 'Chapter7/Discussion_after_Definition7.6.1' in items:
                        assert page.locator('main p').evaluate_all("""nodes => {
                          const p = nodes.find(n => !n.closest('.lean-annotation, .lean-reference, .namedocs')
                            && n.textContent.trim().startsWith('Not every functor'));
                          const table = [...document.querySelectorAll('main table')]
                            .find(t => !t.closest('.split-toc, .lean-annotation, .namedocs'));
                          return p && table && p.textContent.includes('since if')
                            && p.textContent.includes('are a pair of adjoint functors')
                            && p.textContent.includes('represents the functor')
                            && !!(p.compareDocumentPosition(table) & Node.DOCUMENT_POSITION_FOLLOWING)
                            && table.querySelectorAll('tr').length === 15;
                        }"""), (url, 'the unchanged analogy table interrupts the adjunction argument')
                        page.locator('main table').evaluate_all("""tables => {
                          const table = tables.find(t => !t.closest('.split-toc, .lean-annotation, .namedocs'));
                          table.scrollIntoView({block: 'center'});
                        }""")
                        page.screenshot(path=str(root.parent / f'reader-chapter7-analogy-table-{width}.png'))
                    if 'Chapter7/Example7.6.3' in items:
                        assert page.locator('main .lean-annotation').count() == 5, (
                            url, 'adjunction examples need their own locally placed explanations')
                    if 'Chapter7/Problem7.7.3' in items:
                        assert page.locator('main h1').count() == 1, (
                            url, 'Noetherianity, kernels and Morita equivalence remain fragmented')
                    for item, filename in (('Chapter7/Discussion_after_Definition7.6.1', 'adjunctions'),
                                           ('Chapter7/Example7.6.3', 'adjunction-examples'),
                                           ('Chapter7/Problem7.7.3', 'abelian-modules')):
                        if item in items:
                            page.screenshot(path=str(root.parent / f'reader-chapter7-{filename}-{width}.png'))
                    if 'Chapter7/Definition7.1.1' in items:
                        assert page.locator('main h1').count() == 1, (url, 'category definitions remain fragmented')
                        assert page.locator('main .implementation-references').count() == 1, (
                            url, 'joined category passage repeats dependency inventories')
                        assert page.locator('main').inner_text().index('Definition 7.1.1.') < \
                            page.locator('main').inner_text().index('Example 7.1.6.'), url
                    if 'Chapter7/Example7.3.2' in items:
                        assert page.locator('main .lean-annotation').count() == 4, (
                            url, 'each naturality example needs its own explanation')
                        assert page.locator('main .lean-annotation').evaluate_all("""notes => {
                          const starts = ['Example 7.3.2.', 'Let', 'Let', 'The set of endomorphisms'];
                          return notes.every((note, i) => note.previousElementSibling?.tagName === 'P'
                            && note.previousElementSibling.textContent.trim().startsWith(starts[i]));
                        }"""), (url, 'naturality explanations are not beside their examples')
                    if any(item.startswith('Chapter7/') for item in items):
                        assert not page.locator('main .lean-annotation summary').evaluate_all(
                            "nodes => nodes.some(n => /auxiliary|AssociatedType|ParameterizedType/.test(n.textContent))"), (
                            url, 'conversion names leaked into the mathematical summaries')
                        if 'Chapter7/Example7.3.2' in items:
                            page.screenshot(path=str(root.parent / f'reader-chapter7-naturality-{width}.png'))
                        if 'Chapter7/Definition7.1.1' in items:
                            page.screenshot(path=str(root.parent / f'reader-chapter7-categories-{width}.png'))
                    if all(reviews[item]["decision"] == "book_prose_only" for item in ordered_items):
                        assert page.locator("main .lean-statement, main .implementation-references").count() == 0, (
                            url, "prose-only reading page contains a generated declaration inventory")
                    expected_notes = [note for item in ordered_items for note in annotations.get(item, [])]
                    if any(item in items for item in (
                            "Chapter2/Theorem2.1.2", "Chapter6/Theorem_Dynkin_classification")):
                        assert page.locator("main ul").evaluate_all("""nodes => {
                          const list = nodes.find(node =>
                            !node.closest('.lean-annotation, .lean-reference, .namedocs')
                            && node.children.length === 5
                            && node.firstElementChild.querySelector('.math:not(.display)')
                              ?.textContent.includes('A_n'));
                          return list && [...list.children].every(node =>
                            node.querySelectorAll('.math.display').length === 1
                            && !!node.querySelector('.katex')
                            && !node.querySelector('pre, .lean-annotation')
                            && [...node.querySelectorAll('code')].every(code =>
                              code.classList.contains('math')));
                        }"""), (url, "the complete five-diagram Dynkin list must use rendered mathematics")
                    if "Chapter6/Problem6.1.3_continued_tildeE" in items:
                        assert page.locator("main p").evaluate_all("""nodes => {
                          const original = nodes.filter(node =>
                            !node.closest('.lean-annotation, .lean-reference, .namedocs, .reader-footnotes'));
                          const parts = original.filter(node => /^\\([a-g]\\)/.test(node.textContent.trim()))
                            .map(node => node.textContent.trim().slice(1, 2));
                          const e = original.find(node => node.textContent.trim().startsWith('(e) Show'));
                          const affine = [...document.querySelectorAll('main ul')].find(node =>
                            node.firstElementChild?.querySelector('.math:not(.display)')
                              ?.textContent.includes('\\\\tilde{E}_6'));
                          if (!e || !affine || parts.join('') !== 'abcdefg') return false;
                          const range = document.createRange();
                          range.setStartAfter(e); range.setEndBefore(affine);
                          return !range.cloneContents().querySelector(
                            '.lean-annotation, .lean-reference, p, h1, h2, h3')
                            && affine.children.length === 3
                            && [...affine.children].every(node =>
                              node.querySelectorAll('.math.display').length === 1);
                        }"""), (url, "the Dynkin exercise parts or affine diagram continuation are interrupted")
                        assert page.locator("main h1").count() == 1, (
                            url, "synthetic continuation headings remain in the reading page")
                        assert page.locator("main .footnote-body").count() == 1, (
                            url, "the Sylvester footnote was lost or duplicated")
                        assert "Sylvester criterion" in page.locator("main .footnote-body").inner_text(), (
                            url, "the full original footnote did not follow the joined exercise")
                        assert page.locator("main .reader-footnotes").evaluate("""node => {
                          const end = [...document.querySelectorAll('main p')].find(p =>
                            !p.closest('.lean-annotation, .lean-reference, .reader-footnotes')
                            && p.textContent.trim().startsWith('(g)'));
                          return end && (end.compareDocumentPosition(node) & Node.DOCUMENT_POSITION_FOLLOWING)
                            && node.getBoundingClientRect().height > 0;
                        }"""), (url, "the full footnote must appear after the last original exercise part")
                    if "Chapter6/Problem6.1.5_parts" in items:
                        assert page.locator("main h1").count() == 1, (
                            url, "finite-type introduction/theorem/exercise should form one reading passage")
                        assert page.locator("main p").evaluate_all("""nodes => {
                          const prose = nodes.filter(p => !p.closest(
                            '.lean-annotation, .lean-reference, .namedocs, .reader-footnotes'));
                          const parts = prose.filter(p => /^\\([a-c]\\)/.test(p.textContent.trim()))
                            .map(p => p.textContent.trim().slice(1, 2));
                          return parts.join('') === 'abc'
                            && prose.filter(p => p.textContent.trim().startsWith('Hint:')).length === 2;
                        }"""), (url, "all three original finite-type parts and both hints must remain in order")
                    if "Chapter2/Problem2.15.1" in items:
                        assert page.locator("main p").evaluate_all("""nodes => {
                          const parts = nodes.filter(node =>
                            !node.closest('.lean-annotation, .lean-reference, .namedocs')
                            && /^\\([a-n]\\)/.test(node.textContent.trim()))
                            .map(node => node.textContent.trim().slice(1, 2));
                          return parts.join('') === 'abcdefghijklmn';
                        }"""), (url, "the fourteen original sl₂ problem parts must stay in order")
                    if any(item in items for item in (
                            "Chapter2/Problem2.15.1", "Chapter2/Discussion_2.15_heading")):
                        assert page.locator("main h1").evaluate_all(
                            "nodes => nodes.every(node => !/[\\\\$]/.test(node.textContent))"), (
                                url, "raw mathematical markup leaked into the section title")
                    if "Chapter5/Discussion_semidirect_products" in items:
                        assert page.locator("main p").evaluate_all("""nodes => {
                          const introduction = nodes.find(node =>
                            !node.closest('.lean-annotation, .lean-reference, .namedocs')
                            && node.textContent.trim().startsWith('As a representation of'));
                          const display = introduction?.nextElementSibling;
                          const action = display?.nextElementSibling;
                          return display && !display.closest('.lean-annotation')
                            && !!display.querySelector('.math.display')
                            && action && !action.closest('.lean-annotation')
                            && action.textContent.trim().startsWith('Next, we introduce');
                        }"""), (url, "induced function space is separated from its introduction or A-action")
                    if "Chapter5/Theorem5.27.1" in items:
                        assert page.locator("main p").evaluate_all("""nodes => {
                          const original = nodes.filter(node =>
                            !node.closest('.lean-annotation, .lean-reference, .namedocs'));
                          const formula = original.find(node =>
                            node.textContent.trim().startsWith('(iv) The character'));
                          const count = original.find(node =>
                            node.textContent.trim().startsWith('(iii) We have'));
                          const first = count?.nextElementSibling;
                          const second = first?.nextElementSibling;
                          return !!formula?.nextElementSibling?.querySelector('.math.display')
                            && !formula.nextElementSibling.closest('.lean-annotation')
                            && !!first?.querySelector('.math.display')
                            && !first.closest('.lean-annotation')
                            && !!second?.querySelector('.math.display')
                            && !second.closest('.lean-annotation');
                        }"""), (url, "semidirect character formula or completeness calculation is split")
                    if "Chapter5/Theorem5.22.1" in items:
                        # The book promises the dimension formula at the end of
                        # its statement; annotations must not split that pair.
                        assert page.locator("main p").evaluate_all("""nodes => {
                          const statement = nodes.find(node =>
                            !node.closest('.lean-annotation, .lean-reference, .namedocs')
                            && node.textContent.trim().startsWith('Theorem 5.22.1'));
                          const next = statement?.nextElementSibling;
                          return next && !next.closest('.lean-annotation')
                            && !!next.querySelector('.math.display');
                        }"""), (url, "Weyl theorem is separated from its dimension formula")
                    if "Chapter5/Theorem5.23.2" in items:
                        # Keep the complete Peter–Weyl statement together:
                        # its introduction, display, and summation clause.
                        assert page.locator("main p").evaluate_all("""nodes => {
                          const statement = nodes.find(node =>
                            !node.closest('.lean-annotation, .lean-reference, .namedocs')
                            && node.textContent.trim().startsWith('(ii) (The Peter-Weyl'));
                          const display = statement?.nextElementSibling;
                          const clause = display?.nextElementSibling;
                          return display && !display.closest('.lean-annotation')
                            && !!display.querySelector('.math.display')
                            && clause && !clause.closest('.lean-annotation')
                            && clause.textContent.trim().startsWith('where the summation');
                        }"""), (url, "Peter–Weyl statement, formula, or summation clause is split")
                    if "Chapter5/Problem5.24.1" in items:
                        assert page.locator("main p").evaluate_all("""nodes => {
                          const statement = nodes.find(node =>
                            !node.closest('.lean-annotation, .lean-reference, .namedocs')
                            && node.textContent.trim().startsWith('Problem 5.24.1'));
                          const display = statement?.nextElementSibling;
                          const clause = display?.nextElementSibling;
                          return display && !display.closest('.lean-annotation')
                            && !!display.querySelector('.math.display')
                            && clause && !clause.closest('.lean-annotation')
                            && clause.textContent.trim().startsWith('is isomorphic');
                        }"""), (url, "Specht problem statement is split around its formula")
                    if "Chapter5/Discussion_5.25.1" in items:
                        assert page.locator("main p").evaluate_all("""nodes => {
                          const original = nodes.filter(node =>
                            !node.closest('.lean-annotation, .lean-reference, .namedocs'));
                          const introduction = original.find(node =>
                            node.textContent.trim().startsWith('To begin, let us find'));
                          const basis = original.find(node =>
                            node.textContent.trim().startsWith('Choose a basis'));
                          return introduction?.nextElementSibling?.tagName === 'TABLE'
                            && !!basis?.nextElementSibling?.querySelector('.math.display')
                            && !basis.nextElementSibling.closest('.lean-annotation');
                        }"""), (url, "conjugacy table or eigenbasis is separated from its introduction")
                    if "Chapter5/Discussion_1dim_reps" in items:
                        assert page.locator("main p").evaluate_all("""nodes => {
                          const first = nodes.find(node =>
                            !node.closest('.lean-annotation, .lean-reference, .namedocs')
                            && node.textContent.trim() === 'Therefore,');
                          let current = first;
                          for (let i = 0; i < 6; i++) {
                            current = current?.nextElementSibling;
                            if (!current || current.closest('.lean-annotation')) return false;
                          }
                          return current.textContent.trim().startsWith('so there are');
                        }"""), (url, "determinant-character formulas are interrupted by explanations")
                    expected = dict(markers=[item_anchors[item] for item in ordered_items],
                                    titles=[note["title"] for note in expected_notes])
                    page.evaluate("""expected => {
                      for (const id of expected.markers)
                        if (!document.getElementById(id)?.closest('main'))
                          throw new Error('Missing reading bookmark: ' + id);
                      const actual = [...document.querySelectorAll('main .lean-annotation h2')]
                        .map(x => x.textContent.trim());
                      if (JSON.stringify(actual) !== JSON.stringify(expected.titles))
                        throw new Error('Annotation order/content mismatch');
                    }""", expected)
                    assert page.locator('.header-title h1').evaluate("""node => {
                      const range = document.createRange(); range.selectNodeContents(node);
                      const rects = [...range.getClientRects()].filter(r => r.width > 0);
                      const header = node.closest('header').getBoundingClientRect();
                      const search = document.getElementById('search-wrapper').getBoundingClientRect();
                      return rects.every(r => r.left >= 0 && r.right <= search.left + 1
                        && r.top >= header.top && r.bottom <= header.bottom + 1);
                    }"""), (url, 'book masthead is clipped or overlaps search')
                    page.locator('main .math.display').evaluate_all("""nodes => {
                      for (const n of nodes) {
                        if (n.scrollWidth <= n.clientWidth + 1) continue;
                        if (getComputedStyle(n).overflowX !== 'auto' || n.tabIndex !== 0
                            || n.getAttribute('aria-label') !== 'Scrollable mathematical formula')
                          throw new Error('Wide formula is not accessibly scrollable');
                        n.scrollLeft = n.scrollWidth;
                        if (n.scrollLeft < n.scrollWidth - n.clientWidth - 1)
                          throw new Error('Formula end cannot be reached');
                        n.scrollLeft = 0;
                      }
                    }""")
                    table_note_titles = [note["title"] for item in items
                                         for note in annotations.get(item, [])
                                         if note.get("anchor_kind") == "table"]
                    page.evaluate("""titles => {
                      for (const title of titles) {
                        const heading = [...document.querySelectorAll('main .lean-annotation h2')]
                          .find(node => node.textContent.trim() === title);
                        let preceding = heading?.closest('aside').previousElementSibling;
                        while (preceding?.classList.contains('lean-annotation'))
                          preceding = preceding.previousElementSibling;
                        if (preceding?.tagName !== 'TABLE')
                          throw new Error('Explanation does not follow its table: ' + title);
                      }
                    }""", table_note_titles)
                    list_note_titles = [note["title"] for item in items
                                        for note in annotations.get(item, [])
                                        if note.get("anchor_kind") == "list"]
                    page.evaluate("""titles => {
                      for (const title of titles) {
                        const heading = [...document.querySelectorAll('main .lean-annotation h2')]
                          .find(node => node.textContent.trim() === title);
                        const aside = heading?.closest('aside');
                        let preceding = aside?.previousElementSibling;
                        while (preceding?.classList.contains('lean-annotation'))
                          preceding = preceding.previousElementSibling;
                        if (!['UL', 'OL'].includes(preceding?.tagName) || aside.closest('li'))
                          throw new Error('Explanation does not follow its complete list: ' + title);
                      }
                    }""", list_note_titles)
                    math_note_titles = [note["title"] for item in items
                                        for note in annotations.get(item, [])
                                        if note.get("anchor_kind") == "math"]
                    page.evaluate("""titles => {
                      for (const title of titles) {
                        const heading = [...document.querySelectorAll('main .lean-annotation h2')]
                          .find(node => node.textContent.trim() === title);
                        const aside = heading?.closest('aside');
                        let preceding = aside?.previousElementSibling;
                        while (preceding?.classList.contains('lean-annotation'))
                          preceding = preceding.previousElementSibling;
                        if (!preceding || !(preceding.matches('.math.display')
                              || preceding.querySelector('.math.display')) || aside.closest('p'))
                          throw new Error('Explanation does not follow its complete display: ' + title);
                      }
                    }""", math_note_titles)
                    if "Chapter6/Example6.2.4" in items:
                        assert page.locator('main .math.display').evaluate_all("""nodes =>
                          nodes.every(node => !node.textContent.includes('\\\\overset{\\\\bullet}'))
                        """), (url, 'A₃ subspace diagram has its vertex dot above a space label')
                        assert page.locator('main p').evaluate_all("""nodes => {
                          const introductions = nodes.filter(node =>
                            !node.closest('.lean-annotation, .lean-reference, .namedocs')
                            && node.textContent.trim().includes('six indecomposable representations')
                            && node.textContent.trim().endsWith(':'));
                          return introductions.length === 2 && introductions.every(node => {
                            const first = node.nextElementSibling;
                            const second = first?.nextElementSibling;
                            return first && second && !first.closest('.lean-annotation')
                              && !second.closest('.lean-annotation')
                              && !!first.querySelector('.math.display')
                              && !!second.querySelector('.math.display');
                          });
                        }"""), (url, 'A₃ six-model lists are separated from their introductions')
                    if "Chapter6/Discussion_after_Example6.3.1" in items:
                        assert page.locator('main h1').count() == 1, (
                            url, 'D₄ orientation conclusion should stay on the worked-example page')
                    if "Chapter6/Lemma6.4.6" in items:
                        assert page.locator('main h1').count() == 1, (
                            url, 'root definitions and the sign proof should form one reading passage')
                        assert page.locator('main p').evaluate_all("""nodes => {
                          const labels = nodes.filter(node => !node.closest(
                            '.lean-annotation, .lean-reference, .namedocs, .reader-footnotes'))
                            .map(node => node.textContent.trim().match(/^(Definition|Lemma|Remark) 6\\.4\\.[1-8]\\b/)?.[0])
                            .filter(Boolean);
                          return labels.join('|') === 'Definition 6.4.1|Lemma 6.4.2|Definition 6.4.3|'
                            + 'Remark 6.4.4|Definition 6.4.5|Lemma 6.4.6|Definition 6.4.7|Remark 6.4.8';
                        }"""), (url, 'the eight original root passages must remain in book order')
                    if "Chapter6/Remark6.4.11" in items:
                        assert page.locator('main h1').count() == 1, (
                            url, 'reflection definition and Weyl-group argument should share one page')
                    if "Chapter6/Theorem6.5.2" in items:
                        assert page.locator('main h1').count() == 1, (
                            url, 'dimension vector, theorem introduction and Gabriel statement are split')
                        assert page.locator('main p, main aside').evaluate_all("""nodes => {
                          // Verso keeps joined passages in nested sections, with
                          // bookmark spans between them. Check reading order,
                          // retaining asides so an intervening note still fails.
                          const reading = nodes.filter(node => node.tagName === 'ASIDE'
                            || !node.closest('.lean-annotation, .lean-reference, .namedocs'));
                          const index = reading.findIndex(node => node.tagName === 'P'
                            && node.textContent.trim().startsWith('We are now able'));
                          return index >= 0 && reading[index + 1]?.tagName === 'P'
                            && reading[index + 1].textContent.trim().startsWith('Theorem 6.5.2');
                        }"""), (url, 'Gabriel statement is separated from its original introduction')
                    if "Chapter6/Lemma6.7.2" in items:
                        assert page.locator('main h1').count() == 1, (
                            url, 'Coxeter definition and eventual-negativity lemma should share one page')
                        assert page.locator('main p').evaluate_all("""nodes => {
                          const prose = nodes.filter(node => !node.closest(
                            '.lean-annotation, .lean-reference, .namedocs'));
                          return prose.some(node => node.textContent.trim().startsWith('Assume the contrary'));
                        }"""), (url, 'the eigenvector argument is joined to its preceding display')
                    if "Chapter6/Corollary6.8.4" in items:
                        assert page.locator('main h1').count() == 1, (
                            url, 'the Gabriel proof should be a continuous reading page')
                        assert page.locator('main details.implementation-references').count() == 1, (
                            url, 'joined proof needs one consolidated optional dependency list')
                        assert page.locator('main p, main aside').evaluate_all("""nodes => {
                          const reading = nodes.filter(node => node.tagName === 'ASIDE'
                            || !node.closest('.lean-annotation, .lean-reference, .namedocs'));
                          const prose = reading.filter(node => node.tagName === 'P');
                          const labels = prose.map(node => node.textContent.trim().match(
                            /^(?:Theorem 6\\.8\\.1|Corollary 6\\.8\\.[2-4])\\b/)?.[0]).filter(Boolean);
                          const intro = reading.findIndex(node => node.tagName === 'P'
                            && node.textContent.trim().startsWith('We are now able'));
                          const existence = reading.findIndex(node => node.tagName === 'P'
                            && node.textContent.trim().startsWith('These two corollaries'));
                          return labels.join('|') === 'Theorem 6.8.1|Corollary 6.8.2|Corollary 6.8.3|Corollary 6.8.4'
                            && intro >= 0 && reading[intro + 1]?.textContent.trim().startsWith('Corollary 6.8.2')
                            && existence >= 0 && reading[existence + 1]?.textContent.trim().startsWith('Corollary 6.8.4')
                            && prose.some(node => node.textContent.trim().startsWith('Let Q'))
                            && prose.some(node => node.textContent.trim().startsWith('Proof. Let i'));
                        }"""), (url, 'Gabriel passages are reordered or the original transitions are interrupted')
                    if "Chapter6/Problem6.9.1" in items:
                        assert page.locator('main p').evaluate_all("""nodes => {
                          const prose = nodes.filter(node => !node.closest(
                            '.lean-annotation, .lean-reference, .namedocs'));
                          return prose.some(node => node.textContent.trim().startsWith('(2)'))
                            && prose.some(node => node.textContent.trim().startsWith('(3)'));
                        }"""), (url, 'the infinity and H families need separate paragraphs')
                    if "Chapter6/Definition6.6.4" in items:
                        assert page.locator('main h1').count() == 1, (
                            url, 'reflection constructions and arrow maps should share a reading page')
                        assert page.locator('main p, main aside').evaluate_all("""nodes => {
                          const reading = nodes.filter(node => node.tagName === 'ASIDE'
                            || !node.closest('.lean-annotation, .lean-reference, .namedocs'));
                          const labels = reading.filter(node => node.tagName === 'P')
                            .map(node => node.textContent.trim().match(/^Definition 6\\.6\\.[1-4]\\b/)?.[0])
                            .filter(Boolean);
                          const intro = reading.findIndex(node => node.tagName === 'P'
                            && node.textContent.trim().startsWith('We are now able'));
                          return labels.join('|') === 'Definition 6.6.1|Definition 6.6.2|'
                            + 'Definition 6.6.3|Definition 6.6.4'
                            && intro >= 0 && reading[intro + 1]?.tagName === 'P'
                            && reading[intro + 1].textContent.trim().startsWith('Definition 6.6.3');
                        }"""), (url, 'reflection definitions are out of order or separated from their introduction')
                        assert page.locator('main p').evaluate_all("""nodes => {
                          const formulas = nodes.filter(node => !node.closest(
                            '.lean-annotation, .lean-reference, .namedocs'));
                          // KaTeX's visible text precedes its original TeX in
                          // textContent. Read its retained TeX annotation.
                          return formulas.some(node => node.querySelector(
                            '.math.display annotation[encoding="application/x-tex"]')
                            ?.textContent.startsWith('F_i^+(V)_i ='))
                            && formulas.some(node => node.querySelector(
                              '.math.display annotation[encoding="application/x-tex"]')
                              ?.textContent.startsWith('F_i^-(V)_i ='))
                            && formulas.some(node => node.textContent.trim().startsWith('Also, all maps'))
                            && formulas.some(node => node.textContent.trim().startsWith('Again, all maps'));
                        }"""), (url, 'reflection spaces or their original arrow-map paragraphs are missing')
                    if "Chapter6/Proposition6.6.5" in items:
                        assert page.locator('main .math.display').evaluate_all("""nodes => {
                          const diagrams = nodes.filter(node => !node.closest(
                            '.lean-annotation, .lean-reference, .namedocs')
                            && node.textContent.includes('\\\\begin{array}{ccccc}'));
                          return diagrams.length === 2 && diagrams.every(node =>
                            node.textContent.split('\\\\bullet').length - 1 === 4
                            && node.textContent.includes('\\\\uparrow')
                            && !!node.parentElement.querySelector('.katex'))
                            && !nodes.some(node => node.textContent.trim() === '\\\\uparrow');
                        }"""), (url, 'vertex-simple proof pictures must be complete, rendered four-vertex diagrams')
                    # Check every authored card's binding and actual click behavior,
                    # not only aggregate expansion or the first definition bookmark.
                    for index, annotation in enumerate(expected_notes):
                        note = page.locator("main .lean-annotation").nth(index)
                        for declaration in annotation.get("declarations", []):
                            detail = note.locator("details.lean-statement").filter(
                                has=page.locator("summary", has_text=re.compile(
                                    "^" + re.escape(declaration["label"]) + "$")))
                            assert detail.count() == 1, (url, declaration["name"])
                            summary = detail.locator("summary")
                            assert summary.inner_text().strip() == declaration["label"]
                            definition = detail.locator(".namedocs[id]")
                            assert definition.count() == 1, (url, declaration["name"])
                            # Verso escapes both namespace separators and the
                            # apostrophe in a primed Lean name as three underscores.
                            assert definition.get_attribute("id").startswith(
                                re.sub(r"[.']", "___", declaration["name"])), (url, declaration["name"])
                            assert declaration["name"] in definition.text_content()
                            # Proof links are intentionally hidden while the statement
                            # is collapsed, so inspect the DOM rather than visible roles.
                            proof = detail.locator("a", has_text=re.compile("^Inspect definition or proof$"))
                            assert proof.count() == 1
                            assert proof.get_attribute("href").startswith(
                                "https://github.com/mathlib-initiative/EtingofRepresentationTheory/blob/")
                            assert not detail.evaluate("node => node.open")
                            summary.click()
                            assert detail.evaluate("node => node.open")
                            summary.click()
                            assert not detail.evaluate("node => node.open")
                            card_actions += 2
                        for reference in annotation.get("links", []):
                            link = note.get_by_role("link", name=reference["label"], exact=True)
                            assert link.count() == 1, (url, reference["name"])
                            address = link.get_attribute("href")
                            if reference["name"].startswith("RepresentationTheory."):
                                assert address.startswith(
                                    "https://github.com/mathlib-initiative/EtingofRepresentationTheory/blob/"), (
                                    url, reference["name"], "helper lacks a direct source destination")
                            else:
                                assert address.startswith("https://") and "#doc" in address
                            helper_links += 1
                    for expanded in (False, True):
                        if expanded:
                            page.locator("main details.lean-statement").evaluate_all(
                                "nodes => nodes.forEach(node => node.open = true)")
                        assert page.evaluate("document.documentElement.scrollWidth <= innerWidth + 1"), (
                            url, width, expanded, "page overflow")
                        text = page.locator("main").inner_text()
                        assert "Alignment metadata:" not in text and "book-ref=" not in text, url
                        cases += 1
                    for screenshot_item, filename in (
                            ("Chapter3/Example3.1.2", "chapter3-example"),
                            ("Chapter3/Theorem3.2.2", "chapter3-density"),
                            ("Chapter3/Theorem3.5.4", "chapter3-radical-quotient"),
                            ("Chapter3/Example3.5.6", "chapter3-radical-examples"),
                            ("Chapter3/Theorem3.6.2", "chapter3-characters"),
                            ("Chapter3/Theorem3.7.1", "chapter3-jordan-holder"),
                            ("Chapter3/Theorem3.8.1", "chapter3-krull-schmidt"),
                            ("Chapter3/Lemma3.8.2", "chapter3-fitting"),
                            ("Chapter3/Problem3.8.5", "chapter3-periodic-functions"),
                            ("Chapter3/Problem3.9.1", "chapter3-extensions"),
                            ("Chapter3/Problem3.9.2", "chapter3-polynomial-extensions"),
                            ("Chapter3/Problem3.9.3", "chapter3-quiver-representations"),
                            ("Chapter3/Problem3.9.4", "chapter3-deformations"),
                            ("Chapter3/Problem3.9.5", "chapter3-clifford-algebra"),
                            ("Chapter3/Theorem3.10.2", "chapter3-tensor-classification"),
                            ("Chapter3/Discussion_proof_of_Theorem3.10.2", "chapter3-tensor-proof"),
                            ("Chapter3/Remark3.10.3", "chapter3-tensor-counterexamples"),
                            ("Chapter4/Theorem4.1.1", "chapter4-maschke"),
                            ("Chapter4/Exercise4.2.3", "chapter4-modular-characters"),
                            ("Chapter4/Theorem4.2.1", "chapter4-character-basis"),
                            ("Chapter4/Exercise4.3.1", "chapter4-quaternion-functions"),
                            ("Chapter4/Example4.3_S4", "chapter4-symmetric-four"),
                            ("Chapter4/Theorem4.5.1", "chapter4-character-pairing"),
                            ("Chapter4/Remark4.5.3", "chapter4-convolution-characters"),
                            ("Chapter4/Theorem4.6.2", "chapter4-invariant-inner-product"),
                            ("Chapter4/Proposition4.7.1", "chapter4-matrix-coefficients"),
                            ("Chapter4/Example4.8.1", "chapter4-character-tables"),
                            ("Chapter4/Example4.9.1", "chapter4-tensor-tables"),
                            ("Chapter4/Lemma4.10.3", "chapter4-generic-determinant"),
                            ("Chapter4/Discussion_proof_Theorem4.10.2", "chapter4-frobenius-proof"),
                            ("Chapter4/Problem4.12.1", "chapter4-dihedral"),
                            ("Chapter4/Problem4.12.2", "chapter4-heisenberg"),
                            ("Chapter4/Problem4.12.3", "chapter4-general-linear-powers"),
                            ("Chapter4/Problem4.12.5", "chapter4-icosahedron"),
                            ("Chapter4/Problem4.12.9", "chapter4-heisenberg-tensors"),
                            ("Chapter4/Problem4.12.6", "chapter4-affine-group"),
                            ("Chapter4/Problem4.12.7", "chapter4-quaternions-rotations"),
                            ("Chapter4/Problem4.12.8", "chapter4-finite-rotations"),
                            ("Chapter4/Problem4.12.10", "chapter4-faithful-powers"),
                            ("Chapter4/Problem4.12.11", "chapter4-elasticity"),
                            ("Chapter5/Definition5.1.1", "chapter5-representation-types"),
                            ("Chapter5/Problem5.1.2", "chapter5-real-commutant"),
                            ("Chapter5/Example5.1.3", "chapter5-type-examples"),
                            ("Chapter5/Definition5.1.4", "chapter5-indicator"),
                            ("Chapter5/Theorem5.1.5", "chapter5-involution-count"),
                            ("Chapter5/Definition5.2.1", "chapter5-polynomial-definitions"),
                            ("Chapter5/Definition5.2.2", "chapter5-matrix-definitions"),
                            ("Chapter5/Proposition5.2.3", "chapter5-companion-matrix"),
                            ("Chapter5/Proposition5.2.4", "chapter5-algebraic-closure"),
                            ("Chapter5/Discussion_after_Proposition5.2.5", "chapter5-minimal-polynomials"),
                            ("Chapter5/Lemma5.2.6", "chapter5-conjugate-sum"),
                            ("Chapter5/Problem5.2.7", "chapter5-field-character-zeros"),
                            ("Chapter5/Remark5.2.8", "chapter5-cyclotomic-zeros"),
                            ("Chapter5/Theorem5.3.1", "chapter5-frobenius-divisibility"),
                            ("Chapter5/Proposition5.3.2", "chapter5-class-sum-integrality"),
                            ("Chapter5/Exercise5.3.3", "chapter5-odd-order-complex"),
                            ("Chapter5/Definition5.4.1", "chapter5-solvable-series"),
                            ("Chapter5/Lemma5.4.5", "chapter5-root-average"),
                            ("Chapter5/Discussion_proof_of_Theorem5.4.4", "chapter5-coprime-proof"),
                            ("Chapter5/Discussion_proof_of_Theorem5.4.6", "chapter5-normal-subgroup-proof"),
                            ("Chapter5/Discussion_proof_of_Theorem5.4.3", "chapter5-burnside-proof"),
                            ("Chapter5/Discussion_5.5", "chapter5-burnside-history"),
                            ("Chapter5/Theorem5.6.1", "chapter5-product-representations"),
                            ("Chapter5/Definition5.7.1", "chapter5-virtual-representations"),
                            ("Chapter5/Lemma5.7.2", "chapter5-virtual-character-criterion"),
                            ("Chapter5/Definition5.8.1", "chapter5-induction-function-model"),
                            ("Chapter5/Remark5.8.2", "chapter5-induction-hom-model"),
                            ("Chapter5/Remark5.8.3", "chapter5-induction-coset-dimension"),
                            ("Chapter5/Problem5.8.4", "chapter5-induction-in-stages"),
                            ("Chapter5/Exercise5.8.5", "chapter5-character-idempotent"),
                            ("Chapter5/Theorem5.9.1", "chapter5-frobenius-coset-formula"),
                            ("Chapter5/Discussion_proof_of_Theorem5.9.1", "chapter5-frobenius-character-proof"),
                            ("Chapter5/Theorem5.10.1", "chapter5-frobenius-reciprocity"),
                            ("Chapter5/Discussion_Problem5.10.2_parts", "chapter5-tensor-hom-duality"),
                            ("Chapter5/Discussion_5.11_examples", "chapter5-induction-small-groups"),
                            ("Chapter5/Problem5.11.1", "chapter5-induction-a-five"),
                            ("Chapter5/Definition5.12.1", "chapter5-tableaux"),
                            ("Chapter5/Discussion_Young_projectors", "chapter5-young-symmetrizers"),
                            ("Chapter5/Theorem5.12.2", "chapter5-specht-classification"),
                            ("Chapter5/Example5.12.3", "chapter5-specht-examples"),
                            ("Chapter5/Corollary5.12.4", "chapter5-specht-rational-models"),
                            ("Chapter5/Problem5.12.5", "chapter5-involution-dimensions"),
                            ("Chapter5/Lemma5.13.1", "chapter5-sandwich-functional"),
                            ("Chapter5/Discussion_lexicographic_ordering", "chapter5-partition-orders"),
                            ("Chapter5/Lemma5.13.3", "chapter5-young-trace"),
                            ("Chapter5/Lemma5.13.4", "chapter5-idempotent-maps"),
                            ("Chapter5/Discussion_proof_of_Theorem5.12.2", "chapter5-classification-proof"),
                            ("Chapter5/Definition5.14.2", "chapter5-kostka"),
                            ("Chapter5/Theorem5.14.3", "chapter5-permutation-character"),
                            ("Chapter5/Discussion_hook_length_derivation", "chapter5-hook-length-derivation"),
                            ("Chapter5/Theorem5.17.1", "chapter5-hook-length-formula"),
                            ("Chapter5/Theorem5.18.1", "chapter5-double-centralizer"),
                            ("Chapter5/Lemma5.18.3", "chapter5-pure-powers"),
                            ("Chapter5/Theorem5.18.4", "chapter5-schur-weyl"),
                            ("Chapter5/Proposition5.19.1", "chapter5-invertible-tensor-actions"),
                            ("Chapter5/Corollary5.19.2", "chapter5-general-linear-multiplicities"),
                            ("Chapter5/Example5.19.3", "chapter5-symmetric-exterior-powers"),
                            ("Chapter5/Discussion_5.20", "chapter5-weyl-interlude"),
                            ("Chapter5/Discussion_Schur_polynomials", "chapter5-schur-polynomial-definition"),
                            ("Chapter5/Proposition5.21.1", "chapter5-power-sum-expansion"),
                            ("Chapter5/Proposition5.21.2", "chapter5-schur-polynomial-special-values"),
                            ("Chapter5/Discussion_computing_characters_of_L_lambda", "chapter5-tensor-traces"),
                            ("Chapter5/Theorem5.22.1", "chapter5-weyl-character-dimension"),
                            ("Chapter5/Proposition5.22.2", "chapter5-determinant-twist"),
                            ("Chapter5/Definition5.23.1", "chapter5-algebraic-definition"),
                            ("Chapter5/Theorem5.23.2", "chapter5-peter-weyl"),
                            ("Chapter5/Remark5.23.3", "chapter5-special-linear-boundary"),
                            ("Chapter5/Problem5.24.1", "chapter5-specht-sign-twist"),
                            ("Chapter5/Problem5.24.2", "chapter5-matrix-trace-invariants"),
                            ("Chapter5/Discussion_5.25.1", "chapter5-gl2-conjugacy-types"),
                            ("Chapter5/Discussion_1dim_reps", "chapter5-determinant-characters"),
                            ("Chapter5/Theorem5.25.2", "chapter5-principal-series"),
                            ("Chapter5/Discussion_5.25.4", "chapter5-complementary-series"),
                            ("Chapter5/Discussion_complementary_series_summary", "chapter5-gl2-complete-family"),
                            ("Chapter5/Theorem5.26.1", "chapter5-artin-theorem"),
                            ("Chapter5/Remark5.26.2", "chapter5-artin-coefficients"),
                            ("Chapter5/Discussion_proof_of_Theorem5.26.1", "chapter5-artin-proof"),
                            ("Chapter5/Discussion_semidirect_products", "chapter5-semidirect-construction"),
                            ("Chapter5/Theorem5.27.1", "chapter5-semidirect-classification"),
                            ("Chapter5/Exercise5.27.2", "chapter5-semidirect-examples"),
                            ("Chapter5/Exercise5.27.3", "chapter5-semidirect-character-proof"),
                            ("Chapter5/Problem5.16.1", "chapter5-branching-rules"),
                            ("Chapter5/Problem5.16.2", "chapter5-content-scalar"),
                            ("Chapter5/Problem5.16.3", "chapter5-integer-spectrum"),
                            ("Chapter5/Theorem5.15.1", "chapter5-frobenius-formula"),
                            ("Chapter5/Discussion_proof_of_Theorem5.15.1", "chapter5-frobenius-formula-proof"),
                            ("Chapter5/Lemma5.15.3", "chapter5-cauchy-determinant"),
                            ("Chapter5/Remark5.15.5", "chapter5-kostka-triangularity"),
                            ("Chapter2/Theorem2.1.2", "chapter2-gabriel-diagrams"),
                            ("Chapter2/Discussion_after_Theorem2.1.2", "chapter2-finite-group-overview"),
                            ("Chapter2/Problem2.15.1", "chapter2-sl2-problem"),
                            ("Chapter2/Problem2.16.3", "chapter2-bracket-presentations"),
                            ("Chapter2/Problem2.16.4", "chapter2-modular-sl2-classification"),
                            ("Chapter6/Problem6.1.1", "chapter6-field-embeddings"),
                            ("Chapter6/Problem6.1.2", "chapter6-finite-orbit-dimension"),
                            ("Chapter6/Definition6.1.4", "chapter6-dynkin-definition"),
                            ("Chapter6/Discussion_after_Definition6.1.4", "chapter6-dynkin-classification"),
                            ("Chapter6/Problem6.1.3_continued_E7_E8", "chapter6-dynkin-determinants"),
                            ("Chapter6/Problem6.1.3_continued_tildeE", "chapter6-affine-dynkin"),
                            ("Chapter6/Problem6.1.5", "chapter6-finite-type"),
                            ("Chapter6/Problem6.1.5_theorem", "chapter6-gabriel-criterion"),
                            ("Chapter6/Problem6.1.5_parts", "chapter6-finite-type-necessity"),
                            ("Chapter6/Problem6.1.6", "chapter6-mckay"),
                            ("Chapter6/Section6.2_heading", "chapter6-small-quiver-introduction"),
                            ("Chapter6/Remark6.2.1", "chapter6-dimension-notation"),
                            ("Chapter6/Example6.2.2", "chapter6-a1"),
                            ("Chapter6/Example6.2.3", "chapter6-a2"),
                            ("Chapter6/Example6.2.4", "chapter6-a3"),
                            ("Chapter6/Section6.3_heading", "chapter6-star-introduction"),
                            ("Chapter6/Example6.3.1", "chapter6-d4"),
                            ("Chapter6/Discussion_after_Example6.3.1", "chapter6-orientation-classification"),
                            ("Chapter6/Definition6.4.1", "chapter6-cartan-pairing"),
                            ("Chapter6/Lemma6.4.2", "chapter6-even-positive-norm"),
                            ("Chapter6/Definition6.4.3", "chapter6-root-definition"),
                            ("Chapter6/Remark6.4.4", "chapter6-root-finiteness"),
                            ("Chapter6/Definition6.4.5", "chapter6-simple-roots"),
                            ("Chapter6/Lemma6.4.6", "chapter6-root-sign"),
                            ("Chapter6/Definition6.4.7", "chapter6-positive-negative-roots"),
                            ("Chapter6/Remark6.4.8", "chapter6-root-exhaustion"),
                            ("Chapter6/Example6.4.9", "chapter6-root-counts"),
                            ("Chapter6/Definition6.4.10", "chapter6-root-reflections"),
                            ("Chapter6/Remark6.4.11", "chapter6-weyl-finiteness"),
                            ("Chapter6/Definition6.5.1", "chapter6-dimension-vector"),
                            ("Chapter6/Theorem6.5.2", "chapter6-gabriel-classification"),
                            ("Chapter6/Definition6.6.1", "chapter6-reflection-constructions"),
                            ("Chapter6/Definition6.6.2", "chapter6-arrow-reversal"),
                            ("Chapter6/Definition6.6.3", "chapter6-kernel-reflection"),
                            ("Chapter6/Definition6.6.3_maps", "chapter6-kernel-arrow-maps"),
                            ("Chapter6/Definition6.6.4", "chapter6-cokernel-reflection"),
                            ("Chapter6/Proposition6.6.5", "chapter6-vertex-simple-exception"),
                            ("Chapter6/Proposition6.6.6", "chapter6-double-reflection"),
                            ("Chapter6/Proposition6.6.7", "chapter6-reflection-indecomposable"),
                            ("Chapter6/Proposition6.6.8", "chapter6-reflected-dimensions"),
                            ("Chapter1/Discussion_BookOrganization", "chapter1-organization")):
                        if screenshot_item not in items:
                            continue
                        page.locator("main details.lean-statement").evaluate_all(
                            "nodes => nodes.forEach(node => node.open = false)")
                        identifier = item_anchors[screenshot_item]
                        page.locator(f'[id="{identifier}"]').evaluate(
                            "node => node.scrollIntoView({block: 'start'})")
                        page.screenshot(path=str(root.parent / f"{filename}-{width}.png"))
                    if "Chapter6/Theorem_Dynkin_classification" in items:
                        for selector, filename in (
                                (page.locator("main p").filter(has_text=re.compile(r"^\s*\(c\) Show")),
                                 "chapter6-cycle-obstruction"),
                                (page.locator("main .footnote-body"), "chapter6-sylvester-footnote")):
                            selector.first.evaluate("node => node.scrollIntoView({block: 'start'})")
                            page.screenshot(path=str(root.parent / f"{filename}-{width}.png"))
                    if "Chapter6/Proposition6.6.5" in items:
                        diagrams = page.locator('main .math.display').filter(
                            has_text='\\begin{array}{ccccc}')
                        for index, filename in enumerate(("chapter6-sink-complement-diagram",
                                                         "chapter6-vertex-simple-diagram")):
                            diagrams.nth(index).evaluate("node => node.scrollIntoView({block: 'center'})")
                            page.screenshot(path=str(root.parent / f"{filename}-{width}.png"))
                    card = page.locator("main .lean-statement .namedocs[id]").first
                    for item, title, filename in (
                            ("Chapter6/Problem6.1.6", "The two-element subgroup is outside this simple-graph statement",
                             "chapter6-mckay-scope"),
                            ("Chapter6/Example6.2.4", "The six chain models are the nonempty intervals",
                             "chapter6-a3-chain-models"),
                            ("Chapter6/Example6.2.4", "The cospan also has exactly six classes",
                             "chapter6-a3-cospan-models"),
                            ("Chapter6/Example6.3.1", "How Lean supplies the standard representation",
                             "chapter6-d4-standard-model"),
                            ("Chapter6/Lemma6.4.6", "Lean splits by signs instead of cutting an edge",
                             "chapter6-root-sign-explanation"),
                            ("Chapter6/Example6.4.9", "The D and E numbers count positive roots",
                             "chapter6-root-count-explanation"),
                            ("Chapter6/Remark6.4.11", "Finiteness needs a faithful action on the roots",
                             "chapter6-weyl-faithful-action"),
                            ("Chapter6/Theorem6.5.2", "Every positive root gives one isomorphism class",
                             "chapter6-gabriel-explanation"),
                            ("Chapter6/Definition6.6.3_maps", "Arrow maps and representation morphisms are different maps",
                             "chapter6-kernel-maps-explanation"),
                            ("Chapter6/Definition6.6.4", "The source construction is the cokernel counterpart",
                             "chapter6-cokernel-explanation"),
                            ("Chapter6/Proposition6.6.6", "Recovery means an isomorphism compatible with every arrow",
                             "chapter6-double-reflection-explanation"),
                            ("Chapter6/Proposition6.6.8", "Rank–nullity gives the reflection formula",
                             "chapter6-reflected-dimensions-explanation")):
                        if item in items:
                            note = page.locator('main .lean-annotation').filter(
                                has=page.get_by_role('heading', name=title, exact=True))
                            note.evaluate("node => node.scrollIntoView({block: 'center'})")
                            page.screenshot(path=str(root.parent / f"{filename}-{width}.png"))
                    for item, title, filename in (
                            ("Chapter6/Lemma6.7.2", "The integer-vector result needed for dimension vectors",
                             "chapter6-coxeter-scope"),
                            ("Chapter6/Corollary6.8.3", "Isomorphism, not equality of chosen models",
                             "chapter6-gabriel-uniqueness"),
                            ("Chapter6/Corollary6.8.4", "Constructing an indecomposable for each positive root",
                             "chapter6-gabriel-existence"),
                            ("Chapter6/Example6.8.5", "The central reflection produces the three-line dimension vector",
                             "chapter6-d4-reflection-example"),
                            ("Chapter6/Problem6.9.1", "A nonzero-eigenvalue Jordan block splits off",
                             "chapter6-cyclic-summand"),
                            ("Chapter6/Problem6.9.2", "Counting all roots, not only the positive ones",
                             "chapter6-exceptional-root-counts"),
                            ("Chapter6/Problem6.9.3", "The checked obstruction criterion is not a packaged Ext¹ theorem",
                             "chapter6-ext-scope"),
                            ("Chapter6/Problem6.9.3", "A series of actual subrepresentations",
                             "chapter6-vertex-composition-series")):
                        if item not in items:
                            continue
                        page.locator("main details.lean-statement").evaluate_all(
                            "nodes => nodes.forEach(node => node.open = false)")
                        note = page.locator('main .lean-annotation').filter(
                            has=page.get_by_role('heading', name=title, exact=True))
                        note.evaluate("node => node.scrollIntoView({block: 'center'})")
                        page.screenshot(path=str(root.parent / f"{filename}-{width}.png"))
                    if card.count():
                        anchor = card.get_attribute("id")
                        page.goto(url + "#" + quote(anchor), wait_until="domcontentloaded")
                        page.wait_for_function("id => {const node=document.getElementById(id);"
                                              "return node && node.closest('details').open}", arg=anchor)
                        bookmarks += 1
                for route, record in legacy_routes.items():
                    for anchor in record["anchors"]:
                        response = page.goto(prefix + quote(route) + "#" + quote(anchor),
                                             wait_until="domcontentloaded")
                        if response is None:
                            # A fragment-only navigation reuses the current document.
                            # Check its HTTP destination as well as the anchor below.
                            response = page.request.get(page.url.split('#', 1)[0])
                        assert response.status == 200, (route, anchor)
                        page.wait_for_function("id => !!document.getElementById(id)", arg=anchor)
                        assert page.locator(f'[id="{anchor}"]').count() == 1, (route, anchor)
                        assert page.url.endswith("#" + quote(anchor)), (route, anchor, page.url)
                        assert page.evaluate("document.documentElement.scrollWidth <= innerWidth + 1"), (
                            route, anchor, width, "saved bookmark causes overflow")
                        saved_bookmarks += 1
                page.close()
            browser.close()
    finally:
        if server is not None:
            server.shutdown()
            server.server_close()
    assert not errors, errors
    print(json.dumps(dict(site_url=prefix, pages=len(routes), annotated_items=sum(item in annotations for item in discovered),
                          reviewed_reading_items=len(discovered),
                          collapsed_expanded_cases=cases, definition_bookmarks=bookmarks,
                          card_open_close_actions=card_actions, helper_links=helper_links,
                          legacy_routes=len(legacy_routes), saved_bookmark_cases=saved_bookmarks,
                          javascript_errors=len(errors))))


if __name__ == "__main__":
    main()
