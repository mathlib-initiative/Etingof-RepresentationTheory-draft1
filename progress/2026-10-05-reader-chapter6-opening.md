# Chapter 6: field embeddings, finite orbits and Dynkin diagrams

Verified local checkpoint: 405/583 reviewed, 665 explanations, 178 pending.
Chapter 6: 10/64 reviewed. This batch adds fourteen explanations, 23 expandable
statements and 34 mapped statement/helper references. Not published; the full
book goal remains active.

## Reading edition

Give the opening problems mathematical titles. Explain transcendence degree,
dense-orbit polynomial substitution and determinant-localized matrix functions.
The GL coefficient condition includes inverse determinants: do not describe it
as requiring polynomial extension to all matrices or invent a coverage gap.
Explain adjacency versus Cartan matrices, the integer-vector Dynkin condition,
vertex relabeling, determinant recurrences, forbidden cycles/branching and
positive affine kernel labels. Distinguish simple affine graphs and cycle
vertex-count indexing from unrestricted multigraph claims.

Restore all ten converted diagrams in both their generating packets and native
Lean documents, compared with original printed PDF pages 150–152. D branches
at the penultimate chain vertex; E branches at the third vertex. Affine E
labels and branching satisfy the independently reconstructed relation Rm=2m.
Use connected rectangular drawings for the cycle and double fork: the first
render's diagonal fragments did not reach their vertices. Preserve the graph,
labels, captions, original exercise prose and immutable transcription.

Join the classification introduction, theorem and two continued exercise pages
into one reading passage. Keep all five finite diagrams in one list and parts
(a)–(g) in order. No annotation or synthetic heading interrupts the introduction
of the affine list. Keep semantic/source bookmarks and saved public links.
Move the complete Sylvester footnote after the final exercise part.

## Implementation and comparisons

Add reviewed block continuations, with exact prose/math boundaries, an optional
validated list merge and semantic bookmarks. Detach native footnotes whether
inside or beside their source item before joining. Place them after the common
reading section, not before the first navigation bar: Verso has navigation both
above and below its content. The first render caught duplicate nested-note
bookmarks; screenshot inspection subsequently caught the top-navigation placement
bug. Both are fixed, with regressions and actual-browser placement assertions.

Read all ten native items and immutable source spans. Read full polynomial-field
embedding and finite-orbit providers, transformed-matrix and Dynkin predicate
definitions. Compare the finite classification constructors, exported equivalence
and model validity; intermediate graph classification remains a dependency.
Read the cycle kernel/determinant proofs, edge-count target and branch-obstruction
targets/witness setup; not a whole-module audit of their intermediate graph
calculations. Compare affine constructors/marks, the complete marks-kernel proof,
weighted-Laplacian setup, model validity and final classification assembly; the
large private affine case analysis remains a dependency. Detailed bounds are
recorded in reader-reviews.json.

Improve documentation only in AuxiliaryIntegerMatrixProperty, GeneralLinearGroup
Auxiliary and PolynomialRepresentation.FiniteOrbits. No theorem types, definitions,
proofs, options, visibility or review protections change. Original book.json and
source Markdown remain byte-identical. Titles, annotations, reviews, legacy routes
and joins are authoritative editorial inputs, not output-only HTML patches.

## Verification

- 55 reader tests and ten immutable-source gate tests pass. Exact-private-source
  gate passes. Original-text gate: 583 hashes, 235 pages, 5,716 lines, zero errors,
  overlaps or uncovered lines. Scoped whitespace check passes.
- Final official build 64642 terminates with exit 0: all 20,771 jobs pass, zero
  changed alignment panels, 2,436 associations. Earlier build 16798 also passes;
  its screenshots exposed footnote placement and prompted the final rebuild.
  Reader: fourteen footnotes, nine joins, 245 redirects (221 title redirects),
  zero presentation errors. Rendered validation: 923 HTML files, zero errors.
- Final browser 97626 terminates with exit 0: nine pages, eight annotated/twelve
  reviewed items, 36 collapsed/expanded cases, twelve definition bookmarks,
  96 card actions, 22 helper-link cases, ten saved routes and 132 saved-bookmark
  cases. Global discovery covers all 405 reviewed items uniquely. Desktop/phone
  checks include ordered parts, complete finite/affine lists, final footnote
  placement, source-link shape, no JavaScript errors and no page overflow.
  Correct the screenshot-only part-(c) selector to allow leading whitespace.
- Search a8755c02d556de5d contains 789 documents. All eight prose-bearing new
  items have one semantic full-text result, their new title, an existing
  destination and rank 1 for that title query. The two heading-only items have
  valid semantic heading-search destinations, not invented full-text prose.
- Visually inspect desktop classification, closed cycle/double fork, complete
  Sylvester footer, phone affine diagrams and phone finite-orbit prose. Wide
  exceptional diagrams scroll locally; checked statements are initially closed.
- Fresh temporary assembly /tmp/etingof-reader-chapter6-assembly-NoYoqs converts
  all 583 approved items and reproduces all ten titles and corrected displays.
  It verifies regeneration, not publication or the deployed source revision.

Build log: /tmp/etingof-reader-chapter6-opening-build.log.
Browser log: /tmp/etingof-reader-chapter6-opening-7AEIKf/browser.log.
All observed build/browser handles are terminal. No remote writes this batch.

## Publication and next work

Public PR4 is still OPEN, REVIEW_REQUIRED and BLOCKED at
f9c69bafeccd5158a7249449a92446f844dac381, with no merge commit. Preserve approval
and build protections. Publication requires protected merge, actual-main source
pin, materialization/rebuild and public Pages checks. Local build links still
refer to the earlier published source revision; do not call this a live release.

Next: finite-type quivers (three split items), McKay, then the remaining Chapter6
sections. Preliminary source reading is not review credit. The finite-type
matrix predicate quantifies over simple orientations and algebraically closed
fields; its zero-diagonal result uses already-loopless orientation data. Explain
that scope rather than claiming it proves the general self-loop exclusion.
Check McKay's three-irreducible hypothesis and explicit group/dimension coverage
before writing its notes. Continue Chapters7–9 and front/back matter afterward.
