/-
Copyright (c) 2026 mathlib-initiative. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: mathlib-initiative
-/
import Mathlib.CategoryTheory.Preadditive.Projective.Resolution
import RepresentationTheory.Alignment.Attribute

namespace RepresentationTheory.CategoryTheory.Abelian.ObjectData

/-- A projective resolution of X: a chain complex of projective objects augmented by a quasi-isomorphism to X in degree zero. -/
@[source_ref "Chapter8/Definition8.2.1" (role := supporting)]
abbrev AbelianCategoryObjectData {C : Type*} [CategoryTheory.Category C]
    [CategoryTheory.Abelian C] (X : C) :=
  CategoryTheory.ProjectiveResolution X

end RepresentationTheory.CategoryTheory.Abelian.ObjectData
