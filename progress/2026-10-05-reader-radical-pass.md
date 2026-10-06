# Radical and finite-dimensional algebra reading pass

Goal still active: **147/583 reviewed, 204 annotations, 436 pending**.
No new reader changes are live on Pages in this continuation.

## Authoritative work

Reviewed all nine Section 3.5 items, including every original proof paragraph
and the zero-algebra footnote. The heading-only introduction remains book prose;
the eight mathematical items have fourteen new interspersed explanations.

Read the complete public providers for the common simple-module annihilator,
two-sidedness, nilpotence, finite dimension of simples, complete finite coatom
families, the quotient endomorphism product, the sum-of-squares bound, both
radical examples, the radical/semisimplicity bridge and the five-condition
equivalence. These ten modules total 1,259 lines. Also inspected the relevant
Mathlib Artinian nilpotence, semisimple annihilation and algebraically closed
Wedderburn–Artin statements/proofs, and the nonzero indecomposability predicate.

Notes explain arbitrary-ring and arbitrary-field generality where checked,
the algebraic-closedness hypothesis for full k-endomorphism blocks, explicit
finite-family completeness, quotient algebra rather than vector-space
equivalence, existential representatives, type-size quantifiers, ideal-wide
nilpotence and the absence of an explicit exponent. Examples explain n>0 for
the truncated polynomial algebra, any-field diagonal-character classification,
and why noncentral diagonal matrix units act as module projections modulo the
radical. All exact signatures remain genuine compiled declaration cards.
Per-card reader descriptions improve vague public documentation without
changing the checked signature or public source dependency.

One additional genuine partial gap is now explicit: the final block-triangular
generalization of Example 3.5.6 has no corresponding theorem in its aligned
sources. Both ordinary upper-triangular and truncated-polynomial radical and
simple-module results are checked. Source searches found unrelated matrix
triangularization results, not a theorem proving the stated extension.

No Lean provider, naming response, proposal, alignment edge or public PR source
was changed in this pass. The public prerequisite PR remains stable for review.

## Whole-book presentation fix

Corollary 3.5.5 contained a printed running section header between statement
and proof. Reader preparation now suppresses generated body headings only
when their numbered title exactly repeats an enclosing title in native xref
context. Transcription and generated Lean remain untouched. The original ID
is kept on a bookmark span, native semantic search marks it hidden, and its
redundant navigation row is removed. Proof paragraphs are protected by an
additional before/after equality check.

The fresh full-book render identified **80** such repeated headers. All eighty
bookmarks survive, none remain visible as headings, and all are marked hidden
in semantic search. A regression test protects a similarly numbered but
different heading and verifies preservation of the proof and bookmark.
Full-text indexing still preserves the original contents; its 789-document
version remains `c48f56ed05bed526`.

Anchor preflight caught raw TeX in the radical statement and Verso's ordered-list
paragraph (whose `2.` marker is not paragraph text). Correct anchors are the
one-backslash `(ii) \\operatorname{Rad}(A)` and `Let A be the algebra of upper
triangular`. Final native rendering inserted every new annotation successfully.

## Evidence

- Fresh build: `/tmp/etingof-reader-radical-build.log`, success, 20,771 jobs;
  all 2,436 panel associations agree with Lean's export, zero stale panels.
- Private corpus byte equality and registered-only metadata overrides pass.
  Original book: all 583 hashes, 235 pages, 5,716 lines, no gaps or overlaps.
- Reader validation: 204 annotations, twelve complete footnotes, 49 redirects,
  zero errors. Formalization validation covers all 736 HTML files and all
  2,436 exported associations, zero errors.
- Twenty-four reader regression tests and six immutable-corpus gate tests pass.
- Definition-link resolution retains 529 declarations, rewrites 1,647 existing
  links and supplies 1,503 external source destinations.
- `/tmp/etingof-reader-radical-De2srY/browser.log`: all 147 reviewed reading
  routes, including 126 annotated items, at 1440 and 390 pixels; 588 collapsed/
  expanded cases, 242 definition bookmarks, zero JavaScript errors or overflow.
  Every phone navigation area meets the 64-pixel bound. Browser process 26183
  terminated successfully. Visually inspected the phone radical example.
- Screenshots include `verso/release/_out/chapter3-radical-{quotient,examples}-390.png`.
- Completion audit deliberately returns incomplete with 436 pending items.

Materialization in `/tmp/etingof-reader-radical-De2srY/` passed (process 90291
terminated successfully). Its generated public tree is byte-identical to the
clean PR clone at f9c69bafeccd5158a7249449a92446f844dac381. The private tree
includes the latest annotations and header processor, byte-identical to their
authoritative sources. It provisionally pins that public PR head, NOT an
approved merged revision/cache release. Do not publish it as-is: after merge,
rematerialize against the exact merged revision and its published cache.

## Publication and next work

PR #4: https://github.com/mathlib-initiative/EtingofRepresentationTheory/pull/4
Head remains `f9c69bafeccd5158a7249449a92446f844dac381`.
One approval is required; no reviews or review requests existed at the last
read. Asked the user asynchronously which maintainer to request review from.
Do not request an external review until they identify/authorize the reviewer.
Keep all existing review/build/visibility protections intact.

CI run 37246948601 remains live. Its single interval-120 watch is process
**32063**, log `/tmp/etingof-reader-density-matrix-nXdH7T/ci-watch.log`.
Resume this confirmed live handle; do not start another watch or poll Actions
repeatedly. The build was at artifact-cache mapping / strict library build.
No private or Pages push was performed.

Next: Section 3.6, then Jordan–Hölder. Already read the complete three original
Section 3.6 items across pages 52–53 and four whole providers (562 lines):
`Algebra.Module.AuxiliaryQuotientMap`, `Module.SubmoduleQuotientAuxiliary`,
`Algebra.Module.Dual.SimpleFamilies`, `LinearAlgebra.MatrixTraceKernels`.
No new character annotations or review records have been authored yet.

Explain trace composed with the action map; the quotient by the commutator
*subspace*, not an algebra quotient; finite-free commutative-ring scope of the
definition/trace descent; character additivity without A-linear splitting
(the proof uses a k-linear section); finite-family density and a rank-one
trace-one target, so no division by dimension or characteristic-zero hypothesis;
traceless matrices as the commutator span over any commutative ring; and the
actual spanning-plus-independence formulation rather than a separately bundled
basis in the supplied character theorem. The semisimple span proof transports
to the joint endomorphism product and makes each tracial block functional a
scalar trace. The general commutator provider imported by MatrixTraceKernels
has not yet been read; inspect it before reviewing the character quotient.
