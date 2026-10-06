# Chapter 5.2: algebraic numbers and character zeros

Verified local checkpoint: **253/583 reviewed, 427 annotations, 330 pending**.
Chapter 5 is **20/157 reviewed**. All eleven Section 5.2 items now have comparison
records; ten carry 17 notes and the introductory transition remains book prose.
The full-book pass and public publication are still incomplete.

## Reading changes

- Explain IsAlgebraic over ℚ versus IsIntegral over ℤ, coefficient embeddings,
  nonzero versus monic polynomial formulations and matrix eigenvalue encoding.
- Compare the explicit companion matrix with multiplication by the adjoined
  root, its general-ring characteristic-polynomial theorem, and the separate
  rational minimal-polynomial construction.
- Identify the two actual subsets of ℂ, their ring/field structures and
  algebraic-closure result. Distinguish generic closure proofs from the book's
  tensor-matrix proof and the integrally-closed proof from denominator counting.
- Explain minimal polynomials and algebraic conjugacy, with working upstream
  links; obtain integer coefficients through the coefficient-map theorem,
  rather than advertising a checked Vieta calculation.
- Explain the finite-sum theorem's single field embedding and compatible
  choices of conjugates; do not assert the invalid converse for arbitrary choices.
- Explain the uniform finite Galois field before the representation quantifier,
  algebraic simple models, finite coefficient envelope and block-basis transport.
- Explain orthonormality and AM–GM, the dimension restriction, and the actual
  cyclotomic character-zero proof instead of the hint's matrix-conjugation route.
- Explain root-of-unity eigenvalues, traces of powers, coprime power bijections,
  product reindexing, fixed-field rationality and the rational-integral contradiction.

Nine native titles and their registries are shortened. Existing public routes
and section bookmarks were captured from the live xref and preserved. No original
prose, proof, declaration name, visibility, CI setting or protection changed.

## Shared link defect found and fixed

A real-browser check found that our Mathlib URLs lacked `#doc`: the finder's
bare-query machine-data view redirected to `find/undefined`. Failure evidence:
`/tmp/etingof-reader-chapter5-algebraic-7hL32S/mathlib-links.log`.

The shared source-link generator now selects the documentation view. Regression
tests cover annotation links, HTML/xref rewriting and rejection of machine-view
destinations; the publication validator checks both HTML and external xref URLs.
This corrects **237 rendered links, 172 distinct upstream destinations**, across
the current book, not just Section 5.2. All 172 names exist in the current official
declaration index; all 67 authored upstream link names exist as well. Nine new
links were actually followed in a browser to the correct declaration anchors:
`/tmp/etingof-reader-chapter5-algebraic-7hL32S/mathlib-links-doc.log`.
Do not claim all 172 were individually browser-clicked.

## Verification

- Preflight: all 17 anchors match one original paragraph each; all 18 chosen
  cards are present in their native items. Nineteen local helper links resolve
  to real source modules, nine upstream links to documented declarations.
  The lemma's theorem/proof share one native paragraph; its note follows both.
- 32 reader tests pass. Immutable private source assertion passes. All 583
  original span hashes across 235 pages and 5,716 lines remain verified, with
  no overlaps or uncovered lines. Scoped tracked-file whitespace check passes.
- Final fresh build **19153: terminal exit 0**, all 20,771 jobs pass.
  Log: `/tmp/etingof-reader-chapter5-algebraic-checked-build.log`.
  Earlier builds 49419 and 90279 also finished successfully, but predate the
  final link/label fixes; do not substitute them for this final artifact.
- All 2,436 alignment associations synchronize with zero stale panels.
  Reader validation: 427 annotations, twelve complete footnotes, 91 redirects,
  including 76 title redirects, 80 suppressed running headers, zero errors.
  All 778 HTML files pass rendered-formalization validation.
- Final browser **32552: terminal exit 0**: eleven pages, 44 desktop/phone
  collapsed/expanded cases, eighteen checked-definition bookmarks and zero
  JavaScript errors or page overflow. Global route audit covers 253 reviews.
- Final legacy browser **66313: terminal exit 0**: nine renamed pages,
  all 82 desktop/phone old-bookmark redirects preserve their fragments and
  reach the canonical pages with one main heading and zero JS errors/overflow.
- Visually inspected matrix definitions and the common field theorem on phone,
  companion matrix and minimal polynomials on desktop. Refined two ambiguous
  polynomial/matrix card labels before the final build.
- Active search `bed13e3926feb8b6`: 789 documents; all nine changed titles
  occur once with real destinations. Final prepared-index queries for common
  field definition, conjugates/sum and cyclotomic/proof rank their pages first.

Final materializer **25180: terminal exit 0**. Exact generated trees/report and
browser logs: `/tmp/etingof-reader-chapter5-algebraic-checked-VHjVMb/`.
Public checksum comparison against the existing PR clone is unchanged. Private
retained bytes/modes and dependency pin match the authoritative sources.

## Publication and next pass

Read-only remote evidence: PR #4 remains OPEN, REVIEW_REQUIRED, BLOCKED at
`f9c69bafeccd5158a7249449a92446f844dac381`; no merge commit. Auto-merge is not
enabled for the repository; no review requests are assigned.
https://github.com/mathlib-initiative/EtingofRepresentationTheory/pull/4

No remote writes or protection/visibility changes. Do not publish the unmerged
preview pin, enable self-approval, select an arbitrary reviewer or change repository
settings. Once protected merge is available, materialize against actual merged
main, publish private/Pages and check the live reader. Do not restart completed CI.

Next: Section 5.3, Frobenius divisibility. Its four complete native items were
read here, together with the complete 97-line CharacterIntegrality and 156-line
FiniteGroupCharacterArithmetic providers and the 25-line rational-integrality
provider. No Section 5.3 review credit or annotations assigned yet. The class-sum
scalar/integrality proof and class-regrouping/rational-divisibility proof are ready
for editorial comparison and native anchor planning.

Keep the full-book goal active.
