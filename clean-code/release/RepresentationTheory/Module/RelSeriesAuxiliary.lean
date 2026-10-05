/-
Copyright (c) 2026 mathlib-initiative. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: mathlib-initiative
-/

import Mathlib.Order.RelSeries
import Mathlib.Algebra.Module.Submodule.Lattice
import RepresentationTheory.Alignment.Attribute

/-- A finite strictly increasing chain of A-submodules of V, starting at zero and ending at V. -/
structure RepresentationTheory.Module.Filtration.FiniteFiltration (A : Type*) (V : Type*)
    [Ring A] [AddCommGroup V] [Module A V] where

  /-- The finite chain of submodules, with every consecutive inclusion strict. -/
  toRelSeries : RelSeries {p : Submodule A V × Submodule A V | p.1 < p.2}

  /-- The first submodule of the filtration is zero. -/
  toRelSeries_head : toRelSeries.head = ⊥

  /-- The last submodule of the filtration is the whole module. -/
  toRelSeries_last : toRelSeries.last = ⊤

attribute [source_ref "Chapter3/Definition3.4.1" (role := primary)]
  RepresentationTheory.Module.Filtration.FiniteFiltration.toRelSeries
attribute [source_ref "Chapter3/Definition3.4.1" (role := primary)]
  RepresentationTheory.Module.Filtration.FiniteFiltration.toRelSeries_head
attribute [source_ref "Chapter3/Definition3.4.1" (role := primary)]
  RepresentationTheory.Module.Filtration.FiniteFiltration.toRelSeries_last
