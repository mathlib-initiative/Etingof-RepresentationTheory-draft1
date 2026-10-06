/-
Copyright (c) 2026 American Mathematical Society. All rights reserved.
-/

import VersoManual
import RepresentationTheory

open Verso.Genre Manual

namespace IntroductionToRepresentationTheoryVerso.Content.Chapter5.Remark583

#doc (Manual) "Coset values and the dimension of induction" =>

# Coset values and the dimension of induction
%%%
tag := "Chapter5/Remark5.8.3"
number := false
%%%

*Remark 5.8.3.* Notice that if we choose a representative $`x_\sigma` from every right $`H`-coset $`\sigma` of $`G`, then any $`f \in \operatorname{Ind}_H^G V` is uniquely determined by $`\{f(x_\sigma)\}`.

Because of this,

$$`\dim(\operatorname{Ind}_H^G V) = \dim V \cdot (G : H),`

where $`(G : H)` is the index of $`H` in $`G`.

## Formalization
%%%
tag := "Chapter5/Remark5.8.3/formalization"
number := false
%%%

### Primary declarations

{Manual.docstring RepresentationTheory.InductionCoinduction.FiniteIndexEquivalences.finrank_indV}

### Supporting declarations

{Manual.docstring RepresentationTheory.InductionCoinduction.FiniteIndexEquivalences.coindVEquivRightCosetFunctions}

{Manual.docstring RepresentationTheory.InductionCoinduction.FiniteIndexEquivalences.finrank_coindV}
