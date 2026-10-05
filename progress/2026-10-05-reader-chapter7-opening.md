# Chapter 7 opening: categories, functors, naturality and equivalence

Verified local checkpoint: 479/583 reviewed, 753 explanations, 104 pending.
This batch covers orders 464–483: twenty items, twenty explanations, nineteen
expandable statements, sixteen changed titles and thirteen reading-page joins.
Chapter 7 has twenty reviewed items and thirty-nine remaining. Not published;
the full-book goal remains active. This is substantive implementation progress.

## Reading changes

Join each section introduction to its definition and immediate discussion.
The categories page continues through examples, size conventions, full
subcategories and enrichment. Keep the nine functor examples and the four
naturality examples on their own reading pages, with notes at the relevant
examples. Joined pages retain semantic bookmarks and a consolidated dependency
disclosure rather than repeating inventories after each paragraph.

Explain objects and arrow types, category laws and the order of composition;
universe levels rather than an unrestricted class of all types; the homotopy
congruence and quotient; full-subcategory objects and unchanged arrows; linear
hom-spaces and tensor-product enriched composition. Explain functor object and
arrow maps, the two Hom functors, permutation-descended symmetric powers,
equivariant Hom postcomposition and reflection transport on morphisms.

For naturality, distinguish compatible components from unrelated objectwise
isomorphisms. Explain evaluation into the double dual, the infinite-dimensional
obstruction, the every-field three-dimensional transvection obstruction to
natural dualization, evaluation at 1 for natural forgetful endomorphisms, and
why A-linearity leaves only central elements for identity endomorphisms.
Explain quasi-inverses, natural unit/counit and the triangle law, the actual
one-object/two-object equivalence, and the finite-type cardinality skeleton.

State the checked scope: arbitrary commutative-ring Schur construction rather
than irreducible classification, finite outgoing arrows for cokernel reflection,
finite generation over a field for the double-dual functor, all modules for the
endomorphism results, and an arbitrary ring for the center result. The linear
category note does not claim a separately constructed enriched-category record.

Improve fifteen declaration docstrings in eleven formalization source modules
and four module descriptions. In particular, aliases for standard Category,
Functor, NatTrans and Equivalence now have mathematical descriptions instead
of “type operator” or “associated type.” No names, types, definitions, proofs,
alignment roles or options change. Selected statements use mathematical labels;
their exact Lean names remain available inside the checked disclosures.

Restore three paragraph breaks in both conversion packets and native sources:
category objects versus arrows, functor object versus arrow maps, and the two
size remarks. All original words and formulas are retained. The pure chapter
heading item retains its existing heading routes; broader structural-page
polish is not implied by this item’s book-prose-only source comparison.

## Evidence and verification

Read complete native items and immutable pages 181–186 plus the relevant span
187:1–14. Source comparisons and bounded proof-engine exclusions are recorded
per item in reader-reviews.json. Read the selected custom aliases/constructions
and the actual Mathlib category, functor, naturality, full-subcategory, linear,
enriched, equivalence, Yoneda and finite-type skeleton interfaces. Reuse the
previously checked reflection-functor interfaces; no new whole transitive
proof audit is claimed.

- Preflight nineteen anchors and thirteen joins against the preceding render.
  Defer one anchor whose paragraph is deliberately split in the new source;
  the fresh render checks it and all nineteen actual statement cards.
- Capture twenty-two published Chapter 7 routes and one hundred anchors.
  The first official build passes Lean and alignment but fails at migration:
  two unchanged chapter-heading routes were incorrectly keyed to their parent.
  Correct their keys to the actual heading tags, and capture the parent’s
  published route with its stable semantic bookmark. Do not report that failed
  preparation as a passing build.
- Final official build 95491 exits zero: 20,771 jobs, 2,436 associations, no
  panel drift. Fresh render: 986 HTML files, 753 explanations, fourteen intact
  footnotes, forty-eight joins, 347 redirects and 287 legacy-title redirects.
  Reader and rendered-formalization validators report zero errors.
- Sixty-seven reader tests (26 reader-prefixed plus 41 preparation tests), ten
  immutable-source gate tests, exact private-source checks and scoped diff
  whitespace checks pass. Original-text validation checks all 583 hashes,
  235 pages and 5,716 lines without errors, overlaps or uncovered lines.
- Compare all twenty native book passages with their pre-edit contents, ignoring
  only titles and paragraph whitespace. Regenerate from authoritative packets
  into /tmp/etingof-reader-chapter7-opening-assembly-VVrhIu: all twenty titles,
  book bodies and display formulas match.
- Search version d143732015a84ba8 has 789 documents. Each of the nineteen
  searchable passages has exactly one matching title document and ranks first
  for its title query. Do not count the inactive native bucket version.
- The initial browser run exposes a test-harness error: navigating between
  fragments of the same document returns no navigation response. Fix the
  harness to check that document’s HTTP destination, then still verify the
  anchor and overflow. Do not weaken the bookmark checks.
- Final browser run 78041 exits zero: ten selected/regression pages, 34 reviewed
  reading items, 24 annotated items, forty collapsed/expanded cases, sixteen
  definition bookmarks, 128 card actions, 46 helper links, 33 legacy routes and
  320 saved-bookmark cases. No JavaScript errors or horizontal overflow.
  Visually inspect categories and naturality at 1440 and 390 pixels.

Logs: /tmp/etingof-reader-chapter7-opening-final-build.log and
/tmp/etingof-reader-chapter7-opening-final-browser.log. Screenshots are under
verso/release/_out/reader-chapter7-{categories,naturality}-{1440,390}.png.

## Publication and next work

Read-only GitHub check: public source PR 4 remains open, REVIEW_REQUIRED and
BLOCKED at f9c69bafeccd5158a7249449a92446f844dac381. Preserve its approval/build
protections. No remote write or claim of public deployment in this batch.
Current source links remain structural checks against the existing pin, not
verification of newly deployed definitions.

Continue with orders 484 onward: representability/Yoneda, adjoints, abelian
categories, then complexes and exactness. After the full editorial pass, finish
cross-book structural-page polish and publication/live checks. The remaining
104 items and that end-to-end work are not waived by this checkpoint.
