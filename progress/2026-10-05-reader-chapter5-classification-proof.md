# Section 5.13: proof of the Specht classification

Verified local checkpoint: **313/583 reviewed, 505 annotations, 270 pending**.
Chapter 5: **80/157 reviewed, 77 pending**. Nine newly reviewed items:
one prose-only heading and eight annotated passages, with eight explanations
and ten expandable checked statements. This batch is **not published**.
The full-book goal remains active.

## Reading edition

Explain the single bundled complex-linear functional controlling every normalized
row–column sandwich. Compare permutation-basis membership, signed coefficients,
transposition cancellation and linear extension. Explain the source's finite
coordinate/counting factorization instead of implying it implements the book's
successive row rearrangements literally.

Distinguish lexicographic order from dominance, including the incomparable
partitions (4,1,1)/(3,3). Decode `LexLt μ λ` as the book's λ > μ. Explain how
failure of dominance supplies the stronger vanishing theorem, and how scaling
the unnormalized row–column sandwich gives the normalized book statement.

Explain the exact scalar-square coefficient from right-multiplication trace,
the nonzero scalar, projection onto the generated ideal and transferred dimension.
Do not call the normalized Young symmetrizer itself an idempotent.

Explain evaluation at e and its inverse x ↦ x·m over any ring/left module.
Disclose that the result bundles a bijection of underlying types (`≃`), not
a linear equivalence of Hom and an image submodule. The inverse values are
A-linear maps. Compare the direct evaluation proof with the book's direct-sum
proof without claiming a separate aligned direct-sum construction.

Explain how semisimplicity, sandwiches, nonisomorphism and block counting
establish the classification. Retain the entire displayed Hom-space argument
before inserting this closing note; an initial visual check caught an interruption,
which was corrected. Transfer the unnormalized reversed-product model through
the previously checked ideal equivalence.

Shorten nine native titles/first headings and their registered item-title fields.
The section contents label uses Sₙ instead of raw TeX. Capture all ten published
section/child routes and forty-one saved bookmarks. Original book text, proof
declarations and alignment associations remain unchanged.

## Source comparison scope

Read group-algebra provider 105–397, 491–554 and 665–791: complete transposition/
factorization proof, row–column cancellation and both unnormalized/normalized
linear-functional target proofs. Other helpers are dependencies, not a claimed
fresh whole-file reread. Read dominance provider 1–142 and 318–721, with the
column-count identity, first-row counting, complete dominance counting argument,
collision/cancellation and final lexicographic reduction. Other coordinate-bound
helpers remain dependencies, not a claimed complete 721-line read.

Reuse the preceding continuation's complete scalar-multiplication (194) and
idempotent-map (42) provider reads. Reuse Section 5.12's complete classification
providers (252, 282, 263, 481) and ideal-equivalence comparison. All nine original
native Section 5.13 modules were read completely in the preceding continuation.

## Verification

- Thirty-six reader tests and seven immutable-corpus gate tests pass. A new
  duplicate-key regression rejects stale editorial metadata overriding new work.
  The corpus check caught two stale duplicate title entries; the strict audit also
  caught two identical duplicate legacy routes. Remove only those duplicates;
  preserve all unique route/bookmark data. All editorial metadata now audits cleanly.
- All 583 original hashes, 235 pages and 5,716 lines verify without overlaps,
  uncovered lines or errors. Private source corpus is exact except declared
  editorial titles. Scoped whitespace checks pass.
- Final official build **43550: terminal exit 0**, all 20,771 jobs pass:
  `/tmp/etingof-reader-chapter5-classification-proof-final-build.log`.
  Build 89690 terminated exit 1 after its Lean stage succeeded because the new
  duplicate-key audit rejected duplicate legacy routes. Build 10771 then passed
  before the closing-note placement refinement; it is not the final rendering.
  Earlier handles 29684/10009 and their temporary logs were unavailable in the
  continued environment, with no matching live processes. No success is inferred
  for those unavailable handles; fresh work uses observed current processes.
- All 833 HTML files and 2,436 alignment associations validate, with 505 notes,
  twelve complete footnotes, 147 redirects (131 title redirects), one joined page,
  80 suppressed running headers and zero validation errors.
- Final browser **31376: terminal exit 0**: eleven pages/eleven reviewed items,
  44 desktop/phone collapsed/expanded cases, sixteen checked-definition bookmarks,
  zero JavaScript errors or whole-page overflow. Global reading-route coverage
  includes all 313 review records. Earlier browser 13359 passed before placement
  refinement, with the same case counts.
- Legacy/card browser **9478: terminal exit 0**: ten renamed routes, 82 saved
  bookmark cases at desktop/phone widths, forty individual card open/close actions,
  ten uniquely retained checked declarations, exact human labels and proof links,
  no JavaScript errors or page overflow. This check precedes the final note-placement
  refinement; no native route, heading, card or bookmark changed in that refinement.
  Final static checks verify all ten checked declarations uniquely and require
  the closing note to follow the complete final proof paragraph.
- Fifteen reader card/helper references across eight distinct public source modules
  match exact Git blob bytes at the existing PR head. Additionally, all **838**
  materialized public files match the complete untruncated GitHub tree at that head.
- Search `c303d5e6440a433a`, 789 documents: nine new titles each occur once,
  resolve to existing destinations and rank first for relevant queries. The final
  placement-only rendering retains that exact checked search version.
- Visually inspected phone idempotent-map and trace notes, desktop partition orders,
  and the final desktop classification proof after placement correction. The last
  proof now reads continuously before its Lean explanation; checked signatures
  remain collapsed and the contents has no raw TeX for this section.

Final materializer **37452: terminal exit 0**. Exact private retained bytes/modes
and dependency pin pass. Final public bytes equal the GitHub-tree-verified earlier
materialization. Final artifacts/browser log:
`/tmp/etingof-reader-chapter5-classification-proof-final-FokxpW/`.
Earlier materializer 35107 passed; legacy/search logs:
`/tmp/etingof-reader-chapter5-classification-proof-current-1P42kV/`.

## Publication and next work

Read-only check: PR #4 remains OPEN, REVIEW_REQUIRED and BLOCKED at
`f9c69bafeccd5158a7249449a92446f844dac381`, with no merge commit:
https://github.com/mathlib-initiative/EtingofRepresentationTheory/pull/4

No remote writes or changes to visibility, CI or review/build protections.
Materialized private dependency uses the unmerged preview pin; local HTML source
links still use existing main. Neither proves publication. After protected merge,
pin actual merged main, rebuild/materialize, publish and check live source links.

Next: Section 5.14's six items, whose original native modules were read completely
while this build ran. Preparation reads completed: Young-diagram/Kostka definition
provider 27 lines; linear-independent-family 186; direct-sum-equivalences 81;
partition-linear-map vanishing 433. Bounded preparation reads: induced/monoid-algebra
provider 1–145 (514 total), permutation-polynomial definitions/coefficient proof
1–110 (719 total). Do not claim the latter complete or credit Section 5.14 yet.
The full-book pass and live publication remain incomplete.
