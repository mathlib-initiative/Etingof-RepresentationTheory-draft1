# Chapter 4: representations, tensor products and geometric models

Verified local checkpoint: **228/583 reviewed, 362 annotations, 355 pending**.
Chapter 4 is **55/60**, with five problems remaining. Full-book completion and
public publication are still outstanding; the goal remains active.

## Reading changes

Eight new reviews: the problems heading, Problems 4.12.1–4.12.5 and 4.12.9,
and the complete Hamilton historical interlude. Six problems receive 23 notes.

- Dihedral representations: rotation/reflection matrices, odd/even character
  counts, paired rotation eigenvalues, exhaustive classification and the actual
  tensor-square isomorphism. Explain the N=4 reducible residual summand and its
  two character lines. Explicit gaps: the separate checked N=4 splitting and
  identification with the complexified geometric polygon-plane action.
- Heisenberg representations: the triple multiplication law, general action
  `(rho_z(a,b,c)f)(t) = z^(bt-c) f(t-a)`, inverse-root central convention,
  existence/uniqueness, irreducibility, quotient characters, the p Fourier
  summands of R1 (not all p² characters), and the full dimension-square count.
- Symmetric/exterior powers: characteristic-zero field generality, the
  zero-space exception to irreducibility, polynomial eigenvector extraction,
  prime/binary diagonal weights, symmetric transvections and exterior
  permutations. Explain the actual proof differences from the hint.
- Graphs: non-squarefree real adjacency characteristic polynomial means a
  repeated eigenvalue; faithful permutation matrices and the commutative
  distinct-spectrum centralizer give the checked proof.
- Icosahedron: replace meaningless numerical-theorem descriptions with the
  12-, 20- and 30-point internal irreducible decompositions and their
  multiplicities. Explain conditional equivariant comparison with arbitrary
  transitive actions of the required stabilizer sizes. Explicitly distinguish
  these checked coset models from unconstructed geometric point sets.
- Heisenberg tensors: center-supported characters, character products and
  twists, p copies of R_(zw) for noninverse roots, and all p² linear characters
  once for inverse roots. The latter is not p copies of R1.
- Four registered reader titles replace conversion descriptions: Problems,
  graph symmetries, A₅ on vertices/faces/edges, and Hamilton's quaternions.
  Complete historical text, original numbered headings, formulas and Lean
  proofs are preserved.

Read all of the dihedral, Heisenberg, complex-character, graph, coset-action,
exterior/symmetric action, eigenbasis, symmetric-basis and basis-pair providers.
The finite-group decomposition engine was inspected at its invariant-subspace,
character-labeling, fixed-point count and final multiplicity/decomposition
arguments; not every intervening conjugacy/stabilizer helper was reread. Per-item
comparison records bound those claims in reader-reviews.json.

## Verification

- 29 reader regression tests pass. Immutable-source assertion permits only
  registered title changes. Book corpus: 583 verified span hashes, 235 pages,
  5,716 lines, no overlap or uncovered lines.
- Official fresh build **68746: terminal exit 0**, all 20,771 jobs pass.
  Log: `/tmp/etingof-reader-chapter4-problems-build.log`.
  All 2,436 declaration associations synchronized; zero stale panels.
- Reader validation: 362 notes, twelve full footnotes, 75 redirects including
  60 title redirects, 80 suppressed running headers, zero errors. All 762 HTML
  files pass rendered-formalization validation. Selected statements were native
  compiled cards, not copied types; all 36 new card/source links map to real
  modules, not fallback repository searches.
- Browser **23206: terminal exit 0**. Eight pages, six annotated items,
  32 collapsed/expanded desktop/phone cases, twelve definition bookmarks,
  no overflow or JavaScript errors. Global route coverage audits all 228
  reviewed items before selecting changed pages. Log:
  `/tmp/etingof-reader-chapter4-problems-yYOGSO/browser-final.log`.
  Visually inspected Heisenberg, Heisenberg tensors and symmetric/exterior
  powers on phone, and the icosahedron decomposition on desktop.
- Legacy browser **63246: terminal exit 0**. Four old routes at both widths;
  fifteen retained bookmarks, one main title, unchanged fragment and no errors.
  Log: `/tmp/etingof-reader-chapter4-problems-yYOGSO/legacy-browser-final.log`.
  An initial test expected index.html rather than the canonical directory URL;
  corrected that test expectation, with no product change. Registered routes
  and anchors also match the live published xref (normalize its leading slash).
- Active search version `f30aadf8415c68b9`, 789 documents. Each replacement title
  has one result for its semantic item. `Problems` occurs in other chapters too;
  match the semantic identifier, not title text alone.
- Editorial audit is incomplete: 355 items pending, zero metadata errors.
  These checks do not prove full-book correctness or live publication.

## Materialization/publication

Materializer **65591: terminal exit 0**. Exact generated trees/report:
`/tmp/etingof-reader-chapter4-problems-yYOGSO/{generated-public,generated-private,materialization.json}`.
Public checksum comparison with the existing PR clone is unchanged. Private
retained bytes/modes and dependency pin match the authoritative sources.

Read-only GitHub check: public PR #4 is OPEN, REVIEW_REQUIRED, head
`f9c69bafeccd5158a7249449a92446f844dac381`, no merge commit. No remote writes,
proof changes, visibility changes or protection changes. Do not publish the
unmerged preview pin. Publication still requires protected public merge,
rematerialization against actual merged main and downstream/private/Pages
publication followed by live checks. The completed CI watch remains terminal;
do not restart or poll old completed runs. Reviewer choice remains unanswered;
do not select an arbitrary reviewer or weaken approval. Editorial work can
continue while publication awaits review.

## Next pass

Five Chapter 4 items remain: 4.12.6 affine group, 4.12.7 quaternions/rotations,
4.12.8 finite rotation-group classification, 4.12.10 faithful representations
and symmetric/tensor powers, 4.12.11 elasticity. Original texts have been read;
no review credit is assigned without comparing their providers.

Ready for 4.12.10: complete RepresentationPolynomialFunctions (397 lines),
TensorPowerRepresentations (291 lines) and SymmetricPowerRepresentations
(361 lines) read in contiguous chunks during this turn. The polynomial proof
uses a dual vector outside finitely many proper fixed subspaces; its free orbit
is separated by degree-one evaluations. Products of normalized separating
functions construct delta functions, giving surjectivity from the graded direct
sum of symmetric powers to the regular representation. Semisimple lifting and
an embedding of a simple module into the regular representation give a nonzero
intertwiner into one homogeneous degree. It is injective because the source is
simple. Source hypotheses explicitly include finite-dimensional V and W.

SymmetricPowerLift separately embeds the symmetric power into tensor powers
using the characteristic-zero symmetric-invariant equivalence; its equivariance
is proved. The aligned tensor-power endpoint instead gives an independent
character proof: tensor characters are powers, zero multiplicities would kill
all polynomial character averages, and interpolation isolates the identity
character value dim(V). Unitarization proves that only the identity can have
that character value in a faithful representation. Explain this distinction
instead of claiming that endpoint follows the book's polynomial-function hint.
Degree zero is allowed. All auxiliary map/module conversions and the power-map
providers used here were inspected; no notes or reviews yet for 4.12.10.

MatrixConjugationActions is 1,778 lines and AffineGroupRepresentations 1,913;
only their size was checked here, not their proofs. FiniteRotationGroups is
4,078 lines; prior declaration outlines are not proof review. Chapters 5–9,
five Chapter 2 items, front/back matter and full publication remain in scope.
