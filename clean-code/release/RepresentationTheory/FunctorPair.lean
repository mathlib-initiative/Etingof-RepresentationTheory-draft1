/-
Copyright (c) 2026 mathlib-initiative. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: mathlib-initiative
-/

import Mathlib.CategoryTheory.Adjunction.Basic
import RepresentationTheory.Alignment.Attribute

/-!
# Adjunctions between functors

The unit, counit and triangle laws relating a left adjoint and a right adjoint.
-/

namespace RepresentationTheory.FunctorPair

/-- An adjunction F ⊣ G, with natural unit and counit and their triangle identities. Its Hom equivalence identifies maps F(X) → Y with maps X → G(Y). -/
@[source_ref "Chapter7/Definition7.6.1" (role := supporting)]
abbrev Data {C : Type*} {D : Type*} [CategoryTheory.Category C]
    [CategoryTheory.Category D] (F : CategoryTheory.Functor C D)
    (G : CategoryTheory.Functor D C) := CategoryTheory.Adjunction F G

end RepresentationTheory.FunctorPair
