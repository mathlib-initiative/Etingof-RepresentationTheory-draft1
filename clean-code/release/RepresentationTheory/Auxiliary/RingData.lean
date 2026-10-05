/-
Copyright (c) 2026 mathlib-initiative. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: mathlib-initiative
-/

import Mathlib.CategoryTheory.Abelian.Projective.Dimension
import Mathlib.Algebra.Category.ModuleCat.Abelian
import Mathlib.Algebra.Ring.Opposite
import RepresentationTheory.Alignment.Attribute

universe u

namespace RepresentationTheory.Auxiliary.RingData

/-- Every left module has dimension at most d. -/
def auxiliaryRingNatProperty (R : Type u) [Ring R] (d : ℕ) : Prop :=
  ∀ (M : ModuleCat.{u} R), CategoryTheory.HasProjectiveDimensionLE M d

/-- Left global dimension. -/
noncomputable def auxiliaryRingENatInvariant (R : Type u) [Ring R] : ℕ∞ :=
  ⨅ (d : ℕ) (_ : auxiliaryRingNatProperty R d), (d : ℕ∞)

/-- A second auxiliary property of a ring indexed by a natural number. -/
abbrev auxiliaryRingNatPropertyAux (R : Type u) [Ring R] (d : ℕ) : Prop :=
  auxiliaryRingNatProperty R d

/-- A second auxiliary extended-natural-valued invariant of a ring. -/
noncomputable abbrev auxiliaryRingENatInvariantAux (R : Type u) [Ring R] : ℕ∞ :=
  auxiliaryRingENatInvariant R

/-- A third auxiliary property of a ring indexed by a natural number. -/
def auxiliaryRingNatPropertyThird (R : Type u) [Ring R] (d : ℕ) : Prop :=
  auxiliaryRingNatProperty Rᵐᵒᵖ d

/-- Right global dimension. -/
noncomputable def auxiliaryRingENatInvariantThird (R : Type u) [Ring R] : ℕ∞ :=
  auxiliaryRingENatInvariant Rᵐᵒᵖ

/-- The third auxiliary natural-number-indexed ring property is equivalent to the second one for
the opposite ring. -/
@[simp]
theorem auxiliaryRingNatPropertyThird_opposite_iff (R : Type u) [Ring R] (d : ℕ) :
    auxiliaryRingNatPropertyThird R d ↔ auxiliaryRingNatPropertyAux Rᵐᵒᵖ d :=
  Iff.rfl

/-- The third auxiliary extended-natural-valued ring invariant equals the second one for the
opposite ring. -/
@[simp]
theorem auxiliaryRingENatInvariantThird_opposite (R : Type u) [Ring R] :
    auxiliaryRingENatInvariantThird R = auxiliaryRingENatInvariantAux Rᵐᵒᵖ :=
  rfl

end RepresentationTheory.Auxiliary.RingData

-- Recovered exact-module book alignment.
attribute [source_ref "Chapter9/Definition9.4.3" (role := primary)] _root_.RepresentationTheory.Auxiliary.RingData.auxiliaryRingENatInvariant
attribute [source_ref "Chapter9/Definition9.4.3" (role := primary)] _root_.RepresentationTheory.Auxiliary.RingData.auxiliaryRingENatInvariantAux
attribute [source_ref "Chapter9/Definition9.4.3" (role := primary)] _root_.RepresentationTheory.Auxiliary.RingData.auxiliaryRingENatInvariantThird
attribute [source_ref "Chapter9/Definition9.4.3" (role := supporting)] _root_.RepresentationTheory.Auxiliary.RingData.auxiliaryRingENatInvariantThird_opposite
attribute [source_ref "Chapter9/Definition9.4.3" (role := supporting)] _root_.RepresentationTheory.Auxiliary.RingData.auxiliaryRingNatProperty
attribute [source_ref "Chapter9/Definition9.4.3" (role := supporting)] _root_.RepresentationTheory.Auxiliary.RingData.auxiliaryRingNatPropertyAux
attribute [source_ref "Chapter9/Definition9.4.3" (role := supporting)] _root_.RepresentationTheory.Auxiliary.RingData.auxiliaryRingNatPropertyThird
attribute [source_ref "Chapter9/Definition9.4.3" (role := supporting)] _root_.RepresentationTheory.Auxiliary.RingData.auxiliaryRingNatPropertyThird_opposite_iff
