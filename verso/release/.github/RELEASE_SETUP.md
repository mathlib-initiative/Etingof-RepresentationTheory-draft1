# Maintainer setup

This source repository remains private. The repository owner has authorized
public hosting of the rendered book on GitHub Pages in the separate
`mathlib-initiative/EtingofRepresentationTheory-verso-pages` repository.
Branch protection on private `main` is intentionally not required.

This is a materialized destination, not a source-review repository. Review and
merge changes in `mathlib-initiative/Etingof-RepresentationTheory-draft1`.
Only the materialization process updates the generated tree, including its
exact public Git dependency pin and synchronized formalization panels. Do not
open PRs here or edit that pin independently of the generating sources.

Before materialization, require successful public CI and the immutable,
revision-bound formalization cache for the exact public SHA. Preserve private
repository history when publishing the complete verified generated snapshot.

Required CI is enforced by the build/publish workflow before rendered artifacts
are published. It validates the exact Git dependency layout, verifies and
replays the pinned cache, checks panel alignment, builds with strict diagnostics,
and validates the reading presentation. The publish job needs only
`contents: write` for its durable private GitHub Release; no workflow creates
or merges PRs or commits source updates.

Each successful private-main build publishes rendered HTML as a durable private
GitHub Release and retains a short-lived Actions artifact. Publishing the
verified render to the separate public Pages repository is a separate operation.
