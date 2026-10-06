"""Readable structural labels must survive release assembly without source edits."""

import json
from pathlib import Path
import sys
import unittest

PROJECT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(PROJECT))
from assemble_verso_release import structure_display_title


class StructureTitleTests(unittest.TestCase):
    def test_override_keeps_number_and_does_not_mutate_node(self):
        node = {"node_id": "chapter-02/section-2-15", "number": "2.15",
                "title": r"Representations of $\mathfrak{sl}(2)$"}
        original = dict(node)
        result = structure_display_title(node, {node["node_id"]: "Representations of sl₂"})
        self.assertEqual(result, "2.15. Representations of sl₂")
        self.assertEqual(node, original)

    def test_unoverridden_and_unnumbered_titles_are_preserved(self):
        self.assertEqual(structure_display_title(
            {"node_id": "chapter-01", "number": "1", "title": "Introduction"}, {}),
            "1. Introduction")
        self.assertEqual(structure_display_title(
            {"node_id": "frontmatter", "title": "Preface"}, {}), "Preface")

    def test_actual_sl2_override_matches_native_and_preserves_original_book(self):
        release = PROJECT / "verso/release"
        self.assertEqual((release / "metadata/book.json").read_bytes(),
                         (PROJECT / "verso/metadata/book.json").read_bytes())
        book = json.loads((release / "metadata/book.json").read_text())
        titles = json.loads((release / "metadata/reader-titles.json").read_text())
        node = next(n for n in book["nodes"] if n["node_id"] == "chapter-02/section-2-15")
        expected = json.dumps(structure_display_title(node, titles), ensure_ascii=False)
        native = (release / "IntroductionToRepresentationTheoryVerso/Structure/Chapter02/Section215.lean")
        self.assertIn(f"#doc (Manual) {expected} =>", native.read_text())

    def test_small_quiver_structural_titles_are_readable_and_regenerable(self):
        release = PROJECT / "verso/release"
        book = json.loads((release / "metadata/book.json").read_text())
        titles = json.loads((release / "metadata/reader-titles.json").read_text())
        for key, filename in (("chapter-06/section-6-2", "Section62.lean"),
                              ("chapter-06/section-6-3", "Section63.lean")):
            node = next(n for n in book["nodes"] if n["node_id"] == key)
            display = structure_display_title(node, titles)
            self.assertNotIn("$", display)
            self.assertNotIn("\\_", display)
            native = release / "IntroductionToRepresentationTheoryVerso/Structure/Chapter06" / filename
            self.assertIn(f"#doc (Manual) {json.dumps(display, ensure_ascii=False)} =>", native.read_text())


if __name__ == "__main__":
    unittest.main()
