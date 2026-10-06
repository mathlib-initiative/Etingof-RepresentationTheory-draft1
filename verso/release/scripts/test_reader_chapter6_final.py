"""Keep restored paragraph boundaries in both packet and native sources."""

from pathlib import Path
import unittest


PROJECT = Path(__file__).resolve().parents[3]
NATIVE = PROJECT / "verso/release/IntroductionToRepresentationTheoryVerso/Content/Chapter6"
CASES = (
    ("Lemma6.7.2", "Lemma672", "`\n\nAssume the contrary,"),
    ("Corollary6.8.3", "Corollary683", "isomorphic._\n\n*Proof.* Let $`i` be the smallest integer"),
    ("Corollary6.8.4", "Corollary684", "`\n\nLet $`Q'` be the quiver"),
    ("Problem6.9.1", "Problem691", "with $`B`.\n\n(3) $`H_n`:"),
)


class Chapter6FinalParagraphTests(unittest.TestCase):
    def test_paragraph_boundaries_are_regeneration_inputs(self):
        for item, module, boundary in CASES:
            paths = (PROJECT / f"conversion-packets/sol/Chapter6/{item}/Content.lean",
                     NATIVE / f"{module}.lean")
            for path in paths:
                with self.subTest(path=path):
                    self.assertIn(boundary, path.read_text())


if __name__ == "__main__":
    unittest.main()
