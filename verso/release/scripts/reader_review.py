#!/usr/bin/env python3
"""Track the entire editorial scope independently of HTML formatting checks.

An annotation's presence is not proof of mathematical correctness. Reviewed
items must have a human-authored record stating what was compared and which
source modules were read. This report makes omissions explicit; the completion
gate rejects a polished sample or mechanically generated inventories.
"""

from __future__ import annotations

import argparse
from collections import Counter
import json
from pathlib import Path


METADATA = Path(__file__).resolve().parent.parent / "metadata"


def unique_json_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate editorial metadata key: {key}")
        result[key] = value
    return result


def audit(require_complete: bool = False, metadata: Path = METADATA, *, emit: bool = True) -> dict:
    def read(name):
        return json.loads((metadata / name).read_text(encoding="utf-8"),
                          object_pairs_hook=unique_json_object)
    items = read("items.json")["items"]
    annotations = read("reader-annotations.json")
    reviews = read("reader-reviews.json")
    sources = read("declaration-sources.json")
    for name in ("reader-titles.json", "reader-legacy-routes.json", "reader-joins.json"):
        if (metadata / name).exists():
            value = read(name)
            if name == "reader-legacy-routes.json":
                if set(value) - {"published_revision", "routes"} or not isinstance(value.get("routes"), dict):
                    raise ValueError("legacy routes must be inside the routes map")
                for route, record in value["routes"].items():
                    if not route or not isinstance(record, dict) or not record.get("key") \
                            or not isinstance(record.get("anchors"), list) or not record["anchors"]:
                        raise ValueError("legacy route lacks a semantic key or saved anchors")
    known = {item["id"] for item in items}
    errors = []
    unknown = (set(annotations) | set(reviews)) - known
    if unknown:
        errors.append(f"unknown reviewed items: {sorted(unknown)}")
    if len(known) != len(items):
        errors.append("duplicate semantic item IDs")
    for item_id in sorted(set(annotations) - set(reviews)):
        errors.append(f"annotation has no comparison record: {item_id}")
    chapters = {}
    gaps = []
    partial_gaps = []
    for item in items:
        chapter = item["id"].split("/", 1)[0]
        chapter_counts = chapters.setdefault(chapter, Counter())
        chapter_counts["items"] += 1
        review = reviews.get(item["id"])
        if review is None:
            chapter_counts["pending"] += 1
            continue
        if review.get("decision") not in {"annotated", "book_prose_only", "unformalized"} or not review.get("comparison"):
            errors.append(f"review lacks an editorial decision or comparison: {item['id']}")
            continue
        if review["decision"] == "annotated":
            upstream_modules = review.get("upstream_source_modules", [])
            if not annotations.get(item["id"]) or not (review.get("source_modules") or upstream_modules):
                errors.append(f"review lacks annotations or source evidence: {item['id']}")
                continue
            missing_modules = set(review.get("source_modules", [])) - set(sources.values())
            if missing_modules:
                errors.append(f"review names unknown source modules: {item['id']}: {sorted(missing_modules)}")
            if any(not module.startswith("Mathlib.") for module in upstream_modules):
                errors.append(f"upstream review evidence is not a Mathlib module: {item['id']}")
            if upstream_modules and not any(link.get("name") and not link["name"].startswith("RepresentationTheory.")
                                            for note in annotations[item["id"]] for link in note.get("links", [])):
                errors.append(f"upstream review lacks reader links to Mathlib: {item['id']}")
            for annotation in annotations[item["id"]]:
                for declaration in annotation.get("declarations", []):
                    if declaration["name"] not in sources:
                        errors.append(f"checked declaration lacks a source mapping: {item['id']}: {declaration['name']}")
            if review.get("coverage_gap"):
                if not any(note.get("kind") == "coverage_gap" for note in annotations[item["id"]]):
                    errors.append(f"partial coverage gap lacks an explicit reader note: {item['id']}")
                partial_gaps.append(dict(item=item["id"], description=review["coverage_gap"]))
        elif review["decision"] == "unformalized":
            notes = annotations.get(item["id"], [])
            if not review.get("coverage_gap") or not notes:
                errors.append(f"unformalized item lacks an explicit gap or reader note: {item['id']}")
                continue
            if any(note.get("kind") != "coverage_gap" or note.get("declarations") or note.get("links")
                   for note in notes):
                errors.append(f"unformalized item presents checked evidence: {item['id']}")
                continue
            gaps.append(dict(item=item["id"], description=review["coverage_gap"]))
        elif annotations.get(item["id"]):
            errors.append(f"book-only decision conflicts with annotation: {item['id']}")
        chapter_counts["reviewed"] += 1
    reviewed = sum(counts["reviewed"] for counts in chapters.values())
    pending = len(items) - reviewed
    result = dict(total_items=len(items), reviewed_items=reviewed, pending_items=pending,
                  annotations=sum(len(value) for value in annotations.values()),
                  unformalized_items=gaps,
                  partial_formalization_gaps=partial_gaps,
                  chapters={chapter: dict(counts) for chapter, counts in sorted(chapters.items())}, errors=errors)
    result["status"] = "complete" if not errors and not pending else "incomplete"
    if emit:
        print(json.dumps(result, indent=2, sort_keys=True))
    if errors or (require_complete and pending):
        raise SystemExit(1)
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--require-complete", action="store_true")
    audit(parser.parse_args().require_complete)
