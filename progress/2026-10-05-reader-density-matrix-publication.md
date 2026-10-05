# Density, matrix modules and filtrations: reading and publication checkpoint

The full-book goal remains active: **138/583 reviewed, 190 annotations, 445 pending**.
The completion audit deliberately rejects this partial pass. No new reading
changes have been deployed to public Pages in this continuation.

## Reading changes

Reviewed thirteen further Chapter 3 items, from the Section 3.2 hypothesis
through Lemma 3.4.2: ten annotated mathematical items and three unobstructed
transitions. The fifteen new explanations cover simultaneous prescribed
images, algebraic rather than topological density, independent operators on
pairwise nonisomorphic simples, finite matrix products, column modules,
opposite-ring duals, transpose and matrix-entry pairings, matrix-unit proofs,
finite-free presentations, strict filtrations and simple successive quotients.
They distinguish the actual checked proof route from the book's route,
existential from canonical choices, and decomposition from nonsplit filtrations.

Read and compared all three Chapter 1 items, including the entire Gerovitch
footnote and page-break continuation of the acknowledgments. Keep these as
book prose without fabricated historical proofs or declaration panels.

Fourteen additional exact declaration renames and eighteen improved source
docstrings were synchronized through providers, naming responses, proposals,
declaration-source mappings and private references. The cumulative reviewed
renames number 49. The docstring matcher now recognizes aliases and structure
fields while retaining its mandatory unique-match check.

The native render exposed an ambiguous `(ii) Let` anchor shared by a theorem
statement and its proof. It is now `(ii) Let V =`; a regression test checks
that ambiguous prefixes fail and the refined anchor inserts at the statement.

The phone view had excessively tall neighboring-page navigation. The
authoritative reader CSS now limits those titles to two visible lines while
retaining complete DOM text and native title attributes. The generated preview
CSS is byte-identical to this source. This CSS refinement followed the full
release gate; reader validation was rerun, and the final browser pass also
asserts a maximum 64-pixel mobile navigation height.

## Verification

Evidence directory: `/tmp/etingof-reader-density-matrix-nXdH7T/`.

- `release-gate.log`: full release gate passed, 12,722 available declarations,
  736 HTML pages and deterministic materialization. Its derived self-test root
  commit is local evidence only, not a publication pin.
- Public strict build: 18,947 jobs; private strict build: 20,771 jobs; success.
- Original book: 583 span hashes, 235 pages, 5,716 lines, no gaps or overlaps.
- Alignment: 2,436 citations, exact agreement with the adjudicated ledger;
  12,722 declarations, 796 registry modules, 824 public modules, no errors.
- Fresh reading HTML: 190 annotations, twelve complete footnotes, 49 redirects,
  525 retained checked declarations and 1,507 source destinations; no errors.
- Twenty-three reader regressions and six immutable-corpus gate tests pass.
- Compiled indexes contain all 49 new declaration names and no old names.
- The six newly changed public Lean files compare equal to the preceding PR
  head after reviewed identifier substitutions and comment/whitespace masking.
- `browser-5.log`: all 138 reviewed reading routes, 552 desktop/phone
  collapsed/expanded cases, 226 working definition bookmarks, zero JavaScript
  errors or overflow. Bookmark-span pages and the heading-only Chapter 2
  introduction are included, not silently omitted.
- `browser-6.log`: final rerun passed on all 138 reviewed routes, with 552
  desktop/phone collapsed/expanded cases, 226 working bookmarks, no JavaScript
  errors or overflow, and navigation at most 64 pixels tall on every phone
  view. Both browser processes **87360** and **71638** terminated successfully.

The old Nix Chromium executable had been garbage-collected. Restored the exact
package through `nix shell nixpkgs#chromium`; use
`/nix/store/g0yvxs8p2ijrvmxpd5mim1ni0fyk9bnh-chromium-154.0.8037.57/bin/chromium`.
The first two browser failure logs are environmental launch failures, not
reader test successes. The fourth caught the initial incomplete route discovery.

## Publication state

Updated generated public PR #4 through a normal descendant commit:
https://github.com/mathlib-initiative/EtingofRepresentationTheory/pull/4

Head: `f9c69bafeccd5158a7249449a92446f844dac381`.
Base: `752fe269b3233f08f0795aa4bcdc5b4c84be7a50`.
Total diff: 47 Lean files plus README, no deletions or CI-setting changes.
The six added files were copied from the validated materialization into the
isolated clone `/tmp/etingof-chapter3-release-HI02bp/public-update`, then
committed and pushed. Its worktree is clean. Root proof/migration changes
remain untouched and uncommitted.

Ruleset 21347752 remains active, without bypass actors: one approval, resolved
review threads, strict passing `build`. PR is OPEN / REVIEW_REQUIRED / BLOCKED;
the authenticated author cannot supply their own approval.

Current CI run: **37246948601**, build job **111566591928**. One watch uses
interval 120, exec process **32063**, output `ci-watch.log` in this directory.
Resume that handle; do not start duplicate monitors or poll Actions repeatedly.
The superseded run 37245109826 was requested cancelled after the new head was
pushed; its old monitor is process 26605 and its log remains in the preceding
checkpoint's evidence directory.

After approval, merge through the protected workflow, wait for the exact merged
revision's cache release, then rematerialize the private edition with that
revision and deploy. The generated private snapshot here still pins OLD main
and MUST NOT be published as-is; it also predates the final CSS refinement.
No private/main or Pages push occurred in this continuation.

Public reading URL:
https://mathlib-initiative.github.io/EtingofRepresentationTheory-verso-pages/

## Next editorial work

Continue Chapter 3 at Section 3.5. Already read its introduction, Definition
3.5.1, Proposition 3.5.2, and the complete public providers
`RingTheory.SimpleModuleAnnihilator` and `RingTheory.JacobsonRadical.TwoSided`.
No new Section 3.5 review records or annotations have been authored yet. Explain
the radical as the Jacobson radical, generality to arbitrary rings, the
same-universe quantifier and unrestricted forward implication, maximal-ideal
quotient test, and two-sidedness despite `Ideal` being a left-ideal type.

Chapter 2 still has five pending items: Theorem 2.1.2, its following finite-group
overview, and Problems 2.15.1, 2.16.3 and 2.16.4. Their original passages were
located/read, but their required full mathematical comparisons remain pending.
The overview's conversion-style heading also needs a mathematical title.
