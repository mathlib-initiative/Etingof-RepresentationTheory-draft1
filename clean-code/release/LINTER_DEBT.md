# Linter debt

This release deliberately keeps `lake build --iofail` as its build command. Compiler,
elaborator, runtime, deprecation, missing-documentation, and other non-linter messages therefore
remain fatal.

The clean-room migration is not yet Mathlib-lint-clean. The generated corpus has a large formatting
and API-linter backlog, and it already contained local linter suppressions before the strict-build
audit. The package-level suppressions in `lakefile.toml` are temporary migration debt, not a claim
that the underlying warnings have been resolved.

[`linter-debt.json`](linter-debt.json) is the reviewed inventory. `validate_linter_debt.py` fails if
the package-level suppression set or the local `set_option linter.… false` inventory changes without
an explicit ledger update. The retirement work is tracked in
[issue #1](https://github.com/mathlib-initiative/EtingofRepresentationTheory/issues/1).

Five narrowly scoped `linter.checkUnivs` exceptions preserve intentionally independent component
universes in representation structures. Mathlib's universe linter reports these as a heuristic
warning; collapsing the universes was tested and rejected because it breaks existing polymorphic
callers. Each exception is attached to one declaration and carries an inline justification.

The target state is an empty ledger and a clean `lake build --iofail` with the Mathlib standard
linter set enabled. API-oriented linters should be restored first, followed by generated source
normalization and the remaining style linters.
