"""Exact diagram/layout repairs must still reject every unreviewed TeX change."""

import hashlib
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest

PROJECT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT))
import validate_native_verso as validator


class ExactTexRepairTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.packets = {}
        for path in (PROJECT / "conversion-packets").glob("*/*/*/Content.lean"):
            item = json.loads(path.with_name("packet.json").read_text())["item"]["id"]
            if item in validator.TEX_REPAIRS:
                cls.packets[item] = path

    def test_all_seven_reviewed_packets_pass_without_tex_waivers(self):
        self.assertEqual(len(self.packets), 7)
        for item, path in self.packets.items():
            with self.subTest(item=item):
                self.assertNotIn("tex", validator.FIDELITY_WAIVERS.get(item, {}))
                self.assertEqual(validator.validate(path), [])

    def test_changed_source_invalidates_each_reviewed_repair(self):
        for item, path in self.packets.items():
            source_hash = hashlib.sha256(path.with_name("source.md").read_bytes()).hexdigest()
            self.assertEqual(source_hash, validator.TEX_REPAIRS[item]["source_sha256"])
            with self.assertRaisesRegex(ValueError, "source hash changed"):
                validator.expected_native_tex(item, "0" * 64, [])

    def test_unreviewed_items_keep_the_original_ordered_comparison(self):
        original = ["x", "y"]
        self.assertEqual(validator.expected_native_tex("unreviewed", "0" * 64, original), original)

    def test_every_formula_mutation_is_rejected(self):
        tested = 0
        with tempfile.TemporaryDirectory(prefix="etingof-tex-repair-test-") as temp:
            destination = Path(temp) / "Content.lean"
            for item, path in self.packets.items():
                for name in ("packet.json", "source.md"):
                    shutil.copyfile(path.with_name(name), destination.with_name(name))
                original = path.read_text()
                for match in validator.NATIVE_TEX.finditer(original):
                    with self.subTest(item=item, formula=tested):
                        group = 1 if match.group(1) is not None else 2
                        changed = original[:match.end(group)] + r"\,+1" + original[match.end(group):]
                        destination.write_text(changed)
                        self.assertTrue(any("TeX payload mismatch" in e for e in validator.validate(destination)))
                        tested += 1
                for changed in (original + "\n$`unreviewed`\n",
                                validator.NATIVE_TEX.sub("", original, count=1)):
                    destination.write_text(changed)
                    self.assertTrue(any("TeX payload mismatch" in e for e in validator.validate(destination)))
        self.assertEqual(tested, 172)


if __name__ == "__main__":
    unittest.main()
