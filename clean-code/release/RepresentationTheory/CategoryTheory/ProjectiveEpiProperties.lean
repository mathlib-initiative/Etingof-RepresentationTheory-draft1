/-
Copyright (c) 2026 mathlib-initiative. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: mathlib-initiative
-/

import Mathlib.CategoryTheory.Preadditive.Projective.Basic
import Mathlib.CategoryTheory.Generator.Basic
import Mathlib.CategoryTheory.Limits.Shapes.Biproducts
import RepresentationTheory.Alignment.Attribute

universe u v w

open CategoryTheory CategoryTheory.Limits

namespace RepresentationTheory.CategoryTheory.ProjectiveEpiProperties

/-- A projective separator. -/
def IsProjectiveEpiSigmaDesc {C : Type u} [Category.{v} C] (P : C) : Prop :=
  Projective P ∧ IsSeparator P

namespace IsProjectiveEpiSigmaDesc

variable {C : Type u} [Category.{v} C] {P : C}

/-- Every object satisfying this property is projective. -/
theorem projective (h : IsProjectiveEpiSigmaDesc P) : Projective P := h.1

/-- Every object satisfying this property is a separator. -/
theorem isSeparator (h : IsProjectiveEpiSigmaDesc P) : IsSeparator P := h.2

/-- Projectivity together with epimorphic coproduct desc morphisms characterizes this property. -/
theorem iff_projective_and_epi_sigma_desc [∀ X : C, HasCoproduct fun _ : P ⟶ X => P] :
    IsProjectiveEpiSigmaDesc P ↔
      Projective P ∧ ∀ X : C, Epi (Sigma.desc fun f : P ⟶ X => f) := by
  rw [IsProjectiveEpiSigmaDesc, isSeparator_iff_epi]

end IsProjectiveEpiSigmaDesc

/-- A projective object whose finite direct sums map epimorphically onto every object. -/
class HasProjectiveEpiWitnesses {C : Type u} [Category.{v} C] [HasZeroMorphisms C] (P : C)
    extends toProjective : Projective P where
  /-- For each object X, some finite biproduct of P admits an epimorphism to X. -/
  exists_epi : ∀ (X : C), ∃ (n : ℕ) (_ : HasBiproduct (fun _ : Fin n => P))
    (f : biproduct (fun _ : Fin n => P) ⟶ X), Epi f

/-
/-- The projectivity structure carried by an object satisfying this property. -/
-/

end RepresentationTheory.CategoryTheory.ProjectiveEpiProperties

-- Recovered exact-module book alignment.
attribute [source_ref "Chapter9/Definition9.6.2" (role := primary)] _root_.RepresentationTheory.CategoryTheory.ProjectiveEpiProperties.HasProjectiveEpiWitnesses
attribute [source_ref "Chapter9/Definition9.6.2" (role := primary)] _root_.RepresentationTheory.CategoryTheory.ProjectiveEpiProperties.IsProjectiveEpiSigmaDesc
attribute [source_ref "Chapter9/Definition9.6.2" (role := supporting)] _root_.RepresentationTheory.CategoryTheory.ProjectiveEpiProperties.HasProjectiveEpiWitnesses.exists_epi
attribute [source_ref "Chapter9/Definition9.6.2" (role := supporting)] _root_.RepresentationTheory.CategoryTheory.ProjectiveEpiProperties.HasProjectiveEpiWitnesses.toProjective
attribute [source_ref "Chapter9/Definition9.6.2" (role := supporting)] _root_.RepresentationTheory.CategoryTheory.ProjectiveEpiProperties.IsProjectiveEpiSigmaDesc.iff_projective_and_epi_sigma_desc
attribute [source_ref "Chapter9/Definition9.6.2" (role := supporting)] _root_.RepresentationTheory.CategoryTheory.ProjectiveEpiProperties.IsProjectiveEpiSigmaDesc.isSeparator
attribute [source_ref "Chapter9/Definition9.6.2" (role := supporting)] _root_.RepresentationTheory.CategoryTheory.ProjectiveEpiProperties.IsProjectiveEpiSigmaDesc.projective
