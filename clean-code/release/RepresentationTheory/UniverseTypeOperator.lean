/-
Copyright (c) 2026 mathlib-initiative. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: mathlib-initiative
-/

import Mathlib.CategoryTheory.Category.Basic
import RepresentationTheory.Alignment.Attribute

/-!
# Category structures

The category structure used in Definition 7.1.1, via Mathlib's standard interface.
-/

namespace RepresentationTheory.UniverseTypeOperator

/-- A category structure on the object type C: morphisms, identities, composition and their laws. This is an alias for Mathlib's Category. -/
@[source_ref "Chapter7/Definition7.1.1" (role := supporting)]
abbrev TypeOperator (C : Type*) := CategoryTheory.Category C

end RepresentationTheory.UniverseTypeOperator
