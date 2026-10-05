# Section 5.12: tableaux, Young symmetrizers and Specht modules

Verified local checkpoint: **304/583 reviewed, 497 annotations, 279 pending**.
Chapter 5: **71/157 reviewed, 86 pending**. Seven newly reviewed items:
one prose-only introduction and six annotated pages, with ten explanations
and twenty-one expandable checked statements. This batch is **not published**;
the full-book goal remains active.

## Reading edition

Explain multiset partitions, discrete diagram cells, zero-based tableau labels,
the canonical row-major filling and the row/column subgroup intersection.
Distinguish the normalized row and signed-column averages from their product:
the factors are idempotent, but that does not make their product idempotent.

Explain the genuinely reversed product in the classification implementation.
With row sum r and signed column sum s, the book uses rs/(|P||Q|), whereas
the main classification uses sr. Compare the checked group-algebra-linear
bridge between the generated ideals; do not identify these products as equal.
Separate simplicity, distinctness and exhaustion, and explain their hypotheses.

Give the trivial/sign actions for one-row/one-column partitions and the small
Specht examples. The (2,1) and (2,2) identifications use the previously checked
S3/S4 catalogues plus Specht simplicity and their checked dimensions; distinguish
these combined deductions from the direct dimension statements. The (3,1)
and (2,1,1) equivalences identify the untwisted and sign-twisted three-dimensional
models in the book's convention. Do not invent a formalization gap here.

Explain rational group-algebra modules and complex scalar extension rather
than pretending that the theorem computes a matrix basis. Explain the sum
of irreducible dimensions as the number of permutations whose square is one,
including the identity. The elementary factorial counting formula is a reader
deduction, not an advertised checked declaration; its n=0..8 values agree with
enumeration: 1,1,2,4,10,26,76,232,764.

Seven native item titles/first headings and corresponding registry title fields
change; prose, proof declarations and alignment associations do not. The section
contents label now uses Sₙ instead of raw TeX. Capture the published section
landing route as well as all seven original child routes and their bookmarks.

Fix the renderer to honour explicit `book_prose_only` decisions. Previously,
it treated an introduction without authored notes as unreviewed and displayed
a generic membership-defined-subtype statement. Keep its machine alignment
record, but suppress fallback statements and implementation inventories on
prose-only items. A new regression test checks both suppression and retained
alignment. The browser also rejects inventories on entirely prose-only pages.
The joined Problem 5.10.2 page retains its deliberately annotated continuation.

## Source comparison scope

Complete reads: partition construction 327 lines; partition auxiliary 282;
linear-equivalence/bounds 263; simple-module subtype representation 481;
auxiliary submodules 252; partition models 252; partition-subspace auxiliary
579; simple dimensions 79; symmetric-group classification 69; involution rank
sum 60; character-polynomial provider 1–157 including its simple FDRep endpoint.
Truncated combined outputs were corrected by individual/overlapping rereads.

Bounded reads: normalized projector proofs in group-algebra provider 616–658;
Mathlib partition definition 40–88; rational/complex symmetrizer definitions
in WeightCharacter 74–111; sandwich helper 1–32; invariant symmetric bilinear
form definition 1–36; real-character-to-form result and real-coefficient helper
694–725; S3 examples 430–534; S4 example results 94–175. Reuse the previously
reviewed Chapter 4 catalogues and representation models. Do not claim the
entire 791-line group-algebra or large character/weight providers were reread.

## Verification

- Thirty-five reader tests and seven immutable-corpus gate tests pass.
  All 583 original hashes, 235 pages and 5,716 lines verify, with no overlaps,
  uncovered lines or errors. Private-source exactness and scoped whitespace pass.
- Final build **90838: terminal exit 0**, all 20,771 jobs pass.
  `/tmp/etingof-reader-chapter5-specht-build-verified.log`.
  Earlier builds 98214 and 60527 succeeded before the final prose-only and
  contents-label fixes; neither is the final rendering.
- All 825 HTML files and 2,436 alignment associations validate. Reader checks:
  497 annotations, twelve complete footnotes, 139 redirects (123 title redirects),
  one joined page, 80 suppressed running headers and zero validation errors.
- Browser **72126: terminal exit 0**: twelve pages/thirteen reviewed items,
  48 desktop/phone collapsed/expanded cases, fourteen definition bookmarks,
  no JavaScript errors or whole-page overflow. Global route coverage includes
  all 304 reviewed items. Entirely prose-only pages are checked explicitly.
- Legacy browser **39216** completed all eight renamed routes, seventy saved
  bookmark cases and 84 individual card open/close actions before terminating
  with exit 1 on an overbroad final assertion: it incorrectly treated the
  annotated joined continuation of Problem 5.10.2 as an unannotated whole page.
  A corrected route-scoped check passes all 51 entirely prose-only items and
  explicitly retains that joined continuation. Logs preserve the failure;
  this is not claimed as a wholly passing legacy-script invocation.
- All twenty-one selected checked declarations occur exactly once, using actual
  declaration bindings rather than guessed HTML IDs. Thirty-one local card/helper
  references resolve to source files in the existing public PR clone. Mathlib's
  partition finder was checked against its official page and existing anchor.
- Prepared search `a178284f8f20bf43`, 789 documents: all seven new titles occur
  once, point to existing destinations and rank first for their relevant queries.
- Visually inspected final phone tableau and reversed-product explanations and
  desktop classification. Original prose leads; checked signatures are collapsed;
  the sidebar displays Sₙ, not raw TeX.

Final materializer **76536: terminal exit 0**. Exact private retained bytes/modes
and dependency pin verify. Public checksum comparison with the PR clone is
unchanged. Final materialization/browser/search/regression logs:
`/tmp/etingof-reader-chapter5-specht-verified-RcwaMd/`.

## Publication and next work

Read-only PR check: #4 remains OPEN, REVIEW_REQUIRED and BLOCKED, at
`f9c69bafeccd5158a7249449a92446f844dac381`, with no merge commit:
https://github.com/mathlib-initiative/EtingofRepresentationTheory/pull/4

No remote writes or changes to visibility, CI settings or review/build protections.
The local preview source URLs still use existing main; the materialized private
dependency is the unmerged preview pin. Neither proves publication. After the
protected source merge, materialize against actual merged main, rebuild, publish
and verify live links.

Next: Section 5.13's nine items. Their native modules have been read completely
during the final build. Subsequently read the complete scalar-multiplication
provider (194 lines) and idempotent-map provider (42 lines). The former proves
the exact normalized Young-symmetrizer coefficient by tracing right multiplication
and transferring the ideal dimension. The latter is a direct evaluation/inverse
proof over any ring and left module, rather than the book's direct-sum proof.
Important presentation distinction: its outer equivalence is `≃` between types,
not a bundled `≃ₗ` on Hom and an image submodule; the inverse is an A-linear map.
These are preparation findings, not new review credit or completed annotations.
The remaining full-book editorial pass and live publication are incomplete.
