# Chapter 6: reflection functors

Verified local checkpoint: 444/583 reviewed, 714 explanations, 139 pending.
Chapter 6: 49/64 reviewed, fifteen pending. Orders 438–448 add eleven reviewed
items, nine explanations, fourteen expandable statements and twenty-five
distinct statement/helper references. Not published; the full-book goal is active.
This continuation makes authoritative editorial and documentation changes and
verifies their fresh render: substantive progress, not a status-only turn.

## Reading edition

Give ten items mathematical titles. Keep the existing Reflection functors
section title. Join sinks/sources, arrow reversal, the introductory sentence,
kernel reflection, its arrow-map paragraph and cokernel reflection into one
continuous reading page, retaining every semantic bookmark. Five new joins
preserve original passage order. The four propositions retain their complete
original proofs, with explanations afterward.

Explain sink/source predicates through empty arrow types, including loop
exclusion and isolated vertices. Explain arrow-indexed direct sums, so parallel
arrows remain separate summands. Distinguish the original vertex set from the
reversed arrow types, and representation arrow maps from the functor's action
on morphisms between representations.

The kernel construction works over a commutative semiring without incoming-arrow
or vertex-dimension finiteness. The cokernel construction works over a commutative
ring with finitely many outgoing arrows. State the additional finite-dimensional
hypotheses of the subsequent field-valued theorems. Explain the vertex-simple
exception, recovery up to an arrow-compatible isomorphism, the separate zero
outcome and the integer-cast rank–nullity reflection formula.

Inspect printed pages 169–170 (PDF raw pages 177–178). The projection paragraph
really does print V_i where the reversed arrow i→j must target V_j. Preserve the
book's wording and explain the indexing typo alongside the checked construction.
Also restore both proof diagrams: all four vertex dots, leaf zero labels below
the dots, the central W/1 labels and the upward arrow. Reunite the second picture,
which conversion had split into three independent displays. Make these layout
repairs in conversion-packets/sol/Chapter6/Proposition6.6.5/Content.lean and its
native module, leaving immutable source Markdown unchanged.

## Source comparison

Complete native items and immutable spans 168:3–173:12 were read. Read the full
vertex predicate/reversal modules, the full 254-line indecomposable dichotomy
module and the full 164-line rank–nullity module. Compare kernel/quotient object
and arrow-map definitions and both functor assemblies/laws through explicit
bounded excerpts. Read the complete final isomorphism assemblies, including
the actual theorem behind the surjectivity alias and the vertexwise
arrow-compatible isomorphism definition. Compare zero alternatives and the
nonzero/compatible-splitting proof branches for reflection preservation.

Detailed bounds and dependency exclusions are recorded in reader-reviews.json.
Long chart/cast/naturality and compatible-splitting engines are dependencies,
not newly claimed full transitive proof audits. Surjective is described in the
comparison text; source_modules contains its mapped aligned alias module,
because declaration-sources.json does not export that underlying module itself.

Improve documentation only in eleven formalization modules: QuiverVertexPredicates,
AuxiliaryQuiverRepresentationTransform, QuiverRepresentationAuxiliaryFunctor,
QuiverRepresentationQuotientTransform, QuiverRepresentationQuotientFunctor,
QuiverRepresentation.Auxiliary, Quiver.FiniteFreeSurjectivity, Surjective,
Quiver.FiniteFreeInjectivity, Quiver.AuxiliaryAtVertex and Quiver.AuxiliaryNatInt.
Correct misleading "endofunctor" and "nonempty codomain" descriptions. No
formal theorem types, definitions, proofs, options, attributes, alignment roles
or repository protections change.

## Verification

- All nine annotation anchors and all five joins pass independent preflight
  against the preceding render. Capture eleven published routes with 57 anchors;
  the section-heading route already has the same three anchors. Add ten new
  records without duplicate keys.
