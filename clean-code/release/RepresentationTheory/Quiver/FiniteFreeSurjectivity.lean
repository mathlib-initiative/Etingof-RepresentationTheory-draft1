/-
Copyright (c) 2026 mathlib-initiative. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: mathlib-initiative
-/

import RepresentationTheory.Surjective
import RepresentationTheory.Alignment.Attribute

namespace RepresentationTheory.Quiver.FiniteFreeSurjectivity

/-- At a sink with surjective incoming map, cokernel reflection after kernel reflection recovers an isomorphic representation. -/
@[source_ref "Chapter6/Proposition6.6.6" (role := supporting)]
alias nonemptyAuxiliaryOfSurjective :=
  RepresentationTheory.Surjective.nonempty_of_surjective

end RepresentationTheory.Quiver.FiniteFreeSurjectivity
