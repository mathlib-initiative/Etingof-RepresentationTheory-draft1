"""Regeneration must retain the cohomology definition outside the de Rham footnote."""

import json
from pathlib import Path
import re
import unittest


PROJECT = Path(__file__).resolve().parents[3]
META = PROJECT / 'verso/release/metadata'


class Chapter7FinalTests(unittest.TestCase):
    def test_cohomology_is_main_prose_not_a_footnote(self):
        paths = (
            PROJECT / 'conversion-packets/sol/Chapter7/Definition7.8.1/Content.lean',
            PROJECT / 'verso/release/IntroductionToRepresentationTheoryVerso/Content/Chapter7/Definition781.lean',
        )
        footnotes = []
        for path in paths:
            with self.subTest(path=path):
                text = path.read_text().split('## Formalization')[0]
                foot = re.search(r'^\[\^differentials\]: (.*)$', text, re.M).group(1)
                footnotes.append(foot)
                self.assertTrue(foot.endswith('This explains the term "differential".'))
                self.assertNotIn('H^i', foot)
                main = re.search(r'^\*Definition 7\.8\.1\.\* (.*)$', text, re.M).group(1)
                self.assertIn('H^i =', main)
                self.assertTrue(main.endswith('if it is exact in all terms.'))
                self.assertIn('all terms.\n\n[^differentials]:', text)
        self.assertEqual(*footnotes)

    def test_tensor_question_is_separate_from_the_displayed_differential(self):
        paths = (
            PROJECT / 'conversion-packets/sol/Chapter7/Problem7.8.7/Content.lean',
            PROJECT / 'verso/release/IntroductionToRepresentationTheoryVerso/Content/Chapter7/Problem787.lean',
        )
        for path in paths:
            with self.subTest(path=path):
                self.assertIn(chr(96) + '\n\n(i) Show that this is a complex.', path.read_text())

    def test_scope_and_linearity_are_explained(self):
        notes = json.loads((META / 'reader-annotations.json').read_text())
        reviews = json.loads((META / 'reader-reviews.json').read_text())
        for item in ('Chapter7/Problem7.8.7', 'Chapter7/Example7.9.6'):
            self.assertTrue(reviews[item]['coverage_gap'])
            self.assertTrue(any(n.get('kind') == 'coverage_gap' for n in notes[item]))
        explanation = ' '.join(notes['Chapter7/Definition7.9.1'][0]['explanation'])
        self.assertIn('scalar-preservation alias alone does not include additivity', explanation)


if __name__ == '__main__':
    unittest.main()
