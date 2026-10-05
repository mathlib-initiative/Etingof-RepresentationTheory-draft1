"""Chapter 9 must expose mathematical statements and their actual scope."""

import json
from pathlib import Path
import unittest

PROJECT = Path(__file__).resolve().parents[3]
META = PROJECT / 'verso/release/metadata'


class Chapter9ReaderTests(unittest.TestCase):
    def setUp(self):
        self.notes = json.loads((META / 'reader-annotations.json').read_text())
        self.reviews = json.loads((META / 'reader-reviews.json').read_text())

    def prose(self, stem):
        return ' '.join(p for n in self.notes['Chapter9/' + stem] for p in n['explanation'])

    def test_entire_chapter_has_a_reading_decision(self):
        items = json.loads((META / 'items.json').read_text())['items']
        chapter = [i for i in items if i['id'].startswith('Chapter9/')]
        self.assertEqual(len(chapter), 35)
        self.assertTrue(all(self.reviews[i['id']]['comparison'] for i in chapter))

    def test_original_proof_and_theorem_have_separate_paragraphs(self):
        for item, stem, following in (
            ('Proposition9.1.1', 'Proposition911', 'so $`e`'),
            ('Theorem9.2.1', 'Theorem921', '_(ii)_'),
        ):
            for path in (
                PROJECT / f'conversion-packets/sol/Chapter9/{item}/Content.lean',
                PROJECT / f'verso/release/IntroductionToRepresentationTheoryVerso/Content/Chapter9/{stem}.lean',
            ):
                with self.subTest(path=path):
                    self.assertIn(chr(96) + '\n\n' + following, path.read_text())

    def test_chapter_opening_does_not_create_an_empty_title_wrapper(self):
        title = json.loads((META / 'reader-titles.json').read_text())['Chapter9/Introduction']
        path = PROJECT / 'verso/release/IntroductionToRepresentationTheoryVerso/Content/Chapter9/Introduction.lean'
        self.assertEqual(path.read_text().count('# ' + title + '\n'), 2)
        self.assertTrue(title.startswith('Chapter 9.'))

    def test_generator_criterion_does_not_claim_projectivity_from_detection(self):
        self.assertIn('Projective P hypothesis', self.prose('Exercise9.6.3'))
        self.assertIn('alone do not establish projectivity', self.prose('Exercise9.6.3'))
        self.assertTrue(self.reviews['Chapter9/Exercise9.6.3']['coverage_gap'])

    def test_path_algebra_assumptions_are_visible(self):
        prose = self.prose('Problem9.4.6')
        self.assertIn('finitely many vertices', prose)
        self.assertIn('does not construct the canonical projective covers', prose)
        self.assertEqual(sum(n.get('kind') == 'coverage_gap'
                             for n in self.notes['Chapter9/Problem9.4.6']), 2)

    def test_morita_definition_uses_finite_module_interfaces(self):
        names = [d['name'] for n in self.notes['Chapter9/Definition9.7.1']
                 for d in n['declarations']]
        self.assertEqual(len(names), 2)
        self.assertTrue(all(name.endswith(chr(39)) for name in names))
        self.assertIn('categories of all modules', self.prose('Definition9.7.1'))
        self.assertIn('k-linear equivalences of all modules', self.prose('Corollary9.7.3'))

    def test_dimension_and_balancing_conventions_are_explained(self):
        self.assertIn('zero module’s dimension to 0', self.prose('Definition9.4.1'))
        self.assertIn('stronger sign +1', self.prose('Problem9.4.5'))
        self.assertIn('precomposition', self.prose('Theorem9.6.4'))
        self.assertIn('not postcomposition', self.prose('Theorem9.6.4'))
        self.assertIn('apply G first, then F', self.prose('Problem9.6.5'))
        self.assertIn('resolution itself may continue indefinitely', self.prose('Problem9.4.2'))

    def test_each_exercise_part_has_its_own_explanation(self):
        for item, count in [('Problem9.4.2', 3), ('Problem9.5.3', 3), ('Problem9.6.5', 4)]:
            self.assertEqual(len(self.notes['Chapter9/' + item]), count)
        note = self.notes['Chapter9/Problem9.6.5'][2]
        self.assertEqual(note['anchor_kind'], 'math')
        self.assertTrue(note['after'].startswith(chr(92) + 'xi'))


if __name__ == '__main__':
    unittest.main()
