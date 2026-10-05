#!/usr/bin/env python3
"""Mechanical source synchronization for reviewed editorial naming decisions.

The decisions are explicit; this does not infer mathematics from identifiers.
All edits start in staging sources and reviewed declaration records, never in
published repositories. Re-running it is harmless.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

from assemble_verso_release import escape_inline


ROOT = Path(__file__).resolve().parent
PREFIX = "RepresentationTheory.Algebra.ModuleActions"
OLD = PREFIX + ".RingAddCommGroupAuxiliary"
TITLE_DECISIONS = {
    "Chapter3/Introduction_to_3.2": "Density theorem: the setting",
    "Chapter3/Introduction_to_3.7": "Composition series and their uniqueness",
    "Chapter3/Introduction_to_3.8": "Decomposing representations into indecomposables",
}
EXACT_RENAMES = {
    "RepresentationTheory.Algebra.Module.Pi.SimpleModules.indexedAuxiliaryEndomorphism":
        "RepresentationTheory.Algebra.Module.Pi.SimpleModules.componentProjection",
    "RepresentationTheory.Algebra.Module.Pi.SimpleModules.isSimpleModule_pi_iff_exists_simple_auxiliaryRange":
        "RepresentationTheory.Algebra.Module.Pi.SimpleModules.isSimpleModule_pi_iff_exists_simple_component",
    "RepresentationTheory.Algebra.Module.FiniteFamilySemisimplicity.Auxiliary":
        "RepresentationTheory.Algebra.Module.FiniteFamilySemisimplicity.MatrixProductAlgebra",
    "RepresentationTheory.Algebra.Module.FiniteFamilySemisimplicity.auxiliaryAlgebra_simpleModule_classification":
        "RepresentationTheory.Algebra.Module.FiniteFamilySemisimplicity.matrixProductAlgebra_simpleModule_classification",
    "RepresentationTheory.Algebra.Module.FiniteFamilySemisimplicity.columnModule_aux1_equiv_imp_eq":
        "RepresentationTheory.Algebra.Module.FiniteFamilySemisimplicity.columnModule_equiv_imp_eq",
    "RepresentationTheory.Algebra.Module.FiniteFamilySemisimplicity.auxiliaryLinearEquivDirectSumColumns":
        "RepresentationTheory.Algebra.Module.FiniteFamilySemisimplicity.regularModuleEquivColumns",
    "RepresentationTheory.Algebra.Module.FiniteFamilySemisimplicity.piAuxiliaryLinearEquivDirectSum":
        "RepresentationTheory.Algebra.Module.FiniteFamilySemisimplicity.freeModuleEquivColumns",
    "RepresentationTheory.Algebra.Module.FiniteFamilySemisimplicity.auxiliaryLinearEquivDual":
        "RepresentationTheory.Algebra.Module.FiniteFamilySemisimplicity.regularModuleEquivDual",
    "RepresentationTheory.Module.DualOppositeAction.AuxiliaryModuleType":
        "RepresentationTheory.Module.DualOppositeAction.LinearDual",
    "RepresentationTheory.Module.RelSeriesAuxiliary.ModuleRelSeriesAuxiliary":
        "RepresentationTheory.Module.Filtration.FiniteFiltration",
    "RepresentationTheory.Module.RelSeriesAuxiliary.ModuleRelSeriesAuxiliary.toRelSeries":
        "RepresentationTheory.Module.Filtration.FiniteFiltration.toRelSeries",
    "RepresentationTheory.Module.RelSeriesAuxiliary.ModuleRelSeriesAuxiliary.toRelSeries_head":
        "RepresentationTheory.Module.Filtration.FiniteFiltration.toRelSeries_head",
    "RepresentationTheory.Module.RelSeriesAuxiliary.ModuleRelSeriesAuxiliary.toRelSeries_last":
        "RepresentationTheory.Module.Filtration.FiniteFiltration.toRelSeries_last",
    "RepresentationTheory.Algebra.Module.Filtrations.exists_auxiliaryData_simple_quotients":
        "RepresentationTheory.Algebra.Module.Filtrations.exists_finiteFiltration_simple_quotients",
    "RepresentationTheory.ModuleTheory.AuxiliaryCondition.AuxiliaryModuleCondition":
        "RepresentationTheory.ModuleTheory.Semisimplicity.IsSemisimple",
    "RepresentationTheory.LieAlgebra.FiniteDimensionalModules.AuxiliaryLieModuleCondition":
        "RepresentationTheory.LieAlgebra.FiniteDimensionalModules.IsIndecomposable",
    "RepresentationTheory.LieAlgebra.FiniteDimensionalModules.isIrreducible_of_auxiliaryLieModuleCondition":
        "RepresentationTheory.LieAlgebra.FiniteDimensionalModules.isIrreducible_of_isIndecomposable",
    "RepresentationTheory.Algebra.ParameterizedComplexRelations.ParameterizedAlgebra":
        "RepresentationTheory.Algebra.ParameterizedComplexRelations.QuantumEnvelopingAlgebra",
    "RepresentationTheory.LieAlgebra.ModularRepresentations.AuxiliaryType_aux1":
        "RepresentationTheory.LieAlgebra.ModularRepresentations.CharacterModule",
    "RepresentationTheory.LieAlgebra.ModularRepresentations.AuxiliaryType":
        "RepresentationTheory.LieAlgebra.ModularRepresentations.CyclicModule",
    "RepresentationTheory.LieAlgebra.ModularRepresentations.distinguishedElement_aux1":
        "RepresentationTheory.LieAlgebra.ModularRepresentations.generatorY",
    "RepresentationTheory.LieAlgebra.ModularRepresentations.distinguishedElement":
        "RepresentationTheory.LieAlgebra.ModularRepresentations.generatorX",
    "RepresentationTheory.LieAlgebra.ModularRepresentations.finrank_eq_aux1":
        "RepresentationTheory.LieAlgebra.ModularRepresentations.finrank_cyclicModule",
    "RepresentationTheory.Module.Auxiliary.auxiliary_unique":
        "RepresentationTheory.Algebra.Identity.unique",
    "RepresentationTheory.LinearAlgebra.TensorOperations.AuxiliaryType_aux2":
        "RepresentationTheory.LinearAlgebra.TensorOperations.TensorPower",
    "RepresentationTheory.LinearAlgebra.TensorOperations.AuxiliaryType_aux1":
        "RepresentationTheory.LinearAlgebra.TensorOperations.SymmetricPower",
    "RepresentationTheory.LinearAlgebra.TensorOperations.AuxiliaryType":
        "RepresentationTheory.LinearAlgebra.TensorOperations.ExteriorPower",
    "RepresentationTheory.LinearAlgebra.SymmetricTensors.distinguishedElement_aux1":
        "RepresentationTheory.LinearAlgebra.SymmetricTensors.basis",
    "RepresentationTheory.LinearAlgebra.AlternatingTensors.linearEquiv_aux2":
        "RepresentationTheory.LinearAlgebra.AlternatingTensors.symmetricQuotientEquiv",
    "RepresentationTheory.LinearAlgebra.AlternatingTensors.linearEquiv_aux3":
        "RepresentationTheory.LinearAlgebra.AlternatingTensors.symmetricQuotientEquivOfCharZero",
    "RepresentationTheory.LinearAlgebra.AlternatingTensors.linearEquiv_aux1":
        "RepresentationTheory.LinearAlgebra.AlternatingTensors.exteriorQuotientEquivOfCharZero",
    "RepresentationTheory.LinearAlgebra.AlternatingTensors.linearEquiv":
        "RepresentationTheory.LinearAlgebra.AlternatingTensors.exteriorQuotientEquiv",
    "RepresentationTheory.Auxiliary.UnavailableFormalExpression.auxiliaryFact":
        "RepresentationTheory.Geometry.TetrahedronAngle.irrational_arccos_one_third_div_pi",
    "RepresentationTheory.LieAlgebra.SpecialLinearPresentation.auxiliary_fact_aux7":
        "RepresentationTheory.LieAlgebra.SpecialLinearPresentation.bracket_basis2_basis1",
    "RepresentationTheory.LieAlgebra.SpecialLinearPresentation.auxiliary_fact_aux5":
        "RepresentationTheory.LieAlgebra.SpecialLinearPresentation.enveloping_commutator_relations",
    "RepresentationTheory.LieAlgebra.SpecialLinearPresentation.auxiliary_fact_aux6":
        "RepresentationTheory.LieAlgebra.SpecialLinearPresentation.matrix_basis2",
    "RepresentationTheory.LieAlgebra.ThreeGeneratorPresentations.property_and":
        "RepresentationTheory.LieAlgebra.ThreeGeneratorPresentations.enveloping_commutator_relations",
    "RepresentationTheory.LieAlgebra.ThreeGeneratorPresentations.algEquiv_aux1":
        "RepresentationTheory.LieAlgebra.ThreeGeneratorPresentations.weylQuotientEquiv",
    "RepresentationTheory.CategoryTheory.QuiverLinearDiagrams.AuxiliaryQuiverModuleData.predicateAux'''":
        "RepresentationTheory.CategoryTheory.QuiverLinearDiagrams.AuxiliaryQuiverModuleData.IsZero",
    "RepresentationTheory.CategoryTheory.QuiverLinearDiagrams.AuxiliaryQuiverModuleData.predicateAux''":
        "RepresentationTheory.CategoryTheory.QuiverLinearDiagrams.AuxiliaryQuiverModuleData.IsNonzero",
    "RepresentationTheory.CategoryTheory.QuiverLinearDiagrams.AuxiliaryQuiverModuleData.predicateAux'":
        "RepresentationTheory.CategoryTheory.QuiverLinearDiagrams.AuxiliaryQuiverModuleData.IsIrreducible",
    "RepresentationTheory.CategoryTheory.QuiverLinearDiagrams.AuxiliaryQuiverModuleData.predicateAux":
        "RepresentationTheory.CategoryTheory.QuiverLinearDiagrams.AuxiliaryQuiverModuleData.IsIndecomposable",
    "RepresentationTheory.Ring.CoatomExistence.exists_coatom_subobject":
        "RepresentationTheory.Ring.CoatomExistence.exists_maximal_leftIdeal",
    "RepresentationTheory.Ring.CoatomExistence.exists_coatom_subobject_aux1":
        "RepresentationTheory.Ring.CoatomExistence.exists_maximal_rightIdeal",
    "RepresentationTheory.Ring.CoatomExistence.exists_coatom_subobject_aux2":
        "RepresentationTheory.Ring.CoatomExistence.exists_maximal_twoSidedIdeal",
    "RepresentationTheory.LinearAlgebra.ModulePredicates.AuxiliaryModulePredicate":
        "RepresentationTheory.LinearAlgebra.ModulePredicates.IsFaithfulRepresentation",
    "RepresentationTheory.MvPolynomial.QuotientProperty.quotient_property_of_low_degree_homogeneous_mem":
        "RepresentationTheory.MvPolynomial.QuotientProperty.quotient_indecomposable_of_high_degree_homogeneous_mem",
    "RepresentationTheory.Algebra.DualModules.auxiliaryModuleProperty_squareZeroPlaneDual":
        "RepresentationTheory.Algebra.DualModules.isIndecomposable_squareZeroPlaneDual",
    "RepresentationTheory.Algebra.DualModules.auxiliaryModuleProperty_and_not_isCyclicModule":
        "RepresentationTheory.Algebra.DualModules.isIndecomposable_and_not_isCyclicModule_squareZeroPlaneDual",
}

# Exact, statement-reviewed descriptions. Keep the declaration registry and
# reviewed naming responses synchronized with the authoritative Lean docstrings.
DOCSTRINGS = {
    "RepresentationTheory.Algebra.Module.Pi.SimpleModules.componentProjection":
        "The projection onto the i-th component of a product-ring module, given by the action of the central idempotent supported at i.",
    "RepresentationTheory.Algebra.Module.Pi.SimpleModules.isSimpleModule_pi_iff_exists_simple_component":
        "A module over a finite product of rings is simple exactly when one component is simple over its factor and every other component is zero.",
    "RepresentationTheory.Algebra.Module.FiniteFamilySemisimplicity.MatrixProductAlgebra":
        "The finite product of full matrix algebras with block sizes d_i over k, with componentwise algebra operations.",
    "RepresentationTheory.Algebra.Module.FiniteFamilySemisimplicity.matrixProductAlgebra_simpleModule_classification":
        "The column modules classify finite-dimensional simple modules of a finite product of full matrix algebras, and every module over the product is semisimple.",
    "RepresentationTheory.Algebra.Module.FiniteFamilySemisimplicity.columnModule_equiv_imp_eq":
        "Column modules supported on different nonzero matrix blocks are not isomorphic as modules over the product algebra.",
    "RepresentationTheory.Algebra.Module.FiniteFamilySemisimplicity.regularModuleEquivColumns":
        "Reading each matrix by columns identifies the regular module of a finite matrix product with d_i copies of the column module in block i.",
    "RepresentationTheory.Algebra.Module.FiniteFamilySemisimplicity.freeModuleEquivColumns":
        "A free module of rank n over a finite matrix product is the direct sum of n*d_i copies of the column module in each block i.",
    "RepresentationTheory.Algebra.Module.FiniteFamilySemisimplicity.regularModuleEquivDual":
        "The matrix-entry pairing identifies the regular module with its linear dual, with the dual action twisted by blockwise transpose.",
    "RepresentationTheory.Algebra.Module.FiniteFamilySemisimplicity.exists_linearEquiv_directSum_columnModules":
        "Every finite-dimensional module over a finite product of full matrix algebras is a finite direct sum of their column modules, over any field.",
    "RepresentationTheory.Algebra.Module.FiniteFamilySemisimplicity.column_isSimpleModule":
        "The column-vector module supported on any nonzero block of a finite matrix product is simple.",
    "RepresentationTheory.Algebra.Module.FiniteFamilySemisimplicity.simpleModule_linearEquiv_columnModule":
        "Every finite-dimensional simple module over a finite matrix product is isomorphic to a column module supported on one block.",
    "RepresentationTheory.Module.DualOppositeAction.LinearDual":
        "The k-linear dual of V; the acting algebra parameter is retained for the opposite-algebra module construction.",
    "RepresentationTheory.Module.Filtration.FiniteFiltration":
        "A finite strictly increasing chain of A-submodules of V, starting at zero and ending at V.",
    "RepresentationTheory.Module.Filtration.FiniteFiltration.toRelSeries":
        "The finite chain of submodules, with every consecutive inclusion strict.",
    "RepresentationTheory.Module.Filtration.FiniteFiltration.toRelSeries_head":
        "The first submodule of the filtration is zero.",
    "RepresentationTheory.Module.Filtration.FiniteFiltration.toRelSeries_last":
        "The last submodule of the filtration is the whole module.",
    "RepresentationTheory.Algebra.Module.Filtrations.exists_finiteFiltration_simple_quotients":
        "A finite-dimensional module over any field admits a finite filtration from zero to the whole module with simple successive quotients.",
    "RepresentationTheory.Algebra.Module.SimpleScalarSurjectivity.family_algebra_smul_surjective":
        "One algebra element realizes any prescribed k-linear endomorphisms on a finite pairwise nonisomorphic family of finite-dimensional simple modules over an algebraically closed field.",
    "RepresentationTheory.ModuleTheory.Semisimplicity.IsSemisimple":
        "Semisimplicity: every submodule has a complement, equivalently the module is a direct sum of simple modules.",
    "RepresentationTheory.Module.EndomorphismEvaluation.endApplyBasisLinearEquiv":
        "Evaluation on a finite k-basis identifies End_k(V), with A acting by postcomposition, with one copy of V for each basis vector.",
    "RepresentationTheory.Module.EndomorphismEvaluation.endApplyFinBasisLinearEquiv":
        "Evaluation on a chosen finite k-basis identifies End_k(V) with finrank_k(V) copies of V as an A-module.",
    "RepresentationTheory.Algebra.Module.ComplementConstructions.exists_map_agreeing_on_iSup":
        "A surjection from a module spanned by simple submodules restricts to an A-linear equivalence on the sum of a selected subset of those submodules.",
    "RepresentationTheory.Algebra.Module.ComplementConstructions.exists_map_agreeing_on_iSup_of_internal":
        "A surjection from an internal direct sum of simple submodules restricts to an A-linear equivalence on a direct sum of selected original summands.",
    "RepresentationTheory.Algebra.Module.IsotypicDecomposition.exists_equiv_directSum_fin":
        "A submodule of finitely many copies of pairwise nonisomorphic simple modules has the same simple types, with each multiplicity bounded by the original one.",
    "RepresentationTheory.Algebra.Module.IsotypicDecomposition.exists_linearIndependent_coordinates_directSum":
        "The inclusion of a submodule of a finite direct sum of simple modules is blockwise a matrix of endomorphisms with right-linearly independent rows.",
    "RepresentationTheory.Algebra.Module.SimpleMatrixCoordinates.exists_injective_coordinates_directSum":
        "A submodule of a finite direct sum of simple modules admits bounded multiplicities and injective block maps represented by endomorphism-valued matrices.",
    "RepresentationTheory.Module.SemisimpleHomDecomposition.homEquivMultiplicityMaps":
        "For finite-dimensional semisimple modules, postcomposition gives a k-linear equivalence between A-linear maps and families of maps between their multiplicity spaces.",
    "RepresentationTheory.LieAlgebra.FiniteDimensionalModules.IsIndecomposable":
        "A nonzero Lie module is indecomposable if every complementary pair of invariant submodules has a zero member.",
    "RepresentationTheory.LieAlgebra.FiniteDimensionalModules.isIrreducible_of_isIndecomposable":
        "Every indecomposable finite-dimensional complex sl(2) module is irreducible.",
    "RepresentationTheory.LieAlgebra.FiniteDimensionalModules.exists_polynomial_model":
        "The d-dimensional complex sl(2) module is equivalent to homogeneous binary polynomials of degree d-1, with h, e and f acting by x∂x-y∂y, x∂y and y∂x.",
    "RepresentationTheory.Algebra.ParameterizedComplexRelations.QuantumEnvelopingAlgebra":
        "The complex quantum enveloping algebra on e, f, K and L, with K and L mutual inverses and the quantum sl(2) relations in cleared-denominator form.",
    "RepresentationTheory.LieAlgebra.ModularRepresentations.CharacterModule":
        "The one-dimensional character module on k, with X acting by mu and Y acting by zero.",
    "RepresentationTheory.LieAlgebra.ModularRepresentations.CyclicModule":
        "The module on functions ZMod p -> k, with X acting diagonally by a+i and Y by gamma times the cyclic shift.",
    "RepresentationTheory.LieAlgebra.ModularRepresentations.generatorX":
        "The matrix unit E00 in the two-dimensional Lie algebra with relation [X,Y]=Y.",
    "RepresentationTheory.LieAlgebra.ModularRepresentations.generatorY":
        "The matrix unit E01 in the two-dimensional Lie algebra with relation [X,Y]=Y.",
    "RepresentationTheory.LieAlgebra.ModularRepresentations.finrank_cyclicModule":
        "The cyclic family indexed by ZMod p has dimension p over k.",
    "RepresentationTheory.Algebra.Identity.unique":
        "Two two-sided identities for an associative bilinear multiplication are equal; no chosen unit is assumed.",
    "RepresentationTheory.LinearAlgebra.TensorOperations.TensorPower":
        "The n-fold tensor power of V over k, indexed by Fin n.",
    "RepresentationTheory.LinearAlgebra.TensorOperations.SymmetricPower":
        "The quotient of the n-fold tensor power by differences T-s(T) for transpositions s.",
    "RepresentationTheory.LinearAlgebra.TensorOperations.ExteriorPower":
        "The quotient of the n-fold tensor power by tensors fixed by a transposition; over a field it is equivalent to the usual exterior power.",
    "RepresentationTheory.LinearAlgebra.SymmetricTensors.basis":
        "A basis of the symmetric power indexed by multisets of n indices from a chosen basis of V.",
    "RepresentationTheory.LinearAlgebra.AlternatingTensors.symmetricQuotientEquiv":
        "When n! is nonzero in the field, averaging over permutations identifies the symmetric quotient with the invariant tensor subspace.",
    "RepresentationTheory.LinearAlgebra.AlternatingTensors.symmetricQuotientEquivOfCharZero":
        "In characteristic zero, permutation averaging identifies each symmetric power with the invariant tensors.",
    "RepresentationTheory.LinearAlgebra.AlternatingTensors.exteriorQuotientEquiv":
        "When n! is nonzero in the field, signed permutation averaging identifies the exterior quotient with the alternating tensor subspace.",
    "RepresentationTheory.LinearAlgebra.AlternatingTensors.exteriorQuotientEquivOfCharZero":
        "In characteristic zero, signed permutation averaging identifies each exterior power with the alternating tensors.",
    "RepresentationTheory.Geometry.TetrahedronAngle.irrational_arccos_one_third_div_pi":
        "The tetrahedral angle arccos(1/3) is an irrational multiple of pi, proved by an integer recurrence for scaled cosines and a divisibility contradiction.",
    "RepresentationTheory.LieAlgebra.SpecialLinearPresentation.bracket_basis2_basis1":
        "The coordinate generators h and f satisfy [h,f] = -2f.",
    "RepresentationTheory.LieAlgebra.SpecialLinearPresentation.enveloping_commutator_relations":
        "The images of e, f and h in the enveloping algebra satisfy he-eh=2e, hf-fh=-2f and ef-fe=h.",
    "RepresentationTheory.LieAlgebra.SpecialLinearPresentation.matrix_basis2":
        "The coordinate generator h maps to the diagonal matrix with entries 1 and -1.",
    "RepresentationTheory.LieAlgebra.SpecialLinearPresentation.PresentedAlgebra":
        "The free algebra on e, f and h modulo the relations he-eh=2e, hf-fh=-2f and ef-fe=h.",
    "RepresentationTheory.LieAlgebra.SpecialLinearPresentation.algEquiv":
        "The three-generator presentation of sl(2)'s enveloping algebra is equivalent to the basis-independent enveloping algebra of its coordinate Lie algebra.",
    "RepresentationTheory.LieAlgebra.ThreeGeneratorPresentations.enveloping_commutator_relations":
        "The images of the Heisenberg generators in the enveloping algebra satisfy yx-xy=c, yc-cy=0 and xc-cx=0.",
    "RepresentationTheory.LieAlgebra.ThreeGeneratorPresentations.weylQuotientEquiv":
        "The quotient of the Heisenberg enveloping algebra by c-1 is algebra-isomorphic to the Weyl algebra, sending x and y to its first and second operators.",
    "RepresentationTheory.LieAlgebra.ThreeGeneratorPresentations.AuxiliaryType":
        "The Heisenberg Lie algebra on coordinate triples (x,y,c), with bracket [u,v]=(0,0,v_x*u_y-u_x*v_y).",
    "RepresentationTheory.LieAlgebra.ThreeGeneratorPresentations.AuxiliaryType_aux1":
        "The free algebra on x, y and c modulo the Heisenberg commutator relations yx-xy=c, yc-cy=0 and xc-cx=0.",
    "RepresentationTheory.LieAlgebra.ThreeGeneratorPresentations.AuxiliaryType_aux2":
        "The quotient of the Heisenberg enveloping algebra by the two-sided ideal generated by c-1.",
    "RepresentationTheory.LieAlgebra.ThreeGeneratorPresentations.algEquiv":
        "The three-generator Heisenberg presentation is equivalent to its basis-independent enveloping algebra; the generators map to the images of x, y and c.",
    "RepresentationTheory.CategoryTheory.QuiverLinearDiagrams.AuxiliaryQuiverModuleData.IsZero":
        "The quiver representation is zero: every vector at every vertex is zero.",
    "RepresentationTheory.CategoryTheory.QuiverLinearDiagrams.AuxiliaryQuiverModuleData.IsNonzero":
        "At least one vertex space in the quiver representation has a nonzero vector.",
    "RepresentationTheory.CategoryTheory.QuiverLinearDiagrams.AuxiliaryQuiverModuleData.IsIrreducible":
        "The quiver representation is nonzero and every subrepresentation is either zero at all vertices or the whole representation.",
    "RepresentationTheory.CategoryTheory.QuiverLinearDiagrams.AuxiliaryQuiverModuleData.IsIndecomposable":
        "The quiver representation is nonzero and every isomorphism to a binary direct sum has a zero summand.",
    "RepresentationTheory.Ring.CoatomExistence.exists_maximal_leftIdeal":
        "Every nonzero unital ring has a maximal proper left ideal, represented as a coatom of its left regular module's submodule lattice.",
    "RepresentationTheory.Ring.CoatomExistence.exists_maximal_rightIdeal":
        "Every nonzero unital ring has a maximal proper right ideal, represented as a coatom of the opposite ring's regular module's submodule lattice.",
    "RepresentationTheory.Ring.CoatomExistence.exists_maximal_twoSidedIdeal":
        "Every nonzero unital ring has a maximal proper two-sided ideal, constructed by Zorn's lemma.",
    "RepresentationTheory.LinearAlgebra.ModulePredicates.IsFaithfulRepresentation":
        "Faithfulness of the representation: two algebra elements are equal whenever they act identically on every vector. This is Mathlib's FaithfulSMul predicate.",
    "RepresentationTheory.MvPolynomial.QuotientProperty.quotient_indecomposable_of_high_degree_homogeneous_mem":
        "The regular quotient module is indecomposable when a proper ideal contains every homogeneous polynomial of degree at least N.",
    "RepresentationTheory.Algebra.DualModules.isIndecomposable_squareZeroPlaneDual":
        "The dual of the three-dimensional square-zero plane algebra is indecomposable: every nonzero submodule contains its scalar-part functional.",
    "RepresentationTheory.Algebra.DualModules.isIndecomposable_and_not_isCyclicModule_squareZeroPlaneDual":
        "The dual of the three-dimensional square-zero plane algebra is indecomposable but is not generated by any single vector.",
    "RepresentationTheory.RingTheory.Quotient.Constructions.TwoSidedIdeal.AuxiliaryType":
        "The quotient ring A/I, constructed from the ring congruence of the two-sided ideal I.",
    "RepresentationTheory.RingTheory.Quotient.Constructions.TwoSidedIdeal.auxiliaryAlgebra":
        "The algebra structure on the quotient by a two-sided ideal, with scalars inherited from A.",
    "RepresentationTheory.RingTheory.Quotient.Constructions.TwoSidedIdeal.auxiliaryAlgHom":
        "The quotient algebra homomorphism from A to A/I.",
    "RepresentationTheory.RingTheory.Quotient.Constructions.TwoSidedIdeal.auxiliaryAlgHom_eq_iff":
        "Two representatives define the same quotient class exactly when their difference belongs to I.",
    "RepresentationTheory.RingTheory.Quotient.Constructions.TwoSidedIdeal.auxiliaryAlgHom_mul":
        "The product of two quotient classes is the class of the product of their representatives.",
    "RepresentationTheory.RingTheory.Quotient.Constructions.Ring.AuxiliaryType":
        "Left ideals of A, expressed as submodules of the left regular module.",
    "RepresentationTheory.RingTheory.Quotient.Constructions.Ring.quotientModule":
        "The left A-module structure on A/I for a left ideal I; I need not be two-sided.",
    "RepresentationTheory.FreeAlgebra.RelationQuotient.FreeAlgebra.AuxiliaryType":
        "The algebra presented by generators X and relations rel: the free algebra modulo the two-sided ideal generated by those relations.",
    "RepresentationTheory.FreeAlgebra.RelationQuotient.FreeAlgebra.AuxiliaryType.algebra_adjoin_generators_eq_top":
        "The images of the specified generators generate the entire presented algebra.",
    "RepresentationTheory.FreeAlgebra.RelationQuotient.FreeAlgebra.AuxiliaryType.auxiliaryAlgHom_relation":
        "Every specified defining relation has zero image in the presented algebra.",
    "RepresentationTheory.Algebra.AuxiliaryStructure.AuxiliaryStructure.auxiliaryPredicate":
        "The element is a two-sided identity for the associative bilinear multiplication.",
    "RepresentationTheory.Algebra.AuxiliaryStructure.AuxiliaryStructure.auxiliaryPredicate_unique":
        "Two two-sided identities for the same multiplication are equal.",
    "RepresentationTheory.Algebra.AuxiliaryFieldCommRingType.AuxiliaryFieldCommRingType":
        "A unital algebra structure over k on the commutative ring A. Commutativity of A is an assumption.",
    "RepresentationTheory.Algebra.AuxiliaryAlgebraPairType.AuxiliaryAlgebraPairType":
        "Unital algebra homomorphisms from A to B over the commutative base ring k.",
    "RepresentationTheory.LinearAlgebra.ModuleConditions.AuxiliaryModuleCondition":
        "Simplicity of an A-module: it is nonzero and has no submodules other than zero and itself.",
    "RepresentationTheory.LinearAlgebra.ModulePairAuxiliaries.ModulePairAuxiliary'":
        "A-linear maps between the two modules, preserving addition and the A-action.",
    "RepresentationTheory.LinearAlgebra.ModulePairAuxiliaries.ModulePairAuxiliary":
        "A-linear equivalences between the two modules: bundled isomorphisms with inverses.",
    "RepresentationTheory.LinearAlgebra.ModulePairAuxiliaries.AuxiliaryModulePairPredicate":
        "The two A-modules are isomorphic, expressed as existence of an A-linear equivalence.",
    "RepresentationTheory.LinearAlgebra.ModuleDecompositions.AuxiliaryDecompositionPredicate":
        "Indecomposability: the module is nonzero, and every complementary pair of submodules has a zero member.",
    "RepresentationTheory.LinearAlgebra.ModuleDecompositions.AuxiliaryModuleData":
        "A decomposition of V into a product of two nonzero A-modules, with a specified A-linear equivalence.",
    "RepresentationTheory.LinearAlgebra.ModuleDecompositions.AuxiliaryDecompositionPredicate'":
        "The module is nonzero and admits no decomposition into a product of two nonzero A-modules.",
    "RepresentationTheory.LinearAlgebra.ModuleDecompositions.auxiliaryDecompositionPredicate_iff_auxiliaryDecompositionPredicate'":
        "Internal indecomposability via complementary submodules is equivalent to having no external decomposition into two nonzero modules.",
}


def renamed(name: str) -> str:
    if name in EXACT_RENAMES:
        return EXACT_RENAMES[name]
    if name.startswith(OLD + "."):
        return PREFIX + name[len(OLD):]
    if name == OLD:
        return PREFIX + ".LeftModule"
    if name == OLD + "'":
        return PREFIX + ".RightModule"
    return name


def replace_names(value):
    if isinstance(value, str):
        value = value.replace(OLD + ".", PREFIX + ".").replace(OLD + "'", PREFIX + ".RightModule").replace(OLD, PREFIX + ".LeftModule")
        for old, new in EXACT_RENAMES.items():
            value = re.sub(re.escape(old) + r"(?![\w'.])", lambda _: new, value)
        return value
    if isinstance(value, list):
        return [replace_names(child) for child in value]
    if isinstance(value, dict):
        return {renamed(key): replace_names(child) for key, child in value.items()}
    return value


def write_if_changed(path: Path, value: str) -> bool:
    if path.read_text(encoding="utf-8") == value:
        return False
    path.write_text(value, encoding="utf-8")
    return True


def main():
    changed = []
    for folder in (ROOT / "clean-code/release", ROOT / "verso/release"):
        for path in folder.rglob("*.lean"):
            if any(part in {".lake", "_out"} for part in path.relative_to(folder).parts):
                continue
            text = path.read_text(encoding="utf-8")
            text = replace_names(text) if any(name in text for name in EXACT_RENAMES) else text
            module = path.relative_to(folder).with_suffix("").as_posix().replace("/", ".")
            for old, new in EXACT_RENAMES.items():
                if (old.rsplit(".", 1)[0] == module
                        or f"open {old.rsplit('.', 1)[0]}\n" in text):
                    text = re.sub(r"(?<![\w'.])" + re.escape(old.rsplit(".", 1)[1]) + r"(?![\w'.])",
                                  lambda _: new.rsplit(".", 1)[1], text)
                    if old.rsplit(".", 1)[0] != new.rsplit(".", 1)[0]:
                        for command in ("namespace", "end", "open"):
                            text = text.replace(f"{command} {old.rsplit('.', 1)[0]}\n",
                                                f"{command} {new.rsplit('.', 1)[0]}\n")
            for command in ("namespace", "end", "open"):
                text = text.replace(f"{command} RepresentationTheory.Auxiliary.UnavailableFormalExpression\n",
                                    f"{command} RepresentationTheory.Geometry.TetrahedronAngle\n")
                text = text.replace(f"{command} {OLD}\n", f"{command} {PREFIX}\n")
                text = text.replace(f"{command} {PREFIX}.LeftModule\n", f"{command} {PREFIX}\n")
            if "RingAddCommGroupAuxiliary" not in text:
                if write_if_changed(path, text):
                    changed.append(str(path.relative_to(ROOT)))
                continue
            text = replace_names(text)
            text = text.replace("RingAddCommGroupAuxiliary.", "")
            if path.name == "ModuleActions.lean":
                text = text.replace("namespace RingAddCommGroupAuxiliary\n", "")
                text = text.replace("end RingAddCommGroupAuxiliary\n", "")
                text = text.replace("abbrev RingAddCommGroupAuxiliary'", "abbrev RightModule")
                text = text.replace("abbrev RingAddCommGroupAuxiliary", "abbrev LeftModule")
            if write_if_changed(path, text):
                changed.append(str(path.relative_to(ROOT)))
    proposals_path = ROOT / "manifests/alignment/cleanroom-proposals.jsonl"
    proposals = [json.loads(line) for line in proposals_path.read_text(encoding="utf-8").splitlines()]
    response_changes = {}
    renamed_declarations = 0
    for row in proposals:
        before = row.get("new_fqn", "")
        after = renamed(before)
        if before == after:
            continue
        row["new_fqn"] = after
        if before in EXACT_RENAMES:
            if before.rsplit(".", 1)[0] != after.rsplit(".", 1)[0]:
                row["proposed_name"] = after.rsplit(".", 1)[-1]
                row["namespace"] = after.rsplit(".", 1)[0].removeprefix("RepresentationTheory.")
            else:
                row["proposed_name"] = row["proposed_name"].rsplit(".", 1)[0] + "." + after.rsplit(".", 1)[-1] if "." in row["proposed_name"] else after.rsplit(".", 1)[-1]
        else:
            row["proposed_name"] = after.rsplit(".", 1)[-1]
            row["namespace"] = "Algebra.ModuleActions"
        response_changes.setdefault(row["response"], {})[row["temporary_id"]] = row
        renamed_declarations += 1
    for row in proposals:
        docstring = DOCSTRINGS.get(row.get("new_fqn"))
        if docstring is None:
            continue
        path = ROOT / "clean-code/release" / (row["new_module"].replace(".", "/") + ".lean")
        source = path.read_text(encoding="utf-8")
        spellings = {row["proposed_name"], row["new_fqn"], "_root_." + row["new_fqn"]}
        if row["new_fqn"].startswith(row["new_module"] + "."):
            spellings.add(row["new_fqn"][len(row["new_module"]) + 1:])
        name = "(?:" + "|".join(re.escape(value) for value in sorted(spellings, key=len, reverse=True)) + ")"
        # Structure projections have their documentation on field declarations,
        # which have no `def`/`theorem` keyword. Still require one exact name match.
        declaration = r"(?:abbrev|def|theorem|lemma|class|structure|alias)\s+" + name + r"(?=[\s({:])"
        field = name + r"(?=[ \t]*:)"
        pattern = re.compile(r"(/--(?:(?!-/).)*-/)(\s*(?:@\[(?:(?!/--).)*?\]\s*)?(?:noncomputable\s+)?(?:" + declaration + "|" + field + "))", re.S)
        matches = list(pattern.finditer(source))
        if len(matches) != 1:
            raise ValueError(f"expected one source docstring for {row['new_fqn']}: {len(matches)}")
        match = matches[0]
        source = source[:match.start(1)] + f"/-- {docstring} -/" + source[match.end(1):]
        if write_if_changed(path, source):
            changed.append(str(path.relative_to(ROOT)))
        row["cleanroom_docstring"] = docstring
        response_path = ROOT / "clean-room-packets" / row["response"]
        response = json.loads(response_path.read_text(encoding="utf-8"))
        entries = [entry for entry in response["declarations"] if entry["temporary_id"] == row["temporary_id"]]
        if len(entries) != 1:
            raise ValueError(f"missing unique reviewed response for {row['new_fqn']}")
        entries[0]["docstring"] = docstring
        write_if_changed(response_path, json.dumps(response, indent=2, ensure_ascii=False) + "\n")
    if response_changes or DOCSTRINGS:
        proposals_path.write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in proposals), encoding="utf-8")
    for relative, entries in response_changes.items():
        path = ROOT / "clean-room-packets" / relative
        response = json.loads(path.read_text(encoding="utf-8"))
        for declaration in response["declarations"]:
            if declaration["temporary_id"] in entries:
                row = entries[declaration["temporary_id"]]
                declaration["new_name"] = row["proposed_name"]
                if row.get("namespace"):
                    declaration["namespace"] = row["namespace"]
        path.write_text(json.dumps(response, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    for relative in ("verso/release/metadata/reader-annotations.json", "verso/release/metadata/declaration-sources.json"):
        path = ROOT / relative
        data = replace_names(json.loads(path.read_text(encoding="utf-8")))
        if write_if_changed(path, json.dumps(data, indent=2, ensure_ascii=False) + "\n"):
            changed.append(relative)
    # Presentation headings are separate from the immutable book transcription.
    metadata = ROOT / "verso/release/metadata"
    payload = json.loads((metadata / "items.json").read_text(encoding="utf-8"))
    book = json.loads((metadata / "book.json").read_text(encoding="utf-8"))
    nodes = {node["node_id"]: node for node in book["nodes"]}
    titles_path = metadata / "reader-titles.json"
    titles = json.loads(titles_path.read_text(encoding="utf-8")) if titles_path.exists() else {}
    for item in payload["items"]:
        previous = item["title"]
        title = TITLE_DECISIONS.get(item["id"], previous)
        if "heading" in previous.lower():
            node = nodes[item["node_id"]]
            title = node["title"]
            if item["id"] == "Chapter2/Introduction":
                title = "What is representation theory?"
            title = title.replace("$\\mathfrak{sl}(2)$", "sl(2)").replace("$", "")
        for suffix in (" (continues to missing page)", " (statement on missing page)", " (from missing page)"):
            title = title.replace(suffix, "")
        if title == previous and item["id"] not in titles:
            continue
        titles[item["id"]] = title
        item["title"] = title
        path = ROOT / "verso/release" / (item["verso_module"].replace(".", "/") + ".lean")
        if not path.exists():
            if item.get("verso_projection", {}).get("structure_only"):
                continue
            raise FileNotFoundError(path)
        source = path.read_text(encoding="utf-8")
        rendered_title = escape_inline(title)
        source = re.sub(r'(?m)^(#doc \(Manual\) )"(?:[^"\\]|\\.)*"( =>)$',
                        lambda match: match.group(1) + json.dumps(rendered_title) + match.group(2),
                        source, count=1)
        # Only generated titles are changed; original paragraphs stay untouched.
        lines = source.splitlines(keepends=True)
        for index, line in enumerate(lines):
            if line.startswith("# ") and line[2:].strip() in {previous, escape_inline(previous)}:
                lines[index] = "# " + rendered_title + "\n"
        if write_if_changed(path, "".join(lines)):
            changed.append(str(path.relative_to(ROOT)))
    (metadata / "items.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    titles_path.write_text(json.dumps(titles, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"renamed_declarations": renamed_declarations, "reader_titles": len(titles), "changed_sources": changed}, indent=2))


if __name__ == "__main__":
    main()
