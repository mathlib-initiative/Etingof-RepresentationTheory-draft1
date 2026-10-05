/-
Copyright (c) 2026 mathlib-initiative. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: mathlib-initiative
-/

import Mathlib.CategoryTheory.Abelian.Basic
import Mathlib.Algebra.Homology.ShortComplex.ShortExact
import RepresentationTheory.Alignment.Attribute

/-!
# Semisimple abelian categories

Semisimplicity means that every short exact sequence admits a splitting.
-/

open CategoryTheory

namespace RepresentationTheory.CategoryTheory.Abelian.CategoryProperties

/-- Semisimplicity of an abelian category: every short exact sequence admits a splitting. -/
@[source_ref "Chapter7/Definition7.9.4" (role := supporting)]
def AbelianCategoryProperty (C : Type*) [Category C] [Abelian C] : Prop :=
  ∀ (S : ShortComplex C), S.ShortExact → Nonempty S.Splitting

end RepresentationTheory.CategoryTheory.Abelian.CategoryProperties
