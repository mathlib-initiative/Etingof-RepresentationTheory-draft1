# Chapters 5.6–5.9: products, virtual characters, induction and Frobenius's formula

Verified checkpoint before the subsequent Section 5.10 edits:
**290/583 reviewed, 469 annotations, 293 pending; Chapter 5: 57/157.**
Seventeen newly reviewed items contain thirteen annotated passages, twenty-three
new notes and twenty-one checked cards. Four headings/transitions retain original
prose without redundant declaration inventories. Sixteen navigation titles are
shortened; live old routes and their bookmarks are retained.

## Mathematical comparisons

- Product irreducibles: external tensor action, nonzero/simple invariant-subspace
  meaning, algebraic-closedness convention and no characteristic/order restriction.
  The exported theorem does not require the groups to be finite.
- Virtual representations: finite-support integer coefficients on simple
  representation isomorphism classes, additive character and integer dimension.
  Explain the norm-one sum-of-squares criterion and positive-degree sign exclusion.
- Restriction keeps the underlying module. The book's full equivariant-function
  induction is Lean's coinduction, with right translation by g, not g inverse.
  Coinvariant induction has finite-support generators and agrees at finite index.
  The function-to-group-algebra Hom comparison itself needs no finite index.
- Coset evaluation, reconstruction and dimension: distinguish linear coordinates
  from an untwisted permutation action, and finite index from finiteness of G.
- Induction in stages: the source checks a full linear/equivariant coinvariant
  equivalence, not merely a map. Report the absent separate infinite-index
  function-space transitivity theorem rather than identifying the two models.
- Character idempotent: normalized inverse weights, left ideal, both inverse
  maps and the generator inversion relative to the book's convention.
- Frobenius's coset/averaged formulas: actual finite-group complex proofs exist
  despite misleading generic source docstrings. Explain representative independence,
  zero-extension, averaging/projector trace, fixed-point counting and regrouping.
  Explicitly distinguish that proof from the book's diagonal-block argument.
  Four coverage notes report the general-field/infinite-ambient scope not supplied.

Complete native passages and all cited local provider modules were read, with
bounded upstream reads and reuse of previously reviewed tensor/orthogonality
engines recorded precisely in `reader-reviews.json`.

## Verification

- Thirty-two reader tests passed; immutable private corpus exactness passed.
  All 583 original span hashes, 235 pages and 5,716 lines remain accounted for,
  without overlaps, missing lines or errors. Scoped whitespace check passed.
- Build **97019: terminal exit 0**, all 20,771 jobs passed.
  `/tmp/etingof-reader-chapter5-induction-build.log`
- Reader validation: 469 annotations, twelve complete footnotes, 124 redirects
  (109 title redirects), 80 suppressed running headers, zero errors.
  All 811 HTML files and 2,436 alignment associations validated.
- Browser **71674: terminal exit 0**: seventeen pages, sixty-eight
  desktop/phone collapsed/expanded cases, twenty-four definition bookmarks,
  zero JS errors/whole-page overflow; all 290 reviewed reading routes covered.
- Legacy browser **48134: terminal exit 0**, confirmed on the next continuation:
  sixteen renamed pages, all 148 desktop/phone old-bookmark redirects pass.
- All six new Mathlib finder links actually reached the correct official module
  and declaration anchor; browser **50956: terminal exit 0**.
- Prepared search version `215145ad349a0bde`, 789 documents. All sixteen titles
  have unique entries/existing destinations; six representative actual index
  queries rank their revised pages first.
- Visually inspected phone function-model/virtual-definition pages and desktop
  coset formula. The apparent phone formula clipping is intentional horizontal
  scrolling: measured client width 358, content width 498, reachable scroll 140,
  overflow-x auto. The next continuation adds keyboard access to this region.
  The observed clipped mobile masthead is also fixed in that next batch, not here.

Materializer **93663: terminal exit 0**. Exact generated trees and reports:
`/tmp/etingof-reader-chapter5-induction-lJjzNi/`.
Public checksum comparison against the existing PR clone was unchanged;
private retained bytes/modes and the dependency pin were verified.

## Publication

No remote writes or protection/visibility changes. Public PR #4 remains open,
REVIEW_REQUIRED and BLOCKED at `f9c69bafeccd5158a7249449a92446f844dac381`,
with no merge commit, revalidated at the start of the next continuation:
https://github.com/mathlib-initiative/EtingofRepresentationTheory/pull/4

These local changes are not published. Preserve the protected-merge requirement;
once merged, materialize against the actual merged-main revision, publish through
the generating repositories and verify the live reader. Do not publish an
unmerged preview dependency or weaken protections. The full-book goal stays active.
