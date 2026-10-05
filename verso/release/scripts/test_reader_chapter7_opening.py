"""Regeneration inputs for the opening categories and functors passages."""

import json
from pathlib import Path
import unittest


PROJECT = Path(__file__).resolve().parents[3]
METADATA = PROJECT / 'verso/release/metadata'


class Chapter7OpeningTests(unittest.TestCase):
    def test_paragraph_breaks_exist_in_both_generating_sources(self):
        cases = (
            ('Definition7.1.1', 'Definition711', 'sol', '(ii) For every'),
            ('Definition7.2.1', 'Definition721', 'sol', '(ii) for each'),
            ('Discussion_after_Example7.1.3', 'DiscussionAfterExample713', 'sol', 'We also mention'),
        )
        for item, module, route, start in cases:
            for path in (
                PROJECT / f'conversion-packets/{route}/Chapter7/{item}/Content.lean',
                PROJECT / f'verso/release/IntroductionToRepresentationTheoryVerso/Content/Chapter7/{module}.lean',
            ):
                with self.subTest(path=path):
                    self.assertIn('\n\n' + start, path.read_text())

    def test_four_naturality_examples_have_separate_notes(self):
        notes = json.loads((METADATA / 'reader-annotations.json').read_text())['Chapter7/Example7.3.2']
        self.assertEqual(len(notes), 4)
        self.assertEqual([len(n['declarations']) for n in notes], [2, 1, 1, 1])
        self.assertEqual(len({n['after'] for n in notes}), 4)

    def test_all_four_section_introductions_lead_into_their_definitions(self):
        joins = json.loads((METADATA / 'reader-joins.json').read_text())
        for section, definition in [('7.1', '7.1.1'), ('7.2', '7.2.1'), ('7.3', '7.3.1'), ('7.4', '7.4.1')]:
            self.assertTrue(any(j['head'] == 'Chapter7/Introduction_' + section
                                and j['tail'] == 'Chapter7/Definition' + definition
                                and j['kind'] == 'blocks' for j in joins))


if __name__ == '__main__':
    unittest.main()
