/-
Copyright (c) 2026 mathlib-initiative. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Kim Morrison
-/

import Mathlib.GroupTheory.GroupAction.Basic
import RepresentationTheory.Alignment.Attribute

/-! # Module predicates -/

namespace RepresentationTheory.LinearAlgebra.ModulePredicates

/-- Faithfulness of the representation: two algebra elements are equal whenever they act identically on every vector. This is Mathlib's FaithfulSMul predicate. -/
@[source_ref "Chapter2/Definition2.7.3" (role := supporting),
  source_ref "Chapter2/Remark2.7.2/Derived2" (role := supporting)]
abbrev IsFaithfulRepresentation (A : Type*) (V : Type*) [Ring A] [AddCommGroup V]
    [Module A V] :=
  FaithfulSMul A V

end RepresentationTheory.LinearAlgebra.ModulePredicates
