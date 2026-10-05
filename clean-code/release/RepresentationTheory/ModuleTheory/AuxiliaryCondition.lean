/-
Copyright (c) 2026 mathlib-initiative. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: mathlib-initiative
-/

import Mathlib.RingTheory.SimpleModule.Basic
import RepresentationTheory.Alignment.Attribute

/-- Semisimplicity: every submodule has a complement, equivalently the module is a direct sum of simple modules. -/
@[source_ref "Chapter3/Definition3.1.1" (role := supporting)]
abbrev RepresentationTheory.ModuleTheory.Semisimplicity.IsSemisimple (A : Type*) (V : Type*)
    [Ring A] [AddCommGroup V] [Module A V] :=
  IsSemisimpleModule A V
