# Section 5.10: Frobenius reciprocity, tensor models and duality

Verified local checkpoint: **294/583 reviewed, 479 annotations, 289 pending**.
Chapter 5: **61/157 reviewed, 96 pending**. Four newly reviewed items contain
two annotated passages with ten notes and eleven expandable checked statements.
The original introduction and exercise preamble have prose-only review records.
These changes are **not published**, and the full-book goal remains active.

## Reader-facing changes

- Explain Theorem 5.10.1 as a k-linear reciprocity equivalence for the book's
  full equivariant-function model, called coinduction in Lean. No group/index/
  dimension finiteness is required. Explain evaluation at 1, the inverse
  v → (x → β(ρ(x)v)), both inverse checks and naturality in both arguments.
- Explain the identity-induction/restriction and identity-coinduction/evaluation
  counterparts of exercise parts (a,c), without asserting a separately checked
  two-sided group-algebra bimodule identification.
- Explain the function/group-algebra Hom comparison in (b), and the finite
  coset-sum comparison in (d). Decode why Lean's generator indexed by g
  corresponds to the usual balanced tensor indexed by g inverse.
- Explain the opposite direction in (e), with induction in the source:
  induction is left adjoint to restriction. The checked declaration itself
  needs no finite-group hypothesis, despite its position in a finite-G section.
- Explain the actual finite-dimensional complex duality isomorphism in (f):
  compare characters at g and g inverse, then apply character rigidity.
  Explicitly distinguish it from the book's general-field pairing construction.
- Correct the earlier Chapter 2.11.6 coverage explanation: a related additive
  balanced-tensor adjunction does exist, and is now linked. It is not the
  complete two-sided, scalar-compatible bimodule equivalence requested there.
- Shorten four titles and retain published routes/bookmarks. A previously
  registered legacy title includes “continues to missing page”; it was captured
  from the actual live xref rather than assumed to match the local title.

## Original sentence and responsive presentation

Problem 5.10.2 had been split mid-sentence across two source-page items. A new,
explicit `reader-joins.json` record reunites the prepared reading pages and
paragraph while retaining the original source spans, hashes, words, both semantic
bookmarks and old destinations. Both parts now share one canonical reading page
with one main heading. Previous/next skips the former continuation page.
Preparation rejects a drifted sentence boundary and compares the entire resulting
book-prose sequence before and after the join. Native source has only a markup
blank line added between independently labeled parts (e) and (f).

The clipped masthead was caused by an absolutely positioned search field. The
authoritative stylesheet now reserves its space, wraps the complete title and
uses responsive type/search widths. Mobile search results fit the viewport.
Original wide equations retain their mathematical layout and horizontal scrolling;
overflowing formulas also receive a named, keyboard-focusable scroll region.
Preparation now resolves relative HTML roots before invoking the search builder.

No proof/declaration names, alignment associations, visibility, CI settings or
review/build protections changed.

## Evidence and verification

- Read complete native Section 5.10 and parts (a)–(f). Read full providers:
  HomAdjunction 129 lines, InductionCoinduction 217, CharacterRigidity 242 and
  BalancedTensorProduct.Adjunction 256. Upstream Coinduced 230–315,
  Induced 110–266 and FiniteIndex 1–100 were read; the previously reviewed
  finite-index inverse/isomorphism endpoint 101–198 is reused explicitly.
- All ten note anchors match one original paragraph. Card/helper mappings
  resolve to source modules; sixteen local references also match existing PR
  source files. Placement follows completed formulas and the final proof,
  rather than splitting displays from their “is given by” clauses.
- Thirty-four reader tests and seven immutable-corpus gate tests pass.
  All 583 source hashes across 235 pages and 5,716 lines remain verified,
  without overlap, uncovered lines or errors. Private-source exactness passes.
- Final official build **15817: terminal exit 0**, all 20,771 jobs pass.
  `/tmp/etingof-reader-chapter5-reciprocity-build-verified.log`
  Earlier attempts caught a paragraph-prefix anchor mismatch and the search
  overlay; both were corrected before this fresh final build and browser pass.
- Reader validation: 479 annotations, twelve complete footnotes, 128 redirects
  (112 title redirects), one joined reading page, 80 suppressed running headers,
  zero errors. All 814 HTML files and 2,436 alignment associations validate.
- Browser **28942: terminal exit 0**: eight pages containing nine reviewed
  items (six annotated), thirty-two desktop/phone collapsed/expanded cases,
  fourteen checked-definition bookmarks, zero JS errors/whole-page overflow.
  Global route audit covers all 294 review records, including the joined items.
- Responsive/legacy browser **29789: terminal exit 0**: all 34 saved bookmarks
  on four renamed pages pass at desktop/phone widths. The complete joined
  original sentence is present in one paragraph, all seven exercise notes are
  present, main heading is unique and navigation has no self-loop.
- Masthead text and actual interactive search results fit at widths
  320, 390, 600, 700, 701, 900, 1200 and 1440. ArrowRight on the focused wide
  function-model equation actually scrolls it. No JavaScript errors.
- Visually inspected the final phone reciprocity theorem and desktop tensor/Hom
  exercise. Full masthead is visible; original mathematics and human note labels
  are readable, with checked statements collapsed by default.
- Actual prepared search version `69cebcae9922fa8c`, 789 documents. Four titles
  each occur once with real destinations, including the joined canonical page.
  Queries for reciprocity/evaluation/identity, induction/restriction/group/algebras
  and tensor/Hom/duality rank the corresponding revised pages first.
- Official-link browser **17583: terminal exit 0**: all six Mathlib links reach
  their correct official module/declaration anchor, not the machine finder view.

Materializer **17954: terminal exit 0**. Final exact generated trees, report,
browser and link logs:
`/tmp/etingof-reader-chapter5-reciprocity-verified-dK22Fc/`.
Private retained bytes/modes and dependency pin match. Public checksum comparison
against the existing PR clone is unchanged. Earlier temporary materializations
precede the final masthead correction and are not the final artifacts.

## Publication gate and next work

Final read-only check: public PR #4 is still OPEN, REVIEW_REQUIRED and BLOCKED
at `f9c69bafeccd5158a7249449a92446f844dac381`, with no merge commit:
https://github.com/mathlib-initiative/EtingofRepresentationTheory/pull/4

No remote writes. Do not publish the unmerged preview dependency or weaken
protections. After the protected merge, materialize against actual merged main,
rebuild/publish through the generating repositories and verify the public reader.

Next: Section 5.11's S3/S4 and A5 induced-representation decompositions, then
the symmetric-group classification. All three Section 5.11 native items were
read and located, but their providers were not compared and no review credit
or annotations beyond Section 5.10 have been assigned.

The full-book pass and live publication remain incomplete. The explicit partial
coverage gap for the tensor framework/general-field duality is not a proof defect
that should be concealed by the reader presentation.
