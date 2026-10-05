/-
Copyright (c) 2026 American Mathematical Society. All rights reserved.
-/

import RepresentationTheory.Algebra.ModuleActions
import RepresentationTheory.Algebra.AuxiliaryStructure
import RepresentationTheory.LinearAlgebra.ModuleAuxiliaryData
import RepresentationTheory.LinearAlgebra.ProductModules
import RepresentationTheory.LinearAlgebra.ModulePredicates

/- Examples and correspondences used in the authored opening annotations. -/
open RepresentationTheory.Algebra.ModuleActions

section Representation
variable (k A V : Type*) [CommRing k] [Ring A] [Algebra k A]
  [AddCommGroup V] [Module k V]

example (ρ : A →ₐ[k] Module.End k V) : Module A V := moduleOfAlgHom k A V ρ
example (ρ : A →ₐ[k] Module.End k V) (a : A) (v : V) :
    letI := moduleOfAlgHom k A V ρ
    a • v = ρ a v := moduleOfAlgHom_smul_apply k A V ρ a v
example (ρ : A →ₐ[k] Module.End k V) :
    letI := moduleOfAlgHom k A V ρ
    letI := moduleOfAlgHom_isScalarTower k A V ρ
    actionAlgHom k A V = ρ := actionAlgHom_eq k A V ρ

variable [Module A V] [IsScalarTower k A V]
example : A →ₐ[k] Module.End k V := actionAlgHom k A V
example : moduleOfAlgHom k A V (actionAlgHom k A V) = (inferInstance : Module A V) :=
  moduleOfAlgHom_actionAlgHom k A V
example (W : Submodule A V) (a : A) (v : V) (hv : v ∈ W) :
    a • v ∈ W := W.smul_mem a hv
example : Submodule A V := ⊥
example : Submodule A V := ⊤
end Representation

section RightRepresentation
variable (k A V : Type*) [CommRing k] [Ring A] [Algebra k A]
  [AddCommGroup V] [Module k V] [Module Aᵐᵒᵖ V] [IsScalarTower k Aᵐᵒᵖ V]
example : Aᵐᵒᵖ →ₐ[k] Module.End k V := oppositeActionAlgHom k A V
end RightRepresentation

section BinarySum
variable (A V₁ V₂ : Type*) [Ring A] [AddCommGroup V₁] [AddCommGroup V₂]
  [Module A V₁] [Module A V₂]
example (a : A) (v₁ : V₁) (v₂ : V₂) :
    a • ((v₁, v₂) : V₁ × V₂) = (a • v₁, a • v₂) := rfl
end BinarySum

section Faithfulness
variable (k A V : Type*) [CommRing k] [Ring A] [Algebra k A]
  [AddCommGroup V] [Module k V] [Module A V] [IsScalarTower k A V]

-- The terminology used beside Definition 2.7.3 is the injectivity condition
-- in the original book, not faithfulness of each individual orbit map.
example : RepresentationTheory.LinearAlgebra.ModulePredicates.IsFaithfulRepresentation A V ↔
    Function.Injective (actionAlgHom k A V) := by
  constructor
  · intro h
    letI : FaithfulSMul A V := h
    intro a b hab
    apply FaithfulSMul.eq_of_smul_eq_smul (α := V)
    intro v
    exact LinearMap.congr_fun hab v
  · intro h
    refine ⟨fun {a b} hab => h ?_⟩
    ext v
    exact hab v
end Faithfulness
