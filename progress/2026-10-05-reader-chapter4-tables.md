# Chapter 4: character tables and tensor products

Verified local checkpoint: **212/583 reviewed, 330 annotations, 371 pending**;
Chapter 4 is 39/60. These changes are not live; the full-book goal remains active.
The preceding goal-assessment response made no implementation progress. This
continuation verified the previously built authoritative Sections 4.8–4.9 batch
and proceeds to Section 4.10.

Four items have seventeen explanations and mathematical titles. Notes now follow
their own complete tables, using an explicit table anchor rather than collecting
all explanations before the first table. Two renderer regressions and a browser
assertion cover this placement. All 29 reader tests pass in the preceding build.

The explanations distinguish actual constructed representations from candidate
character arithmetic: A4's cyclic quotient and sum-zero action; Q8 and S4 family
ordering; A5's exact quadratic arithmetic, spectral three-dimensional summands,
outer twist and reduced permutation actions; natural Hom multiplicities and
actual tensor-product isomorphisms. Missing tetrahedron/icosahedron equivalences
are explicit gaps. The book's (13254) is retained but flagged: the even conjugator
(23)(45) takes (12345) to it, so it cannot name the other five-cycle class. The
table's (13245) and the formalization's square representative are consistent.

Read-only comparison checked all 36 printed tensor-product cells against the
actual Lean multiplicity vectors, including repeated summands and symmetry of
the omitted lower triangle. Source-reading boundaries are recorded honestly in
reader-reviews.json; no full audit of all spectral machinery is claimed.

Verification completed:

- Official build: exit 0, 20,771 jobs, log
  `/tmp/etingof-reader-chapter4-tables-build.log`; 2,436 native associations,
  zero stale panels. Build validation preserves all 583 book spans and twelve
  full footnotes, with 330 annotations and zero reader errors.
- Rendered-formalization validation: all 754 HTML files, zero errors.
- Browser process 15479: terminal exit 0; four pages, sixteen desktop/phone
  collapsed/expanded cases, eight definition bookmarks, no overflow or JS errors.
  Global discovery also checked unique routes for all 212 reviewed items. Log:
  `/tmp/etingof-reader-chapter4-tables-zRbBXH/browser-final.log`.
- Legacy browser process 25646: terminal exit 0; four old routes at both widths,
  all 22 registered anchors present and heading hashes preserved.
- Active search version `c67e87eb9b3a0a92`: each of the four replacement titles
  has exactly one result. Visually inspected phone Q8 and desktop tensor tables;
  notes follow tables and original cells remain readable.
- Full materializer succeeded in the preceding turn. Exact current private
  retained bytes/modes and dependency pin were checked in this continuation.
  Public checksum comparison against the existing PR clone is unchanged.

Materializations:
`/tmp/etingof-reader-chapter4-tables-zRbBXH/{generated-public,generated-private}`.
PR #4 remains OPEN, REVIEW_REQUIRED, head
`f9c69bafeccd5158a7249449a92446f844dac381` on the current read-only GitHub check.
No GitHub writes, proof changes, protection changes or visibility changes.
Do not push the private preview pin. After the protected merge, rematerialize
against actual merged main, publish descendants and check the live public URL.
This does not prevent continuing the remaining editorial work.
