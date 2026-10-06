/-
Copyright (c) 2026 mathlib-initiative. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: mathlib-initiative
-/

import Mathlib.CategoryTheory.Functor.Basic
import RepresentationTheory.Alignment.Attribute

/-!
# Functors between categories

The object and arrow maps, with preservation laws, used in Definition 7.2.1.
-/

namespace RepresentationTheory.CategoryPair

/-- Functors from C to D, with object and morphism maps preserving identities and composition. This is an alias for Mathlib's Functor. -/
@[source_ref "Chapter7/Definition7.2.1" (role := supporting),
  source_ref "Chapter7/Introduction_7.2" (role := supporting)]
abbrev AssociatedType (C : Type*) (D : Type*) [CategoryTheory.Category C]
    [CategoryTheory.Category D] := CategoryTheory.Functor C D

end RepresentationTheory.CategoryPair
