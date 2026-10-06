/-
Copyright (c) 2026 American Mathematical Society. All rights reserved.
-/

import VersoManual
import RepresentationTheory

open Verso.Genre Manual

namespace IntroductionToRepresentationTheoryVerso.Content.Chapter5.Lemma5134

#doc (Manual) "Maps from an idempotent-generated ideal" =>

# Maps from an idempotent-generated ideal
%%%
tag := "Chapter5/Lemma5.13.4"
number := false
%%%

*Lemma 5.13.4.* _Let $`A` be an algebra and let $`e` be an idempotent in $`A`. Then for any left $`A`-module $`M`, one has $`\operatorname{Hom}_A(Ae, M) \cong eM` (namely, $`x \in eM` corresponds to $`f_x : Ae \to M` given by $`f_x(a) = ax`, $`a \in Ae`)._

## Formalization
%%%
tag := "Chapter5/Lemma5.13.4/formalization"
number := false
%%%

### Supporting declarations

{Manual.docstring RepresentationTheory.ModuleTheory.Idempotent.linearMapSpanSingletonEquivFixedByIdempotent}
