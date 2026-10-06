/-
Copyright (c) 2026 American Mathematical Society. All rights reserved.
-/

import VersoManual
import RepresentationTheory

open Verso.Genre Manual

namespace IntroductionToRepresentationTheoryVerso.Content.Chapter9.Corollary973

#doc (Manual) "The unique basic representative" =>

# The unique basic representative
%%%
tag := "Chapter9/Corollary9.7.3"
number := false
%%%

*Corollary 9.7.3.* _(i) Any finite abelian category $`\mathcal{C}` is equivalent to the category of finite dimensional modules over a unique basic algebra $`B = B(\mathcal{C})`._

_(ii) Any finite dimensional algebra $`A` is Morita equivalent to a unique basic algebra $`B = B_A`, such that $`\dim B_A \leq \dim A`._

## Formalization
%%%
tag := "Chapter9/Corollary9.7.3/formalization"
number := false
%%%

### Primary declarations

{Manual.docstring RepresentationTheory.Auxiliary.FiniteAlgebraCandidates.Auxiliary.exists_type_with_three_conditions}

{Manual.docstring RepresentationTheory.Auxiliary.FiniteAlgebraCandidates.Auxiliary.exists_type_with_three_conditions_finrank_le_and_unique}

{Manual.docstring RepresentationTheory.Auxiliary.FiniteAlgebraCandidates.Auxiliary.exists_type_with_two_conditions}

{Manual.docstring RepresentationTheory.Auxiliary.FiniteAlgebraCandidates.Auxiliary.finrank_le_of_two_conditions}

### Supporting declarations

{Manual.docstring RepresentationTheory.Auxiliary.FiniteAlgebraCandidates.Auxiliary.algEquiv_of_two_shared_conditions}

{Manual.docstring RepresentationTheory.Auxiliary.FiniteAlgebraCandidates.Auxiliary.algEquiv_of_two_shared_conditions'}

{Manual.docstring RepresentationTheory.Auxiliary.FiniteAlgebraCandidates.Auxiliary.finrank_le_of_two_conditions'}

{Manual.docstring RepresentationTheory.Auxiliary.FiniteAlgebraCandidates.Auxiliary.relation_self}

{Manual.docstring RepresentationTheory.RingAuxiliary.RingAuxiliary.refl}

{Manual.docstring RepresentationTheory.RingAuxiliary.RingAuxiliary.symm}

{Manual.docstring RepresentationTheory.RingAuxiliary.RingAuxiliary.trans}
