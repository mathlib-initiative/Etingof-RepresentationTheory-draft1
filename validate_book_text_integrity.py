#!/usr/bin/env python3
"""Validate the released book-text partition and every recorded span digest."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections import Counter
from pathlib import Path


FRONTMATTER = re.compile(r"frontmatter-([1-9][0-9]*)")
NUMBERED = re.compile(r"(0|[1-9][0-9]*)")


def page_key(page: str) -> tuple[int, int]:
    """Return the physical book order, never lexicographic filename order."""
    if match := FRONTMATTER.fullmatch(page):
        return (0, int(match.group(1)))
    if match := NUMBERED.fullmatch(page):
        return (1, int(match.group(1)))
    raise ValueError(f"unsupported source page name: {page!r}")


def load_items(path: Path) -> list[dict]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    items = payload.get("items") if isinstance(payload, dict) else None
    if not isinstance(items, list):
        raise SystemExit(f"{path} does not contain an items array")
    return items


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("items", type=Path)
    parser.add_argument("source_markdown", type=Path)
    args = parser.parse_args()

    items = load_items(args.items)
    source_root = args.source_markdown
    page_paths = [path for path in source_root.glob("*.md") if path.is_file()]
    try:
        page_paths.sort(key=lambda path: page_key(path.stem))
    except ValueError as error:
        raise SystemExit(str(error)) from error
    if not page_paths:
        raise SystemExit(f"no Markdown pages found in {source_root}")

    pages = {path.stem: path.read_bytes().splitlines(keepends=True) for path in page_paths}
    page_order = list(pages)
    page_index = {page: index for index, page in enumerate(page_order)}
    coverage = {
        (page, line): []
        for page, lines in pages.items()
        for line in range(1, len(lines) + 1)
    }
    errors: list[str] = []
    ids: set[str] = set()
    orders: set[int] = set()
    previous_position: tuple[int, int] | None = None
    verified_hashes = 0

    for index, item in enumerate(items):
        if not isinstance(item, dict):
            errors.append(f"item {index} is not an object")
            continue
        item_id = item.get("id")
        order = item.get("order")
        span = item.get("span")
        digest = item.get("source_sha256")
        if not isinstance(item_id, str) or not item_id:
            errors.append(f"item {index} has no nonempty id")
            continue
        if item_id in ids:
            errors.append(f"duplicate item id: {item_id}")
        ids.add(item_id)
        if not isinstance(order, int) or order < 1:
            errors.append(f"{item_id}: invalid order {order!r}")
        elif order in orders:
            errors.append(f"{item_id}: duplicate order {order}")
        else:
            orders.add(order)
        if not isinstance(span, dict):
            errors.append(f"{item_id}: missing span")
            continue
        start = span.get("start")
        end = span.get("end")
        if not isinstance(start, dict) or not isinstance(end, dict):
            errors.append(f"{item_id}: invalid span endpoints")
            continue
        start_page, start_line = start.get("page"), start.get("line")
        end_page, end_line = end.get("page"), end.get("line")
        if start_page not in pages or end_page not in pages:
            errors.append(
                f"{item_id}: span names an absent page: {start_page!r}..{end_page!r}"
            )
            continue
        if not isinstance(start_line, int) or not isinstance(end_line, int):
            errors.append(f"{item_id}: span line numbers must be integers")
            continue
        start_position = (page_index[start_page], start_line)
        end_position = (page_index[end_page], end_line)
        if previous_position is not None and start_position < previous_position:
            errors.append(f"{item_id}: item order disagrees with physical page order")
        previous_position = start_position
        if start_position > end_position:
            errors.append(f"{item_id}: span ends before it starts")
            continue

        source_parts: list[bytes] = []
        valid_span = True
        for page in page_order[start_position[0] : end_position[0] + 1]:
            lines = pages[page]
            first = start_line if page == start_page else 1
            last = end_line if page == end_page else len(lines)
            if first < 1 or last > len(lines) or first > last:
                errors.append(
                    f"{item_id}: invalid line interval {page}:{first}-{last} "
                    f"for a {len(lines)}-line page"
                )
                valid_span = False
                break
            for line in range(first, last + 1):
                coverage[(page, line)].append(item_id)
            source_parts.extend(lines[first - 1 : last])
        if not valid_span:
            continue
        actual_digest = hashlib.sha256(b"".join(source_parts)).hexdigest()
        if digest != actual_digest:
            errors.append(
                f"{item_id}: source_sha256 mismatch: metadata={digest!r}, "
                f"actual={actual_digest}"
            )
        else:
            verified_hashes += 1

    gaps = [location for location, owners in coverage.items() if not owners]
    overlaps = [
        (location, owners) for location, owners in coverage.items() if len(owners) > 1
    ]
    if gaps:
        errors.append(f"uncovered source lines: {len(gaps)}; examples={gaps[:10]}")
    if overlaps:
        errors.append(f"multiply covered source lines: {len(overlaps)}; examples={overlaps[:10]}")
    expected_orders = set(range(1, len(items) + 1))
    if orders != expected_orders:
        errors.append(
            "item orders are not exactly consecutive: "
            f"missing={sorted(expected_orders - orders)[:10]}, "
            f"unexpected={sorted(orders - expected_orders)[:10]}"
        )

    report = {
        "errors": len(errors),
        "item_kinds": dict(sorted(Counter(item.get("kind") for item in items).items())),
        "items": len(items),
        "lines": len(coverage),
        "overlaps": len(overlaps),
        "pages": len(pages),
        "source_hashes_verified": verified_hashes,
        "uncovered_lines": len(gaps),
    }
    print(json.dumps(report, sort_keys=True))
    if errors:
        raise SystemExit("\n".join(errors[:100]))


if __name__ == "__main__":
    main()
