/-
Copyright (c) 2026 mathlib-initiative. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: mathlib-initiative
-/

import Mathlib
import RepresentationTheory.CategoryTheory.QuiverLinearDiagrams
import RepresentationTheory.QuiverRepresentation.VertexCompositionSeries
import RepresentationTheory.Alignment.Attribute

/-!
# Vertex simples, arrow-map obstructions and composition-series multiplicities
-/

namespace RepresentationTheory.Quiver.Auxiliary

open Module

variable {k Q : Type*} [Field k] [Quiver Q]

/-- The additive commutative group structure induced on a module over a field. -/
@[reducible]
noncomputable def addCommGroupOfModule {M : Type*} [inst : AddCommMonoid M] [Module k M] :
    AddCommGroup M :=
  Module.addCommMonoidToAddCommGroup k

/-- The vertex-simple representation: a one-dimensional space at i and zero elsewhere. -/
abbrev auxiliaryObjectAtVertex [DecidableEq Q] (i : Q) :
    RepresentationTheory.CategoryTheory.QuiverLinearDiagrams.AuxiliaryQuiverModuleData k Q :=
  RepresentationTheory.QuiverRepresentation.VertexCompositionSeries.representationAtVertex i

/-- The source condition: no arrow has target i. -/
def auxiliaryVertexPropertyTwo (i : Q) : Prop := ∀ j, IsEmpty (j ⟶ i)

/-- The sink condition: no arrow has source i. -/
def auxiliaryVertexPropertyOne (i : Q) : Prop := ∀ j, IsEmpty (i ⟶ j)

/-- The arrow-map coboundary of a family of vertex maps: on an arrow a, send f to
W(a) ∘ f_source − f_target ∘ V(a). -/
noncomputable def auxiliaryElidedDefinition
    (V W : RepresentationTheory.CategoryTheory.QuiverLinearDiagrams.AuxiliaryQuiverModuleData k Q) :
    (∀ i, V.obj i →ₗ[k] W.obj i) →
      (∀ p : (Σ i j, (i ⟶ j)), V.obj p.1 →ₗ[k] W.obj p.2.1) :=
  fun f p =>
    letI : AddCommGroup (W.obj p.2.1) := addCommGroupOfModule (k := k)
    W.map p.2.2 ∘ₗ f p.1 - f p.2.1 ∘ₗ V.map p.2.2

/-- Surjectivity of the arrow-map coboundary. This concrete obstruction criterion
does not itself define or identify a categorical Ext¹ object. -/
def auxiliaryRelation
    (V W : RepresentationTheory.CategoryTheory.QuiverLinearDiagrams.AuxiliaryQuiverModuleData k Q) : Prop :=
  Function.Surjective (auxiliaryElidedDefinition V W)

/-- For a source i, the arrow-map coboundary from any representation to the simple at i is surjective. This concrete criterion is not a packaged categorical Ext¹ theorem. -/
@[source_ref "Chapter6/Problem6.9.3" (role := supporting)]
theorem any_relates_to_auxiliaryObjectAtVertex [DecidableEq Q]
    (i : Q) (hi : auxiliaryVertexPropertyTwo i)
    (V : RepresentationTheory.CategoryTheory.QuiverLinearDiagrams.AuxiliaryQuiverModuleData k Q) :
    auxiliaryRelation V (auxiliaryObjectAtVertex i) := by
  intro g
  refine ⟨0, funext fun p => ?_⟩
  have hbne : p.2.1 ≠ i := by
    intro h
    exact (hi p.1).elim (h ▸ p.2.2)
  have hsub : Subsingleton ((auxiliaryObjectAtVertex (k := k) i).obj p.2.1) := by
    change Subsingleton (Fin (if p.2.1 = i then 1 else 0) → k)
    rw [if_neg hbne]
    exact ⟨fun a b => funext fun x => x.elim0⟩
  exact LinearMap.ext fun x => hsub.elim _ _

/-- For a sink i, the arrow-map coboundary from the simple at i to any representation is surjective. This concrete criterion is not a packaged categorical Ext¹ theorem. -/
@[source_ref "Chapter6/Problem6.9.3" (role := supporting)]
theorem auxiliaryObjectAtVertex_relates_to_any [DecidableEq Q]
    (i : Q) (hi : auxiliaryVertexPropertyOne i)
    (V : RepresentationTheory.CategoryTheory.QuiverLinearDiagrams.AuxiliaryQuiverModuleData k Q) :
    auxiliaryRelation (auxiliaryObjectAtVertex i) V := by
  intro g
  refine ⟨0, funext fun p => ?_⟩
  have hane : p.1 ≠ i := by
    intro h
    exact (hi p.2.1).elim (h ▸ p.2.2)
  have hsub : Subsingleton ((auxiliaryObjectAtVertex (k := k) i).obj p.1) := by
    change Subsingleton (Fin (if p.1 = i then 1 else 0) → k)
    rw [if_neg hane]
    exact ⟨fun a b => funext fun x => x.elim0⟩
  exact LinearMap.ext fun x => by rw [hsub.elim x 0, map_zero, map_zero]

/-- The dimension of the vector space at a vertex. -/
noncomputable def auxiliaryVertexValue
    (V : RepresentationTheory.CategoryTheory.QuiverLinearDiagrams.AuxiliaryQuiverModuleData k Q)
    (i : Q) : ℕ :=
  finrank k (V.obj i)

/-- Under the displayed finite-basis hypothesis, the auxiliary value at a vertex equals the supplied natural number. -/
theorem auxiliaryVertexValue_eq_of_fin_basis
    {Vα : RepresentationTheory.CategoryTheory.QuiverLinearDiagrams.AuxiliaryQuiverModuleData k Q}
    {α : Q → ℕ} (basis : ∀ v, Basis (Fin (α v)) k (Vα.obj v)) (v : Q) :
    auxiliaryVertexValue Vα v = α v := by
  rw [auxiliaryVertexValue, Module.finrank_eq_card_basis (basis v), Fintype.card_fin]

/-- The length is the total dimension. -/
@[source_ref "Chapter6/Problem6.9.3" (role := supporting),
  source_ref "Chapter6/Section6.9_heading" (role := supporting)]
theorem existsAuxiliaryDataWithVertexValues [DecidableEq Q]
    (Vα : RepresentationTheory.CategoryTheory.QuiverLinearDiagrams.AuxiliaryQuiverModuleData k Q)
    (n : ℕ) (order : Q ≃ Fin n)
    (horder : ∀ {v w : Q}, (v ⟶ w) → (order w : ℕ) < (order v : ℕ))
    (α : Q → ℕ) (basis : ∀ v, Basis (Fin (α v)) k (Vα.obj v)) :
    ∃ s : RepresentationTheory.QuiverRepresentation.VertexCompositionSeries.VertexCompositionSeries Vα,
      s.length = ∑ l : Fin n, α (order.symm l) ∧
        ∀ i, s.multiplicity i = auxiliaryVertexValue Vα i := by
  obtain ⟨s, hlen, hmult⟩ :=
    RepresentationTheory.QuiverRepresentation.VertexCompositionSeries.exists_vertexCompositionSeries_with_multiplicity
      Vα n order horder α basis
  exact ⟨s, hlen, fun i => (hmult i).trans
    (auxiliaryVertexValue_eq_of_fin_basis basis i).symm⟩

end RepresentationTheory.Quiver.Auxiliary

/-- Alias for the arrow-map coboundary. -/
alias _root_.RepresentationTheory.Quiver.Auxiliary.Auxiliary.statement013184 := _root_.RepresentationTheory.Quiver.Auxiliary.auxiliaryElidedDefinition
