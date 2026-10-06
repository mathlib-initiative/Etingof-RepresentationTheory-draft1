"""Reader fixes must survive regeneration from their authoritative inputs."""

import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

PROJECT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT))
from assemble_verso_release import retitle_document
from validate_release_candidate import available_declarations
import validate_native_verso as validator


class ReaderRegenerationTests(unittest.TestCase):
    def test_retitle_updates_a_previously_renamed_heading_and_keeps_unicode(self):
        original = '#doc (Manual) "Old title" =>\n\n# Previously renamed title\n\nOriginal prose.\n'
        updated = retitle_document(original, "Representations of Sₙ")
        self.assertIn('#doc (Manual) "Representations of Sₙ" =>', updated)
        self.assertIn('\n# Representations of Sₙ\n', updated)
        self.assertNotIn(r'\u2099', updated)
        self.assertTrue(updated.endswith('Original prose.\n'))

    def test_retitle_rejects_a_missing_document_header(self):
        with self.assertRaisesRegex(ValueError, 'top-level document title'):
            retitle_document('# Old heading\n', 'New heading')

    def test_every_generated_module_reproduces_the_staged_reading_edition(self):
        with tempfile.TemporaryDirectory(prefix='etingof-reader-regeneration-test-') as temp:
            root = Path(temp)
            (root / 'metadata').mkdir()
            shutil.copyfile(PROJECT / 'verso/release/metadata/reader-titles.json',
                            root / 'metadata/reader-titles.json')
            available = root / 'available.json'
            available.write_text(json.dumps(available_declarations()))
            result = subprocess.run([
                sys.executable, str(PROJECT / 'assemble_verso_release.py'),
                str(PROJECT / 'verso/metadata'), str(PROJECT / 'conversion-packets'), str(root),
                '--alignment-edges', str(PROJECT / 'manifests/alignment/adjudicated-alignment-edges.jsonl'),
                '--source-nodes', str(PROJECT / 'manifests/alignment/source-nodes.jsonl'),
                '--cleanroom-proposals', str(PROJECT / 'manifests/alignment/cleanroom-proposals.jsonl'),
                '--available-declarations', str(available),
                '--approved-items', str(PROJECT / 'manifests/book/approved-verso-items.json'),
            ], check=True, capture_output=True, text=True)
            self.assertEqual(json.loads(result.stdout)['converted_items'], 583)
            generated = root / 'IntroductionToRepresentationTheoryVerso'
            staged = PROJECT / 'verso/release/IntroductionToRepresentationTheoryVerso'
            paths = {p.relative_to(generated) for p in generated.rglob('*.lean')}
            staged_paths = {p.relative_to(staged) for kind in ('Content', 'Structure')
                            for p in (staged / kind).rglob('*.lean')}
            self.assertEqual(paths, staged_paths)
            self.assertEqual(len(paths), 690)
            for relative in sorted(paths):
                with self.subTest(module=str(relative)):
                    self.assertEqual((generated / relative).read_text().rstrip(),
                                     (staged / relative).read_text().rstrip())
            for filename in ('GeneratedImports.lean', 'IntroductionToRepresentationTheoryVerso.lean'):
                self.assertEqual((root / filename).read_text().rstrip(),
                                 (PROJECT / 'verso/release' / filename).read_text().rstrip())

    def test_frobenius_footnote_retains_its_reference_and_entire_body(self):
        source = PROJECT / 'conversion-packets/sol/Chapter5/Theorem5.14.3'
        original = (source / 'Content.lean').read_text()
        reference = '[^Chapter5/Theorem5.14.3/footnote-1]'
        with tempfile.TemporaryDirectory(prefix='etingof-frobenius-note-test-') as temp:
            destination = Path(temp) / 'Content.lean'
            for name in ('source.md', 'packet.json'):
                shutil.copyfile(source / name, destination.with_name(name))
            mutations = (
                original.replace(reference, '', 1),
                original.replace(reference, reference + reference, 1),
                original.replace('to be zero.', 'to be one.'),
            )
            for changed in mutations:
                destination.write_text(changed)
                self.assertTrue(any('footnote' in error for error in validator.validate(destination)))


if __name__ == '__main__':
    unittest.main()
