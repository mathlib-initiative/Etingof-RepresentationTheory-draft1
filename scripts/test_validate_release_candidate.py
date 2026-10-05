"""Editorial presentation files must not weaken the immutable-corpus gate."""

import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import validate_release_candidate as gate


class PrivateSourceIntegrityTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="etingof-source-integrity-")
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.release = self.root / "verso/release"
        self.patches = [patch.object(gate, "ROOT", self.root), patch.object(gate, "VERSO", self.release)]
        for p in self.patches:
            p.start()
            self.addCleanup(p.stop)
        for base in (self.root / "verso", self.release):
            (base / "source-markdown").mkdir(parents=True)
            (base / "metadata").mkdir()
            (base / "source-markdown/1.md").write_text("Original paragraph.\n")
            (base / "metadata/items.json").write_text(json.dumps({
                "schema_version": "items/v1", "items": [{
                    "id": "Chapter3/Introduction", "title": "Old title", "source_sha256": "abc"
                }]
            }))
        (self.release / "metadata/reader-titles.json").write_text(json.dumps({
            "Chapter3/Introduction": "Readable title"
        }))
        item_path = self.release / "metadata/items.json"
        self.edition = json.loads(item_path.read_text())
        self.edition["items"][0]["title"] = "Readable title"
        item_path.write_text(json.dumps(self.edition))

    def test_declared_editorial_title_is_allowed(self):
        gate.assert_private_sources_exact()

    def test_editorial_page_join_records_are_allowed_without_changing_the_corpus(self):
        (self.release / "metadata/reader-joins.json").write_text("[]")
        gate.assert_private_sources_exact()

    def test_unregistered_title_change_is_rejected(self):
        self.edition["items"][0]["title"] = "Another title"
        (self.release / "metadata/items.json").write_text(json.dumps(self.edition))
        with self.assertRaises(SystemExit):
            gate.assert_private_sources_exact()

    def add_structure_metadata(self):
        book = {"nodes": [{"node_id": "chapter-03/section-3-1", "number": "3.1",
                           "title": "Original section title"}]}
        for base in (self.root / "verso", self.release):
            (base / "metadata/book.json").write_text(json.dumps(book))
        return book

    def test_declared_structure_title_preserves_original_book_metadata(self):
        self.add_structure_metadata()
        (self.release / "metadata/reader-titles.json").write_text(json.dumps({
            "Chapter3/Introduction": "Readable title",
            "chapter-03/section-3-1": "Readable section title"
        }))
        gate.assert_private_sources_exact()

    def test_unknown_structure_title_is_rejected(self):
        self.add_structure_metadata()
        (self.release / "metadata/reader-titles.json").write_text(json.dumps({
            "Chapter3/Introduction": "Readable title",
            "chapter-03/section-3-99": "Unknown section"
        }))
        with self.assertRaises(SystemExit):
            gate.assert_private_sources_exact()

    def test_structure_override_does_not_allow_changing_original_book(self):
        book = self.add_structure_metadata()
        book["nodes"][0]["title"] = "Changed source title"
        (self.release / "metadata/book.json").write_text(json.dumps(book))
        (self.release / "metadata/reader-titles.json").write_text(json.dumps({
            "Chapter3/Introduction": "Readable title",
            "chapter-03/section-3-1": "Changed source title"
        }))
        with self.assertRaises(SystemExit):
            gate.assert_private_sources_exact()

    def test_source_span_metadata_change_is_rejected(self):
        self.edition["items"][0]["source_sha256"] = "changed"
        (self.release / "metadata/items.json").write_text(json.dumps(self.edition))
        with self.assertRaises(SystemExit):
            gate.assert_private_sources_exact()

    def test_book_paragraph_change_is_rejected(self):
        (self.release / "source-markdown/1.md").write_text("Changed paragraph.\n")
        with self.assertRaises(SystemExit):
            gate.assert_private_sources_exact()

    def test_unknown_metadata_file_is_rejected(self):
        (self.release / "metadata/unexpected.json").write_text("{}")
        with self.assertRaises(SystemExit):
            gate.assert_private_sources_exact()

    def test_missing_original_metadata_is_rejected(self):
        (self.release / "metadata/items.json").unlink()
        with self.assertRaises(SystemExit):
            gate.assert_private_sources_exact()


if __name__ == "__main__":
    unittest.main()
