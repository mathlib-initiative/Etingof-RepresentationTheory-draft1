# Introduction to Representation Theory — aligned Verso edition

## Read the book

**[Read the rendered Verso book](https://mathlib-initiative.github.io/EtingofRepresentationTheory-verso-pages/).**

The rendered edition is publicly hosted on GitHub Pages at the repository
owner's direction. This source repository remains private.

[Download a copy](https://github.com/mathlib-initiative/EtingofRepresentationTheory-verso/releases/latest)
for offline reading.

The edition presents the complete text of *Introduction to Representation
Theory* by Pavel Etingof, Oleg Golberg, Sebastian Hensel, Tiankai Liu, Alex
Schwendner, Dmitry Vaintrob, and Elena Yudovina (AMS, 2011;
[catalogue entry](https://bookstore.ams.org/stml-59/)). Formalization panels
appear beside the corresponding text and come from the exact revision of the
[public Lean library](https://github.com/mathlib-initiative/EtingofRepresentationTheory)
pinned in `lakefile.toml`.

## Browse the source

- [`IntroductionToRepresentationTheoryVerso/Content/`](IntroductionToRepresentationTheoryVerso/Content/)
  contains the item-by-item Verso edition.
- [`source-markdown/`](source-markdown/) contains the page-level transcription.
- [`metadata/`](metadata/) defines the book's semantic navigation.

`AlignmentExport.lean` reads `source_ref` attributes from the pinned public
library, and `scripts/sync_formalization_panels.py` regenerates the panels.
Private CI rejects stale panels and builds the book. The public reading site is
hosted separately in
[`EtingofRepresentationTheory-verso-pages`](https://github.com/mathlib-initiative/EtingofRepresentationTheory-verso-pages).

## Build locally

```text
lake update
lake env lean --run AlignmentExport.lean > formalization-alignment.json
python3 scripts/sync_formalization_panels.py --check formalization-alignment.json
lake build
python3 scripts/build_site.py
```

The build checks the reading presentation and requires its alignment ledger to
match Lean's export. It checks preservation of paragraphs, displayed formulas,
tables, and complete footnotes during reader preparation.

The editorial pass is tracked separately in `metadata/reader-reviews.json`.
Passing a build does not mean every chapter has been reviewed. To check that
the full-book pass is complete:

```text
python3 scripts/reader_review.py --require-complete
python3 scripts/validate_reader.py _out/html-multi --require-complete
```

`reader-report.json` reports both the presentation checks and outstanding
editorial coverage. Renamed page titles retain redirects and anchors for the
previously published reading URLs.

## Development

This repository is generated output. Make changes and open PRs in the
[background source repository](https://github.com/mathlib-initiative/Etingof-RepresentationTheory-draft1),
then publish through its materialization process. Do not edit the dependency pin
or open PRs here.

## Copyright and access

Copyright © 2026 American Mathematical Society. All rights reserved.

mathlib-initiative hosts this private repository on behalf of the American
Mathematical Society and assisted with the technical preparation of the Verso
alignment. mathlib-initiative disclaims any copyright, ownership, or other
intellectual-property claim in the book, its text, and this aligned edition.
See [LICENSE](LICENSE) for the repository's access and use terms.

Do not publish, copy, distribute, or grant access to the repository or rendered
book without express authorization from the American Mathematical Society.
