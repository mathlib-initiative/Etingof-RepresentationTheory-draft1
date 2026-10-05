#!/usr/bin/env python3
"""Open a reader source PR only in the authoritative repository."""

import argparse
import json
from pathlib import Path
import subprocess

SOURCE_REPOSITORY = "mathlib-initiative/Etingof-RepresentationTheory-draft1"


def pr_command(repository, base, head, title, body_file):
    if repository != SOURCE_REPOSITORY:
        raise ValueError("Reader PRs must target the authoritative background repository")
    return [
        "gh", "pr", "create", "--repo", SOURCE_REPOSITORY,
        "--base", base, "--head", head, "--title", title,
        "--body-file", str(body_file),
    ]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", default=SOURCE_REPOSITORY)
    parser.add_argument("--head", required=True)
    parser.add_argument("--title", required=True)
    parser.add_argument("--body-file", type=Path, required=True)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    if args.repo != SOURCE_REPOSITORY:
        parser.error("Refusing a reader PR outside " + SOURCE_REPOSITORY)
    if not args.body_file.is_file():
        parser.error("The PR body file must exist")
    base = subprocess.run(
        ["gh", "api", "repos/" + SOURCE_REPOSITORY, "--jq", ".default_branch"],
        check=True, text=True, capture_output=True,
    ).stdout.strip()
    if not base:
        parser.error("Could not establish the authoritative default branch")
    command = pr_command(args.repo, base, args.head, args.title, args.body_file)
    if args.dry_run:
        print(json.dumps(command))
    else:
        subprocess.run(command, check=True)


if __name__ == "__main__":
    main()
