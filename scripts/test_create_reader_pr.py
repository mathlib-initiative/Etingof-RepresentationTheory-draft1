import unittest
from pathlib import Path
import tempfile

from create_reader_pr import SOURCE_REPOSITORY, assert_generated_workflow_boundaries, pr_command


class RepositoryBoundaryTests(unittest.TestCase):
    def test_authoritative_repo_and_default_branch_are_explicit(self):
        command = pr_command(SOURCE_REPOSITORY, "main", "reader", "Reader", "body.md")
        self.assertEqual(command[command.index("--repo") + 1], SOURCE_REPOSITORY)
        self.assertEqual(command[command.index("--base") + 1], "main")

    def test_each_materialized_destination_is_rejected(self):
        for name in (
            "EtingofRepresentationTheory",
            "EtingofRepresentationTheory-verso",
            "EtingofRepresentationTheory-verso-pages",
        ):
            with self.subTest(name=name), self.assertRaises(ValueError):
                pr_command("mathlib-initiative/" + name, "main", "reader", "Reader", "body.md")

    def test_arbitrary_other_repository_is_rejected(self):
        with self.assertRaises(ValueError):
            pr_command("someone/a-fork", "main", "reader", "Reader", "body.md")

    def test_actual_generated_workflows_have_no_source_pr_automation(self):
        assert_generated_workflow_boundaries(Path(__file__).resolve().parents[1])

    def fixture_workflows(self, root):
        for release in ("clean-code/release", "verso/release"):
            directory = Path(root) / release / ".github/workflows"
            directory.mkdir(parents=True)
            (directory / "ci.yml").write_text("name: Build\npermissions:\n  contents: read\n")

    def test_extra_generated_workflow_is_rejected(self):
        with tempfile.TemporaryDirectory() as root:
            self.fixture_workflows(root)
            path = Path(root) / "verso/release/.github/workflows/update.yml"
            path.write_text("run: gh pr create\n")
            with self.assertRaises(ValueError):
                assert_generated_workflow_boundaries(root)

    def test_source_or_pr_mutation_in_ci_is_rejected(self):
        for mutation in ("gh pr create", "gh pr merge", "git commit", "git push",
                         "pull-requests: write", "uses: peter-evans/create-pull-request@v7"):
            with self.subTest(mutation=mutation), tempfile.TemporaryDirectory() as root:
                self.fixture_workflows(root)
                path = Path(root) / "verso/release/.github/workflows/ci.yml"
                path.write_text("name: Build\nrun: " + mutation + "\n")
                with self.assertRaises(ValueError):
                    assert_generated_workflow_boundaries(root)


if __name__ == "__main__":
    unittest.main()
