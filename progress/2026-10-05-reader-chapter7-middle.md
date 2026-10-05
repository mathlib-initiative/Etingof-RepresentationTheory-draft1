# Chapter 7: representability, adjoints and abelian categories

Verified local checkpoint: 496/583 reviewed, 772 explanations, 87 pending.
This batch covers orders 484–500: seventeen items, nineteen explanations,
twenty-nine expandable statements, seventeen revised titles and twelve joins.
Chapter 7 has 37 reviewed items and 22 remaining. Not published; the goal stays
active. The previous goal turn made substantive implementation progress.

## Reading changes

Unite representability, Yoneda, enrichment and the regular-module example.
Unite the adjunction definition, uniqueness and operator analogy; keep the five
adjunction examples on a separate page with locally placed notes. Unite the
abelian-category introduction, concrete definition and module examples. Unite
the Noetherian exercise, intrinsic categorical properties, Morita example and
linearity discussion. Preserve semantic bookmarks and collapsed statements.

Explain the book/Mathlib representable-versus-corepresentable terminology,
Yoneda variance and uniqueness relative to a specified natural isomorphism;
enriched hom-objects and evaluation at 1. Explain units/counits, the triangle
laws and Hom bijections, correct the first-variable variance in the Lean note,
and identify the canonical comparison as relative to the chosen adjunctions.
Explain tensor currying, both Frobenius directions and finite index, enveloping
algebra, group algebra/units and tensor/symmetric free-algebra adjunctions.

Explain the intrinsic abelian axioms and both directions of the module-category
bridge, universes for the chosen embedding, Noetherian kernels and finite
generation, categorical versus elementwise Mono/Epi, the actual ℚ/M₂(ℚ)
Morita example with nonisomorphic rings, and k-linear Hom groups.

Restore the sentence cut by the floating analogy table in both the authoritative
conversion packet and native module: its two halves now form one paragraph,
with the unchanged caption/table following it. Every prose word, formula and
table cell is retained; only this explicit layout repair and editorial titles
change. Preserve the original transcription and source hashes.

Improve thirteen declaration/supporting docstrings in five source modules and
one module description. Replace the opaque adjunction alias description and
“category-shaped” descriptions; make the finitely-generated module property
and its closure instances explicit. No names, formal types, definitions,
proofs, alignment roles or options change.

## Explicit scope differences

- Example 7.5.3: the regular module corepresents the underlying-set forgetful
  functor. A separate k-linear enriched comparison and the named algebra’s
  categorical finite-dimensional nonrepresentability theorem are not supplied.
  The aligned dual-eigenspace theorem is a related linear-algebra obstruction,
  not that categorical counterexample.
- Example 7.6.3: displayed tensor-dual adjunctions range over finite-dimensional
  group and Lie representation categories, not all representations. The reverse
  induction adjunction separately retains its finite-index hypothesis.
- Example 7.7.2: the aligned FGModuleCat witnesses require the algebra itself
  finite-dimensional. They do not package the abelian category of
  finite-dimensional modules over arbitrary, possibly infinite-dimensional A.

These differences are visible reader notes and recorded review gaps, not
claims that missing generality has been newly proved.

## Evidence and verification

Read complete native passages and immutable spans 187:15–191:12, including the
entire table. Per-item source comparisons and proof-engine exclusions are in
reader-reviews.json. Read the complete short custom modules and selected
RepresentationAdjunctions definitions/final naturality proofs; inspect actual
Mathlib representability, adjunction, uniqueness, abelian and embedding
interfaces. Large imported rigidity, embedding and Morita proofs remain
dependencies; no whole transitive proof audit is claimed.

- Capture seventeen published routes and 98 saved anchors before title edits.
  Where public search lacks the introduction entry, use its actual native
  xref address rather than guessing a route.
- Preflight all nineteen anchors and eleven joins against the preceding render.
  Defer the one deliberately changed table-ending join to the fresh render,
  which checks it and all twenty-nine actual docstring cards.
- A new table-hash test initially stops at the opening :::table delimiter.
  Correct its closing-delimiter match; the unchanged table hash then passes
  in both packet and native module. No expected hash is weakened or replaced.
- Official build 42455 exits zero: all 20,771 jobs, 2,436 associations, no
  panel drift. Fresh render: 1,002 HTML files, 772 explanations, fourteen
  complete footnotes, sixty joins, 375 redirects and 303 legacy-title redirects.
  Reader and rendered-formalization validators report zero errors.
- Seventy reader tests (29 reader-prefixed and 41 preparation tests), ten
  immutable-source gate tests, exact private-source checks and scoped diff
  whitespace checks pass. Original-text validation verifies all 583 hashes,
  235 pages and 5,716 lines without errors, overlaps or uncovered lines.
- Compare the seventeen native bodies with their pre-edit contents, allowing
  exactly the explicit table repair and titles. Regeneration into
  /tmp/etingof-reader-chapter7-middle-assembly-ZceUrD reproduces all seventeen
  titles, bodies, table cells and display formulas.
- Search version ae5f364233bd82cf has 789 documents. Each revised passage has
  one matching title document and ranks first for its title query.
- Browser run 15572 exits zero: eight selected/regression pages, 26 reviewed
  reading items, twenty annotated items, 32 collapsed/expanded cases, fourteen
  definition bookmarks, 164 card actions, eighteen helper links, 25 legacy
  routes and 280 saved-bookmark checks. No JavaScript errors or overflow.
  The regression explicitly checks a continuous adjunction paragraph before
  all fifteen table rows, five separately placed example notes and joined
  module-category discussion. Visually inspect table at 1440/390 pixels and
  the Noetherian/module-category page at 390 pixels.

Logs: /tmp/etingof-reader-chapter7-middle-build.log and
/tmp/etingof-reader-chapter7-middle-browser.log. Screenshots are under
verso/release/_out/reader-chapter7-{analogy-table,adjunctions,
adjunction-examples,abelian-modules}-{1440,390}.png.

## Publication and next work

Read-only GitHub query: public source PR 4 remains open, REVIEW_REQUIRED and
BLOCKED at f9c69bafeccd5158a7249449a92446f844dac381. Approval/build protections
remain unchanged. No remote write or claim of public deployment in this batch.
Source links are structurally checked against the existing pin; verification
of the newly deployed source definitions is still required after publication.

Continue with orders 501–522: complexes/cohomology, exact functors, adjoint
exactness/reflection and the historical interlude. Then Chapters 8–9 and the
remaining front/back matter, cross-book structural polish, materialization and
full public live verification. This checkpoint does not waive those tasks.
