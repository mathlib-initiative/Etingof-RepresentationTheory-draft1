# Characters and Jordan–Hölder reading pass

Goal remains active: **153/583 items reviewed, 213 annotations, 430 pending**.
No new reader changes have been published to Pages in this continuation.

## Authoritative changes

Reviewed all six Section 3.6–3.7 items, including both character theorem parts,
both Jordan–Hölder proofs, the complete characteristic-p footnote, and both
length/series paragraphs. Added nine explanations beside the relevant original
paragraphs; the transition-only introduction to 3.7 remains unobstructed prose.

Read the complete character definition and quotient providers, submodule/quotient
trace-additivity proof, simple-character independence and spanning proofs, matrix
commutator-span computation, composition-series comparison, finite-copy trace
formula and zero-character example, and maximum strict-chain length provider.
Inspected Mathlib's actual quotient-module JordanHolderLattice instance,
Equivalent definition, full general Jordan–Hölder induction and its last-factor
helper, quotient simplicity criterion, Module.length and the composition-series
length proof.

Reader explanations distinguish the commutator vector-space quotient from an
algebra quotient; a k-linear splitting used to compute trace from an A-linear
splitting; independence of distinct simple characters in any characteristic
from loss of natural-number multiplicities modulo p; matrix commutator span over
any commutative ring from field-only statements; separately checked spanning
and independence from a bundled Basis construction; factor-index bijections
from equality in factor order; and composition length from base-field dimension.
The general Jordan–Hölder source proof is not misrepresented as a separately
checked version of the book's complete character argument.

Every declaration card retains its genuine compiled signature. Per-card reader
documentation replaces vague descriptions without introducing fake constant
names. There were no public Lean, naming-response, proposal or alignment edits.
PR #4 remains stable for review at f9c69bafeccd5158a7249449a92446f844dac381.

## Evidence

- First fresh build: `/tmp/etingof-reader-character-build.log`, success,
  20,771 jobs; all 2,436 exported panel associations agree, zero stale panels.
- Original corpus and registered-only metadata overrides remain byte-identical.
  All 583 source hashes, 235 pages and 5,716 lines pass exact single coverage.
- Twenty-four reader regression tests and six immutable-corpus tests pass:
  `/tmp/etingof-reader-character-tests.log`.
- Reader preparation/validation: 213 annotations, twelve complete footnotes,
  49 redirects and 80 suppressed repeated running headers; zero errors.
- Formalization validation: all 736 HTML files and 2,436 associations, zero errors.
- `/tmp/etingof-reader-characters-h30416/browser.log`: all 153 reviewed routes,
  131 annotated items, 612 desktop/phone collapsed/expanded cases, 252 definition
  bookmarks; zero overflow or JavaScript errors, all phone navigation within
  64 pixels. Browser process 29076 terminated successfully.
- Visually inspected the character theorem at desktop width and Jordan–Hölder
  at phone width. The first character note interrupted the theorem's two parts;
  its authoritative anchor now follows the density proof paragraph instead.
  The second fresh render and focused browser checks pass: both theorem parts
  and the density proof precede the note, at desktop and phone widths.
- Final fresh build: process 87276 terminated successfully,
  `/tmp/etingof-reader-characters-h30416/final-build.log`, 20,771 jobs and zero
  reader/panel errors. Final render retains 539 checked declarations, rewrites
  1,683 links and supplies 1,493 external source destinations.
- `/tmp/etingof-reader-characters-h30416/final-browser.log`: the character and
  Jordan–Hölder pages, eight desktop/phone collapsed/expanded cases, four
  working definition bookmarks, no overflow or JavaScript errors. Process
  76444 terminated successfully. Final formalization validation again covers
  all 736 HTML files and 2,436 exported associations with zero errors.
- Completion audit correctly fails with 430 items pending:
  `/tmp/etingof-reader-characters-h30416/completion-audit.json`.

Final materialization passed (process 36207 terminated successfully):
`/tmp/etingof-reader-characters-h30416/final-materialization.json`.
The generated public tree is byte-identical to the clean PR clone. Generated
private annotation/review metadata are byte-identical to the authoritative
files, including the final placement anchor. This preview pins the unmerged
public PR head, NOT an approved merged/cache-published revision. Rematerialize
against the exact merged commit and its published cache before pushing private
or Pages updates.

A direct native re-render over already prepared output was correctly rejected
by the fresh-output gate; its mixed output was not accepted as evidence. The
official build helper cleared its own output and completed the final fresh
render (process 87276, `/tmp/etingof-reader-characters-h30416/final-build.log`).

## Publication and next work

PR https://github.com/mathlib-initiative/EtingofRepresentationTheory/pull/4 is
open and REVIEW_REQUIRED, with no review requests at the last read. A previous
asynchronous question asks the user which maintainer to request. Do not bypass
the approval/build/visibility protections or publish the unmerged preview.
CI run 37246948601 is still monitored by the original interval-120 watch,
process 32063, `/tmp/etingof-reader-density-matrix-nXdH7T/ci-watch.log`.

Next: Section 3.8. Already read the full original theorem, lemma, continued
proof and Problem 3.8.3 across pages 54–55 and all three core providers:
EndomorphismDichotomy (142 lines), IndependentSpanningFamilies (861 lines),
FiniteDecompositions (132 lines), totaling 1,135 lines. Inspected Mathlib's
Fitting-decomposition statements and proofs in Artinian.Module.
No Section 3.8 review records or annotations have been added yet.

Explain any-field kernel/range stabilization instead of the book's eigenvalue
argument; why indecomposability is essential for nilpotent-sum closure, without
a commutativity assumption; finite independent spanning submodules as an
internal direct sum, with the zero module using the empty family; matching one
summand by inclusion/projection composites summing to identity; and the source's
common-complement quotient equivalence and smaller-dimension induction rather
than pretending it transcribes the book's final projection map line by line.