- 62 reader tests (22 reader-prefixed and forty prepare-reader tests), ten
  immutable-source gate tests and exact-private-source validation pass.
  Original-text validation checks all 583 hashes, 235 pages and 5,716 lines:
  zero errors, overlaps or uncovered lines. Scoped whitespace checks pass.
- Official build 92464 exits 0 with sources frozen: all 20,771 Lean jobs pass,
  2,436 alignment associations and zero changed panels. Fresh render: 959 HTML
  files, 714 explanations, fourteen footnotes, twenty-eight joins, 300 redirects,
  including 257 legacy-title redirects. Presentation and rendered-formalization
  validators report zero errors.
- Browser 93808 exits 1 on a new assertion that reads a rendered KaTeX element's
  whole textContent as though it starts with raw TeX. Inspect the actual HTML
  and fix the assertion to use KaTeX's retained application/x-tex annotation.
  This changes the test oracle, not the original formulas or renderer.
- Final browser 65222 exits 0: ten pages, nineteen annotated and twenty-five
  reviewed items, forty collapsed/expanded cases, sixteen definition bookmarks,
  148 individual card actions, 54 helper-link checks, 25 legacy routes and 240
  saved-bookmark cases. Global route discovery covers all 444 reviewed items.
  Runs include the new reflection items and root-sign, Gabriel, organization
  footnote and quaternion/unitary regressions. No JavaScript errors or page
  overflow. New assertions check definition order, uninterrupted introduction,
  both reflection spaces and map paragraphs, and two complete four-vertex
  proof diagrams rendered by KaTeX.
- Visually inspect desktop recovery/dimension explanations, both repaired proof
  pictures and the arrow-map/printed-typo explanation. Inspect phone proof
  diagrams, arrow-map explanation and cokernel explanation. Statements are
  collapsed by default; the original prose is readable and the diagrams match
  the printed layout.
- Search version 6a1d8753930225d2 has 789 documents. Each of the ten revised
  titles has one full-text document and ranks first. Folded construction parts
  target their own retained bookmarks on the joined page.
- Assembly /tmp/etingof-reader-chapter6-reflection-assembly-JCB4kr reproduces
  decoded titles and all display math for the first 49 Chapter 6 items, including
  both diagram repairs. This is regeneration evidence, not publication.

Build log: /tmp/etingof-reader-chapter6-reflection-build.log.
Browser log: /tmp/etingof-reader-chapter6-reflection-browser.log.
Final processes are terminal. No remote write, materialization or deployed
source-pin verification is claimed. The preceding authoritative public PR4
query remains OPEN / REVIEW_REQUIRED / BLOCKED at
f9c69bafeccd5158a7249449a92446f844dac381, with no merge commit; no new PR query
was needed for these local edits. Preserve protections.

## Remaining work and observed presentation edge

Fifteen Chapter 6 items remain: orders 449–463, covering Coxeter elements,
the Gabriel proof and final problems. Their complete native passages were read
as preparation in this continuation, but no annotations, title edits or review
credit have been applied. Read the 24-line Coxeter coordinate definition and
bounded ReflectionDynamics excerpts 1–84, 281–345 and 423–522. The latter prove
eventual negativity for nonzero nonnegative integer vectors; it is not yet a
whole 522-line module audit. Its argument uses periodicity of the particular
integer orbit and a nonzero invariant sum, rather than separately packaging the
book's real operator-sum identity. Remaining source modules were only located.

Phone screenshots expose a remaining typography edge: punctuation following a
long inline formula can wrap onto its own line. The native HTML has the correct
adjacent punctuation, so this is not an authoring typo. Address it in the final
reader-wide presentation pass without changing original prose or forcing wide
formulas to overflow. Do not mistake passing overflow checks for proof that all
line-breaking details are polished.

Continue Chapter 6, then Chapters 7–9/front/back matter. Completion still requires
protected merge, the actual public-main source pin, materialization/rebuild and
public live checks. Do not repeatedly rematerialize the whole public repository
for each editorial batch.
