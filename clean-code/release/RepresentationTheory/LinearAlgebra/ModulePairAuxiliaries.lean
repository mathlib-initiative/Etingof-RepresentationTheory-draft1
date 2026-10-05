/-
Copyright (c) 2026 mathlib-initiative. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Kim Morrison
-/
import Mathlib.Algebra.Module.Equiv.Basic
import RepresentationTheory.Alignment.Attribute

/-!
# Data relating pairs of modules
-/

namespace RepresentationTheory.LinearAlgebra.ModulePairAuxiliaries

/-- A-linear maps between the two modules, preserving addition and the A-action. -/
@[source_ref "Chapter2/Definition2.3.6" (role := supporting)]
abbrev ModulePairAuxiliary' (A : Type*) (V₁ V₂ : Type*) [Ring A]
    [AddCommGroup V₁] [AddCommGroup V₂] [Module A V₁] [Module A V₂] :=
  V₁ →ₗ[A] V₂

/-- A-linear equivalences between the two modules: bundled isomorphisms with inverses. -/
@[source_ref "Chapter2/Definition2.3.6" (role := supporting)]
abbrev ModulePairAuxiliary (A : Type*) (V₁ V₂ : Type*) [Ring A]
    [AddCommGroup V₁] [AddCommGroup V₂] [Module A V₁] [Module A V₂] :=
  V₁ ≃ₗ[A] V₂

/-- The two A-modules are isomorphic, expressed as existence of an A-linear equivalence. -/
@[source_ref "Chapter2/Definition2.3.6" (role := supporting)]
abbrev AuxiliaryModulePairPredicate (A : Type*) (V₁ V₂ : Type*) [Ring A]
    [AddCommGroup V₁] [AddCommGroup V₂] [Module A V₁] [Module A V₂] : Prop :=
  Nonempty (ModulePairAuxiliary A V₁ V₂)

end RepresentationTheory.LinearAlgebra.ModulePairAuxiliaries
