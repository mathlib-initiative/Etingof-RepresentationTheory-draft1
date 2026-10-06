# Chapter 6: McKay and small-quiver examples

Verified local checkpoint: 417/583 reviewed, 689 explanations, 166 pending.
Chapter 6: 22/64 reviewed, 42 pending. This batch adds nine reviewed items,
seventeen explanations, twenty expandable checked statements and twenty-eight
mapped statement/helper references. Not published. The full-book goal is active.

The preceding user-question turn restated status and made no implementation
progress. This goal turn makes the source changes and completes verification
described below; it is substantive progress, not a wait or a status-only turn.

## Reading edition

Give McKay, A₁/A₂/A₃, D₄, dimension notation and the two introductions clear
mathematical reader labels. Replace both structural section titles containing
raw dollar/subscript markup. Keep the original book metadata/text immutable.
Join the D₄ orientation conclusion to the worked example without rewriting
either original paragraph or losing either semantic bookmark.

Explain McKay multiplicities as intertwiner-space dimensions, complete simple
families, character inversion, paths of positive multiplicity, integer Cartan
nonnegativity and the dimension-weighted null vector. The checked simple affine
predicate requires at least three irreducibles and zero-one adjacency. Explicitly
flag its excluded two-element double-edge case and the absence of aligned
group-by-group diagram/dimension tables for parts (d) and (e).

Distinguish nonzero finite-dimensional indecomposability, dimension restrictions,
model indecomposability and complete unique-isomorphism classification. Explain
the three linear-map models, six chain intervals and six cospan models, over any
field. Put explanations after the decomposition/six-model displays rather than
between an introducing colon and the formulas.

Compare the converted A₃ subspace diagrams with printed page 157 (PDF raw page
165). Restore the space labels below vertex dots in the generating packet and
native module: the OCR conversion put the dots above the labels. Keep immutable
source Markdown unchanged. Regression checks compare all packet/native displays.

Explain D₄'s center-first twelve tuples: three leaf simples, eight center-one
patterns and the exceptional (2;1,1,1) triple of lines. Explain that the exported
standard representation is a noncomputable choice from general root realization,
not the book's coordinate construction. The general classification supplies
orientation-independent positive-root indexing over any field, not a canonical
equivalence of oriented representation categories.

## Source comparison and renderer correction

Full native passages and immutable spans 153:21–164:2 were read. Detailed bounded
source evidence and dependency exclusions are recorded in reader-reviews.json;
do not treat this as a whole-module re-audit of the long private complement,
connectivity and general-root construction engines.

Change source documentation only in FiniteSubgroupRepresentationTheory,
FourVertexStarRepresentationClassification,
FiniteDimensionalFourVertexStarRepresentations, AuxiliaryFiniteSetMembership and
Quiver.DimensionVectorClassification. Correct false unavailable/elided alias
descriptions. No theorem types, definitions, proofs, options, alignment roles,
visibility or review/build protections change.

Add a display-math annotation anchor. The first official build (87436) passes
Lean/alignment but its prose-integrity check rejects an aside inserted inside
Verso's native paragraph wrapper. Inspect the actual HTML, fix placement after
the whole display-only paragraph and reject a mixed prose/display paragraph.
Tests cover standalone/native displays, inline-only/ambiguous matches and mixed
paragraphs. Final official build 35824 passes with sources frozen.

Capture eleven public routes and 59 bookmarks, including the two structural
parents. Two introduction routes already exist in the ledger; remove duplicate
records rather than leave silently overriding JSON keys. Preserve the existing
anchors, which match the newly captured sets. The duplicate-key and immutable
metadata gates pass after this correction.

## Verification

- 62 reader tests (22 reader-prefixed and 40 prepare-reader tests) and ten
  immutable-source gate tests pass. Exact-private-source and scoped whitespace
  checks pass. Original-text validation verifies all 583 hashes, 235 pages and
  5,716 lines, with zero errors, overlaps or uncovered lines.
- Final official build 35824 exits 0: all 20,771 Lean jobs pass; 2,436 alignment
  associations, zero changed panels. Fresh render has 935 HTML files, 689 notes,
  fourteen footnotes, twelve joins and 260 redirects (233 legacy-title redirects).
  Presentation and rendered-formalization validators report zero errors.
- Browser 85787 exits 0: eighteen pages, seventeen annotated/twenty-four reviewed
  items, 72 collapsed/expanded cases, 24 definition bookmarks, 228 individual card
  actions, 68 helper-link cases, 24 saved routes and 292 saved-bookmark cases.
  Global route discovery proves all 417 reviewed items have unique reading
  destinations. Desktop/phone checks include all first 22 Chapter6 items,
  organization-footnote and quaternion/unitary regressions. No JavaScript errors
  or page overflow. Wide formulas remain accessibly horizontally scrollable.
- Add browser assertions for complete A₃ six-model lists uninterrupted by notes,
  notes following complete display wrappers, repaired vertex-label direction and
  the joined D₄ conclusion. Save desktop/phone screenshots for all nine items and
  McKay scope, chain/cospan lists and D₄ standard-model explanations. Visually
  inspect the desktop chain list and D₄ explanation, and phone cospan list,
  McKay scope and D₄ explanation. Checked statements are closed by default.
- Search a439dc512509a4d6 has 789 documents. Each of the nine new titles has
  exactly one full-text document and ranks first; context has readable structural
  mathematical titles. The orientation result targets the joined D₄ bookmark.
- Temporary assembly /tmp/etingof-reader-chapter6-small-quivers-assembly-43WL25
  reproduces all first 22 Chapter6 titles/displays and both changed structural
  titles. Compare decoded title literals. This proves regeneration, not publication.

Build log: /tmp/etingof-reader-chapter6-small-quivers-build.log.
Browser log: /tmp/etingof-reader-chapter6-small-quivers-browser.log.
Both processes are terminal. No remote writes, materialization or live source-pin
verification is claimed. Public PR4 is still OPEN / REVIEW_REQUIRED / BLOCKED at
f9c69bafeccd5158a7249449a92446f844dac381, with no merge commit. Preserve protections.

## Next work

Continue the remaining Chapter6 passages from Section6.4_heading through roots,
reflections/Coxeter/Gabriel and final problems, then Chapters7–9/front/back matter.
Orders 422–430 cover the Cartan form, roots, simple roots, finiteness and the
positive/negative decomposition. Their metadata was inspected; no new annotations
or review credit has been applied. Do not repeatedly rematerialize the entire
public repository for each editorial batch. Publication still requires protected
merge, the actual public-main pin, materialization/rebuild and public live checks.
