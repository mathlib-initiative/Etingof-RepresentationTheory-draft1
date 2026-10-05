# Chapter 6: roots, reflections and Gabriel's statement

Verified local checkpoint: 433/583 reviewed, 705 explanations, 150 pending.
Chapter 6: 38/64 reviewed, 26 pending. The batch covers orders 422–437:
sixteen items, sixteen explanations, twenty-seven expandable statements and
forty-one statement/helper references (forty distinct declarations). Not published.
The whole-book goal remains active.

The preceding user-question turn checked the goal but made no implementation
progress. This continuation resumes the same official build handle, observes
its successful completion, checks the fresh render and fixes a browser assertion.
This is substantive verification progress, not a status-only turn.

## Reading edition

Give fourteen items mathematical titles rather than conversion labels. Preserve
the existing Roots and Gabriel section labels. Join the root introduction and
eight following definition/lemma/remark passages into one reading page. Keep
the reflection definition with the Weyl-group finiteness argument, and the
dimension-vector definition with the introduction and Gabriel statement.
Eleven new joins preserve all original passage bookmarks and book order.

Explain adjacency R versus Cartan A = 2I − R, the integer pairing versus the
book's real extension, positive/even norms and the norm-two root predicate.
Explain the source's finite-box argument on the Cartan image, coordinate simple
roots and the sign-splitting proof; keep the printed graph-cut proof intact.
Clarify that positive means nonnegative coordinates, not strictly positive ones.

Explain A-type roots through the zero-sum coordinate lattice and positive
intervals. Distinguish positive-root counts from full root-system counts; state
the D-type rank restriction and the finite calculations yielding 36, 63 and 120.
Explain the norm-two reflection formula, involution and pairing preservation,
and why a faithful action—not merely preservation of a finite root set—is
needed for Weyl-group finiteness.

Explain integer-cast vertex dimensions, arbitrary-field scope, simple Dynkin
orientation, finite-dimensional hypotheses and uniqueness up to isomorphism.
Separate root finiteness from representation realization and uniqueness.

## Source comparison

Complete native passages and immutable spans 164:3–168:2 were read for the
editorial changes. Detailed full/bounded source comparisons and exclusions are
recorded in reader-reviews.json. In particular, the long D/E counting engines
and lower-level reflection/representation realization engines are dependencies,
not a newly claimed whole transitive proof audit.

Source documentation changes are confined to fourteen modules:
AuxiliaryIntegerMatrixTransform, AuxiliaryIntegerMatrixVectorProperty,
AuxiliaryFiniteIndexIntegerFunction, AuxiliaryIntegerVectorTransforms,
AuxiliaryFiniteDimensionalFamily, IntegerMatrixVectorPredicates,
IntegerVectorPredicate, IntegralVectorSign, IntegerZeroSumCoordinates,
FiniteSetCardinality, AdjInputSetCardinalities, MatrixBoundedVectors,
Quiver.DimensionVectorClassification and Quiver.LinearAlgebra.Auxiliary.
Correct generic/unavailable alias descriptions and mathematical doc wording.
No theorem types, definitions, proofs, options, attributes or alignment roles
are changed by these documentation edits.

Capture eighteen published routes with ninety-two anchors, including structural
parents. Two introduction routes already have matching records; add sixteen
new route records without duplicate JSON keys. All sixteen annotation anchors
and eleven join boundaries passed independent preflight checks.

## Verification

- Official build 74828 exits 0, with sources frozen: all 20,771 Lean jobs pass;
  2,436 alignment associations and zero changed panels. The reading render has
  949 HTML files, 705 explanations, fourteen footnotes, twenty-three joins and
  285 redirects, including 247 legacy-title redirects. Presentation and
  rendered-formalization validation report zero errors.
- Browser 19368 exits 1 on an overstrict new assertion: it assumes the Gabriel
  introduction and theorem are direct sibling paragraphs. Actual HTML retains
  nested sections and semantic bookmark spans, but the reading paragraphs are
  consecutive. Fix the assertion to check reading order through section wrappers,
  retaining asides so an intervening explanation would still fail.
- Final browser 62904 exits 0: twenty-three pages, twenty-nine annotated and
  forty reviewed items, 92 collapsed/expanded cases, 32 definition bookmarks,
  336 individual card actions, 96 helper-link checks, 42 legacy routes and 476
  saved-bookmark cases. Global discovery gives all 433 reviewed items unique
  reading destinations. Desktop/phone runs include the first 38 Chapter 6 items,
  the organization footnote and quaternion/unitary regressions. No JavaScript
  errors or page overflow. Original eight root labels remain in book order;
  the Gabriel introduction is immediately followed by its original statement.
- Visually inspect desktop sign-proof, root-count and Gabriel explanations,
  and phone root-count, faithful Weyl-action and Gabriel explanations. Checked
  statements are closed by default; original prose and lists remain readable.
- Search version 0c20159fa8bc667d contains 789 documents. All fourteen revised
  titles have exactly one full-text document and rank first. Joined passages
  target their own retained semantic bookmarks. Gabriel's existing section
  label also occurs on the structural parent; this is not a unique-title claim
  for that unchanged section label.
- 62 reader tests (22 reader-prefixed and 40 prepare-reader tests) and ten
  immutable-source gate tests pass. Exact-private-source validation passes.
  Original-text validation verifies all 583 hashes, 235 pages and 5,716 lines:
  zero errors, overlaps or uncovered lines.
- Temporary assembly /tmp/etingof-reader-chapter6-roots-assembly-a6HVTq matches
  decoded titles and all display math for the first 38 Chapter 6 items. This
  verifies regeneration, not publication.

Build log: /tmp/etingof-reader-chapter6-roots-build.log.
Browser log: /tmp/etingof-reader-chapter6-roots-browser.log.
Both final processes are terminal. No remote writes, materialization, deployed
source-pin verification or publication are claimed. Public PR4 remains OPEN /
REVIEW_REQUIRED / BLOCKED at f9c69bafeccd5158a7249449a92446f844dac381, with no
merge commit. Preserve review and build protections.

## Next work

Continue orders 438–463: reflection functors, Coxeter elements, the Gabriel proof
and final problems, then Chapters 7–9/front/back matter. Native reflection items
438–448 were read as preparation in this continuation. Vertex predicate/reversal
definitions and bounded kernel/quotient functor source excerpts were also read.
No editorial changes or review credit have yet been applied to these items;
truncated combined source output must not be treated as a complete module read.

Publication still requires protected merge, the actual public-main source pin,
materialization/rebuild and checks at the public Verso URL. Do not repeatedly
rematerialize the entire public repository for each editorial batch.
