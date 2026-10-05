/-
Copyright (c) 2026 mathlib-initiative. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: mathlib-initiative
-/

import Mathlib.Algebra.Module.Projective
import Mathlib.RingTheory.SimpleModule.Basic
import Mathlib.Order.Lattice
import RepresentationTheory.LinearAlgebra.ModuleDecompositions
import RepresentationTheory.Alignment.Attribute

namespace RepresentationTheory.RingModuleAuxiliary

/-- An indecomposable projective module with a surjection to M and a superfluous kernel. -/
structure Auxiliary (R : Type*) [Ring R]
    (M : Type*) [AddCommGroup M] [Module R M] where
  /-- The projective module P covering M. -/
  Carrier : Type*
  /-- The additive commutative group structure provided on the attached type. -/
  [instAddCommGroupCarrier : AddCommGroup Carrier]
  /-- The scalar action of the ambient ring on the attached type. -/
  [instModuleCarrier : Module R Carrier]
  /-- The attached type is a projective module over the ambient ring. -/
  [projective : Module.Projective R Carrier]
  /-- P is nonzero and indecomposable. -/
  auxiliaryProperty :
    RepresentationTheory.LinearAlgebra.ModuleDecompositions.AuxiliaryDecompositionPredicate R Carrier
  /-- The covering map P to M. -/
  toLinearMap : Carrier →ₗ[R] M
  /-- The associated linear map reaches every element of the ambient module. -/
  surjective_toLinearMap : Function.Surjective toLinearMap
  /-- If a submodule together with the map kernel spans the attached type, then the submodule is
  all of it. -/
  eq_top_of_sup_kernel_eq_top :
    ∀ N : Submodule R Carrier, N ⊔ LinearMap.ker toLinearMap = ⊤ → N = ⊤

attribute [instance] Auxiliary.instAddCommGroupCarrier
  Auxiliary.instModuleCarrier
  Auxiliary.projective

end RepresentationTheory.RingModuleAuxiliary

-- Recovered exact-module book alignment.
attribute [source_ref "Chapter9/Definition9.2.2" (role := primary)] _root_.RepresentationTheory.RingModuleAuxiliary.Auxiliary
attribute [source_ref "Chapter9/Definition9.2.2" (role := supporting)] _root_.RepresentationTheory.RingModuleAuxiliary.Auxiliary.Carrier
attribute [source_ref "Chapter9/Definition9.2.2" (role := supporting)] _root_.RepresentationTheory.RingModuleAuxiliary.Auxiliary.auxiliaryProperty
attribute [source_ref "Chapter9/Definition9.2.2" (role := supporting)] _root_.RepresentationTheory.RingModuleAuxiliary.Auxiliary.eq_top_of_sup_kernel_eq_top
attribute [source_ref "Chapter9/Definition9.2.2" (role := supporting)] _root_.RepresentationTheory.RingModuleAuxiliary.Auxiliary.instAddCommGroupCarrier
attribute [source_ref "Chapter9/Definition9.2.2" (role := supporting)] _root_.RepresentationTheory.RingModuleAuxiliary.Auxiliary.instModuleCarrier
attribute [source_ref "Chapter9/Definition9.2.2" (role := supporting)] _root_.RepresentationTheory.RingModuleAuxiliary.Auxiliary.projective
attribute [source_ref "Chapter9/Definition9.2.2" (role := supporting)] _root_.RepresentationTheory.RingModuleAuxiliary.Auxiliary.surjective_toLinearMap
attribute [source_ref "Chapter9/Definition9.2.2" (role := supporting)] _root_.RepresentationTheory.RingModuleAuxiliary.Auxiliary.toLinearMap
