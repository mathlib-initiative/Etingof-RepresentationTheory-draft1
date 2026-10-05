# Maintainer setup

This source repository remains private. The repository owner has authorized
public hosting of the rendered book on GitHub Pages in the separate
`mathlib-initiative/EtingofRepresentationTheory-verso-pages` repository.
Branch protection on private `main` is intentionally not required. Required CI
is enforced by the updater workflow before it requests a merge, rather than by
a protected-branch rule.
In **Settings → Actions → General → Workflow permissions**, allow read and
write permissions and allow GitHub Actions to create and approve pull requests.
The updater requests only the `actions: write`, `contents: write`, and
`pull-requests: write` permissions it needs.

The public repository sends `repository_dispatch` events containing its exact
tested commit SHA. The `Update formalization dependency` workflow opens a pull
request that changes the Git pin and deterministic formalization panels
exported from that exact public revision. It regenerates the ignored Lake
manifest only to resolve and build the dependency; the manifest is not included
in the pull request, and the workflow never copies the public repository into
this one. Because GitHub suppresses recursive workflow events created by
`GITHUB_TOKEN`, the updater explicitly dispatches `ci.yml` on the new branch
and waits for the exact head commit to pass. It then rechecks both public and
private `main` and requests an immediate head-bound squash merge. The strict
revision checks and head-bound merge are the accepted private-repository update
controls. Every successful push to private `main` publishes the rendered HTML
as a durable private GitHub Release and also retains a short-lived Actions
artifact. The separate public Pages repository currently serves the validated
render from `e59720c1347adbc5cf8c444c49086d6b83d8d5cb`; publishing newer renders
there is a separate operation.
