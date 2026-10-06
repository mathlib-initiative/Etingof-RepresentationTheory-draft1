/-
Copyright (c) 2026 mathlib-initiative. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: mathlib-initiative
-/
import Mathlib.CategoryTheory.NatTrans
import RepresentationTheory.Alignment.Attribute

/-!
# Natural transformations

Compatible families of morphisms between the values of two functors.
-/

namespace RepresentationTheory.FunctorPairConstructions

/-- Natural transformations from F to G: a morphism at each object, compatible with every morphism of the source category. -/
@[source_ref "Chapter7/Definition7.3.1" (role := supporting)]
abbrev associatedType {C : Type*} {D : Type*} [CategoryTheory.Category C]
    [CategoryTheory.Category D] (F G : CategoryTheory.Functor C D) :=
  CategoryTheory.NatTrans F G

end RepresentationTheory.FunctorPairConstructions
