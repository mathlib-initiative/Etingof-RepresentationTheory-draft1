/-
Copyright (c) 2026 American Mathematical Society. All rights reserved.
-/

import VersoManual
import RepresentationTheory

open Verso.Genre Manual

namespace IntroductionToRepresentationTheoryVerso.Content.Chapter5.Introduction59

#doc (Manual) "Characters of induced representations" =>

# Characters of induced representations
%%%
tag := "Chapter5/Introduction_5.9"
number := false
%%%

## 5.9. The Frobenius formula for the character of an induced representation
%%%
tag := "Chapter5/Introduction_5.9/heading-1"
%%%

Let us now compute the character $`\chi` of $`\operatorname{Ind}_H^G V` when $`(G : H) < \infty`. In each right coset $`\sigma \in H \backslash G`, choose a representative $`x_\sigma`.

## Formalization
%%%
tag := "Chapter5/Introduction_5.9/formalization"
number := false
%%%

### Supporting declarations

{Manual.docstring RepresentationTheory.AuxiliaryQuotientSummation.auxiliary_theorem}
