# Section 5.23: Algebraic representations and Peter–Weyl

Verified local checkpoint: 366/583 reviewed, 585 explanations, 217 pending.
Chapter 5: 133/157 reviewed, 24 pending. Six newly reviewed items, thirteen
notes, twenty-two expandable statements and thirty-one statement/helper
references. The full-book goal remains active; this batch is not published.

## Reading edition

Replace six synthetic titles/H1s and item-title records, plus the raw-math
parent title. Preserve the original mathematical heading, all original
paragraphs, formulas and proofs. Capture seven public routes and all 49
bookmarks. The existing theorem redirect already captured four of its
bookmarks: retain their union with the newly captured seven, not a duplicate
JSON route. Replace the existing theorem title override rather than retaining
duplicate keys. The metadata audit confirms uniqueness after these fixes.

Explain algebraicity as regular matrix entries in k[gij,det(g)^-1], the
extra inverse-determinant coordinate and the difference from strict polynomial
representations. Separate algebraicity from action laws; explain the zero-map
counterexample rather than presenting a raw supporting declaration.

Explain integer highest weights by the smallest nonnegative common shift
and determinant-inverse twist of the Schur model. Identify the finite-dimensional
and bare action definitions as the same representation. Explain invariant
subspace preservation, unbounded tensor degree, uniqueness up to equivariant
isomorphism, and the common polynomial shift used to distinguish labels.

For complete reducibility, state the algebraic-closure/characteristic-zero
hypotheses and distinguish distinct irreducible types from repeated summands
encoding multiplicity. For Peter–Weyl, identify the actual localized coordinate
ring, the negative-reversed-weight dual model and its equivariant identification
with the linear dual, finitely supported direct sum and both ordered group
actions. Keep the complete two-part statement, display and summation clause
contiguous before the annotations.

Compare the book's embedding argument with the source's common determinant
denominator clearing, polynomial semisimplicity and untwisting proof. Explain
evaluation at identity and matrix coefficients, finite-dimensional stable
semisimple envelopes, algebra-density/component injection and coefficient
independence, global spanning, and the bijective map intertwining g^-1*x*h.

For SL, explain why determinant twists disappear, the converse identification
only by uniform shifts, the quotient-set bijection, and classification of
algebraic simple SL representations with the regular-matrix-entry hypothesis.
Explicitly flag that these are group results, not a proof of complete
reducibility/classification for every finite-dimensional sl(V) representation.
Explain the trace projection for N>0 in characteristic zero without claiming
it proves the omitted representation theorem. Treat empty rank separately.

## Comparison scope

Read all six native items, Section523 structure and immutable 133:7–21,
134:1–7. Complete provider comparisons: GeneralLinearGroup.Auxiliary,
AuxiliaryModuleData, AuxiliaryRepresentationParameters (171 lines),
AuxiliaryRepresentationDecompositions (284 lines),
AuxiliaryEquivariantDecomposition (627 lines), GeneralLinear.AuxiliaryRepresentations
(through the final bare/alternative action definitions), CoordinatePolynomials
(through the final determinant-denominator clearing theorem), and
SpecialLinearRestriction (552 lines).

Bounded comparisons: AuxiliarySemisimpleDecomposition 1–144 through the full
aligned proof; GeneralLinearGroup.AuxiliaryDecomposition 410–447 for the
polynomial semisimplicity target; GeneralLinearCoordinateLocalization 1–95 for
determinant/localization/evaluation; AuxiliaryInvariantBilinearPairings 1–165
for dual identification/invariance; LocalizationActions 292–325 for the
commuting product action; TensorLocalization 1–140 for algebraicity and
matrix-coefficient construction, and 158–265 fully for component map,
product equivariance, evaluation at identity and range containment.

SpecialLinearRepresentation 1–83 defines regular-entry and GL-extension
predicates; 704–794 contains the simple algebraic extension proof; 834–878
contains the classification targets. Its intermediate scalar-extension and
Fourier-polynomial lemmas remain dependencies, not fully reread providers.
Recheck ModuleEquivAndTraceSeparation 68–82, reusing the earlier tensor-action
span/Schur simplicity comparison. Algebra-density, joint coefficient
independence and stable finite-envelope helper proofs likewise remain
dependencies; do not claim a whole-project proof audit.

## Verification

- Metadata audit: zero errors and all 31 statement/helper references have
  known source mappings. 38 reader tests and seven immutable-source gate
  tests pass. Scoped whitespace checks pass.
- Original-text gate: 583 hashes, 235 pages, 5,716 lines; zero errors,
  overlaps or uncovered lines. Exact-private-source gate passes.
- Official build 10330: terminal exit 0, all 20,771 jobs pass. Alignment
  synchronization changes zero panels. Reader report: 2,436 associations,
  585 notes, fourteen footnotes, six joined routes, 209 redirects (188
  title redirects), zero presentation errors. Rendered association
  validation covers all 890 HTML files with zero errors.
- Browser 23112: terminal exit 0; eight pages, six annotated/eight reviewed
  items, 32 collapsed/expanded cases, twelve definition bookmarks, 92
  individual card actions, eighteen helper-link cases, seven legacy routes
  and 98 saved-bookmark cases. Zero JavaScript errors or overflow. Includes
  the book-organization and unitary-footnote regressions; global discovery
  verifies unique routes for all 366 reviewed items.
- Add a browser regression that the Peter–Weyl introductory paragraph,
  displayed direct sum and summation clause remain adjacent on both widths.
- Search 5e28c1a4293248dc: 789 documents. All six renamed titles appear once,
  have existing destinations and are searchable. Five distinguishing queries
  rank first; the broad introduction query ranks third among related pages.
- Add reusable desktop/phone screenshots for the algebraicity definition,
  Peter–Weyl theorem and SL boundary. Visually inspect the desktop theorem
  and phone SL remark: original statement/formula flow remains intact,
  exact signatures are collapsed behind mathematical labels, and no
  default namespace/metadata inventory is displayed.

Build log: /tmp/etingof-reader-chapter5-algebraic-build.log.
Browser log: /tmp/etingof-reader-chapter5-algebraic-wlVDJT/browser.log.
All processes have exited. No materialization or deployment is claimed;
canonical sources will be materialized in the publication batch.

## Publication dependency and next work

Read-only check this continuation: public PR4 remains OPEN, REVIEW_REQUIRED
and BLOCKED at f9c69bafeccd5158a7249449a92446f844dac381, with no merge
commit. Preserve review/build protections and do not publish the unmerged
materialized preview. Publication still requires protected public merge,
actual-main pin, materialization/rebuild and live Pages checks. Remaining
editorial work means the goal is active, not blocked or complete.

Next: Section 5.24. Read all three native items and Section524 structure:
heading, reversed Young-symmetrizer/sign-twist problem, and trace-generation
problem. Read complete 165-line SymmetricGroup.PartitionSubmodules proof:
right multiplication maps, same nonzero quasi-idempotent scalar, normalized
inverse and permutation equivariance. These are preparation, not review
credit. SignTwist (621 lines) and Generation (161 lines), their tensor and
weighted-component dependencies, and complete original problem spans still
need comparison. No Section5.24 edits or review credit are included here.
