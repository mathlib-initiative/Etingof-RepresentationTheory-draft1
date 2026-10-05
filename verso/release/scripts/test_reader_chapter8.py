"""Chapter 8's generation inputs must preserve prose boundaries and honest scope notes."""

import json
from pathlib import Path
import unittest

PROJECT = Path(__file__).resolve().parents[3]
META = PROJECT / 'verso/release/metadata'


class Chapter8ReaderTests(unittest.TestCase):
    def test_all_chapter_items_have_a_reading_decision(self):
        items = json.loads((META / 'items.json').read_text())['items']
        reviews = json.loads((META / 'reader-reviews.json').read_text())
        chapter = [i for i in items if i['id'].startswith('Chapter8/')]
        self.assertEqual(len(chapter), 24)
        self.assertTrue(all(reviews[i['id']]['comparison'] for i in chapter))

    def test_generation_inputs_separate_conditions_and_comparison_definition(self):
        for item, stem, before, after in (
            ('Theorem8.1.5', 'Theorem815', '._', '_(iii) The functor'),
            ('Problem8.2.5', 'Problem825', chr(96) + '.', 'The collection'),
        ):
            paths = (
                PROJECT / f'conversion-packets/sol/Chapter8/{item}/Content.lean',
                PROJECT / f'verso/release/IntroductionToRepresentationTheoryVerso/Content/Chapter8/{stem}.lean',
            )
            for path in paths:
                with self.subTest(path=path):
                    self.assertIn(before + '\n\n' + after, path.read_text())

    def test_blank_page_scan_marker_is_not_part_of_the_koszul_exercise(self):
        paths = (
            PROJECT / 'conversion-packets/sol/Chapter8/Problem8.2.10/Content.lean',
            PROJECT / 'verso/release/IntroductionToRepresentationTheoryVerso/Content/Chapter8/Problem8210.lean',
        )
        for path in paths:
            with self.subTest(path=path):
                text = path.read_text()
                self.assertNotIn('[Blank page', text)
                self.assertIn('(v) Compute', text)
                for part in ('(i)', '(ii)', '(iii)', '(iv)'):
                    self.assertIn(part, text)

    def test_finite_dimensional_restrictions_are_visible(self):
        notes = json.loads((META / 'reader-annotations.json').read_text())
        reviews = json.loads((META / 'reader-reviews.json').read_text())
        for item in ('Chapter8/Example8.1.7', 'Chapter8/Problem8.2.8'):
            with self.subTest(item=item):
                self.assertTrue(reviews[item]['coverage_gap'])
                gaps = [n for n in notes[item] if n.get('kind') == 'coverage_gap']
                self.assertEqual(len(gaps), 1)
                self.assertIn('finite-dimensional', ' '.join(gaps[0]['explanation']))

    def test_variance_and_general_ext_are_explained(self):
        notes = json.loads((META / 'reader-annotations.json').read_text())
        explanation = lambda item: ' '.join(
            p for n in notes['Chapter8/' + item] for p in n['explanation'])
        self.assertIn('opposite ring', explanation('Problem8.1.3'))
        self.assertIn('contravariant in M and covariant in N', explanation('Definition8.2.4'))
        self.assertIn('not equipped with a tensor product', explanation('Discussion_after_Problem8.2.8'))
        self.assertTrue(any(
            l['name'] == 'CategoryTheory.ProjectiveResolution.extAddEquivCohomologyClass'
            for n in notes['Chapter8/Definition8.2.4'] for l in n.get('links', [])))

    def test_all_five_koszul_parts_have_specific_explanations(self):
        notes = json.loads((META / 'reader-annotations.json').read_text())['Chapter8/Problem8.2.10']
        self.assertEqual(len(notes), 5)
        self.assertTrue(all(n['declarations'] for n in notes))
        self.assertIn('arbitrary modules', ' '.join(notes[3]['explanation']))
        self.assertIn('no assertion about their graded multiplication', ' '.join(notes[4]['explanation']))

    def test_tensor_explanation_does_not_interrupt_similarly(self):
        notes = json.loads((META / 'reader-annotations.json').read_text())['Chapter8/Problem8.2.8']
        self.assertEqual(notes[0]['anchor_kind'], 'math')
        self.assertTrue(notes[0]['after'].startswith(chr(92) + 'operatorname{Tor}'))
        self.assertNotEqual(notes[0]['after'], 'Similarly,')


if __name__ == '__main__':
    unittest.main()
