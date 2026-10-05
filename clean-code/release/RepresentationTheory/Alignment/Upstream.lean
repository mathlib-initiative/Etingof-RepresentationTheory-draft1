/-
Copyright (c) 2026 mathlib-initiative. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Kim Morrison
-/
import Mathlib.Algebra.Algebra.Basic
import Mathlib.Algebra.Algebra.Defs
import Mathlib.Algebra.Algebra.Subalgebra.Basic
import Mathlib.Algebra.Algebra.Subalgebra.Lattice
import Mathlib.Algebra.Category.ModuleCat.Abelian
import Mathlib.Algebra.CharP.Defs
import Mathlib.Algebra.CharP.Lemmas
import Mathlib.Algebra.DirectSum.Ring
import Mathlib.Algebra.FreeAlgebra
import Mathlib.Algebra.Group.Action.Defs
import Mathlib.Algebra.Homology.HomologicalComplex
import Mathlib.Algebra.Homology.ShortComplex.HomologicalComplex
import Mathlib.Algebra.Lie.Basic
import Mathlib.Algebra.Lie.Classical
import Mathlib.Algebra.Lie.OfAssociative
import Mathlib.Algebra.Lie.Solvable
import Mathlib.Algebra.Lie.Subalgebra
import Mathlib.Algebra.Lie.TensorProduct
import Mathlib.Algebra.Lie.UniversalEnveloping
import Mathlib.Algebra.Module.Defs
import Mathlib.Algebra.Module.Equiv.Defs
import Mathlib.Algebra.Module.LinearMap.End
import Mathlib.Algebra.Module.Pi
import Mathlib.Algebra.Module.RingHom
import Mathlib.Algebra.Module.Submodule.Ker
import Mathlib.Algebra.Module.Submodule.Map
import Mathlib.Algebra.Module.Submodule.Range
import Mathlib.Algebra.MonoidAlgebra.Basic
import Mathlib.Algebra.MonoidAlgebra.Defs
import Mathlib.Algebra.MvPolynomial.Basic
import Mathlib.Algebra.Ring.Defs
import Mathlib.Algebra.Ring.Pi
import Mathlib.CategoryTheory.Abelian.Basic
import Mathlib.CategoryTheory.Adjunction.Unique
import Mathlib.CategoryTheory.Category.Basic
import Mathlib.CategoryTheory.FintypeCat
import Mathlib.CategoryTheory.Functor.Basic
import Mathlib.CategoryTheory.Functor.Category
import Mathlib.CategoryTheory.Functor.FullyFaithful
import Mathlib.CategoryTheory.Linear.Basic
import Mathlib.CategoryTheory.NatIso
import Mathlib.CategoryTheory.Preadditive.Projective.Basic
import Mathlib.CategoryTheory.Preadditive.Projective.Resolution
import Mathlib.CategoryTheory.Yoneda
import Mathlib.Combinatorics.Enumerative.Partition.Basic
import Mathlib.Data.Matrix.Basis
import Mathlib.FieldTheory.IsAlgClosed.Basic
import Mathlib.FieldTheory.Minpoly.Basic
import Mathlib.FieldTheory.Minpoly.Field
import Mathlib.FieldTheory.Minpoly.IsConjRoot
import Mathlib.FieldTheory.Minpoly.IsIntegrallyClosed
import Mathlib.GroupTheory.OrderOfElement
import Mathlib.LinearAlgebra.Basis.Defs
import Mathlib.LinearAlgebra.Basis.VectorSpace
import Mathlib.LinearAlgebra.CliffordAlgebra.Basic
import Mathlib.LinearAlgebra.DFinsupp
import Mathlib.LinearAlgebra.Dimension.RankNullity
import Mathlib.LinearAlgebra.Dual.Lemmas
import Mathlib.LinearAlgebra.Finsupp.VectorSpace
import Mathlib.LinearAlgebra.FreeAlgebra
import Mathlib.LinearAlgebra.FreeModule.Finite.Matrix
import Mathlib.LinearAlgebra.Isomorphisms
import Mathlib.LinearAlgebra.Matrix.StdBasis
import Mathlib.LinearAlgebra.Matrix.ToLin
import Mathlib.LinearAlgebra.PiTensorProduct.Basic
import Mathlib.LinearAlgebra.Prod
import Mathlib.LinearAlgebra.Projection
import Mathlib.LinearAlgebra.Quotient.Defs
import Mathlib.LinearAlgebra.TensorProduct.Associator
import Mathlib.LinearAlgebra.TensorProduct.Defs
import Mathlib.LinearAlgebra.TensorProduct.Map
import Mathlib.Order.Atoms
import Mathlib.Order.JordanHolder
import Mathlib.Order.KrullDimension
import Mathlib.RepresentationTheory.Basic
import Mathlib.RepresentationTheory.Character
import Mathlib.RepresentationTheory.Coinduced
import Mathlib.RepresentationTheory.Maschke
import Mathlib.RepresentationTheory.Rep.Iso
import Mathlib.RepresentationTheory.Rep.Res
import Mathlib.RingTheory.Artinian.Module
import Mathlib.RingTheory.FiniteLength
import Mathlib.RingTheory.Length
import Mathlib.RingTheory.Nilpotent.Basic
import Mathlib.RingTheory.SimpleModule.Basic
import Mathlib.RingTheory.SimpleModule.IsAlgClosed
import Mathlib.RingTheory.TensorProduct.Basic
import RepresentationTheory.Alignment.Attribute

