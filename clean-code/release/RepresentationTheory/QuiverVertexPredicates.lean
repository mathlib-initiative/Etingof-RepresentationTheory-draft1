/-
Copyright (c) 2026 mathlib-initiative. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: mathlib-initiative
-/

import Mathlib
import RepresentationTheory.Alignment.Attribute

/-!
# Quiver Vertex Predicates

Sinks have no outgoing arrows; sources have no incoming arrows.
-/

/-- A sink: there are no arrows from this vertex to any vertex. -/
@[source_ref "Chapter6/Definition6.6.1" (role := supporting)]
def RepresentationTheory.QuiverVertexPredicates.vertexProperty
    (V : Type*) [Quiver V] (i : V) : Prop :=
  ∀ (j : V), IsEmpty (i ⟶ j)

/-- A source: there are no arrows from any vertex to this vertex. -/
@[source_ref "Chapter6/Definition6.6.1" (role := supporting)]
def RepresentationTheory.QuiverVertexPredicates.vertexCondition
    (V : Type*) [Quiver V] (i : V) : Prop :=
  ∀ (j : V), IsEmpty (j ⟶ i)
