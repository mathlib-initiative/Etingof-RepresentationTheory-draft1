# Section 5.18: Schur–Weyl duality for gl(V)

Verified local checkpoint: 344/583 reviewed, 549 explanations, 239 pending.
Chapter 5: 111/157 reviewed, 46 pending. Eight newly reviewed items, twelve
passage-specific notes, thirteen expandable statements and 25 statement/helper
references. Not published; the full-book goal remains active.

## Reading edition

Replace eight synthetic page titles/H1s and matching item-title fields with
mathematical titles. Replace the parent section's escaped-TeX title with plain
gl(V); preserve the original mathematical heading and every book sentence.

Explain the arbitrary-field bicentralizer and semisimplicity results separately
from the algebraically closed evaluation decomposition and simple-type
correspondence. Explain Hom multiplicity spaces, postcomposition by B,
precomposition when changing representatives, and compatible actions on both
tensor factors. Record the field restriction explicitly as a coverage gap,
not as a theorem that silently proves more than its checked assumptions.

Distinguish permutation reindexing, the infinitesimal one-factor-at-a-time
action Δn(b), repeated factorwise powers, and the enveloping-algebra image.
Explain invariant tensor endomorphisms versus the symmetric-power quotient,
polarization and division by n!, Newton identities in a commuting subalgebra
even when A is noncommutative, Vandermonde coefficient extraction, and n=0.

Explain Maschke's passage to the actual image algebra and distinguish its
faithful action from injectivity of the entire group-algebra map. For the
partition-labelled decomposition, expose the algebraic-closure limitation and
distinguish the indexed statement carrying Specht identifications/action laws
from the packaged statement asserting a bare linear equivalence. Explain
unused-label zero factors and distinct nonzero multiplicity spaces.

Join the isolated closing theorem sentence to the end of the intervening
lemma, retaining its exact text and bookmarks. Add an explicit hide_navigation
join option: remove this folded tail's redundant sidebar and section-search
entry without deleting its semantic anchor. Capture nine published routes
and all 45 bookmarks before changing titles. Existing proofs and declaration
associations are unchanged.

## Comparison scope

Read all eight native modules, section structure and original 122–124.
Complete the 221-line enveloping-action provider across preparation and this
turn, and the complete 77-line tensor-decomposition provider.

Bounded centralizer comparison: 1–145, 150–267, 660–806 and 905–1025;
isotypic-centralizer definitions 1–95/120–175 and complete bijection and
exhaustivity targets 200–337. Intermediate Schur/isotypic helpers are
dependencies, not a claimed full reread of both modules.

Bounded tensor constructions: repeated-vector definition 1–35, polarization
130–231, interpolation 253–290, general-algebra definitions/interpolation
635–725 and full Newton/generator targets 725–910. Compare the symmetric
quotient constructor in SymmetricPower.Basis 1–120 and Mathlib's
TensorPower/Symmetric 1–90. Intermediate inclusion-exclusion and invariant-span
helpers remain dependencies.

Mutual-centralizers definitions, image/Maschke/faithfulness, averaging and
mutual-centralizer/semisimplicity proofs 1–243; decomposition signatures and
compatibility alias binding compared separately. Partition provider's
direct-sum/action/data definitions 1–210 and complete labelling/indexed/tensor
targets 309–570. Intermediate classification/cardinality helpers are
dependencies, not a whole-module reread.

## Verification and reader defects fixed

- Strict metadata/source-reference audit: zero errors; all 25 references have
  known source mappings. 38 reader tests and seven immutable-source gate tests
  pass. Scoped whitespace checks pass.
- Original-text validator: 583 hashes, 235 pages, 5,716 lines; zero errors,
  overlaps or uncovered lines. Exact-private-source gate passes.
- Final official build 81376: terminal exit 0; all 20,771 jobs pass. Alignment
  sync changes zero panels. Reader report: 2,436 associations, 549 notes,
  fourteen footnotes, five joined routes, 183 redirects, 163 title redirects;
  presentation validation has zero errors. All 865 HTML files pass the rendered
  association check.
- Initial build 83186 caught an editorial anchor error: Theorem 5.18.4's (i)
  shares its paragraph with the theorem label. Correct the prefix to the full
  label; subsequent builds pass. No book wording is changed to satisfy it.
- Actual search test exposed a Unicode-dash tokenizer defect: ordinary
  “Maschke Schur Weyl” ranked its own new title seventh. Configure the same
  ASCII/typographic dash separators during indexing and browser loading.
  Final index 37a18d9f99db429c has 789 documents; all six substantive new titles
  are unique, point to existing pages and rank first for distinguishing queries.
  Both “Schur Weyl” and “Schur–Weyl” variants pass; all seven dash characters
  tokenize consistently. Reuse this configuration for the entire book.
- Final browser 28766: terminal exit 0; nine pages, seven annotated/ten
  reviewed items, 36 collapsed/expanded cases, ten definition bookmarks,
  56 individual card actions, 24 helper-link cases, nine legacy routes and
  90 saved-bookmark cases; zero JavaScript errors or overflow. Includes the
  chapter-1 book-organization and chapter-4 unitary-footnote regressions.
  Global discovery covers all 344 reviewed items uniquely.
- Extend the reusable browser check with screenshots for the double
  centralizer, pure-power lemma and Schur–Weyl theorem, and an assertion that
  explicitly folded navigation titles are absent. Visually inspect phone
  lemma and final desktop theorem. A screenshot's transient sidebar gap was
  checked against a fresh browser: adjacent remaining rows have the normal
  two-pixel separation; no persistent empty row remains.
- Independently verify the folded tail has readerHidden section metadata and
  exactly one retained anchor, and is absent from sidebar navigation.

Build log: /tmp/etingof-reader-chapter5-schur-weyl-build.log.
Browser logs: /tmp/etingof-reader-chapter5-schur-weyl-7cKJ9X/.
All build/browser/diagnostic processes have exited. Materialization is deferred
to the publication batch; this checkpoint does not claim a newly materialized
or deployed repository. The previous public snapshot is unchanged.

## Publication and next work

Read-only PR #4 check: OPEN, REVIEW_REQUIRED, BLOCKED; head f9c69baf,
mergeCommit null. No remote writes, visibility changes or protection changes.
After protected merge, pin actual main, materialize/rebuild/publish and check
the live public render. Local source URLs are not live-publication evidence.

Next: Section 5.19, Schur–Weyl duality for GL(V). Its four native items and
structure have been read, as has the complete 287-line MapSpanCentralizer
provider. It proves the span of invertible factorwise maps over any infinite
field using finite bad shifts and explicit Lagrange interpolation; the
centralizer identification additionally uses characteristic zero. No 5.19
items are credited yet. Still compare the original continuation page 125,
the corollary's AuxiliarySimpleModuleData target (through
AuxiliaryElidedStatement.auxiliaryElidedStatement001452), and the example's
486-line ExteriorSymmetricAuxiliary provider. Preserve and explain field
assumptions and the exact equivariance/content of those statements.