attribute [source_ref "Chapter2/Definition2.11.1" (role := supporting)] _root_.TensorProduct.add_tmul
attribute [source_ref "Chapter2/Definition2.11.1" (role := supporting)] _root_.TensorProduct.smul_tmul
attribute [source_ref "Chapter2/Definition2.11.1" (role := supporting)] _root_.TensorProduct.tmul
attribute [source_ref "Chapter2/Definition2.11.1" (role := supporting)] _root_.TensorProduct.tmul_add
attribute [source_ref "Chapter2/Definition2.11.1" (role := supporting)] _root_.TensorProduct.tmul_smul
attribute [source_ref "Chapter2/Definition2.14.2/Derived3" (role := supporting)] _root_.Module.Dual.instLieModule
attribute [source_ref "Chapter2/Definition2.14.2/Derived3" (role := supporting)] _root_.Module.Dual.instLieRingModule
attribute [source_ref "Chapter2/Definition2.14.2/Derived3" (role := supporting)] _root_.TensorProduct.LieModule.lieModule
attribute [source_ref "Chapter2/Definition2.14.2/Derived3" (role := supporting)] _root_.TensorProduct.LieModule.lieRingModule
attribute [source_ref "Chapter2/Definition2.3.6/Derived4" (role := supporting)] _root_.LinearEquiv.symm
attribute [source_ref "Chapter2/Definition2.9.6" (role := supporting)] _root_.LieHom
attribute [source_ref "Chapter2/Definition2.9.7" (role := supporting)] _root_.LieModule
attribute [source_ref "Chapter2/Discussion_2.1_irreducible_indecomposable/Derived9" (role := supporting)] _root_.LinearMap.toMatrixAlgEquiv'
attribute [source_ref "Chapter2/Discussion_2.1_overview/Derived3" (role := supporting)] _root_.Module.End.instAlgebra
attribute [source_ref "Chapter2/Discussion_2.1_overview/Derived4" (role := supporting)] _root_.MonoidAlgebra
attribute [source_ref "Chapter2/Discussion_2.1_overview/Derived4" (role := supporting)] _root_.UniversalEnvelopingAlgebra
attribute [source_ref "Chapter2/Discussion_after_Theorem2.1.2" (role := supporting)] _root_.MonoidAlgebra
attribute [source_ref "Chapter2/Discussion_after_Theorem2.1.2" (role := supporting)] _root_.MonoidAlgebra.single_mul_single
attribute [source_ref "Chapter2/Discussion_after_Theorem2.1.2/Derived2" (role := supporting)] _root_.IsSemisimpleRing.isSemisimpleModule
attribute [source_ref "Chapter2/Discussion_commutativity_examples" (role := supporting)] _root_.AddMonoidAlgebra.commRing
attribute [source_ref "Chapter2/Discussion_commutativity_examples" (role := supporting)] _root_.CommRing
attribute [source_ref "Chapter2/Discussion_commutativity_examples" (role := supporting)] _root_.MvPolynomial
attribute [source_ref "Chapter2/Discussion_concrete_Lie_examples/Derived2" (role := supporting)] _root_.LieAlgebra.SpecialLinear.sl
attribute [source_ref "Chapter2/Discussion_concrete_Lie_examples/Derived2" (role := supporting)] _root_.LieAlgebra.SpecialLinear.sl_bracket
attribute [source_ref "Chapter2/Discussion_concrete_Lie_examples_continued/Derived4" (role := supporting)] _root_.LieAlgebra.Orthogonal.mem_so
attribute [source_ref "Chapter2/Discussion_concrete_Lie_examples_continued/Derived4" (role := supporting)] _root_.LieAlgebra.Orthogonal.so
attribute [source_ref "Chapter2/Discussion_proof_Corollary2.3.10" (role := supporting)] _root_.IsAlgClosed.exists_root
attribute [source_ref "Chapter2/Discussion_pure_tensors" (role := supporting)] _root_.PiTensorProduct
attribute [source_ref "Chapter2/Discussion_pure_tensors/Derived4" (role := supporting)] _root_.TensorProduct.assoc
attribute [source_ref "Chapter2/Discussion_tensor_product_maps" (role := supporting)] _root_.TensorProduct.map
attribute [source_ref "Chapter2/Discussion_tensor_product_maps" (role := supporting)] _root_.TensorProduct.map_tmul
attribute [source_ref "Chapter2/Discussion_tensors_type/Derived2" (role := supporting)] _root_.Module.Basis.repr
attribute [source_ref "Chapter2/Discussion_tensors_type/Derived2" (role := supporting)] _root_.Module.Basis.sum_repr
attribute [source_ref "Chapter2/Example2.2.4" (role := supporting)] _root_.AddMonoidAlgebra.algebra
attribute [source_ref "Chapter2/Example2.2.4" (role := supporting)] _root_.Algebra.id
attribute [source_ref "Chapter2/Example2.2.4" (role := supporting)] _root_.Finsupp.basisSingleOne
attribute [source_ref "Chapter2/Example2.2.4" (role := supporting)] _root_.FreeAlgebra.basisFreeMonoid
attribute [source_ref "Chapter2/Example2.2.4" (role := supporting)] _root_.FreeAlgebra.equivMonoidAlgebraFreeMonoid
attribute [source_ref "Chapter2/Example2.2.4" (role := supporting)] _root_.FreeAlgebra.instAlgebra
attribute [source_ref "Chapter2/Example2.2.4" (role := supporting)] _root_.Module.End.instAlgebra
attribute [source_ref "Chapter2/Example2.2.4" (role := supporting)] _root_.Module.End.mul_apply
attribute [source_ref "Chapter2/Example2.2.4" (role := supporting)] _root_.MonoidAlgebra.algebra
attribute [source_ref "Chapter2/Example2.2.4" (role := supporting)] _root_.MonoidAlgebra.single_mul_single
attribute [source_ref "Chapter2/Example2.3.3" (role := supporting)] _root_.FreeAlgebra.lift
attribute [source_ref "Chapter2/Example2.3.3" (role := supporting)] _root_.FreeAlgebra.lift_symm_apply
attribute [source_ref "Chapter2/Example2.3.3" (role := supporting)] _root_.FreeAlgebra.lift_ι_apply
attribute [source_ref "Chapter2/Example2.9.2" (role := supporting)] _root_.LieRing.ofAssociativeRing
attribute [source_ref "Chapter2/Example2.9.2" (role := supporting)] _root_.LieSubalgebra
attribute [source_ref "Chapter2/Example2.9.2_continued" (role := supporting)] _root_.LieSubalgebra
attribute [source_ref "Chapter2/Example2.9.8" (role := supporting)] _root_.LieAlgebra.ad
attribute [source_ref "Chapter2/Example2.9.8" (role := supporting)] _root_.LieHom.map_lie
attribute [source_ref "Chapter2/Exercise2.11.7" (role := supporting)] _root_.TensorProduct.instModule
attribute [source_ref "Chapter2/Exercise2.11.7" (role := supporting)] _root_.TensorProduct.smul_tmul'
attribute [source_ref "Chapter2/Exercise2.11.7" (role := supporting)] _root_.TensorProduct.tmul_smul
attribute [source_ref "Chapter2/Problem2.11.6" (role := supporting)] _root_.Module
attribute [source_ref "Chapter2/Problem2.11.6" (role := supporting)] _root_.Module.compHom
attribute [source_ref "Chapter2/Problem2.11.6" (role := supporting)] _root_.SMulCommClass
attribute [source_ref "Chapter2/Problem2.16.1" (role := supporting)] _root_.LieAlgebra.coe_derivedSeries_one_eq
attribute [source_ref "Chapter2/Problem2.16.1" (role := supporting)] _root_.LieAlgebra.derivedSeries
attribute [source_ref "Chapter2/Problem2.16.1/Derived2" (role := supporting)] _root_.LieAlgebra.IsSolvable
attribute [source_ref "Chapter2/Problem2.16.1/Derived2" (role := supporting)] _root_.LieAlgebra.isSolvable_iff
attribute [source_ref "Chapter2/Problem2.16.5" (role := supporting)] _root_.IsOfFinOrder
attribute [source_ref "Chapter2/Problem2.3.16" (role := supporting)] _root_.Subalgebra.center
attribute [source_ref "Chapter2/Problem2.3.16/Derived2" (role := supporting)] _root_.Subalgebra.center_eq_top
attribute [source_ref "Chapter2/Problem2.3.17" (role := supporting)] _root_.Module.End
attribute [source_ref "Chapter2/Problem2.4.1" (role := supporting)] _root_.IsCoatom
attribute [source_ref "Chapter2/Problem2.4.1" (role := supporting)] _root_.IsCoatom.lt_iff
attribute [source_ref "Chapter2/Proposition2.3.9/Derived4" (role := supporting)] _root_.LinearMap.ker
attribute [source_ref "Chapter2/Proposition2.3.9/Derived4" (role := supporting)] _root_.LinearMap.range
attribute [source_ref "Chapter3/Corollary3.5.5/Derived2" (role := supporting)] _root_.Module.finrank_linearMap
attribute [source_ref "Chapter3/Corollary3.5.5/Derived2" (role := supporting)] _root_.Submodule.finrank_quotient_add_finrank
attribute [source_ref "Chapter3/Definition3.1.1" (role := supporting)] _root_.IsSemisimpleModule.exists_linearEquiv_dfinsupp
attribute [source_ref "Chapter3/Definition3.1.1" (role := supporting)] _root_.isSemisimpleModule_iff_exists_linearEquiv_dfinsupp
attribute [source_ref "Chapter3/Discussion_after_Theorem3.7.1" (role := supporting)] _root_.Module.length_compositionSeries
attribute [source_ref "Chapter3/Discussion_after_Theorem3.7.1/Derived2" (role := supporting)] _root_.Module.length
attribute [source_ref "Chapter3/Discussion_after_Theorem3.7.1/Derived4" (role := supporting)] _root_.CompositionSeries
attribute [source_ref "Chapter3/Discussion_proof_of_Theorem3.3.1/Derived2" (role := supporting)] _root_.Subspace.dual_finrank_eq
attribute [source_ref "Chapter3/Discussion_proof_of_Theorem3.3.1/Derived2" (role := supporting)] _root_.Subspace.instModuleDualFiniteDimensional
attribute [source_ref "Chapter3/Introduction_to_3.10/Derived2" (role := supporting)] _root_.Algebra.TensorProduct.tmul_mul_tmul
attribute [source_ref "Chapter3/Lemma3.4.2/Derived4" (role := supporting)] _root_.exists_compositionSeries_of_isNoetherian_isArtinian
attribute [source_ref "Chapter3/Lemma3.4.2/Derived5" (role := supporting)] _root_.Submodule.Quotient.module
attribute [source_ref "Chapter3/Lemma3.4.2/Derived6" (role := supporting)] _root_.exists_compositionSeries_of_isNoetherian_isArtinian
attribute [source_ref "Chapter3/Lemma3.4.2/Derived7" (role := supporting)] _root_.Submodule.comap
attribute [source_ref "Chapter3/Lemma3.8.2/Derived2" (role := supporting)] _root_.LinearMap.isCompl_iSup_ker_pow_iInf_range_pow
attribute [source_ref "Chapter3/Lemma3.8.2/Derived4" (role := supporting)] _root_.IsNilpotent.isUnit_one_sub
attribute [source_ref "Chapter3/Problem3.3.3/Derived12" (role := supporting)] _root_.Matrix.single
attribute [source_ref "Chapter3/Problem3.3.3/Derived6" (role := supporting)] _root_.Pi.module'
attribute [source_ref "Chapter3/Problem3.9.1/Derived7" (role := supporting)] _root_.LinearMap.quotKerEquivRange
attribute [source_ref "Chapter3/Problem3.9.5" (role := supporting)] _root_.CliffordAlgebra
attribute [source_ref "Chapter3/Problem3.9.5/Derived2" (role := supporting)] _root_.CliffordAlgebra.ι_mul_ι_add_swap
attribute [source_ref "Chapter3/Problem3.9.5/Derived2" (role := supporting)] _root_.CliffordAlgebra.ι_sq_scalar
attribute [source_ref "Chapter3/Proposition3.1.4/Derived4" (role := supporting)] _root_.IsSemisimpleModule.eq_bot_or_exists_simple_le
attribute [source_ref "Chapter3/Remark3.10.3" (role := supporting)] _root_.isSimpleModule_self_iff_isUnit
attribute [source_ref "Chapter3/Remark3.8.6/Derived2" (role := supporting)] _root_.Module.length
attribute [source_ref "Chapter3/Remark3.8.6/Derived2" (role := supporting)] _root_.Order.LTSeries.length_le_krullDim
attribute [source_ref "Chapter3/Remark3.8.6/Derived2" (role := supporting)] _root_.isFiniteLength_iff_isNoetherian_isArtinian
attribute [source_ref "Chapter3/Theorem3.2.2/Derived5" (role := supporting)] _root_.DFinsupp.linearEquivFunOnFintype
attribute [source_ref "Chapter3/Theorem3.2.2/Derived7" (role := supporting)] _root_.DirectSum.GNonUnitalNonAssocSemiring
attribute [source_ref "Chapter3/Theorem3.2.2/Derived7" (role := supporting)] _root_.Pi.ring
attribute [source_ref "Chapter3/Theorem3.6.2/Derived10" (role := supporting)] _root_.IsSemisimpleRing.exists_algEquiv_pi_matrix_of_isAlgClosed
attribute [source_ref "Chapter3/Theorem3.6.2/Derived11" (role := supporting)] _root_.IsSemisimpleRing.exists_algEquiv_pi_matrix_of_isAlgClosed
attribute [source_ref "Chapter3/Theorem3.6.2/Derived7" (role := supporting)] _root_.Matrix.single_mul_single_of_ne
attribute [source_ref "Chapter3/Theorem3.6.2/Derived7" (role := supporting)] _root_.Matrix.single_mul_single_same
attribute [source_ref "Chapter3/Theorem3.6.2/Derived9" (role := supporting)] _root_.Matrix.stdBasis
attribute [source_ref "Chapter3/Theorem3.7.1" (role := supporting)] _root_.CompositionSeries
attribute [source_ref "Chapter3/Theorem3.7.1" (role := supporting)] _root_.covBy_iff_quot_is_simple
attribute [source_ref "Chapter3/Theorem3.7.1/Derived11" (role := supporting)] _root_.CompositionSeries.jordan_holder
attribute [source_ref "Chapter3/Theorem3.7.1/Derived13" (role := supporting)] _root_.CompositionSeries.jordan_holder
attribute [source_ref "Chapter3/Theorem3.7.1/Derived13" (role := supporting)] _root_.Submodule.Quotient.module
attribute [source_ref "Chapter3/Theorem3.7.1/Derived14" (role := supporting)] _root_.IsSimpleOrder.eq_bot_or_eq_top
attribute [source_ref "Chapter3/Theorem3.7.1/Derived15" (role := supporting)] _root_.LinearMap.ker_coprod_of_disjoint_range
attribute [source_ref "Chapter3/Theorem3.7.1/Derived16" (role := supporting)] _root_.Submodule.Quotient.module
attribute [source_ref "Chapter3/Theorem3.7.1/Derived18" (role := supporting)] _root_.CompositionSeries.jordan_holder
attribute [source_ref "Chapter3/Theorem3.7.1/Derived18" (role := supporting)] _root_.Submodule.comap
attribute [source_ref "Chapter3/Theorem3.7.1/Derived18" (role := supporting)] _root_.Submodule.map
attribute [source_ref "Chapter3/Theorem3.7.1/Derived19" (role := supporting)] _root_.CompositionSeries.jordan_holder
attribute [source_ref "Chapter3/Theorem3.7.1/Derived19" (role := supporting)] _root_.Submodule.comap
attribute [source_ref "Chapter3/Theorem3.7.1/Derived19" (role := supporting)] _root_.Submodule.map
attribute [source_ref "Chapter3/Theorem3.7.1/Derived20" (role := supporting)] _root_.CompositionSeries.jordan_holder
attribute [source_ref "Chapter3/Theorem3.7.1/Derived20" (role := supporting)] _root_.Submodule.comap
attribute [source_ref "Chapter3/Theorem3.7.1/Derived20" (role := supporting)] _root_.Submodule.map
attribute [source_ref "Chapter3/Theorem3.7.1/Derived21" (role := supporting)] _root_.CompositionSeries.jordan_holder
attribute [source_ref "Chapter3/Theorem3.7.1/Derived21" (role := supporting)] _root_.Submodule.comap
attribute [source_ref "Chapter3/Theorem3.7.1/Derived21" (role := supporting)] _root_.Submodule.map
attribute [source_ref "Chapter3/Theorem3.7.1/Derived9" (role := supporting)] _root_.CharP.cast_eq_zero
attribute [source_ref "Chapter4/Discussion_4.4" (role := supporting)] _root_.Representation.dual
attribute [source_ref "Chapter4/Discussion_4.4" (role := supporting)] _root_.Representation.tprod
attribute [source_ref "Chapter4/Example4.1.3/Derived5" (role := supporting)] _root_.sub_pow_char_of_commute
attribute [source_ref "Chapter4/Introduction/Derived2" (role := supporting)] _root_.Representation
attribute [source_ref "Chapter4/Introduction/Derived3" (role := supporting)] _root_.Rep.equivalenceModuleMonoidAlgebra
attribute [source_ref "Chapter4/Introduction/Derived3" (role := supporting)] _root_.Representation.asModule
attribute [source_ref "Chapter4/Introduction/Derived3" (role := supporting)] _root_.Representation.ofModule
attribute [source_ref "Chapter4/Introduction_4.10" (role := supporting)] _root_.MvPolynomial.X
attribute [source_ref "Chapter4/Introduction_4.2" (role := supporting)] _root_.FDRep.char_conj
attribute [source_ref "Chapter4/Introduction_4.2" (role := supporting)] _root_.FDRep.character
attribute [source_ref "Chapter4/Introduction_4.7" (role := supporting)] _root_.LinearMap.toMatrix
attribute [source_ref "Chapter4/Theorem4.1.1/Derived10" (role := supporting)] _root_.MonoidAlgebra.Submodule.exists_isCompl
attribute [source_ref "Chapter4/Theorem4.1.1/Derived10" (role := supporting)] _root_.isSemisimpleModule_iff
attribute [source_ref "Chapter4/Theorem4.1.1/Derived11" (role := supporting)] _root_.Submodule.exists_isCompl
attribute [source_ref "Chapter4/Theorem4.1.1/Derived11" (role := supporting)] _root_.Submodule.projection
attribute [source_ref "Chapter4/Theorem4.1.1/Derived12" (role := supporting)] _root_.Submodule.ker_projection
attribute [source_ref "Chapter4/Theorem4.1.1/Derived12" (role := supporting)] _root_.Submodule.projection_apply_left
attribute [source_ref "Chapter4/Theorem4.1.1/Derived12" (role := supporting)] _root_.Submodule.projection_apply_right
attribute [source_ref "Chapter4/Theorem4.1.1/Derived13" (role := supporting)] _root_.LinearMap.conjugate
attribute [source_ref "Chapter4/Theorem4.1.1/Derived13" (role := supporting)] _root_.LinearMap.equivariantProjection
attribute [source_ref "Chapter4/Theorem4.1.1/Derived13" (role := supporting)] _root_.LinearMap.sumOfConjugates
attribute [source_ref "Chapter4/Theorem4.1.1/Derived14" (role := supporting)] _root_.LinearMap.equivariantProjection_condition
attribute [source_ref "Chapter4/Theorem4.1.1/Derived14" (role := supporting)] _root_.MonoidAlgebra.exists_leftInverse_of_injective
attribute [source_ref "Chapter4/Theorem4.1.1/Derived15" (role := supporting)] _root_.LinearMap.sumOfConjugatesEquivariant
attribute [source_ref "Chapter4/Theorem4.1.1/Derived16" (role := supporting)] _root_.LinearMap.isCompl_of_proj
attribute [source_ref "Chapter4/Theorem4.1.1/Derived16" (role := supporting)] _root_.MonoidAlgebra.Submodule.exists_isCompl
attribute [source_ref "Chapter4/Theorem4.1.1/Derived9" (role := supporting)] _root_.IsSemisimpleRing.exists_algEquiv_pi_matrix_of_isAlgClosed
attribute [source_ref "Chapter4/Theorem4.5.1/Derived3" (role := supporting)] _root_.FDRep.scalar_product_char_eq_finrank_equivariant
attribute [source_ref "Chapter5/Definition5.12.1" (role := supporting)] _root_.Nat.Partition
attribute [source_ref "Chapter5/Definition5.8.1" (role := supporting)] _root_.Representation.coindV
attribute [source_ref "Chapter5/Discussion_after_Proposition5.2.5" (role := supporting)] _root_.minpoly
attribute [source_ref "Chapter5/Discussion_after_Proposition5.2.5" (role := supporting)] _root_.minpoly.aeval
attribute [source_ref "Chapter5/Discussion_after_Proposition5.2.5" (role := supporting)] _root_.minpoly.dvd
attribute [source_ref "Chapter5/Discussion_after_Proposition5.2.5" (role := supporting)] _root_.minpoly.min
attribute [source_ref "Chapter5/Discussion_after_Proposition5.2.5" (role := supporting)] _root_.minpoly.monic
attribute [source_ref "Chapter5/Discussion_after_Proposition5.2.5/Derived2" (role := supporting)] _root_.IsConjRoot
attribute [source_ref "Chapter5/Discussion_after_Proposition5.2.5/Derived2" (role := supporting)] _root_.IsConjRoot.aeval_eq_zero
attribute [source_ref "Chapter5/Discussion_after_Proposition5.2.5/Derived2" (role := supporting)] _root_.minpoly.dvd
attribute [source_ref "Chapter5/Discussion_after_Proposition5.2.5/Derived3" (role := supporting)] _root_.IsConjRoot.isIntegral
attribute [source_ref "Chapter5/Discussion_after_Proposition5.2.5/Derived3" (role := supporting)] _root_.minpoly.isIntegrallyClosed_eq_field_fractions'
attribute [source_ref "Chapter5/Discussion_proof_of_Theorem5.3.1" (role := supporting)] _root_.FDRep.char_orthonormal
attribute [source_ref "Chapter5/Discussion_verification_of_Ind" (role := supporting)] _root_.Representation.coind
attribute [source_ref "Chapter5/Discussion_verification_of_Ind" (role := supporting)] _root_.Representation.coindV
attribute [source_ref "Chapter5/Discussion_verification_of_Ind/Derived2" (role := supporting)] _root_.Representation.coind
attribute [source_ref "Chapter5/Introduction_5.8" (role := supporting)] _root_.Rep.res
attribute [source_ref "Chapter7/Definition7.3.1" (role := supporting)] _root_.CategoryTheory.NatIso.ofComponents
attribute [source_ref "Chapter7/Discussion_after_Definition7.2.1" (role := supporting)] _root_.CategoryTheory.Functor.comp
attribute [source_ref "Chapter7/Discussion_after_Definition7.2.1" (role := supporting)] _root_.CategoryTheory.Functor.id
attribute [source_ref "Chapter7/Discussion_after_Definition7.4.1" (role := supporting)] _root_.FintypeCat.Skeleton.equivalence
attribute [source_ref "Chapter7/Discussion_after_Definition7.6.1" (role := supporting)] _root_.CategoryTheory.Adjunction.leftAdjointUniq
attribute [source_ref "Chapter7/Discussion_after_Definition7.6.1" (role := supporting)] _root_.CategoryTheory.Adjunction.rightAdjointUniq
attribute [source_ref "Chapter7/Discussion_after_Definition7.8.1" (role := supporting)] _root_.HomologicalComplex
attribute [source_ref "Chapter7/Discussion_after_Definition7.8.1" (role := supporting)] _root_.HomologicalComplex.Hom
attribute [source_ref "Chapter7/Discussion_after_Definition7.8.1" (role := supporting)] _root_.HomologicalComplex.homology
attribute [source_ref "Chapter7/Discussion_after_Example7.1.3" (role := supporting)] _root_.CategoryTheory.Category
attribute [source_ref "Chapter7/Discussion_after_Problem7.7.3" (role := supporting)] _root_.CategoryTheory.Abelian
attribute [source_ref "Chapter7/Example7.1.5" (role := supporting)] _root_.CategoryTheory.Functor.FullyFaithful.ofFullyFaithful
attribute [source_ref "Chapter7/Example7.1.6" (role := supporting)] _root_.CategoryTheory.Linear
attribute [source_ref "Chapter7/Example7.7.2" (role := supporting)] _root_.ModuleCat.abelian
attribute [source_ref "Chapter7/Introduction_7.3" (role := supporting)] _root_.CategoryTheory.Functor.category
attribute [source_ref "Chapter7/Introduction_7.5" (role := supporting)] _root_.CategoryTheory.Functor.IsCorepresentable
attribute [source_ref "Chapter7/Introduction_7.5" (role := supporting)] _root_.CategoryTheory.Functor.IsRepresentable
attribute [source_ref "Chapter8/Discussion_after_Problem8.2.8" (role := supporting)] _root_.CategoryTheory.EnoughProjectives
attribute [source_ref "Chapter8/Discussion_after_Problem8.2.8" (role := supporting)] _root_.CategoryTheory.ProjectiveResolution
