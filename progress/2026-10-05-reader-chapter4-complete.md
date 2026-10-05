# Chapter 4: editorial pass complete, publication still pending

Verified local checkpoint: **233/583 reviewed, 392 annotations, 350 pending**.
Chapter 4 is **60/60 reviewed**. This completes the chapter's editorial pass,
not the full-book goal or public publication.

## Reading changes

Five problems reviewed since the previous checkpoint; 30 new notes. All changes
are in authoritative reader metadata, with selected statements drawn from native
compiled Verso cards. No original prose, proof, declaration name or title changed
in this batch.

- 4.12.6: inverse-pullback affine action, zero-sum model and averaging proof,
  exhaustive irreducibles, fixed-point characters, twists and tensor products.
  Explain q >= 3 hypotheses and the separate q = 2 classification/tensor case.
- 4.12.7: real irreducibility of complex two-space; the commuting algebra's
  dimension/division properties; coordinate quaternion basis and products;
  squared norm versus norm; explicit SU(2) matrix isomorphism; quaternion
  conjugation, Euler half-angle surjectivity and kernel of the SO(3) map.
  Explicit gap: the source does not identify the commuting algebra with the
  coordinate quaternion algebra. Group isomorphism is not advertised as a
  bundled homeomorphism/manifold theorem or covering-space theorem.
- 4.12.8: oriented poles rather than axis lines, cyclic stabilizers,
  Burnside/orbit-stabilizer equation, repeated stabilizer orders and five
  abstract group types. Explain SU(2)'s unique involution, full inverse images
  and the orders of binary lifts. Explicit gap: no geometric polyhedron
  construction/conjugacy classification or named binary-group presentations.
- 4.12.10: nonzero intertwiners are embeddings from simple modules; free dual
  orbit, separating polynomials, regular representation and homogeneous degree
  extraction. Explain degree zero, finite-dimensional complex hypotheses,
  symmetrization lift and the tensor endpoint's separate character proof.
- 4.12.11: concrete symmetric-matrix action; scalar/skew/trace-free decomposition;
  real and complex irreducibility; two real parameters and symmetry of outputs.
  Explain the final real odd-degree-eigenvalue proof, not just complex Schur.
  Explicit gap: equivariance is assumed and the physical derivation/positivity
  is not proved.

Per-item reader-reviews.json records bound the inspected provider regions.
QuaternionRotationMaps was read completely across the last two editorial turns.
FiniteRotationGroups' pole count, case endpoints and SU(2) lifting arguments were
compared; not every intervening S4/A5 or axis-coordinate helper was reread.

## Verification

- Preflight: all 30 note anchors match one original prose paragraph each;
  26 selected native cards and 64 source mappings resolve to real modules,
  with no fallback repository searches. Reader audit has zero errors.
- 29 regression tests pass. Immutable private-source assertion passes.
  Original book corpus: 583 span hashes verified, 235 pages, 5,716 lines,
  no overlaps or uncovered lines.
- Official fresh build **3587: terminal exit 0**; all 20,771 jobs pass.
  Log: `/tmp/etingof-reader-chapter4-final-build.log`.
  2,436 alignment associations synchronized; zero stale panels.
- Reader validation: 392 notes, twelve complete footnotes, 75 redirects
  including 60 title redirects, 80 suppressed running headers, zero errors.
  All 762 HTML files pass rendered-formalization validation. No new titles
  or routes in this batch; earlier legacy-title browser checks remain relevant.
- Browser **92183: terminal exit 0**: five annotated problem pages, twenty
  desktop/phone collapsed/expanded cases, ten definition bookmarks, zero
  overflow or JavaScript errors. Global route audit covers all 233 reviewed
  items before selecting the five changed pages.
  Log: `/tmp/etingof-reader-chapter4-final-sQK0su/browser-final.log`.
- Visually inspected quaternion irreducibility on phone, rotation classification
  on desktop, and elasticity on phone. Additional phone screenshots inspect
  elasticity parameters, affine tensor decomposition and quaternion isomorphism
  notes. Additional screenshot process **4464: terminal exit 0**.
- Search version remains `f30aadf8415c68b9`, 789 documents (no title changes).

## Materialization and publication

Materializer **49397: terminal exit 0**. Exact generated trees/report:
`/tmp/etingof-reader-chapter4-final-sQK0su/{generated-public,generated-private,materialization.json}`.
Public checksum comparison with the PR clone is unchanged. Private retained
bytes/modes and dependency pin match the authoritative sources.

Read-only remote check: public PR #4 is OPEN, REVIEW_REQUIRED, BLOCKED, head
`f9c69bafeccd5158a7249449a92446f844dac381`, no merge commit:
https://github.com/mathlib-initiative/EtingofRepresentationTheory/pull/4

No remote writes, visibility changes or protection changes. Do not publish the
unmerged preview pin. Publication requires independent approval/protected merge,
rematerialization against actual merged main, then private/Pages publication and
live checks. Do not restart the previously completed CI watch. Reviewer choice
remains unanswered; do not select an arbitrary reviewer or weaken approval.

## Next pass

Proceed to Chapter 5, starting with Frobenius–Schur types and their indicator.
Read its original introduction, Definition 5.1.1, even-dimension discussion,
Problem 5.1.2, Definition 5.1.4 and Theorem 5.1.5. The complete small providers
FiniteGroupRepresentations/Auxiliary.lean and AuxiliaryScalar.lean are read.
Only lines 1–200 of InversionAndInvariantForms were read in this turn; further
provider comparison is needed before crediting the even-dimension/indicator
results. No Chapter 5 review credit or annotations assigned yet.

Still pending: all 157 Chapter 5 items, Chapters 6–9, five Chapter 2 items,
front/back matter and full public publication. Keep the goal active.
