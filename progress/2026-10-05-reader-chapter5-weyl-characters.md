# Section 5.22: Characters of Lλ

Verified local checkpoint: 360/583 reviewed, 572 explanations, 223 pending.
Chapter 5: 127/157 reviewed, 30 pending. Five newly reviewed items, ten notes,
twelve expandable statements and thirty statement/helper references. The
full-book goal remains active; this batch is not published.

## Reading edition

Replace five synthetic page titles/H1s and their item-title records, plus the
parent section title. Remove escaped namespace-like notation and raw dollar
math from navigation. Preserve all original prose, mathematical headings,
displays and proofs. Capture six public routes and all 41 bookmarks before
retitling.

Explain the coordinate Young-symmetrizer image, its commuting GL action and
the rational polynomial of nonnegative weight multiplicities. Explain why
cycle-constant tensor labels produce a power sum for each cycle, including
fixed points. Compare the book's character-table argument with the source's
normalized quasi-idempotent trace and symmetrizer character-separation proof.

For the Weyl theorem, explain column pigeonhole/sign cancellation when p>N,
the algebraic-closure assumption for the checked converse, the padded
partition weight identity, the diagonal evaluation/trace bridge and its
weight-spanning hypothesis. Explicitly distinguish the aligned rational
weight-polynomial statement from the book's arbitrary-g eigenvalue trace
formulation and general characteristic-zero field setting.

Explain rational rather than natural-number division in the dimension
formula, positivity/nonvanishing, the weight-space internal direct sum and
algebraic geometric-sum specialization rather than numerical 0/0. Explain
degree-zero/empty-product cases and the checked two-box-column examples.
Keep the original theorem paragraph immediately beside its promised dimension
formula: all four theorem notes now follow that complete statement/display.

Explain partition labels degree by degree, then all tensor degrees, together
with the invertible-action span bridge and row restriction. Do not imply
this paragraph already classifies all algebraic representations.

For the column shift, replace vague auxiliary-model descriptions by the
determinant character, actual top exterior power and their equivariant
identification. Present both genuine isomorphism-existence theorems. Explain
the polynomial/weight shift, algebraicity and weight-spanning checks,
decomposition/Schur-polynomial independence, and tensor unitor construction.
Distinguish this from the book's tensor inclusion proof and retain the actual
field hypotheses. Lean #check confirms the exterior action identity and
wedge/determinant isomorphism retain IsAlgClosed but omit CharZero; the final
shifted isomorphism requires both.

## Comparison scope

Read all five native items and Section522 structure, original 132:15–37 and
133:1–5. Read complete Partitions.GeneralLinear (737 lines) and ExteriorPower
(503 lines), including all vanishing, padding, positivity, weight, determinant
and final isomorphism proofs. Read complete 103-line cycle-polynomial provider.

Bounded WeightCharacter comparison: 1–120, 130–195, 235–390, 510–575 for
models/definitions; 1850–1968 for trace/coefficient assembly; 3240–3555 for
coefficient-to-character bridge and full symmetrizer-weighted polynomial
proof; all 3480–3945 for the final character/dimension chain, including the
internal weight-space direct sum and univariate cancellation. Earlier
projection/trace/stability helper proofs remain dependencies, not newly
reviewed whole modules.

Read UnitTupleActions 1–165 through the complete diagonal evaluation/trace
theorem. Read AuxiliaryDecomposition 1–105 and full comparison targets
603–773. Its intermediate decomposition/trace-separation prerequisites remain
dependencies. Read GeneralLinearGroup.Auxiliary 1–72 for algebraicity and
coordinate evaluation, and GeneralLinearGroupPolynomialEvaluation 1–95 for
determinant evaluation/twist and restriction interface. Recheck the complete
compatible partition-decomposition target 386–455, reusing Section5.18's
comparison and Section5.19's complete span bridge.

## Verification

- Metadata audit: zero errors, all thirty references have known source
  mappings. 38 reader tests and seven immutable-source gate tests pass.
  Scoped whitespace checks pass.
- Original-text gate: 583 hashes, 235 pages, 5,716 lines; zero errors,
  overlaps or uncovered lines. Exact-private-source gate passes.
- Final official build 10145: terminal exit 0, all 20,771 jobs pass.
  Alignment synchronization changes zero panels. Reader report: 2,436
  associations, 572 notes, fourteen footnotes, six joined routes, 203
  redirects (182 title redirects), zero presentation errors. Rendered
  association validation covers all 884 HTML files with zero errors.
- Final browser 22277: terminal exit 0; seven pages, five annotated/seven
  reviewed items, 28 collapsed/expanded cases, ten definition bookmarks,
  52 individual card actions, 36 helper-link cases, six legacy routes and
  82 saved-bookmark cases. Zero JavaScript errors or overflow. Includes the
  book-organization and unitary-footnote regressions; global discovery
  verifies unique routes for all 360 reviewed items.
- Add a browser regression that the original Weyl theorem paragraph is
  immediately followed by its displayed dimension formula, on both widths.
  Fix the checker's expected declaration-ID prefix to account for Verso's
  apostrophe escaping, while retaining exact FQN text, correct-card binding,
  unique bookmarks, proof links and individual open/close assertions.
- Search c20a6d9d491b4ac5: 789 documents. All five new titles appear once,
  have existing destinations and rank first for distinguishing queries.
- Add reusable screenshots for tensor traces, Weyl theorem and determinant
  twist. Visually inspect the phone determinant-twist page and desktop Weyl
  page, then move notes after the formula and recheck the fresh render. Exact
  signatures remain collapsed behind mathematical labels.

The first browser attempt found stale GL wording from an edit during the
render; a fresh official rebuild resolved it. The second found the apostrophe
expectation bug in the checker; after that correction, browser 6559 passed.
Visual review then prompted the theorem/formula flow change, followed by the
final official build and browser pass above. Earlier passing artifacts are
not substituted for these final current-source results.

Build log: /tmp/etingof-reader-chapter5-weyl-characters-build.log.
Final browser log:
/tmp/etingof-reader-chapter5-weyl-characters-mzNuba/browser-flow-final.log.
All processes have exited. No materialization or deployment is claimed;
canonical sources will be materialized in the publication batch.

## Publication dependency and next work

Read-only check this continuation: public PR4 remains OPEN, REVIEW_REQUIRED
and BLOCKED at f9c69bafeccd5158a7249449a92446f844dac381, with no merge
commit. Preserve review/build protections and do not publish the unmerged
materialized preview. Publication still requires protected public merge,
actual-main pin, materialization/rebuild and live Pages checks. There is
remaining editorial work, so the goal is active rather than blocked.

Next: Section 5.23, algebraic representations of GL(V). Read its structure
and identify six native items: introduction, definition, highest-weight
discussion, complete-reducibility/Peter–Weyl theorem, proof discussion and
sl/SL remark. The algebraicity definition and comparison dependencies above
will be useful, but the six native items and remaining proof providers still
need comparison. No Section5.23 edits or review credit are included here.
