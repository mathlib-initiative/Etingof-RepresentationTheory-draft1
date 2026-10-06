/-
Copyright (c) 2026 American Mathematical Society. All rights reserved.
-/

import VersoManual
import RepresentationTheory

open Verso.Genre Manual

namespace IntroductionToRepresentationTheoryVerso.Content.Chapter9.Proposition923

#doc (Manual) "Hom dimensions and composition multiplicities" =>

# Hom dimensions and composition multiplicities
%%%
tag := "Chapter9/Proposition9.2.3"
number := false
%%%

*Proposition 9.2.3.* _Let $`N` be any finite dimensional $`A`-module. Then one has $`\dim \operatorname{Hom}_A(P_i, N) = [N : M_i]`, the multiplicity of occurrence on $`M_i` in the Jordan-Hölder series of $`N`._

*Proof.* If $`N = M_j`, the statement is clear. Also, if

$$`0 \to N_1 \to N_2 \to N_3 \to 0`

is an exact sequence of $`A`-modules, then the corresponding sequence

$$`0 \to \operatorname{Hom}_A(P_i, N_1) \to \operatorname{Hom}_A(P_i, N_2) \to \operatorname{Hom}_A(P_i, N_3) \to 0`

is exact, as $`P_i` is projective. This implies the statement. $`\square`

## Formalization
%%%
tag := "Chapter9/Proposition9.2.3/formalization"
number := false
%%%

### Primary declarations

{Manual.docstring RepresentationTheory.Algebra.Module.CompositionSeries.CompositionSeries.moduleNatInvariant_eq_finrank_hom}

### Supporting declarations

{Manual.docstring RepresentationTheory.Algebra.Module.CompositionSeries.CompositionSeries.moduleNatInvariant}

{Manual.docstring RepresentationTheory.Algebra.Module.CompositionSeries.CompositionSeries.moduleNatInvariant_eraseLast}

{Manual.docstring RepresentationTheory.Algebra.Module.CompositionSeries.Module.finrank_hom_eq_finrank_hom_submodule_add_quotient}

{Manual.docstring RepresentationTheory.Algebra.Module.CompositionSeries.Module.finrank_hom_eq_zero_of_bot_eq_top}

{Manual.docstring RepresentationTheory.Algebra.Module.CompositionSeries.Module.finrank_hom_top_eq}
