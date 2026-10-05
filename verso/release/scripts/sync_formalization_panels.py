#!/usr/bin/env python3
# Copyright (c) 2026 American Mathematical Society. All rights reserved.
"""Regenerate Verso formalization panels from the pinned Lean release's attributes."""

from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from pathlib import Path


PACKAGE = "IntroductionToRepresentationTheoryVerso"
PANEL_MARKER = "\n\n## Formalization\n"
INLINE_PANEL_MARKER = "\n\n# Formalization\n"
REPRESENTATION_IMPORT = re.compile(r"^import RepresentationTheory(?:\.[A-Za-z0-9_'.]+)*\n", re.MULTILINE)
MATHEMATICAL_KINDS = frozenset(
    {
        "theorem",
        "lemma",
        "proposition",
        "corollary",
        "definition",
        "example",
        "exercise",
        "remark",
    }
)

def docstring_directive(declaration: str) -> str:
    return f"{{Manual.docstring {declaration}}}"


def escape_inline(value: str) -> str:
    for old, new in (
        ("\\", r"\\"),
        ("`", r"\`"),
        ("[", r"\["),
        ("]", r"\]"),
        ("*", r"\*"),
        ("_", r"\_"),
        ("{", r"\{"),
        ("}", r"\}"),
    ):
        value = value.replace(old, new)
    return value


def load_items(root: Path) -> list[dict]:
    payload = json.loads((root / "metadata/items.json").read_text(encoding="utf-8"))
    items = payload.get("items")
    if not isinstance(items, list):
        raise SystemExit("metadata/items.json does not contain an items array")
    return items


def load_rows(path: Path) -> list[dict]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, list):
        raise SystemExit("alignment export must be a JSON array")
    seen: set[tuple[str, str, str]] = set()
    rows = []
    for index, row in enumerate(payload):
        if not isinstance(row, dict) or set(row) != {"declaration", "imported", "reference", "role"}:
            raise SystemExit(f"alignment row {index} has the wrong schema")
        if row["role"] not in {"primary", "supporting"}:
            raise SystemExit(f"alignment row {index} has invalid role {row['role']!r}")
        if not all(
            isinstance(row[key], str) and row[key]
            for key in ("declaration", "reference", "role")
        ) or not isinstance(row["imported"], bool):
            raise SystemExit(f"alignment row {index} contains a blank or non-string field")
        key = (row["declaration"], row["reference"], row["role"])
        if key in seen:
            raise SystemExit(f"duplicate alignment row: {key}")
        seen.add(key)
        rows.append(row)
    return rows


def resolve_item(reference: str, item_ids: set[str]) -> str:
    matches = [item_id for item_id in item_ids if reference == item_id or reference.startswith(item_id + "/")]
    if not matches:
        raise SystemExit(f"alignment reference does not resolve to a semantic item: {reference}")
    longest = max(len(item_id) for item_id in matches)
    winners = [item_id for item_id in matches if len(item_id) == longest]
    if len(winners) != 1:
        raise SystemExit(f"ambiguous semantic item for alignment reference {reference}: {winners}")
    return winners[0]


def panel(item_id: str, rows: list[dict], heading_level: int = 2) -> str:
    # Multiple source nodes (including derived nodes) may map to the same
    # semantic item. Render each declaration once, with primary taking
    # precedence when those source-node edges have different roles.
    primary = {row["declaration"] for row in rows if row["role"] == "primary"}
    by_role = {
        "primary": primary,
        "supporting": {
            row["declaration"] for row in rows if row["role"] == "supporting"
        }
        - primary,
    }
    groups = []
    for role, title in (("primary", "Primary declarations"), ("supporting", "Supporting declarations")):
        declarations = sorted(by_role[role])
        if not declarations:
            continue
        body = [f"{'#' * (heading_level + 1)} {title}"]
        for declaration in declarations:
            imported_rows = sorted(
                (
                    row
                    for row in rows
                    if row["declaration"] == declaration and row["imported"]
                ),
                key=lambda row: (row["reference"], row["role"]),
            )
            if imported_rows:
                body.append("Declaration: " + escape_inline(declaration))
            else:
                body.append(docstring_directive(declaration))
            for row in imported_rows:
                body.append(
                    escape_inline(
                        f"Alignment metadata: book-ref={row['reference']}; role={row['role']}"
                    )
                )
        groups.append("\n\n".join(body))
    return (
        "\n\n" + "#" * heading_level + " Formalization\n"
        + "%%%\n"
        + f"tag := {json.dumps(item_id + '/formalization')}\n"
        + "number := false\n"
        + "%%%\n\n"
        + "\n\n".join(groups)
        + "\n"
    )


def content_path(root: Path, module: str) -> Path:
    return root / (module.replace(".", "/") + ".lean")


