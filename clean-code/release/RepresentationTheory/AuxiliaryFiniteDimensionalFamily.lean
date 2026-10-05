/-
Copyright (c) 2026 mathlib-initiative. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: mathlib-initiative
-/

import Mathlib
import RepresentationTheory.Alignment.Attribute

/-!
# Dimension vectors

Record the dimension of each vector space in a finite family.
-/

/-- The dimension vector of a finite-dimensional family: at vertex `v`, the value is `Module.finrank k (spaces v)`. -/
@[source_ref "Chapter6/Definition6.5.1" (role := supporting)]
noncomputable def RepresentationTheory.AuxiliaryFiniteDimensionalFamily.auxiliaryNatValue
    {V : Type*} [Fintype V] (k : Type*)
    [Field k] (spaces : V → Type*)
    [∀ v, AddCommGroup (spaces v)] [∀ v, Module k (spaces v)]
    [∀ v, FiniteDimensional k (spaces v)] :
    V → ℕ :=
  fun v => Module.finrank k (spaces v)
