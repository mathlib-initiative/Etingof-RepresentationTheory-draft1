# Repository boundaries

The authoritative repository is
`mathlib-initiative/Etingof-RepresentationTheory-draft1`.
All source changes and all human-review PRs belong here, targeting its default
branch. Use `scripts/create_reader_pr.py` to open reader/publication PRs; its
repository allowlist must not be bypassed with a direct `gh pr create` call.

The following repositories are generated destinations, not source-review repos:

- `mathlib-initiative/EtingofRepresentationTheory`: generated from
  `clean-code/release` by `materialize_release_repositories.py`.
- `mathlib-initiative/EtingofRepresentationTheory-verso`: generated from
  `verso/release` by the same materialization process.
- `mathlib-initiative/EtingofRepresentationTheory-verso-pages`: generated from
  the verified Verso render.

Never open or update a source PR in those destinations. Never hand-edit their
contents. Fix the generating sources here, merge the source PR here, then run
materialization and publish its verified output. Preserve destination history;
do not replace it with the materializer's temporary self-test history.

Before any GitHub mutation, explicitly classify it as source review or generated
publication and verify the exact repository. A passing generated-output PR is
not a substitute for a source PR here. If publication protections require an
output PR or another policy change, stop and explain the conflict; do not silently
move source review to the generated repository.

Keep unrelated dirty-worktree changes out of reader PRs. Preserve original book
text, checked proofs, repository visibility, and required build checks.
