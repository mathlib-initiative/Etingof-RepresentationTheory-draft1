"""Guard the Gabriel diagrams restored from printed pages 7–8.

Check both the generating conversion packet and the materialized native source:
otherwise rebuilding the release could silently restore the conversion defect.
"""

from pathlib import Path
import re
import unittest


PROJECT = Path(__file__).resolve().parents[3]
SOURCES = (
    PROJECT / "conversion-packets/sol/Chapter2/Theorem2.1.2/Content.lean",
    PROJECT / "verso/release/IntroductionToRepresentationTheoryVerso/Content/Chapter2/Theorem212.lean",
)


def diagrams(path):
    text = path.read_text(encoding="utf-8")
    return dict(re.findall(r"- _\$`([^`]+)`:_\s+\$\$`([^`]+)`", text))


def array_rows(display):
    match = re.fullmatch(r"\\begin\{array\}\{(c+)\}\s*(.*?)\s*\\end\{array\}",
                         display, re.S)
    if match is None:
        raise AssertionError("Expected a mathematical array, not an ASCII sketch")
    rows = [[cell.strip() for cell in row.split("&")]
            for row in match[2].split(r"\\")]
    if len(rows) != 3 or len(rows[0]) != len(match[1]):
        raise AssertionError("Malformed diagram array")
    return rows


class GabrielDiagramTests(unittest.TestCase):
    def test_all_five_diagrams_are_math_and_survive_materialization(self):
        packet, native = (diagrams(path) for path in SOURCES)
        self.assertEqual(set(packet), {"A_n", "D_n", "E_6", "E_7", "E_8"})
        self.assertEqual(native, packet)
        for display in native.values():
            self.assertIn(r"\circ", display)

    def test_d_branch_is_at_the_penultimate_chain_vertex(self):
        for path in SOURCES:
            with self.subTest(source=path):
                chain, connector, leaf = array_rows(diagrams(path)["D_n"])
                vertices = [i for i, cell in enumerate(chain) if cell == r"\circ"]
                self.assertEqual(vertices, [0, 2, 4, 8, 10])
                self.assertEqual(chain[6], r"\cdots")
                self.assertEqual(connector[-1], "|")
                self.assertEqual(leaf[-1], r"\circ")
                self.assertEqual(len(connector) - 1, vertices[-2])
                self.assertEqual(len(leaf), len(connector))

    def test_e_diagrams_have_the_right_order_and_third_vertex_branch(self):
        for path in SOURCES:
            for order in (6, 7, 8):
                with self.subTest(source=path, order=order):
                    chain, connector, leaf = array_rows(diagrams(path)[f"E_{order}"])
                    vertices = [i for i, cell in enumerate(chain) if cell == r"\circ"]
                    self.assertEqual(len(vertices) + 1, order)
                    self.assertEqual(vertices, list(range(0, 2 * (order - 1), 2)))
                    self.assertTrue(all(cell == r"\text{---}" for cell in chain[1::2]))
                    self.assertEqual(connector[-1], "|")
                    self.assertEqual(leaf[-1], r"\circ")
                    self.assertEqual(len(connector) - 1, vertices[2])
                    self.assertEqual(len(leaf), len(connector))


if __name__ == "__main__":
    unittest.main()
