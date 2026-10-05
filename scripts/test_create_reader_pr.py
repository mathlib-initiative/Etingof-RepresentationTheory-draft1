import unittest

from create_reader_pr import SOURCE_REPOSITORY, pr_command


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


if __name__ == "__main__":
    unittest.main()
