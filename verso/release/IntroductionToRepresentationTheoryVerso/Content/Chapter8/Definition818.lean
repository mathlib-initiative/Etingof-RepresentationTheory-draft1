/-
Copyright (c) 2026 American Mathematical Society. All rights reserved.
-/

import VersoManual
import RepresentationTheory

open Verso.Genre Manual

namespace IntroductionToRepresentationTheoryVerso.Content.Chapter8.Definition818

#doc (Manual) "Projectivity and injectivity through Hom" =>

# Projectivity and injectivity through Hom
%%%
tag := "Chapter8/Definition8.1.8"
number := false
%%%

*Definition 8.1.8.* A *projective object* in an abelian category $`\mathcal{C}` is an object $`P` such that the functor $`\operatorname{Hom}_\mathcal{C}(P, ?)` is exact.

An *injective object* in an abelian category $`\mathcal{C}` is an object $`I` such that the functor $`\operatorname{Hom}_\mathcal{C}(?, I)` is exact.

## Formalization
%%%
tag := "Chapter8/Definition8.1.8/formalization"
number := false
%%%

### Primary declarations

{Manual.docstring RepresentationTheory.CategoryTheory.Abelian.YonedaFiniteLimitColimitPreservation.coyonedaObjectProperty_iff}

{Manual.docstring RepresentationTheory.CategoryTheory.Abelian.YonedaFiniteLimitColimitPreservation.yonedaObjectProperty_iff}

### Supporting declarations

{Manual.docstring RepresentationTheory.CategoryTheory.Abelian.YonedaFiniteLimitColimitPreservation.coyonedaObjectProperty}

{Manual.docstring RepresentationTheory.CategoryTheory.Abelian.YonedaFiniteLimitColimitPreservation.yonedaObjectProperty}
