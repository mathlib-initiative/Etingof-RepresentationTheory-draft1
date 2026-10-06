#!/usr/bin/env python3
"""Check built ``source_ref`` metadata against the adjudicated alignment ledger."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from collections import Counter
from pathlib import Path


def read_jsonl(path: Path) -> list[dict]:
    with path.open(encoding="utf-8") as stream:
        return [json.loads(line) for line in stream if line.strip()]


def module_path(root: Path, module: str) -> Path:
    return root / (module.replace(".", "/") + ".lean")


def normalized_source_identity(value: str) -> str:
    """Normalize an item ID or old module suffix for exact-module matching.

    Book item modules spell numeric separators with underscores while item IDs
    use dots.  Removing punctuation gives a deliberately narrow identity check
    that catches declarations originating in the module named for an item,
    without trying to infer associations from imports or nearby prose.
    """

    return re.sub(r"[^A-Za-z0-9]", "", value).lower()


def canonical_reference(source_node: dict, derived_ordinal: int | None = None) -> str:
    """Return the stable public reference for one private source claim.

    Partition nodes cite their item directly, while standalone derived nodes use
    the stable ``DerivedNN`` overlay identity within their parent item.  Claims
    classified as covered elsewhere retain their within-item identity with
    ``DerivedN`` when they are not the first claim.  This convention prevents
    distinct proof claims from collapsing to one attribute with conflicting
    roles.
    """

    kind = source_node["kind"]
    if kind == "partition":
        return source_node["item_id"]
    if kind == "derived":
        if derived_ordinal is None:
            raise ValueError("derived source node requires an ordinal")
        return f"{source_node['parent_item_id']}/Derived{derived_ordinal:02d}"

    reference = source_node["item_id"]
    if source_node["verdict"] != "formalized" and source_node["ordinal"] > 1:
        reference += f"/Derived{source_node['ordinal']}"
    return reference


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("release", type=Path)
    parser.add_argument("proposals", type=Path)
    parser.add_argument("adjudicated_edges", type=Path)
    parser.add_argument("source_nodes", type=Path)
    args = parser.parse_args()

    release = args.release.resolve()
    proposal_rows = [
        row for row in read_jsonl(args.proposals) if row.get("new_fqn")
    ]
    proposals = {row["old_fqn"]: row for row in proposal_rows}
    source_node_rows = read_jsonl(args.source_nodes)
    source_nodes = {row["source_node"]: row for row in source_node_rows}
    source_references: dict[str, str] = {}
    derived_counts: dict[str, int] = {}
    for row in source_node_rows:
        derived_ordinal = None
        if row["kind"] == "derived":
            parent = row["parent_item_id"]
            derived_counts[parent] = derived_counts.get(parent, 0) + 1
            derived_ordinal = derived_counts[parent]
        source_references[row["source_node"]] = canonical_reference(
            row, derived_ordinal
        )

    errors: list[str] = []
    # Multiple private source claims can intentionally project to the same
    # public item reference.  A Lean declaration may carry that reference only
    # once, so collapse by (declaration, reference), with the stronger primary
    # role taking precedence.  This matches the Verso panel synchronizer.
    expected_by_reference: dict[tuple[str, str], str] = {}
    cited_item_ids: set[str] = set()
    for edge in read_jsonl(args.adjudicated_edges):
        if edge.get("adjudication_status") != "adjudicated":
            continue
        proposal = proposals.get(edge["old_fqn"])
        if proposal is not None:
            if not module_path(release, proposal["new_module"]).exists():
                continue
            declaration = proposal["new_fqn"]
        elif edge["provider_module"].startswith("Mathlib."):
            # Reviewed alignments may cite declarations already supplied by the
            # pinned Mathlib dependency.  The public package persists those
            # associations in Alignment.Upstream without wrapping or copying
            # the upstream declaration, so its public name is unchanged.
            declaration = edge["old_fqn"]
        else:
            continue
        source_node = source_nodes.get(edge["source_node"])
        if source_node is None:
            errors.append(f"missing source node {edge['source_node']}")
            continue
        key = (declaration, source_references[edge["source_node"]])
        cited_item_ids.add(source_node["item_id"])
        role = edge["role"]
        if role == "primary" or key not in expected_by_reference:
            expected_by_reference[key] = role

    expected = {
        (declaration, reference, role)
        for (declaration, reference), role in expected_by_reference.items()
    }

    command = ["lake", "env", "lean", "--run", "AlignmentExport.lean"]
    completed = subprocess.run(
        command,
        cwd=release,
        check=False,
        capture_output=True,
        text=True,
    )
    if completed.returncode != 0:
        raise SystemExit(
            "alignment export failed:\n" + completed.stdout + completed.stderr
        )
    try:
        exported = json.loads(completed.stdout)
    except json.JSONDecodeError as error:
        raise SystemExit(f"alignment export did not emit JSON: {error}") from error

    actual_rows = [
        (row["declaration"], row["reference"], row["role"])
        for row in exported
    ]
    actual = set(actual_rows)
    if len(actual) != len(actual_rows):
        errors.append("alignment export contains duplicate entries")

    for row in sorted(expected - actual):
        errors.append("missing source_ref: " + " | ".join(row))
    for row in sorted(actual - expected):
        errors.append("unexpected source_ref: " + " | ".join(row))

    partition_items = {
        row["item_id"]: row["item_type"]
        for row in source_node_rows
        if row["kind"] == "partition"
    }
    item_types = sorted(set(partition_items.values()))
    items_total_by_kind = Counter(partition_items.values())
    items_with_source_ref_by_kind = Counter(
        kind for item_id, kind in partition_items.items() if item_id in cited_item_ids
    )
    named_result_kinds = {"theorem", "lemma", "proposition", "corollary", "definition"}
    mathematical_kinds = named_result_kinds | {"example", "exercise", "remark"}
    named_results_without_source_ref = sorted(
        item_id
        for item_id, kind in partition_items.items()
        if kind in named_result_kinds and item_id not in cited_item_ids
    )
    mathematical_items_without_source_ref = sorted(
        item_id
        for item_id, kind in partition_items.items()
        if kind in mathematical_kinds and item_id not in cited_item_ids
    )
    expected_declarations = {declaration for declaration, _, _ in expected}
    actual_declarations = {declaration for declaration, _, _ in actual}

    # Independently enforce the converse citation direction for the strongest
    # recoverable provenance signal in the migration ledger.  A mathematical item
    # cannot have zero citations when an old module named exactly for that item
    # contains reviewed migrated declarations.  We intentionally do not demand
    # that every helper from the module cite the item: only an adjudicated
    # comparison of its formal type with the source can make that determination.
    # This narrower invariant still catches unconverted packets whose empty
    # claim coverage would otherwise make both the alignment ledger and public
    # export omit the entire named item and therefore agree incorrectly.
    items_by_normalized_identity: dict[str, str] = {}
    for item_id in partition_items:
        identity = normalized_source_identity(item_id)
        previous = items_by_normalized_identity.setdefault(identity, item_id)
        if previous != item_id:
            errors.append(
                f"normalized item identity collision: {previous} | {item_id}"
            )
    exact_module_item_proposal_counts: Counter[str] = Counter()
    for proposal in proposal_rows:
        old_module = proposal["old_module"]
        prefix = "EtingofRepresentationTheory."
        if not old_module.startswith(prefix):
            continue
        identity = normalized_source_identity(old_module[len(prefix) :])
        item_id = items_by_normalized_identity.get(identity)
        if item_id is not None and module_path(release, proposal["new_module"]).exists():
            exact_module_item_proposal_counts[item_id] += 1
    # The source transcription splits Problem 5.10.2's unfinished first line
    # from its parts on the following pages.  The Lean module named for the
    # problem formalizes those parts and is therefore cited by the continuation
    # item, rather than by the syntactically item-like lead-in fragment.
    exact_module_item_redirects = {
        "Chapter5/Problem5.10.2": "Chapter5/Discussion_Problem5.10.2_parts",
    }
    uncited_mathematical_items_with_exact_module = sorted(
        item_id
        for item_id in mathematical_items_without_source_ref
        if exact_module_item_proposal_counts[item_id]
        and exact_module_item_redirects.get(item_id) not in cited_item_ids
    )
    for item_id in uncited_mathematical_items_with_exact_module:
        errors.append(
            f"mathematical item with exact source module has no source_ref: {item_id} "
            f"({exact_module_item_proposal_counts[item_id]} reviewed declarations)"
        )
    result = {
        "actual": len(actual),
        "book_declarations_expected": len(expected_declarations),
        "declarations": len(actual_declarations),
        "errors": len(errors),
        "exact_module_items_with_proposals": len(exact_module_item_proposal_counts),
        "expected": len(expected),
        "items_total_by_kind": {
            kind: items_total_by_kind[kind] for kind in item_types
        },
        "items_with_source_ref_by_kind": {
            kind: items_with_source_ref_by_kind[kind] for kind in item_types
        },
        "named_results_without_source_ref": named_results_without_source_ref,
        "mathematical_items_without_source_ref": mathematical_items_without_source_ref,
        "uncited_book_declarations": sorted(
            expected_declarations - actual_declarations
        ),
        "uncited_mathematical_items_with_exact_module": [
            {
                "item_id": item_id,
                "reviewed_declarations": exact_module_item_proposal_counts[item_id],
            }
            for item_id in uncited_mathematical_items_with_exact_module
        ],
    }
    print(json.dumps(result, sort_keys=True))
    if errors:
        raise SystemExit("\n".join(errors[:100]))


if __name__ == "__main__":
    main()
