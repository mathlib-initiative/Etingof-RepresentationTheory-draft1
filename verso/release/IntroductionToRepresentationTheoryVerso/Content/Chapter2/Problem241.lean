/-
Copyright (c) 2026 American Mathematical Society. All rights reserved.
-/

import VersoManual
import RepresentationTheory

open Verso.Genre Manual

namespace IntroductionToRepresentationTheoryVerso.Content.Chapter2.Problem241

#doc (Manual) "Existence of maximal ideals" =>
# Existence of maximal ideals
%%%
tag := "Chapter2/Problem2.4.1"
number := false
%%%
*Problem 2.4.1.* A *maximal* ideal in a ring $`A` is an ideal $`I \neq A` such that any strictly larger ideal coincides with $`A`. (This definition is made for left, right, or two-sided ideals.) Show that any unital ring has a maximal left, right, and two-sided ideal. (Hint: Use Zorn's lemma.)

## Formalization
%%%
tag := "Chapter2/Problem2.4.1/formalization"
number := false
%%%

### Supporting declarations

Declaration: IsCoatom

Alignment metadata: book-ref=Chapter2/Problem2.4.1; role=supporting

Declaration: IsCoatom.lt\_iff

Alignment metadata: book-ref=Chapter2/Problem2.4.1; role=supporting

{Manual.docstring RepresentationTheory.Ring.CoatomExistence.exists_maximal_leftIdeal}

{Manual.docstring RepresentationTheory.Ring.CoatomExistence.exists_maximal_rightIdeal}

{Manual.docstring RepresentationTheory.Ring.CoatomExistence.exists_maximal_twoSidedIdeal}
