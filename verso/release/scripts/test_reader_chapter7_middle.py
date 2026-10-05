"""Keep the floating-table repair and scope disclosures in regeneration inputs."""

import hashlib
import json
from pathlib import Path
import re
import unittest


PROJECT = Path(__file__).resolve().parents[3]
META = PROJECT / 'verso/release/metadata'


class Chapter7MiddleTests(unittest.TestCase):
    def test_adjunction_sentence_precedes_the_unchanged_table(self):
        paths = (
            PROJECT / 'conversion-packets/sol/Chapter7/Discussion_after_Definition7.6.1/Content.lean',
            PROJECT / 'verso/release/IntroductionToRepresentationTheoryVerso/Content/Chapter7/DiscussionAfterDefinition761.lean',
        )
        for path in paths:
            with self.subTest(path=path):
                text = path.read_text()
                self.assertIn('since if $' + chr(96) + 'F, G' + chr(96) + ' are a pair of adjoint functors', text)
                table = re.search(r'^\*Table 1\.\*[\s\S]*?\n:::(?=\n|$)', text, re.M).group()
                self.assertEqual(hashlib.sha256(table.encode()).hexdigest(), '11e6f1598e3ff17f687d8b837904f11bb678f37e94961706c6f0ca795f3032ad')
                self.assertLess(text.index('and $' + chr(96) + 'G(Y)'), text.index('*Table 1.*'))

    def test_scope_differences_have_explicit_reader_notes(self):
        notes = json.loads((META / 'reader-annotations.json').read_text())
        reviews = json.loads((META / 'reader-reviews.json').read_text())
        for item in ('Chapter7/Example7.5.3', 'Chapter7/Example7.6.3', 'Chapter7/Example7.7.2'):
            with self.subTest(item=item):
                self.assertTrue(reviews[item]['coverage_gap'])
                self.assertTrue(any(n.get('kind') == 'coverage_gap' for n in notes[item]))

    def test_reverse_induction_adjunction_keeps_finite_index_in_the_explanation(self):
        notes = json.loads((META / 'reader-annotations.json').read_text())['Chapter7/Example7.6.3']
        name = 'RepresentationTheory.CategoryTheory.RepresentationAdjunctions.restrictionInductionAdjunction'
        note = next(n for n in notes if any(d['name'] == name for d in n['declarations']))
        self.assertIn('finite-index', ' '.join(note['explanation']))


if __name__ == '__main__':
    unittest.main()
