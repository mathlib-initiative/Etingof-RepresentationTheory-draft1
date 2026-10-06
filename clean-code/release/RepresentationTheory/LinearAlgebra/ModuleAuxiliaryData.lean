/-
Copyright (c) 2026 mathlib-initiative. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Kim Morrison
-/
import Mathlib.LinearAlgebra.Span.Basic
import RepresentationTheory.Alignment.Attribute

/-!
# Subrepresentations of a module
-/

namespace RepresentationTheory.LinearAlgebra.ModuleAuxiliaryData

/-- Submodules of an `A`-module: additive subgroups closed under the `A`-action. -/
@[source_ref "Chapter2/Discussion_2.1_overview/Derived6" (role := supporting),
  source_ref "Chapter2/Definition2.3.4" (role := supporting)]
abbrev ModuleAuxiliaryData (A : Type*) (V : Type*) [Ring A] [AddCommGroup V]
    [Module A V] :=
  Submodule A V

/-- The zero subrepresentation, the bottom element of the submodule lattice. -/
@[source_ref "Chapter2/Definition2.3.4" (role := supporting)]
abbrev moduleAuxiliaryData' (A : Type*) (V : Type*) [Ring A] [AddCommGroup V]
    [Module A V] : ModuleAuxiliaryData A V :=
  ⊥

/-- The whole representation, the top element of the submodule lattice. -/
@[source_ref "Chapter2/Definition2.3.4" (role := supporting)]
abbrev moduleAuxiliaryData (A : Type*) (V : Type*) [Ring A] [AddCommGroup V]
    [Module A V] : ModuleAuxiliaryData A V :=
  ⊤

end RepresentationTheory.LinearAlgebra.ModuleAuxiliaryData
