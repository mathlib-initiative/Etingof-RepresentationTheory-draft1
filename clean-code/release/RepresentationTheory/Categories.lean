/-
Copyright (c) 2026 mathlib-initiative. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: mathlib-initiative
-/

import Mathlib.CategoryTheory.Equivalence
import RepresentationTheory.Alignment.Attribute

/-!
# Equivalences of categories

Quasi-inverse functors with coherent natural unit and counit isomorphisms.
-/

namespace RepresentationTheory.Categories

/-- Equivalences between C and D, with a quasi-inverse, natural unit and counit isomorphisms and their triangle compatibility law. -/
@[source_ref "Chapter7/Definition7.4.1" (role := supporting)]
abbrev ParameterizedType (C : Type*) (D : Type*) [CategoryTheory.Category C]
    [CategoryTheory.Category D] := CategoryTheory.Equivalence C D

end RepresentationTheory.Categories
