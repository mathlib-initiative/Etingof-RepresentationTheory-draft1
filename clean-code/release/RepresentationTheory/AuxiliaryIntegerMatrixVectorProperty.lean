/-
Copyright (c) 2026 mathlib-initiative. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: mathlib-initiative
-/
import Mathlib
import RepresentationTheory.Alignment.Attribute

/-!
# Roots of the Cartan lattice

An integral root is a nonzero integer vector of Cartan norm two.
-/

/-- An integral root: a nonzero vector `x` with `xᵀ(2I - adj)x = 2`. The definition itself does not assume that the adjacency is Dynkin. -/
@[source_ref "Chapter6/Definition6.4.3" (role := supporting)]
def RepresentationTheory.AuxiliaryIntegerMatrixVectorProperty.IsAuxiliaryForMatrix (n : ℕ)
    (adj : Matrix (Fin n) (Fin n) ℤ) (x : Fin n → ℤ) : Prop :=
  x ≠ 0 ∧ dotProduct x ((2 • (1 : Matrix (Fin n) (Fin n) ℤ) - adj).mulVec x) = 2
