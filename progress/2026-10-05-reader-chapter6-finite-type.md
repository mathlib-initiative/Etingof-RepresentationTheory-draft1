# Chapter 6: finite-type quivers

Verified local checkpoint: 408/583 reviewed, 672 explanations, 175 pending.
Chapter 6: 13/64 reviewed. This batch adds three reviewed items, seven explanations,
five expandable checked statements and twelve mapped statement/helper references.
Not published. The full-book goal remains active.

## Reading edition and mathematical scope

Join the finite-type definition, Gabriel criterion and three-part necessity
exercise into one page, with mathematical titles and preserved semantic bookmarks.
Keep both original hints and all three parts in order. Explain finite type up
to isomorphism, finite-dimensional indecomposability, all-orientation quantification
and the distinction between directed multiplicities and undirected adjacency.

Explain the strict dimension inequality via common scalar base change: it fixes
arrow transforms and removes an independent parameter from the orbit map. The
source does not separately construct the book's W-plus-k action. Explain the
factor-two normalization of the Cartan form, absolute-value reduction and
denominator clearing. Explain that rational density establishes semidefiniteness;
determinant nonvanishing is also needed for real positive definiteness.

Explicitly distinguish the simple-orientation/algebraically-closed-field matrix
equivalence from the book's general-quiver statement. The zero-diagonal lemma
uses an orientation witness that already prohibits self-arrows; it does not
prove general self-loop exclusion from representation finiteness. Record the
missing general loop/multiple-arrow reduction rather than presenting that lemma
as its proof. The earlier arbitrary-field Dynkin sufficiency is not an excuse
to erase assumptions from this particular equivalence.

## Generating sources and comparison

Read all three native items and immutable spans 152:35–37 and 153:1–20. Read full
PosDefCriterion, Quiver.Finite, AdjacencyMatrixQuadraticForms and
AdjacencyQuadraticForm. Read orientation, indecomposability and isomorphism
definitions and the canonical-orientation proof. Read the complete strict
finite-orbit parameter/scaling proof at FiniteOrbitDimensionBounds 88–320,
reusing the previous localization comparison. Reuse the Chapter2 positive-root
comparison; intermediate decomposition/root constructions remain dependencies,
not a new whole-module audit. Bound FiniteTypeCriterion to its definitions and
exported targets. Detailed evidence and two partial-coverage records are in
reader-reviews.json.

Change documentation only in PosDefCriterion, Quiver.Finite, MatrixOrientation
and QuiverRepresentation.Auxiliary. Replace the false alias descriptions saying
the type contains an elided term. No definitions, theorem types, proofs, options,
visibility or protections change. Keep original Markdown/book metadata immutable;
the registered reader-title overrides are the only item-metadata differences.

Capture three public routes and 21 bookmarks. The first manifest edit placed
them outside the routes map, so the browser tested only the previous ten routes.
Correct the schema and add an audit regression rejecting silently ignored
top-level records and records lacking saved anchors. Rebuild and actually test
all thirteen selected legacy routes. Do not credit a capture as a redirect test.

## Verification

- 56 reader tests and ten immutable-source gate tests pass. Exact-private-source
  and scoped whitespace checks pass. The unchanged original-text gate verifies
  583 hashes, 235 pages and 5,716 lines, with zero errors/overlaps/uncovered lines.
  Review audit: 408 reviewed, 175 pending, zero errors.
- Final official build 2527 terminates with exit 0: all 20,771 jobs pass, no
  changed alignment panels, 2,436 associations. Earlier build 32738 passes but
  lacks the corrected three-route manifest. It also performs an automatic
  dependency rebuild after the last documentation refinement; final build 2527
  uses frozen sources. No current build or browser process remains live.
- Fresh reader: 672 explanations, fourteen footnotes, eleven joins, 250 redirects
  (224 legacy-title redirects), zero presentation errors. Rendered formalization
  validation: 926 HTML files, 2,436 associations, zero errors.
- Final browser 10819 terminates with exit 0: ten pages, eleven annotated/fifteen
  reviewed items, forty collapsed/expanded cases, fourteen definition bookmarks,
  116 individual card actions, 36 helper-link cases, thirteen saved routes and
  174 saved-bookmark cases. Global discovery covers all 408 reviewed items
  uniquely. Include desktop/phone checks of the joined finite-type parts/hints,
  first ten Chapter6 items, complete Sylvester footer, organization-footnote and
  unitary regressions. No JavaScript errors or page overflow.
- Search acb3bff532a956e2: 789 documents. Each new title has one semantic
  full-text result, rank 1 and an existing bookmark on the common reading page.
- Save desktop/phone screenshots for all three items. Visually inspect the
  desktop introduction, phone criterion and phone necessity/hint. Original prose
  precedes its explanation; statements are closed and the gap is visibly separate.
- Temporary assembly /tmp/etingof-reader-chapter6-finite-type-assembly-DuuwLQ
  reproduces all thirteen Chapter6 titles and displays from generating packets.
  Compare decoded title literals: the generator's Unicode escape and native
  apostrophe are semantically identical. This is regeneration, not publication.

Build log: /tmp/etingof-reader-chapter6-finite-type-build.log.
Browser log: /tmp/etingof-reader-chapter6-finite-type-browser.log.
No remote writes, publishable-repository materialization or live source-pin
verification is claimed. Public PR4 remains OPEN, REVIEW_REQUIRED and BLOCKED
at f9c69bafeccd5158a7249449a92446f844dac381, with no merge commit. Keep protections.

## Next work

Continue the remaining 51 Chapter6 items, beginning with McKay and the small-quiver
examples, then roots/reflection functors/Coxeter/Gabriel and the final problems.
Batch related source-documentation changes before the next full build, and freeze
sources while it runs to avoid invalidating all native book modules mid-build.
Chapters7–9 and front/back matter still need their systematic pass afterward.

McKay preparation is not review credit. Read its definitions (tautological
representation, complete simple family and multiplicity), full symmetry proof,
dimension-weighted row identity, complete integer semidefiniteness/null-vector
proofs, connected-path target/setup and final affine-predicate assembly. Bound the
middle connectivity and group-theoretic diagonal/multiplicity engines as
dependencies. The affine assembly assumes at least three irreducibles and
simple adjacency. Check the excluded two-element subgroup and group-by-group
diagram/dimension coverage before drafting notes. The two misleading auxiliary
aliases there are merely negative-identity matrix/character facts; not missing
formal theorem types. No McKay notes or source edits are applied yet.
