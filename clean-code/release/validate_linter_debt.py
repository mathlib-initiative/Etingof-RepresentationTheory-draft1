#!/usr/bin/env python3
"""Reject silent expansion or accidental concealment of the release's linter debt."""

from __future__ import annotations

from collections import Counter
import json
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parent
LEDGER = ROOT / "linter-debt.json"
LAKEFILE = ROOT / "lakefile.toml"
GLOBAL_PATTERN = re.compile(
    r"^(?P<option>(?:weak\.)?linter\.[A-Za-z0-9_.]+)\s*=\s*false\s*$",
    re.MULTILINE,
)
LOCAL_PATTERN = re.compile(r"\bset_option\s+(linter\.[A-Za-z0-9_.]+)\s+false\b")


def fail(message: str) -> None:
    raise SystemExit(message)


def main() -> None:
    ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
    expected_global = set(ledger["global_suppressions"])
    actual_global = set(GLOBAL_PATTERN.findall(LAKEFILE.read_text(encoding="utf-8")))
    if actual_global != expected_global:
        fail(
            "global linter suppressions differ from linter-debt.json: "
            f"missing={sorted(expected_global - actual_global)}, "
            f"unexpected={sorted(actual_global - expected_global)}"
        )

    counts: Counter[str] = Counter()
    files: set[str] = set()
    sources = sorted((ROOT / "RepresentationTheory").rglob("*.lean"))
    sources.extend(
        source
        for source in (ROOT / "AlignmentExport.lean", ROOT / "RepresentationTheory.lean")
        if source.is_file()
    )
    for source in sources:
        relative = source.relative_to(ROOT).as_posix()
        matches = LOCAL_PATTERN.findall(source.read_text(encoding="utf-8"))
        if matches:
            files.add(relative)
            counts.update(matches)

    expected_counts = Counter(ledger["local_suppressions"])
    if counts != expected_counts:
        fail(
            "local linter suppressions differ from linter-debt.json: "
            f"expected={dict(sorted(expected_counts.items()))}, "
            f"actual={dict(sorted(counts.items()))}"
        )
    if sum(counts.values()) != ledger["local_directives"]:
        fail("local linter directive total differs from linter-debt.json")
    if len(files) != ledger["local_files"]:
        fail(
            "local linter-suppression file count differs from linter-debt.json: "
            f"expected={ledger['local_files']}, actual={len(files)}"
        )

    print(
        json.dumps(
            {
                "global_suppressions": len(actual_global),
                "local_directives": sum(counts.values()),
                "local_files": len(files),
                "local_linter_classes": len(counts),
                "tracking_issue": ledger["tracking_issue"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
