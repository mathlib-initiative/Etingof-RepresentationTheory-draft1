/-
Copyright (c) 2026 American Mathematical Society. All rights reserved.
-/

import VersoManual
import RepresentationTheory

open Verso.Genre Manual

namespace IntroductionToRepresentationTheoryVerso.Content.Chapter9.Theorem921

#doc (Manual) "Classifying indecomposable projectives" =>

# Classifying indecomposable projectives
%%%
tag := "Chapter9/Theorem9.2.1"
number := false
%%%

*Theorem 9.2.1.* _(i) For each $`i = 1, \ldots, n` there exists a unique indecomposable finitely generated projective module $`P_i` such that_

$$`
\dim \operatorname{Hom}(P_i, M_j) = \delta_{ij}.
`

_(ii)_ $`A = \bigoplus_{i=1}^n (\dim M_i) P_i`.

_(iii) Any indecomposable finitely generated projective module over $`A` is isomorphic to $`P_i` for some $`i`._

*Proof.* Recall that $`A / \operatorname{Rad}(A) = \bigoplus_{i=1}^n \operatorname{End}(M_i)` and that $`\operatorname{Rad}(A)` is a nilpotent ideal. Pick a basis of $`M_i`, and let $`e_{ij}^0 = E_{jj}^i`, the rank 1 projectors projecting to the basis vectors of this basis ($`j = 1, \ldots, \dim M_i`). Then $`e_{ij}^0` are orthogonal idempotents in $`A / \operatorname{Rad}(A)`. So by Corollary 9.1.3 we can lift them to orthogonal idempotents $`e_{ij}` in $`A`. Now define $`P_{ij} = Ae_{ij}`. Then $`A = \bigoplus_i \bigoplus_{j=1}^{\dim M_i} P_{ij}`, so $`P_{ij}` are projective. Also, we have $`\operatorname{Hom}(P_{ij}, M_k) = e_{ij} M_k`, so $`\dim \operatorname{Hom}(P_{ij}, M_k) = \delta_{ik}`. Finally, $`P_{ij}` is independent of $`j` up to an isomorphism, as $`e_{ij}` for fixed $`i` are conjugate under $`A^\times` by Proposition 9.1.1; thus we will denote $`P_{ij}` by $`P_i`.

We claim that $`P_i` is indecomposable. Indeed, if $`P_i = Q_1 \oplus Q_2`, then $`\operatorname{Hom}(Q_l, M_j) = 0` for all $`j` either for $`l = 1` or for $`l = 2`, so either $`Q_1 = 0` or $`Q_2 = 0`.

Also, there can be no other indecomposable finitely generated projective modules, since any indecomposable projective module has to occur in the decomposition of $`A`. The theorem is proved. $`\square`

## Formalization
%%%
tag := "Chapter9/Theorem9.2.1/formalization"
number := false
%%%

### Primary declarations

{Manual.docstring RepresentationTheory.RingTheory.Artinian.ModuleIdempotents.Auxiliary.statement016753}

{Manual.docstring RepresentationTheory.RingTheory.Artinian.ModuleIdempotents.exists_linearEquiv_projective_family}

{Manual.docstring RepresentationTheory.RingTheory.Artinian.ModuleIdempotents.regularModule_linearEquiv_directSum}

### Supporting declarations

{Manual.docstring RepresentationTheory.LinearAlgebra.ModuleDecompositions.AuxiliaryDecompositionPredicate.endomorphism_ring_isLocal}

{Manual.docstring RepresentationTheory.RingTheory.Artinian.ModuleIdempotents.Auxiliary.statement016667}

{Manual.docstring RepresentationTheory.RingTheory.Artinian.ModuleIdempotents.completeOrthogonalIdempotents_matrix_single}

{Manual.docstring RepresentationTheory.RingTheory.Artinian.ModuleIdempotents.completeOrthogonalIdempotents_pi_matrix_single}

{Manual.docstring RepresentationTheory.RingTheory.Artinian.ModuleIdempotents.completeOrthogonalIdempotents_pi_single_one}

{Manual.docstring RepresentationTheory.RingTheory.Artinian.ModuleIdempotents.exists_index_and_nonzero_map}

{Manual.docstring RepresentationTheory.RingTheory.Artinian.ModuleIdempotents.exists_isCoatom_submodule}

{Manual.docstring RepresentationTheory.RingTheory.Artinian.ModuleIdempotents.exists_orthogonal_idempotents_with_finrank}

{Manual.docstring RepresentationTheory.RingTheory.Artinian.ModuleIdempotents.finite_span_singleton}

{Manual.docstring RepresentationTheory.RingTheory.Artinian.ModuleIdempotents.finrank_linearMap_span_eq_associated_submodule}

{Manual.docstring RepresentationTheory.RingTheory.Artinian.ModuleIdempotents.isIdempotentElem_matrix_single}

{Manual.docstring RepresentationTheory.RingTheory.Artinian.ModuleIdempotents.isInternal_span_singleton_of_completeOrthogonalIdempotents}

{Manual.docstring RepresentationTheory.RingTheory.Artinian.ModuleIdempotents.isNilpotent_of_range_le_proper}

{Manual.docstring RepresentationTheory.RingTheory.Artinian.ModuleIdempotents.matrix_single_mul_mul_matrix_single}

{Manual.docstring RepresentationTheory.RingTheory.Artinian.ModuleIdempotents.module_scalar_linearMap}

{Manual.docstring RepresentationTheory.RingTheory.Artinian.ModuleIdempotents.module_scalar_submodule}

{Manual.docstring RepresentationTheory.RingTheory.Artinian.ModuleIdempotents.nonempty_linearEquiv_of_nonzero_maps_to_simple}

{Manual.docstring RepresentationTheory.RingTheory.Artinian.ModuleIdempotents.nonempty_linearEquiv_of_simple_artinian}

{Manual.docstring RepresentationTheory.RingTheory.Artinian.ModuleIdempotents.orthogonalIdempotents_pi_single}

{Manual.docstring RepresentationTheory.RingTheory.Artinian.ModuleIdempotents.pi_single_one_mul_comm}

{Manual.docstring RepresentationTheory.RingTheory.Artinian.ModuleIdempotents.projective_span_singleton}

{Manual.docstring RepresentationTheory.RingTheory.Artinian.ModuleIdempotents.span_singleton_linearEquiv_of_conjugate}

{Manual.docstring RepresentationTheory.RingTheory.Artinian.ModuleIdempotents.span_singleton_satisfies_module_property}
