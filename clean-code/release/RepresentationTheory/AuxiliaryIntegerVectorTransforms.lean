/-
Copyright (c) 2026 mathlib-initiative. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: mathlib-initiative
-/
import Mathlib
import RepresentationTheory.Alignment.Attribute

/-!
# Integral root reflections

Define `v ↦ v - B(v, α)α` and its specialization to coordinate simple roots.
-/

/-- The formula `v ↦ v - (vᵀAα)α`. For a symmetric Cartan matrix and a root of norm two, this is the root reflection. No root or positivity hypothesis is built into this definition. -/
@[source_ref "Chapter6/Definition6.4.10" (role := supporting)]
def RepresentationTheory.AuxiliaryIntegerVectorTransforms.auxiliaryVectorTransform (n : ℕ)
    (A : Matrix (Fin n) (Fin n) ℤ) (α : Fin n → ℤ) (v : Fin n → ℤ) : Fin n → ℤ :=
  v - (dotProduct v (A.mulVec α)) • α

/-- The reflection formula specialized to the coordinate vector `αᵢ`. The argument `A` is the Cartan matrix, not the adjacency matrix. -/
@[source_ref "Chapter6/Definition6.4.10" (role := supporting)]
def RepresentationTheory.AuxiliaryIntegerVectorTransforms.auxiliaryCoordinateTransform (n : ℕ)
    (A : Matrix (Fin n) (Fin n) ℤ) (i : Fin n) : (Fin n → ℤ) → (Fin n → ℤ) :=
  RepresentationTheory.AuxiliaryIntegerVectorTransforms.auxiliaryVectorTransform n A
    (Pi.single i 1)
