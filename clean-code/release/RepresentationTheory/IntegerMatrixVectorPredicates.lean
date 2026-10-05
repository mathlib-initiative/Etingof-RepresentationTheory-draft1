/-
Copyright (c) 2026 mathlib-initiative. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: mathlib-initiative
-/

import RepresentationTheory.AuxiliaryIntegerMatrixVectorProperty
import RepresentationTheory.Alignment.Attribute

/-!
# Integer Matrix-Vector Predicates

Auxiliary predicates on square integer matrices and integer vectors with matching finite indices.
-/

/-- A positive root: a nonzero integer vector of Cartan norm two with all coordinates nonnegative. -/
@[source_ref "Chapter6/Definition6.4.7" (role := supporting)]
def RepresentationTheory.IntegerMatrixVectorPredicates.integerMatrixVectorCondition
    (n : ℕ) (adj : Matrix (Fin n) (Fin n) ℤ) (x : Fin n → ℤ) : Prop :=
  RepresentationTheory.AuxiliaryIntegerMatrixVectorProperty.IsAuxiliaryForMatrix n adj x ∧
    ∀ i, 0 ≤ x i

/-- A negative root: a nonzero integer vector of Cartan norm two with all coordinates nonpositive. -/
@[source_ref "Chapter6/Definition6.4.7" (role := supporting)]
def RepresentationTheory.IntegerMatrixVectorPredicates.integerMatrixVectorPredicate
    (n : ℕ) (adj : Matrix (Fin n) (Fin n) ℤ) (x : Fin n → ℤ) : Prop :=
  RepresentationTheory.AuxiliaryIntegerMatrixVectorProperty.IsAuxiliaryForMatrix n adj x ∧
    ∀ i, x i ≤ 0
