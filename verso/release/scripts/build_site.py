#!/usr/bin/env python3
# Copyright (c) 2026 American Mathematical Society. All rights reserved.
"""Build the book after removing output left by earlier renders."""

from __future__ import annotations

import shutil
import subprocess
import sys
import tomllib
from pathlib import Path


def main() -> None:
    root = Path(__file__).resolve().parent.parent
    html = root / "_out" / "html-multi"
    if html.exists():
        shutil.rmtree(html)
    subprocess.run(["lake", "build", "--iofail"], cwd=root, check=True)
    alignment = root / "alignment-export.json"
    with alignment.open("w", encoding="utf-8") as output:
        subprocess.run(["lake", "exe", "alignmentExport"], cwd=root, stdout=output, check=True)
    subprocess.run([sys.executable, "scripts/sync_formalization_panels.py", "--check", str(alignment)],
                   cwd=root, check=True)
    subprocess.run(["lake", "exe", "book"], cwd=root, check=True)
    config = tomllib.loads((root / "lakefile.toml").read_text(encoding="utf-8"))
    formalization = next(item for item in config["require"]
                         if item["name"] == "RepresentationTheoryFormalization")
    command = [sys.executable, "scripts/prepare_reader.py", str(html), "--alignment-export", str(alignment)]
    if formalization.get("rev"):
        command.extend(["--formalization-revision", formalization["rev"]])
    subprocess.run(command, cwd=root, check=True)
    subprocess.run([sys.executable, "scripts/validate_reader.py", str(html)], cwd=root, check=True)


if __name__ == "__main__":
    main()
