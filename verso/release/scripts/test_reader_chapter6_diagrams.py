"""Source and graph checks for the diagrams restored from printed pages 150–152."""

from pathlib import Path
import re
import unittest

from test_reader_diagrams import diagrams, array_rows


PROJECT = Path(__file__).resolve().parents[3]
PACKETS = PROJECT / "conversion-packets"
NATIVE = PROJECT / "verso/release/IntroductionToRepresentationTheoryVerso/Content/Chapter6"
FILES = (
    (PACKETS / "terra/Chapter6/Theorem_Dynkin_classification/Content.lean",
     NATIVE / "TheoremDynkinClassification.lean"),
    (PACKETS / "sol/Chapter6/Problem6.1.3_continued_E7_E8/Content.lean",
     NATIVE / "Problem613ContinuedE7E8.lean"),
    (PACKETS / "sol/Chapter6/Problem6.1.3_continued_tildeE/Content.lean",
     NATIVE / "Problem613ContinuedTildeE.lean"),
)


class Chapter6DiagramTests(unittest.TestCase):
    def test_a3_subspace_diagrams_keep_space_labels_below_vertex_dots(self):
        paths = (PACKETS / "sol/Chapter6/Example6.2.4/Content.lean", NATIVE / "Example624.lean")
        displays = [re.findall(r"\$\$`([^`]+)`", path.read_text()) for path in paths]
        self.assertEqual(displays[0], displays[1])
        for path in paths:
            source = path.read_text()
            self.assertNotIn(r"\overset{\bullet}", source)
            self.assertIn(r"\underset{V \cap Y}{\bullet}", source)
            self.assertIn(r"\underset{V \oplus Y}{\bullet}", source)

    def test_every_drawing_survives_source_regeneration_as_one_math_display(self):
        for pair, expected in zip(FILES, (3, 4, 3)):
            packet, native = (re.findall(r"\$\$`([^`]+)`", path.read_text()) for path in pair)
            self.assertEqual(native, packet)
            self.assertEqual(len(native), expected)
            self.assertTrue(all(r"\hspace" not in drawing for drawing in native))
        self.assertEqual(set(diagrams(FILES[0][1])), {"A_n", "D_n", "E_6"})
        self.assertEqual(set(diagrams(FILES[1][1])), {"E_7", "E_8"})

    def test_finite_branches_match_the_original_diagrams(self):
        for pair in FILES[:2]:
            for path in pair:
                for name, display in diagrams(path).items():
                    if name == "A_n":
                        continue
                    chain, connector, leaf = array_rows(display)
                    vertices = [i for i, value in enumerate(chain) if value == r"\circ"]
                    expected = vertices[-2] if name == "D_n" else vertices[2]
                    self.assertEqual(len(connector) - 1, expected)
                    self.assertEqual(connector[-1], "|")
                    self.assertEqual(leaf[-1], r"\circ")
                    if name.startswith("E_"):
                        self.assertEqual(len(vertices) + 1, int(name[2:]))

    def test_affine_labels_and_branch_positions_form_a_positive_kernel_vector(self):
        expected = {r"\tilde{E}_6": ([1, 2, 3, 2, 1], 2, [1, 2]),
                    r"\tilde{E}_7": ([1, 2, 3, 4, 3, 2, 1], 3, [2]),
                    r"\tilde{E}_8": ([1, 2, 3, 4, 5, 6, 4, 2], 5, [3])}
        for path in FILES[2]:
            self.assertEqual(set(diagrams(path)), set(expected))
            for name, display in diagrams(path).items():
                match = re.fullmatch(r"\\begin\{array\}\{(c+)\}\s*(.*?)\s*\\end\{array\}",
                                     display, re.S)
                self.assertIsNotNone(match)
                rows = [[cell.strip() for cell in row.split("&")]
                        for row in match[2].split(r"\\")]
                main, branch, arm = expected[name]
                self.assertEqual(len(rows[-1]), 2 * len(main) - 1)
                self.assertEqual(len(match[1]), len(rows[-1]))
                labels = [int(n) for n in re.findall(r"\\overset\{(\d+)\}\{\\bullet\}", " ".join(rows[-1]))]
                self.assertEqual(labels, main)
                for level, value in enumerate(arm):
                    label_row, edge_row = rows[2 * level:2 * level + 2]
                    nonempty = [(i, v) for i, v in enumerate(label_row) if v]
                    self.assertEqual(nonempty, [(2 * branch, rf"\overset{{{value}}}{{\bullet}}")])
                    self.assertEqual([(i, v) for i, v in enumerate(edge_row) if v], [(2 * branch, "|")])
                # Independently check the graph's weighted adjacency relation,
                # not just a text snapshot of its labels: Rm = 2m.
                marks = main + list(reversed(arm))
                neighbors = [set() for _ in marks]
                def edge(a, b):
                    neighbors[a].add(b)
                    neighbors[b].add(a)
                for i in range(len(main) - 1):
                    edge(i, i + 1)
                edge(branch, len(main))
                for i in range(len(main), len(marks) - 1):
                    edge(i, i + 1)
                self.assertTrue(all(m > 0 for m in marks))
                self.assertTrue(all(2 * value == sum(marks[j] for j in neighbors[i])
                                    for i, value in enumerate(marks)))

    def test_cycle_is_closed_and_double_fork_keeps_all_labels(self):
        for path in FILES[1]:
            displays = re.findall(r"\$\$`([^`]+)`", path.read_text())
            cycle, fork = displays[-2:]
            self.assertIn(r"\begin{array}", cycle)
            chain, connectors, base = array_rows(cycle)
            self.assertEqual([i for i, cell in enumerate(chain) if r"\bullet" in cell], [0, 2, 4])
            self.assertEqual([i for i, cell in enumerate(base) if r"\bullet" in cell], [0, 4])
            self.assertEqual(connectors, ["|", "", "", "", "|"])
            self.assertEqual(base[2], r"\cdots")
            self.assertEqual(re.findall(r"\\overset\{(\d+)\}\{\\bullet\}", cycle), ["1"] * 5)
            self.assertEqual(re.findall(r"\\overset\{(\d+)\}\{\\bullet\}", fork),
                             ["1", "1", "2", "2", "1", "1"])
            body = re.search(r"\\begin\{array\}\{ccccc\}\s*(.*?)\s*\\end\{array\}", fork, re.S)[1]
            rows = [[cell.strip() for cell in row.split("&")] for row in body.split(r"\\")]
            self.assertEqual(len(rows), 5)
            self.assertEqual(rows[1], ["|", "", "", "", "|"])
            self.assertEqual(rows[3], rows[1])
            for row in (rows[0], rows[2], rows[4]):
                self.assertEqual([i for i, cell in enumerate(row) if r"\bullet" in cell], [0, 4])
            self.assertEqual(rows[2][2], r"\cdots")


if __name__ == "__main__":
    unittest.main()
