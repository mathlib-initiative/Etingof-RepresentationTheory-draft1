# Chapter 7: complexes, cohomology and exact functors

Verified local checkpoint: 518/583 reviewed, 797 explanations, 65 pending.
This batch covers orders 501–522: twenty-two items, twenty-five explanations,
forty-nine expandable statements, twenty-two revised titles and nine joins.
All fifty-nine Chapter 7 items now have source-comparison records. This is a
local reading-pass checkpoint, not publication or completion of the full goal.

## Reading changes

Unite the cochain definition with maps, cycles and boundaries; short exact
sequences with their split example and vector-space exercise; the long exact
sequence with its abstract connecting-morphism definition; additive functors
with biproduct preservation and examples; semisimplicity with Maschke and
preservation of split sequences; adjoint exactness with reflection functors.
Keep the historical interlude as the original nineteen prose paragraphs,
without a formalization inventory. Retain all quotations and citations.

Explain upward cochain indexing despite Mathlib's uniform `homology` name,
categorical Mono/Epi and the cokernel comparison, chosen complements and the
nonsplit integer sequence, both independence checks for the connecting map,
all three exact pairs, Koszul sign cancellation, contracting homotopies,
cohomology-preserving splitting and the natural Künneth comparison. Explain
additivity and scalar preservation separately, finite limits/colimits in the
additive abelian setting, semisimplicity of the source rather than target,
opposite-ring right actions in balanced tensors, and the actual Hom/tensor
counterexamples over ℤ. Reflection changes quiver orientation and retains
the finite outgoing-arrow hypothesis; it is not an endofunctor equivalence.

Replace vague docstrings in ten generating formalization modules with their
mathematical meaning, including the cohomology alias, extension record,
semisimplicity predicate and long-exact/Künneth witnesses. No declaration
names, types, proofs, alignment roles, linter options or protections change.

## Layout repairs and scope differences

The de Rham footnote had swallowed the formula defining cohomology and the
definition of exactness. Restore those unchanged words to the main paragraph
in both the conversion packet and native module; retain only the complete
original de Rham example in the note. Separate the first tensor-complex
question from the preceding differential display in both generation inputs.

The visual pass then catches the head item's Notes block interrupting the
joined continuation. Repair block joining to carry notes from both the head
and tail after all reading content, retaining their IDs and return links.
Test nested and external head notes, successive continuations, and rejection
of duplicate note bookmarks. Verify all fourteen rendered note blocks now
follow their complete original reading content.

Two limits are explicitly visible in reader notes and comparison records:

- The selected tensor square-zero statement assumes a field; it does not
  certify part (i)'s arbitrary commutative-ring specialization. Parts (ii)–(iv)
  use the field hypothesis printed in the book.
- The supplied induction exactness theorem assumes finite index. It covers
  the finite-group case, not arbitrary infinite-index subgroups.

The linear-functor note also clarifies that `Functor.Linear` records scalar
preservation separately; the book's linear Hom maps use additivity as well.
Do not present the scalar-preservation alias alone as the combined property.

## Evidence and verification

Read all twenty-two native passages and immutable spans 191:13–204:3.
Source-comparison records state the actual modules/interfaces/proof portions
read, including the full TensorHomology assembly and bounded reads of the
larger complement and reflection engines. Imported proof machinery remains
dependencies; no audit of the entire transitive library is claimed.

- Capture twenty-two published routes and 154 saved anchors before title
  changes. Resolve introduction routes through the actual published xref,
  not guessed slugs. The public search script is under `-verso-search/`.
- All twenty-two native modules exactly match their pre-edit contents except
  the declared titles and two explicit layout repairs. Compare prepared DOM
  prose with the preceding render, allowing only the restored main cohomology
  text and newly separated question. No other paragraph or formula changes.
- Regeneration into
  `/tmp/etingof-reader-chapter7-final-assembly-Pv4Ogq` reproduces all twenty-two
  titles and prose bodies, including footnote and display boundaries.
- Official build 4936 exits zero. After the joined-note placement repair,
  rebuild 1982 also exits zero: all 20,771 jobs, 2,436 associations, no panel
  drift. Final render has 1,024 HTML files, 797 explanations, fourteen notes,
  sixty-nine joins, 406 redirects and 325 legacy-title redirects. Reader and
  rendered-formalization checks report zero errors.
- Seventy-four reader/preparation tests (32 + 42), ten immutable-source gate
  tests, exact private-source checks and scoped whitespace checks pass.
  Original-text validation verifies 583 hashes, 235 pages and 5,716 lines,
  without errors, overlaps or uncovered lines.
- Search version `4acb8299f320f937` has 789 documents. All nineteen nonempty
  revised passages have one matching title document and rank first. Three
  heading-only introductions are excluded from this content-search assertion.
- Initial browser 48641 passes sixteen pages. Following the note-placement
  repair, browser 45516 passes seventeen selected/regression pages, 38 reviewed
  reading items, 28 annotated items, 68 collapsed/expanded cases, 24 definition
  bookmarks, 296 card actions, 26 helper links, 37 legacy routes and 476 saved
  bookmark checks. No JavaScript errors or horizontal overflow. Regressions
  include the original Chapter 1 multi-paragraph note, the adjunction table,
  Chapter 6 classification, and the full Sylvester note after the last exercise
  part. The cohomology regression requires its note after the joined discussion.
- Visually inspect mobile cohomology and exactness pages, desktop tensor
  differential and mobile Künneth conclusion. Supplementary capture 16145
  exits zero and shows the complete de Rham note after the entire joined
  passage, at both desktop and phone widths.

Logs: `/tmp/etingof-reader-chapter7-final-build.log` and
`/tmp/etingof-reader-chapter7-final-browser.log`. Screenshots are under
`verso/release/_out/reader-chapter7-{cohomology,kunneth,exactness,footnote,kunneth-conclusion}-{1440,390}.png`.

## Publication and remaining work

Read-only check of public source PR 4: OPEN, REVIEW_REQUIRED, BLOCKED, head
`f9c69bafeccd5158a7249449a92446f844dac381`, no merge commit. No remote writes,
self-approval, review-rule changes or public deployment in this batch.
Source links are checked structurally against the existing pin; newly
deployed source destinations still require verification after publication.

Continue with all twenty-four Chapter 8 items, then thirty-five Chapter 9
items and six remaining front/back-matter items. The three thin heading-only
wrappers in sections 7.8–7.10 still need consolidation in the cross-book
navigation pass; recording their source review does not waive that defect.
Finish global structural polish, materialize through the protected source
workflow, publish, and perform the full live public verification. The goal
remains active and is not blocked while this in-scope work remains available.
