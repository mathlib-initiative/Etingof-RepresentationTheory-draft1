# Chapter 4: Frobenius determinant and historical interlude

Verified local checkpoint: **220/583 reviewed, 339 annotations, 363 pending**.
Chapter 4 is 47/60, with 13 items remaining. The entire-book goal remains active.
These changes are local, not published. This continuation first completed the
previous character-table batch's verification, recorded separately in
`2026-10-05-reader-chapter4-tables.md`, then authored and verified eight more
items in Sections 4.10–4.11 with nine explanations.

## Reading changes

- Variables are indexed directly by group elements, independently of an
  enumeration. The definition works over any commutative coefficient ring.
- The book's determinant uses x_(g*h), not x_(g*h^-1). Explain simultaneous
  row/column reindexing and the sign introduced by inversion of columns.
- Explain the chosen matrix-block decomposition, actual representation
  determinant factors, their dimensions/degrees, irreducibility, distinctness
  and conjugacy-class count. State algebraic closedness and the restriction
  that group order be nonzero/invertible in the field, not a modular theorem.
- Distinguish the naturally normalized signed identity from the exact
  sign-free existence theorem. The latter rescales one factor by a chosen root
  of the sign. This is proved in the source, not silently omitted.
- Decode the positive-size generic determinant theorem over complex
  coefficients, including the zero-size exception. Explain actual cofactor
  induction and coprimality, rather than claiming the Lean proof follows the
  book's cyclic specialization.
- Interleave the proof with left-multiplication matrix entries, algebra norms,
  the d-fold column contribution of a d-by-d block, independent matrix-unit
  substitutions/retractions, degree/nonvanishing, block-separating evaluations
  and the center dimension count.
- Preserve the complete historical interlude, its quotations and references
  without invented formalized history. Four conversion-generated titles are
  registered and replaced with mathematical/reading titles; actual old
  published routes and fifteen bookmarks are preserved.

Full book prose, formulas and existing Lean proofs are unchanged. Final visual
review tightened two new notes: remove a dangling 'displayed statement'
reference and an awkward plain-text subscript formula. A scan of all authored
annotations finds none of 'precisely', 'the displayed Lean/type/statement' or
'written independently'. This is a wording check, not a correctness proof.

Source reading: complete IndexedPolynomial, all 318 lines of the complex
generic-determinant provider, and GroupIndexedFactorization's 1–1059 norm,
permutation, generic-induction, degree, irreducibility, nonassociation,
center-count and root-absorption arguments. FDRep's decomposition, block
actions, simplicity/nonisomorphism and complete-family endpoints were inspected,
not all intervening module classification machinery. Boundaries and comparisons
are recorded per item in reader-reviews.json.

## Final verification

- All 29 reader regression tests pass. Immutable source assertion permits only
  registered title replacements. Corpus validation: 583 span hashes, 235 pages,
  5,716 lines, no overlaps or uncovered lines.
- Initial official build 65299: terminal exit 0. Final official build after
  wording refinement 5950: terminal exit 0, all 20,771 jobs pass. Final log:
  `/tmp/etingof-reader-chapter4-frobenius-final-build.log`.
  All 2,436 declaration associations are synchronized, zero stale panels.
- Reader build validation: 339 authored notes, twelve full footnotes,
  71 redirects including 56 title redirects, 80 suppressed running headers,
  zero errors. Definition destinations: 664 retained statements, 2,107
  rewritten links, 1,368 source destinations.
- All 758 HTML files pass rendered-formalization validation after the final
  build. All nine new anchors are unique; selected declarations are already
  native compiled cards and all links resolve real mapped source destinations,
  not fallback repository searches.
- Final browser 16637: terminal exit 0; eight changed reading pages, five
  annotated items, 32 desktop/phone collapsed/expanded cases, eight definition
  bookmarks, no overflow or JavaScript errors. Global route coverage audits
  all 220 reviewed items before selecting changed pages. Log:
  `/tmp/etingof-reader-chapter4-frobenius-WkoQUt/browser-final-refined.log`.
  Prior browser 76337 also passed; desktop proof and phone generic-determinant
  screenshots were visually inspected. Final wording is independently confirmed
  in the fresh render and the complete browser suite was rerun.
- Legacy browser 95107: terminal exit 0; four old routes at both widths,
  all fifteen anchors present and old heading hashes retained. No routes or
  anchors changed in the final wording refinement.
- Active search version `875c6f37015ea52d`: each of four replacement titles has
  exactly one result. Do not count superseded native shards as active results.
- Completion audit remains incomplete: 363 pending items, zero metadata errors.
  These checks do not establish full-book correctness or live publication.

## Materialization and publication

Full materializer 50570: terminal exit 0. Generated repositories/report:
`/tmp/etingof-reader-chapter4-frobenius-WkoQUt/{generated-public,generated-private,materialization.json}`.
After the final two prose edits, supplied copy/configuration helpers refreshed
the private tree; exact retained bytes/modes and dependency pin were reverified.
Public checksum comparison with the existing PR clone is unchanged.

Current read-only GitHub check: public PR #4 remains OPEN, REVIEW_REQUIRED,
head `f9c69bafeccd5158a7249449a92446f844dac381`. No remote writes, proof changes,
visibility changes or protection changes. Do not push the private preview pin;
publication requires protected public merge, actual merged-main rematerialization
and downstream/private/Pages publication followed by live checks. The completed
PR CI watch remains terminal; do not restart it or poll old completed runs.
The unresolved reviewer choice is not permission to pick an arbitrary reviewer
or weaken approval. Editorial work can continue in the meantime.

## Next pass: remaining Chapter 4 problems

All original native problem texts 4.12.1–4.12.11, the 4.12 heading and complete
Hamilton historical interlude 4.13 were read during this turn. No review credit
was assigned before comparing their formalizations.

Ready source readings for the next pass:

- Complete DihedralGroupComplexRepresentations, all 959 lines, read in
  contiguous 1–220, 221–470, 471–685, 686–959 chunks. The rotation/reflection
  coordinate matrices, simple criterion 2j != 0, sign/unit characters and parity
  counts, canonical 0 < j < N/2 parameters, dimension-square exhaustiveness and
  actual character-rigidity tensor isomorphism have been inspected. The tensor
  theorem constructs trivial + reflection-sign + the index-two representation;
  do not call that last summand irreducible for every N. In particular N=4
  requires further splitting. Also distinguish this algebraic coordinate model
  from an explicitly constructed complexification/change-of-basis equivalence
  with the polygon-plane action. No notes authored yet for this problem.
- Complete GraphSpectrumSymmetry, all 119 lines. It proves non-squarefreeness
  of the real adjacency characteristic polynomial from two noncommuting graph
  automorphisms: Hermitian diagonalization, distinct-eigenvalue centralizers,
  commuting permutation matrices and faithfulness. Explain how this means
  repeated real eigenvalues for a finite undirected simple graph, and that the
  proof is spectral rather than an irreducible-block decomposition. No notes
  authored yet for this problem.

Heisenberg, symmetric/exterior powers, coset actions, affine group, quaternion
rotation, finite rotation-group classification, tensor identities, polynomial
functions/tensor powers and elasticity providers remain to be compared. The
11 problem statements are already read, but source inspection is not complete.
FiniteRotationGroups is 4,078 lines: only a declaration outline was read here,
not its classification proof. Avoid converting theorem names or numeric suffixes
into unsupported human claims. Remaining Chapters 5–9, five Chapter 2 items,
front/back matter and whole-book publication checks remain in scope.
