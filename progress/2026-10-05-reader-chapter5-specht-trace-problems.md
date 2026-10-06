# Section 5.24: Specht modules, sign twists and matrix traces

Verified local checkpoint: 369/583 reviewed, 591 explanations, 214 pending.
Chapter 5: 136/157 reviewed, 21 pending. Three newly reviewed items, six
notes, twelve expandable statements and seventeen statement/helper references.
The full-book goal remains active; this batch is not published.

## Reading edition

Replace three synthetic titles/H1s and their item-title records. In particular,
remove the escaped/unrendered formula from the first problem's title. Preserve
all original problem statements, displays and hints, the original section
heading and parent numbering. Capture four public routes and all 25 bookmarks.

For Problem5.24.1, explain left ideals and equivariance of right multiplication,
the same nonzero quasi-idempotent scalar in both composites and its normalized
inverse. Explicitly identify the source's A as the unnormalized signed column
sum and B as the unnormalized row sum: BA and AB correspond to the opposite
book letter order aλbλ and bλaλ. The book's nonzero normalization factors do
not change the ideals. Do not mislabel one source carrier by a book convention
or assert equality of the two chosen carriers.

Explain the sign algebra automorphism, its involution/bijectivity, action
precomposition versus tensoring with the one-dimensional sign representation,
and principal left-ideal transport. Explain transposed diagrams, the box
relabeling permutation, row/column interchange and use of the reversed-product
isomorphism. Interpret the exact sign-scaled intertwining law as the actual
representation isomorphism. Distinguish the conjugate partition λ* from a
linear-dual operation.

For Problem5.24.2, identify the actual complex generic matrix-entry polynomial
ring and all-unit simultaneous-conjugation invariant equalizers. Explain
ordered matrix words and trace invariance, including the empty word. Supply
the mathematical bridge omitted by the raw declaration presentation:
multidegrees preserved by conjugation, matching tensor slots, equivariant
contraction preimages in the permutation-action algebra, and one word trace
per cycle. Give the two-cycle/fixed-point example. Explain finite polynomial
algebra generation, both inclusions and summing multihomogeneous components;
do not assert independence, minimality or a word-length bound. State complex
coefficients, k as the matrix count, and validity of the zero cases.

## Comparison scope

Read all three native items, Section524 structure and immutable 135:1–18.
Reuse the previous turn's complete 165-line PartitionSubmodules comparison,
rechecking its aligned carrier and target statement. Read all 621 lines of
SignTwist, including full transpose-diagram/cardinality and box-permutation
construction, subgroup conjugation/sum identities, involutive algebra map,
ideal transport, carrier equivalences, right-permutation multiplication and
final composed sign-scaled intertwiner. Recheck PartitionAuxiliaryConstructions
78–104 and the earlier original Young-projector definitions to verify the
row/column and normalization conventions.

Read complete Generation (161 lines) and WeightedComponents (191 lines),
including generic matrix action, invariant equalizers, trace invariance,
multidegrees/component stability and complete final generation proof.
Bounded Contraction comparison: 1–90 for basis/matrix/endomorphism contraction,
932–1045 for the equivariant multihomogeneous right inverse and full invariant
lifting proof into the permutation-action algebra. Its intermediate monomial
realization, slot symmetrization and injectivity proofs remain dependencies,
not a claim of a full 1,045-line module reread.

PermutationTrace: 1–76 for tensor trace sums/cycle definitions, 225–248 for
ordered cycle products, 430–520 for final cycle-fiber factorization and the
complete global matrix/linear trace factorization targets. Earlier walk-sum
and orbit lemmas remain dependencies. Reuse the earlier checked tensor-power
span/mutual-centralizer comparison and quasi-idempotent/sandwich prerequisites;
do not claim a new whole-project proof audit.

## Verification

- Metadata audit: zero errors and all seventeen references have known
  source mappings. 38 reader tests and seven immutable-source gate tests
  pass. Recheck the reader tests after the final notation/label tightening.
  Scoped whitespace checks pass.
- Original-text gate: 583 hashes, 235 pages, 5,716 lines; zero errors,
  overlaps or uncovered lines. Exact-private-source gate passes.
- Official build 57112: terminal exit 0, all 20,771 jobs pass. Alignment
  synchronization changes zero panels. Reader report: 2,436 associations,
  591 notes, fourteen footnotes, six joined routes, 212 redirects (191
  title redirects), zero presentation errors. Rendered association
  validation covers all 893 HTML files with zero errors.
- Browser 92718: terminal exit 0; five pages, three annotated/five reviewed
  items, twenty collapsed/expanded cases, six definition bookmarks, 52
  individual card actions, ten helper-link cases, four legacy routes and
  fifty saved-bookmark cases. Zero JavaScript errors or overflow. Includes
  book-organization/unitary-footnote regressions; global discovery verifies
  unique routes for all 369 reviewed items.
- Add a browser regression that the first Specht problem's introductory
  paragraph, displayed ideal and final “is isomorphic” clause stay adjacent
  on both widths, before the hint and explanation.
- Search ddf2f016c2729d70: 789 documents. All three renamed titles appear
  once, have existing destinations and rank first for targeted queries.
- Add reusable desktop/phone screenshots for both problems. Visually
  inspect the desktop Specht page and phone matrix-invariant page: original
  prose/formula flow is preserved, explanations have mathematical labels,
  and checked types remain collapsed without a default namespace inventory.

Build log: /tmp/etingof-reader-chapter5-specht-trace-build.log.
Browser log: /tmp/etingof-reader-chapter5-specht-trace-toDY43/browser.log.
All processes have exited. No materialization or deployment is claimed;
canonical generating sources will be materialized in the publication batch.

## Publication dependency and next work

Read-only check this continuation: public PR4 remains OPEN, REVIEW_REQUIRED
and BLOCKED at f9c69bafeccd5158a7249449a92446f844dac381, with no merge
commit. Preserve review/build protections and do not publish the unmerged
materialized preview. Publication requires protected public merge, actual-main
pin, materialization/rebuild and live Pages checks. Remaining editorial work
means the goal is active, not blocked or complete.

Next: Section 5.25, representations of GL₂(Fq). Read the parent structure
and identify eleven native items across four subsection nodes, spanning
135:19–144:22: introduction; four conjugacy types; one-dimensional setup,
derived subgroup and determinant characters; principal-series setup, theorem
and naming paragraph; complementary-series setup, character lemma and complete
classification summary. Select by node_id prefix, not exact parent equality:
the latter finds only the introduction. Native items, four child structures
and finite-field proof providers still need comparison. No Section5.25 edits
or review credit are included here.
