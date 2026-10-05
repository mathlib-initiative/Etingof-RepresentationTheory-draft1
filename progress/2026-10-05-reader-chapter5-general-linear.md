# Sections 5.19–5.20: GL(V) and the Weyl interlude

Verified local checkpoint: 350/583 reviewed, 555 explanations, 233 pending.
Chapter 5: 117/157 reviewed, 40 pending. Six new reviewed items, six notes,
nine expandable statements and thirteen statement/helper references. The
full-book goal remains active; these changes are not published.

## Reading edition

Replace six synthetic page titles/H1s, matching item-title fields, and the two
parent section titles. Remove escaped tensor/underscore notation and raw
TeX dollar signs from navigation titles. Preserve all original prose,
mathematical headings, equations, quotations and bibliography numbers.
Capture eight public routes and all 32 bookmarks before retitling.

For Proposition 5.19.1, explain linear span rather than mere algebra generation,
invertible factorwise tensor actions, infinite-field sufficiency for the
generator algebra and characteristic zero for the centralizer identification.
Explain the finite singular-shift set using charpoly(−b), n+1 distinct good
parameters, the degree-n tensor polynomial and Lagrange interpolation at zero.
Distinguish this explicit linear combination from the book's annihilating
functional argument, including n=0.

For Corollary 5.19.2, explain GL(V)'s postcomposition action on equivariant Hom
spaces, its commutation with permutations, and the linear-span bridge from
B-module simplicity/distinctness to the group interpretation. Identify the
actual checked result as A/B-compatible decomposition data with equivariant
Specht identifications. Record its algebraic-closure assumption and lack of a
separately stated general-field Sn×GL(V) representation isomorphism as an
explicit reader-facing coverage gap.

For Example 5.19.3, identify the fixed and sign-isotypic tensor subspaces.
Explain the symmetric quotient projection and tensor-to-wedge projection,
averaging inverses normalized by n!, and compatibility with all induced
endomorphisms, not only GL(V). Present all six aligned declarations under
mathematical labels. Link the previously reviewed symmetric invariant-subspace
theorem. Distinguish the invariant-subspace dichotomy from nonzero
irreducibility; explain exterior vanishing, Sym^n(0)=0 for positive n, and
both degree-zero powers being k.

Keep the entire Weyl historical interlude as prose without an irrelevant Lean
panel. Confirm thirteen complete paragraphs and five continuous page-break
seams. This preserves the book's historical account; no independent historical
source verification is claimed.

## Comparison scope

Read all six native items and both section structures, immutable 124:17–27,
125–129, and 130:1–5. Reuse the complete 287-line MapSpanCentralizer provider
read in the preceding continuation; recheck interpolation/final span target
150–248. Read the complete AuxiliaryElidedStatement wrapper and
AuxiliarySimpleModuleData provider, comparing the indexed decomposition
reviewed in Section 5.18.

Read all 486 lines of ExteriorSymmetricAuxiliary: fixed/sign kernels, unsigned
and signed permutation sums, quotient/wedge maps, n! identities, inverse
construction, induced maps, both intertwining results, dimension vanishing and
invariant-subspace wrapper. Recheck complete symmetric target 100–166 and
exterior target 106–155; reuse their earlier-reviewed eigenbasis/propagation
helpers and one-row/trivial and one-column/sign Specht identifications.

The review audit accepts modules present in the exported source map. The
corollary's untagged AuxiliarySimpleModuleData dependency is therefore recorded
in the comparison text, while source_modules lists the mapped alias wrapper
and mapped decomposition/span providers. Do not invent an alignment entry or
change a Lean proof to satisfy the audit.

## Verification

- Strict metadata audit: zero errors; all thirteen statement/helper references
  have known source mappings. 38 reader tests and seven immutable-source gate
  tests pass. Scoped whitespace checks pass.
- Original-text gate: 583 hashes, 235 pages, 5,716 lines; zero errors, overlaps
  or uncovered lines. Exact-private-source gate passes, permitting only the
  declared title changes and editorial metadata.
- Official build 30172: terminal exit 0, all 20,771 jobs pass. Alignment sync
  changes zero panels. Reader report: 2,436 associations, 555 notes, fourteen
  footnotes, five joined routes, 191 redirects (171 title redirects), zero
  presentation errors. Rendered association check covers all 873 HTML files.
- Browser 36008: terminal exit 0; eight pages, four annotated/eight reviewed
  items, 32 collapsed/expanded cases, eight definition bookmarks, forty
  individual card actions, eight helper-link cases, eight old routes and
  64 saved-bookmark cases. Zero JavaScript errors or overflow. Includes the
  chapter-1 book-organization and chapter-4 unitary-footnote regressions;
  global discovery covers all 350 reviewed items uniquely.
- Add reusable screenshots for the span proposition, GL multiplicity
  corollary, power example and historical interlude. Visually inspect desktop
  corollary and phone power example; readable labels are visible while the
  exact checked signatures remain collapsed. Inspect retained original
  section headings on both introduction pages.
- Search index 6f354da9b1410029: 789 documents; all six titles unique with
  existing destinations. Five rank first for distinguishing queries. The
  GL(V) introduction ranks second behind its own preserved original book
  heading on the same page; both spaced and typographic-dash queries behave
  identically. This is not a missing search destination or unrelated result.

Build log: /tmp/etingof-reader-chapter5-general-linear-build.log.
Browser log: /tmp/etingof-reader-chapter5-general-linear-JzJ8gv/browser.log.
All processes have exited. No new materialization/deployment is claimed;
publication will rematerialize the canonical sources in one batch.

## Publication and next work

Read-only PR #4 recheck: OPEN, REVIEW_REQUIRED, BLOCKED; head f9c69baf,
mergeCommit null. No remote writes, visibility changes or protection changes.
Actual merged-main pin, materialization, publication and live verification
remain required. Local source URLs do not prove deployed source links.

Next: Section 5.21, Schur polynomials (five items). All five native items and
the section structure have been read, but no items credited and no providers
compared yet. Immutable pages 131–132 still need comparison. Providers:
SymmetricPolynomials/Alternant (830 lines) and PartitionPolynomialEvaluation
(415). Inspect the quotient-as-polynomial witness, determinant exponent/order
conventions, power-sum/character expansion, geometric specialization with
nonzero denominators, and the value at all ones. Distinguish algebraic proof
from the book's limit/L'Hopital argument and check the number-of-variables
parameter rather than silently identifying N with partition degree n.
