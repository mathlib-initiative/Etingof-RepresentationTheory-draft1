# Maintainer setup

The repository is public. Configure branch protection on `main` so that the
`Lean CI / build` check is required.

This is a materialized destination, not a source-review repository. Review and
merge changes in `mathlib-initiative/Etingof-RepresentationTheory-draft1`, then
run `materialize_release_repositories.py` there. Publish only its verified
output, preserving destination history. Do not open PRs here or dispatch
dependency-pin edits to the private generated repository.

Each successful push to `main`—and each trusted manual `Lean CI` run explicitly
started on `main`—publishes a revision-bound release named
`formalization-cache-<40-hex-commit>`. The release tag must resolve to that exact
commit and contains exactly named `formalization-<commit>.tar.gz` and
`formalization-<commit>.tar.gz.sha256` assets. Verify the complete pair and its
checksum before materializing the private repository at that exact public SHA.
Consumers fetch
only those explicit assets; GitHub-generated source archives are never artifact
cache inputs.

Enable **immutable releases** in the public repository settings
before the first push to `main`. That push triggers the first cache publication.
Immutability is not retroactive, so enabling it later cannot protect releases
already published. The publish job recreates any interrupted reserved draft,
uploads and byte-verifies the exact
deterministic pair, publishes it, and then requires the Releases API to report
`immutable: true`. Publication fails closed if the repository does not enforce
immutability or if an existing published release has a partial, unexpected, or
byte-different asset set. After publication is attempted, automation never
deletes the release or its tag; a readiness failure is left intact for
inspection, rerun, or manual remediation so an immutable revision tag cannot be
made permanently unusable.
