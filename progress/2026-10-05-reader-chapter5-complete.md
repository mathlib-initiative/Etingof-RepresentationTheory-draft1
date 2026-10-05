# Sections 5.26–5.27: Artin and semidirect products

Verified local checkpoint: 390/583 reviewed, 627 explanations, 193 pending.
Chapter 5: 157/157 reviewed. This batch reviews the final ten items with
fourteen explanations, eleven expandable statements and 24 mapped statement/
helper references. The full-book goal remains active. Not published.

## Reading edition

Replace ten synthetic titles/H1s and synchronize item/reader-title metadata.
Preserve all original theorem statements, proofs, exercises, formulas and
section headings. Capture twelve public routes and 69 bookmarks before
renaming; the fresh render preserves their destinations through redirects.

Explain Artin's rational induction theorem with finite-group and complex
representation assumptions, conjugation invariance and finite rational
combinations. Distinguish arbitrary finite-dimensional subgroup generators
in Lean from the book's irreducible ones: semisimple decomposition generates
the same span. Explain the Frobenius sum, integer restriction multiplicities,
rational/complex matrix rank equivalence, and rational-character coordinates
versus the entire complex class-function space. Explain the source's direct
rational-separator argument and trivial-character converse versus the book's
virtual-character/complex-spanning proof. Apply coverage to cyclic subgroups.

Explain semidirect multiplication and the source's A ⋊[φ] G convention,
finite G/finite abelian A classification scope, inverse dual action,
stabilizers, chosen coset coordinates and base-point transport. Explain that
the classification package supplies concrete constructions, all four book
assertions, dimensions and transport compatibility. Compare the source's
weight-space completeness proof with the book's squared-dimension count.
Explain the trace over fixed cosets and normalization by stabilizer order.

Organize Exercise5.27.2 by its three mathematical examples rather than the
seventeen-declaration inventory: dihedral inversion orbits and parity counts;
affine additive-character orbits, scalar characters and augmentation model,
including q=2; order-p³ shear orbits, dimension counts and explicit scalar/
shift-and-scale models. Explain the additive Multiplicative wrapper.
For Exercise5.27.3, distinguish the assumed character formula and compatible
action/stabilizer/transport data from its derived simplicity, separation and
completeness; explain character orthogonality and squared-dimension exhaustion.

Improve documentation in three canonical Lean source modules without changing
any definitions, theorem types or proofs. In particular replace the false
“formal statement is unavailable” description on the semidirect theorem.

## Comparison scope

Read all ten native items, both parent structures and immutable
144:23–147:17. Read complete AuxiliarySubgroupFunctions (873 lines),
Auxiliary.SubgroupRepresentationMatrices (320), and CyclicCharacterSpan (39).
Bound the 2,452-line semidirect construction comparison to definitions/action
laws, complete simplicity proof, complete completeness target, dimension
target, full final bundle proof and base-point wrapper. Private transport/
baseChange construction and intermediate weight-space/map lemmas remain
dependencies, not a new whole-module proof audit.

Bound Auxiliary (956 lines) to full hypotheses/conclusions, norm proof
segments, mixed-pair setup and final classification/dimension exhaustion;
middle reindexing/mixed-pair calculations remain dependencies. Bound the three
example providers to their concrete group/actions/characters and full
transferred family/count/model wrappers; intermediate family assembly remains
a dependency. Reuse the previously compared Problem4.12.2 and Problem4.12.6
models. Detailed bounds and editorial decisions are in reader-reviews.json.
No new aligned-source coverage gap is asserted in this batch; previously
identified Chapter5 scope gaps remain explicit.

## Verification

- 38 reader tests and seven immutable-source gate tests pass. Review metadata
  audit: zero errors; all 24 new references mapped. Exact-private-source gate
  passes. Original-text gate: 583 hashes, 235 pages, 5,716 lines, zero errors,
  overlaps or uncovered lines. Scoped whitespace checks pass.
- Official build 42717 terminates with exit 0; all 20,771 jobs pass. Alignment
  synchronization changes zero panels. Fresh reader: 2,436 associations,
  627 notes, fourteen footnotes, six joins, 228 redirects (207 title redirects),
  zero presentation errors. Rendered validation: 909 HTML files, 2,436
  associations, zero errors.
- Browser 78830 terminates with exit 0: twelve pages, nine annotated/twelve
  reviewed items, 48 collapsed/expanded cases, eighteen definition bookmarks,
  48 individual card actions, 26 helper-link cases, twelve saved routes and
  138 saved-bookmark cases. Zero JavaScript errors or page overflow. Global
  discovery checks unique reading routes for all 390 reviewed items.
  Include organization-footnote/unitary regressions. Add guards keeping the
  induced-function display adjacent to its introduction/A-action, and keeping
  the character formula and two-display completeness calculation uninterrupted.
- Search aa1907731fff92b9: 789 documents. All ten new titles appear once, have
  existing destinations and rank first for their title query.
- Add reusable desktop/phone screenshots for the Artin statement/coefficient
  remark/proof and semidirect construction/classification/examples/character
  implication. Visually inspect desktop coefficient remark/examples and phone
  construction/classification/Artin theorem. Default statements stay collapsed,
  mathematical explanation labels are readable, the original theorem parts
  remain together, and wide formulas scroll locally.

Build log: /tmp/etingof-reader-chapter5-artin-semidirect-build.log.
Browser log: /tmp/etingof-reader-chapter5-artin-semidirect-v3w0uq/browser.log.
All observed build/browser handles are terminal. No materialization, live
deployment or remote-source-pin verification is claimed.

## Publication and next work

Read-only GitHub check: public PR4 remains OPEN, REVIEW_REQUIRED and BLOCKED
at f9c69bafeccd5158a7249449a92446f844dac381, with no merge commit. Preserve
review/build protections and do not publish that unmerged source preview.
Publication still requires protected merge, actual-public-main pin,
materialization/rebuild and live Pages checks. Editorial work remains,
so the goal is active, not blocked or complete.

Next finish the five pending Chapter2 items, then Chapters6–9 and front/back
matter. Read all five pending Chapter2 native files while this batch built:
Theorem2.1.2, Discussion_after_Theorem2.1.2, Problem2.15.1, Problem2.16.3 and
Problem2.16.4. They have no new edits or review credit. Provider comparisons
still needed: Gabriel finite-quiver/adjacency classification; reuse verified
finite-group results for the overview; sl₂ weight ladders/Casimir/decomposition/
nilpotent completion/tensor decomposition; iterated-ad Lie presentations; and
positive-characteristic sl₂ parameter classification. Do not mistake native
reading for a completed source comparison.