def inline_structure_path(root: Path, item: dict) -> Path | None:
    projection = item.get("verso_projection", {})
    if not projection.get("structure_only") or not projection.get("inline_in_structure"):
        return None
    match = re.fullmatch(r"chapter-(\d+)", item["node_id"])
    if match is None:
        raise SystemExit(f"unsupported inline structure node for {item['id']}: {item['node_id']}")
    chapter = match.group(1)
    return root / PACKAGE / "Structure" / f"Chapter{chapter}.lean"


def update_content(source: str, item_id: str, rows: list[dict]) -> str:
    if source.count(PANEL_MARKER) > 1:
        raise SystemExit(f"multiple formalization panels in {item_id}")
    base = source.split(PANEL_MARKER, 1)[0].rstrip()
    base = REPRESENTATION_IMPORT.sub("", base)
    if rows:
        lines = base.splitlines(keepends=True)
        import_indices = [index for index, line in enumerate(lines) if line.startswith("import ")]
        if not import_indices:
            raise SystemExit(f"no import location in {item_id}")
        lines.insert(import_indices[-1] + 1, "import RepresentationTheory\n")
        base = "".join(lines).rstrip()
        return base + panel(item_id, rows)
    return base + "\n"


def update_inline_structure(source: str, item_id: str, rows: list[dict]) -> str:
    """Place a panel after inline chapter prose but before child includes."""

    include_marker = "\n{include "
    if include_marker not in source:
        raise SystemExit(f"inline structure has no child include in {item_id}")
    prefix, suffix = source.split(include_marker, 1)
    if prefix.count(INLINE_PANEL_MARKER) > 1:
        raise SystemExit(f"multiple inline formalization panels in {item_id}")
    base = prefix.split(INLINE_PANEL_MARKER, 1)[0].rstrip()
    base = REPRESENTATION_IMPORT.sub("", base)
    if rows:
        lines = base.splitlines(keepends=True)
        import_indices = [index for index, line in enumerate(lines) if line.startswith("import ")]
        if not import_indices:
            raise SystemExit(f"no import location in {item_id}")
        lines.insert(import_indices[-1] + 1, "import RepresentationTheory\n")
        base = "".join(lines).rstrip()
        return base + panel(item_id, rows, heading_level=1) + "\n{include " + suffix
    return base + "\n\n{include " + suffix


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("alignment_json", type=Path)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    root = Path(__file__).resolve().parent.parent
    items = load_items(root)
    by_id = {item["id"]: item for item in items}
    if len(by_id) != len(items):
        raise SystemExit("metadata/items.json contains duplicate item IDs")

    grouped: dict[str, list[dict]] = defaultdict(list)
    for row in load_rows(args.alignment_json):
        grouped[resolve_item(row["reference"], set(by_id))].append(row)

    changed = []
    checked = 0
    for item_id, item in by_id.items():
        path = content_path(root, item["verso_module"])
        inline_structure = False
        if not path.exists():
            structure_path = inline_structure_path(root, item)
            if structure_path is None or not structure_path.exists():
                if grouped.get(item_id):
                    raise SystemExit(f"aligned semantic item has no Content module: {item_id}")
                continue
            path = structure_path
            inline_structure = True
        source = path.read_text(encoding="utf-8")
        if inline_structure:
            updated = update_inline_structure(source, item_id, grouped.get(item_id, []))
        else:
            updated = update_content(source, item_id, grouped.get(item_id, []))
        checked += 1
        if updated != source:
            changed.append(str(path.relative_to(root)))
            if not args.check:
                path.write_text(updated, encoding="utf-8")

    cited_items = {item_id for item_id, rows in grouped.items() if rows}
    item_kinds = sorted({item["kind"] for item in items})
    with_panel_by_kind = {
        kind: sum(
            item["kind"] == kind and item_id in cited_items
            for item_id, item in by_id.items()
        )
        for kind in item_kinds
    }
    total_by_kind = {
        kind: sum(item["kind"] == kind for item in items) for kind in item_kinds
    }
    mathematical_without_panel = sorted(
        item_id
        for item_id, item in by_id.items()
        if item["kind"] in MATHEMATICAL_KINDS and item_id not in cited_items
    )
    report = {
        "alignment_rows": sum(map(len, grouped.values())),
        "checked": checked,
        "changed": len(changed),
        "items_total_by_kind": total_by_kind,
        "items_with_panel_by_kind": with_panel_by_kind,
        "mathematical_items_without_panel": mathematical_without_panel,
    }
    print(json.dumps(report, sort_keys=True))
    if args.check and changed:
        for path in changed[:20]:
            print(path)
        raise SystemExit("formalization panels are not synchronized")


if __name__ == "__main__":
    main()
