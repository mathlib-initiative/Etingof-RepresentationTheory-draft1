/-
Copyright (c) 2026 mathlib-initiative. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: mathlib-initiative
-/

import Mathlib.CategoryTheory.Limits.Preserves.Finite
import RepresentationTheory.Alignment.Attribute

/-!
# Finite-limit and finite-colimit preservation

For additive functors between abelian categories these express left exactness, right exactness
and exactness. The underlying preservation predicates also make sense in general categories.
-/

namespace RepresentationTheory.FunctorPredicateLogic

/-- Preservation of finite limits; left exactness for additive functors between abelian categories. -/
@[source_ref "Chapter7/Definition7.9.3" (role := supporting)]
abbrev Left {C : Type*} {D : Type*} [CategoryTheory.Category C]
    [CategoryTheory.Category D] (F : CategoryTheory.Functor C D) :=
  CategoryTheory.Limits.PreservesFiniteLimits F

/-- Preservation of finite colimits; right exactness for additive functors between abelian categories. -/
@[source_ref "Chapter7/Definition7.9.3" (role := supporting)]
abbrev Right {C : Type*} {D : Type*} [CategoryTheory.Category C]
    [CategoryTheory.Category D] (F : CategoryTheory.Functor C D) :=
  CategoryTheory.Limits.PreservesFiniteColimits F

/-- Preservation of finite limits and finite colimits; exactness in the additive abelian setting. -/
@[source_ref "Chapter7/Definition7.9.3" (role := supporting),
  source_ref "Chapter7/Introduction_7.9" (role := supporting)]
def Conjunction {C : Type*} {D : Type*} [CategoryTheory.Category C]
    [CategoryTheory.Category D] (F : CategoryTheory.Functor C D) : Prop :=
  Left F ∧ Right F

variable {C : Type*} {D : Type*} [CategoryTheory.Category C]
  [CategoryTheory.Category D] {F : CategoryTheory.Functor C D}

/-- The conjunction predicate holds exactly when its left- and right-hand predicates both hold. -/
@[source_ref "Chapter7/Definition7.9.3" (role := supporting)]
theorem conjunction_iff : Conjunction F ↔ Left F ∧ Right F :=
  Iff.rfl

/-- The conjunction predicate implies its left-hand predicate. -/
theorem Conjunction.left (h : Conjunction F) : Left F :=
  h.1

/-- The conjunction predicate implies its right-hand predicate. -/
theorem Conjunction.right (h : Conjunction F) : Right F :=
  h.2

/-- The left- and right-hand predicates imply the conjunction predicate. -/
theorem Conjunction.of_left_right (hL : Left F) (hR : Right F) : Conjunction F :=
  ⟨hL, hR⟩

end RepresentationTheory.FunctorPredicateLogic
