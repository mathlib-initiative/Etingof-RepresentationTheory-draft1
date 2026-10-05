"""The book's contents and bibliographies are reading material, not inventories."""

import json
from pathlib import Path
import tempfile
import unittest

from prepare_reader import (contents_reading_destinations, link_printed_contents,
                            parse, printed_contents_key, reading_prose, SCAN_BLANK_ITEMS)

PROJECT = Path(__file__).resolve().parents[3]
META = PROJECT / 'verso/release/metadata'


class FrontBackReaderTests(unittest.TestCase):
    def test_every_front_and_back_item_has_a_book_only_decision(self):
        items = json.loads((META / 'items.json').read_text())['items']
        reviews = json.loads((META / 'reader-reviews.json').read_text())
        selected = [i for i in items if i['id'].startswith(('Frontmatter/', 'Backmatter/'))]
        self.assertEqual(len(selected), 6)
        self.assertTrue(all(reviews[i['id']]['decision'] == 'book_prose_only' for i in selected))

    def test_historical_citations_have_individual_paragraphs(self):
        for path in (
            PROJECT / 'conversion-packets/sol/Backmatter/ReferencesHistorical/Content.lean',
            PROJECT / 'verso/release/IntroductionToRepresentationTheoryVerso/Content/Backmatter/ReferencesHistorical.lean',
        ):
            text = path.read_text()
            self.assertEqual(sum(line.startswith('\\[') for line in text.splitlines()), 61)
            for label in ('10', '*26*', '*42*', '56'):
                with self.subTest(path=path, label=label):
                    self.assertIn('\n\n\\[' + label + '\\]', text)

    def test_contents_links_preserve_the_complete_original_label_and_math(self):
        document = parse('<main><section><h1>Contents</h1><p>Chapter 5. Results — 93</p>'
                         '<ul><li><p>§5.12. Representations of <code class="math">S_n</code> — 112</p></li></ul>'
                         '<p>Mathematical references — 227</p></section></main>')
        before = reading_prose(document)
        links = {'chapter-05': 'results/#intro', 'chapter-05/section-5-12': 'sn/#definition',
                 'Backmatter/MathematicalReferences': 'references/#refs'}
        self.assertEqual(link_printed_contents(document, links), 3)
        self.assertEqual(reading_prose(document), before)
        self.assertEqual(sum(n.has_class('reader-contents-link') for n in document.walk()), 3)
        self.assertIn('<code class="math">S_n</code>', document.html())
        self.assertIn('Page numbers refer to the printed book', document.html())

    def test_missing_contents_destination_is_not_silently_left_unlinked(self):
        with self.assertRaisesRegex(ValueError, 'no reading destination'):
            link_printed_contents(parse('<main><h1>Contents</h1><p>§9.7. Morita equivalence — 220</p></main>'), {})
        self.assertIsNone(printed_contents_key('An unrelated paragraph.'))

    def test_contents_targets_prose_not_empty_heading_wrappers(self):
        with tempfile.TemporaryDirectory(prefix='etingof-contents-test-') as temp:
            root = Path(temp)
            for route, body in [('wrapper', '<h1 id="C___Intro">Title</h1>'),
                                ('body', '<h1 id="C___Intro___heading-1">Title</h1><p>Original prose.</p>')]:
                (root / route).mkdir()
                (root / route / 'index.html').write_text('<main>' + body + '</main>')
            sections = {key: [dict(id=key, address='/' + route + '/')] for key, route in
                        [('C___Intro', 'wrapper'), ('C___Intro___heading-1', 'body')]}
            items = [dict(id='C/Intro', node_id='chapter-09/section-9-7', order=1)]
            links = contents_reading_destinations(root, sections, items)
            self.assertEqual(links['chapter-09/section-9-7'], 'body/#C___Intro___heading-1')
            self.assertEqual(links['chapter-09'], 'body/#C___Intro___heading-1')

    def test_only_scan_blank_items_are_skipped(self):
        self.assertEqual(SCAN_BLANK_ITEMS, {'Frontmatter/BlankPage1', 'Frontmatter/BlankPage2'})


if __name__ == '__main__':
    unittest.main()
