/-
Copyright (c) 2026 mathlib-initiative. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: mathlib-initiative
-/
import Mathlib.Algebra.Module.Projective
import RepresentationTheory.Alignment.Attribute

namespace RepresentationTheory.Algebra.Module.Property

/-- Projectivity of a module: maps out of it lift across surjective linear maps. -/
@[source_ref "Chapter8/Definition8.1.2" (role := supporting)]
abbrev ModuleProperty (R : Type*) (M : Type*) [Ring R] [AddCommGroup M]
    [Module R M] :=
  Module.Projective R M

end RepresentationTheory.Algebra.Module.Property
