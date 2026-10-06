# Krull–Schmidt and scalar-extension reading pass

Goal active: **161/583 reviewed, 226 annotations, 422 pending**.
Chapter 3: 46/58 reviewed. No new reader updates are live on Pages.

## Authoritative work

Reviewed all eight Section 3.8 items: heading-only introduction, theorem,
endomorphism lemma, continued uniqueness proof, arbitrary-field problem,
Noether–Deuring problem and its full cross-page hint, continuous-function
counterexample, and finite-length remark. Added thirteen mathematical notes;
the heading-only introduction remains book prose.

Read the full finite-dimensional decomposition, dichotomy and wrapper providers
(1,135 lines, begun in the previous continuation), the whole 473-line periodic/
antiperiodic function provider, both complete scalar-extension descent wrappers,
the complete tensor-coordinate and tensor-restriction providers, the repeated-
copy equivalence and split-map proofs, finite-coefficient subalgebra construction
for both maps, and the relevant statements/proof steps in the general finite-
length provider. Inspected Mathlib's Fitting and finite-length/chain-condition
equivalence and Module.length finiteness results.

Notes explain independent spanning submodules versus pairwise disjointness;
noncanonical isomorphic matching and the empty zero-module decomposition;
arbitrary-field Fitting decomposition instead of the eigenvalue proof;
noncommuting nilpotent sums only under the indecomposability hypothesis;
inverse-normalized nilpotents proved via the dichotomy, not assumed from a
false general product rule; identity-sum matching and common-complement
quotient comparison; reversed tensor order and extended-algebra linearity;
specialization to a finite residue-field extension, not a finite subfield of L;
positive integer multiplicity cancellation even in positive characteristic;
retractions rather than mere injections as the split-summand condition;
connectedness and idempotents, antiperiodic generators and their zeros, and the
exact sine/cosine matrix and inverse; and finite module length without any
base-field or vector-space dimension assumption.

Genuine compiled signatures are retained behind mathematically named cards.
Per-card documentation overrides eliminate vague descriptions from these notes.
No public Lean, naming response, proposal, alignment or PR-source edit occurred.
PR #4 remains stable at f9c69bafeccd5158a7249449a92446f844dac381.

## Presentation and validation

Reduced phone main headings to 1.65rem with 1.25 line height. Desktop headings
are unchanged. The reusable browser check now asserts phone title font size
at most 28px and still checks all navigation areas at most 64px, collapsed and
expanded declaration cards, overflow, metadata leakage and definition bookmarks.
Added theorem, Fitting and periodic-function screenshots at both widths.

The native converter joins Lemma 3.8.2 part (ii) and its first proof paragraph
into one paragraph. An anchor beginning `Proof. (i)` therefore matched nothing.
The correct `(ii) If` anchor inserts the explanation after that complete native
paragraph. Preflight verified all thirteen final anchors uniquely. The failed
first preparation was not accepted; the official helper cleared its own output
and completed a fresh final build.

- `/tmp/etingof-reader-krull-hzALZ5/final-build.log`: process 75199 terminated
  successfully, 20,771 jobs, all 2,436 panel associations exact, zero stale panels.
- Original corpus and registered-only editorial overrides are unchanged:
  all 583 hashes, 235 pages and 5,716 lines, no uncovered lines or overlaps.
- Twenty-four reader regression tests and six immutable-corpus tests pass:
  `/tmp/etingof-reader-krull-tests.log`.
- Reader validation: 226 notes, twelve complete footnotes, 49 redirects,
  80 suppressed repeated running headers, zero errors. Native search remains
  789 documents, version c48f56ed05bed526.
- 550 retained checked declarations, 1,739 rewritten links, 1,482 external
  source destinations. All 736 HTML files and 2,436 exported associations pass
  formalization validation. Rendered reader.css matches the authoritative asset.
- Browser check process 42946 terminated successfully:
  `/tmp/etingof-reader-krull-hzALZ5/browser.log`. All 161 reviewed reading routes,
  including 138 annotated items, pass at 1440 and 390 pixels: 644 collapsed/
  expanded cases, 266 working definition bookmarks, zero overflow or JavaScript
  errors. Every phone title is at most 28px and every phone navigation area is
  at most 64px. Visually inspected the Fitting page at desktop width and the
  periodic-function counterexample at phone width; both original problem parts
  precede the explanations on the latter page.
- Completion audit correctly fails with 422 items pending:
  `/tmp/etingof-reader-krull-hzALZ5/completion-audit.json`.

Final materialization passed (process 6673 terminated successfully):
`/tmp/etingof-reader-krull-hzALZ5/final-materialization.json`. Generated public
source is byte-identical to the clean PR clone. Generated private annotations
and CSS match authoritative final files, including the corrected anchor.
This is a provisional unmerged-PR pin, not an approved cache-published release.
Rematerialize against the exact merged commit and its published cache before
publishing private/Pages updates.

## Publication and next work

PR https://github.com/mathlib-initiative/EtingofRepresentationTheory/pull/4
remains OPEN and REVIEW_REQUIRED with no review requests. The earlier user
question asking which maintainer to request is still unanswered. Keep all
review/build/visibility protections intact; do not publish the unmerged preview.
CI run 37246948601 remains on its original watch (process 32063, interval 120),
log `/tmp/etingof-reader-density-matrix-nXdH7T/ci-watch.log`; last read showed
strict library/cache recording still running, prior setup/legal/linter steps green.

Next: Section 3.9, then 3.10, leaving no Chapter 3 items pending. Already read
the full Problem 3.9.1 across pages 56–57, its generated Verso module, and all
750 lines of ExtensionCocycles (including a re-read of the truncated quotient/
zero-cocycle wrapper). Also read all five generated problem modules and the
heading-only IntroductionTo39. No Section 3.9 annotations or review records
have been added yet.

For extensions, explain the cocycle multiplication equation and automatic
f(1)=0, coboundary kernel/range and the quotient Ext encoding, actual A-module
construction/exact inclusion/projection/quotient, shear equivalence fixing the
end terms versus arbitrary underlying-module isomorphism, the book's swapped
B¹(V,W) notation in the converse, and nonzero scalar proportionality modulo
coboundaries. State algebraic closedness for the simple-module classification,
distinguish cocycle representatives from quotient classes, and do not claim a
separately bundled projective-space or arbitrary-short-exact-sequence classifier.
