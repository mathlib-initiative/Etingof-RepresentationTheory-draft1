"""Completion must cover every semantic item, not only annotated examples."""

import json
from pathlib import Path
import tempfile
import unittest

from reader_review import audit


class ReviewTests(unittest.TestCase):
    def test_legacy_routes_cannot_be_silently_ignored_outside_routes_map(self):
        self.write("reader-legacy-routes.json", {"routes": {}, "C___One": {"route": "Old/"}})
        with self.assertRaisesRegex(ValueError, "inside the routes map"):
            audit(metadata=self.metadata, emit=False)
        self.write("reader-legacy-routes.json", {"routes": {"Old/": {"key": "C___One"}}})
        with self.assertRaisesRegex(ValueError, "saved anchors"):
            audit(metadata=self.metadata, emit=False)

    def test_duplicate_editorial_keys_are_rejected(self):
        for name in ("reader-titles.json", "reader-annotations.json", "reader-reviews.json",
                     "reader-legacy-routes.json", "reader-joins.json"):
            with self.subTest(name=name):
                path = self.metadata / name
                existed = path.exists()
                before = path.read_text() if existed else None
                path.write_text('{"Chapter2/One": "new", "Chapter2/One": "stale"}')
                with self.assertRaisesRegex(ValueError, "duplicate editorial metadata key"):
                    audit(metadata=self.metadata, emit=False)
                if existed:
                    path.write_text(before)
                else:
                    path.unlink()

    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.metadata = Path(self.directory.name)
        self.write("items.json", {"items": [{"id": "Chapter2/One"}, {"id": "Chapter3/Two"}]})
        self.write("reader-annotations.json", {"Chapter2/One": [{"declarations": [{"name": "One.result"}]}]})
        self.write("declaration-sources.json", {"One.result": "One"})
        self.reviews = {"Chapter2/One": {"decision": "annotated", "source_modules": ["One"],
                                        "comparison": "Read and compared the exact statement."}}
        self.write("reader-reviews.json", self.reviews)

    def write(self, filename, data):
        (self.metadata / filename).write_text(json.dumps(data), encoding="utf-8")

    def test_polished_sample_is_incomplete(self):
        report = audit(metadata=self.metadata, emit=False)
        self.assertEqual((report["reviewed_items"], report["pending_items"]), (1, 1))
        self.assertEqual(report["status"], "incomplete")
        with self.assertRaises(SystemExit):
            audit(True, self.metadata, emit=False)

    def test_reviewed_book_only_item_counts(self):
        self.reviews["Chapter3/Two"] = {"decision": "book_prose_only",
                                      "comparison": "Transition sentence with no mathematical statement to explain."}
        self.write("reader-reviews.json", self.reviews)
        self.assertEqual(audit(True, self.metadata, emit=False)["status"], "complete")

    def test_explicit_coverage_gap_counts_as_review_not_as_a_proof(self):
        self.reviews["Chapter3/Two"] = {"decision": "unformalized", "comparison": "Compared prose with coverage.",
                                      "coverage_gap": "The Lie-group correspondence is not proved."}
        self.write("reader-reviews.json", self.reviews)
        self.write("reader-annotations.json", {
            "Chapter2/One": [{"declarations": [{"name": "One.result"}]}],
            "Chapter3/Two": [{"kind": "coverage_gap", "explanation": ["Not formalized here."]}]})
        report = audit(True, self.metadata, emit=False)
        self.assertEqual(report["status"], "complete")
        self.assertEqual(report["unformalized_items"][0]["item"], "Chapter3/Two")

    def test_gap_cannot_claim_checked_declarations(self):
        self.reviews["Chapter2/One"].update(decision="unformalized", coverage_gap="No checked result.")
        self.write("reader-reviews.json", self.reviews)
        with self.assertRaises(SystemExit):
            audit(metadata=self.metadata, emit=False)

    def test_partial_gap_needs_a_reader_note_and_is_reported(self):
        self.reviews["Chapter2/One"]["coverage_gap"] = "Only part (b) is proved."
        self.write("reader-reviews.json", self.reviews)
        with self.assertRaises(SystemExit):
            audit(metadata=self.metadata, emit=False)
        self.write("reader-annotations.json", {"Chapter2/One": [
            {"declarations": [{"name": "One.result"}]},
            {"kind": "coverage_gap", "explanation": ["Parts (a) and (c) are not proved."]}]})
        report = audit(metadata=self.metadata, emit=False)
        self.assertEqual(report["partial_formalization_gaps"][0]["item"], "Chapter2/One")

    def test_annotation_without_comparison_is_rejected(self):
        self.write("reader-reviews.json", {})
        with self.assertRaises(SystemExit):
            audit(metadata=self.metadata, emit=False)

    def test_unmapped_checked_declaration_is_rejected(self):
        self.write("declaration-sources.json", {"Other.result": "One"})
        with self.assertRaises(SystemExit):
            audit(metadata=self.metadata, emit=False)

    def test_upstream_only_review_requires_mathlib_evidence_and_links(self):
        self.reviews["Chapter2/One"].pop("source_modules")
        self.reviews["Chapter2/One"]["upstream_source_modules"] = ["Mathlib.LinearAlgebra.TensorProduct.Map"]
        self.write("reader-reviews.json", self.reviews)
        with self.assertRaises(SystemExit):
            audit(metadata=self.metadata, emit=False)
        self.write("reader-annotations.json", {"Chapter2/One": [{"links": [{"name": "TensorProduct.map"}]}]})
        self.assertEqual(audit(metadata=self.metadata, emit=False)["reviewed_items"], 1)
        self.reviews["Chapter2/One"]["upstream_source_modules"] = ["Invented.Module"]
        self.write("reader-reviews.json", self.reviews)
        with self.assertRaises(SystemExit):
            audit(metadata=self.metadata, emit=False)


if __name__ == "__main__":
    unittest.main()
