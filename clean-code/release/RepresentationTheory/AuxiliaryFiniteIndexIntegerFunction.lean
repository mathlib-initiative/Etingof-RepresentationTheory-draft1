/-
Copyright (c) 2026 mathlib-initiative. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: mathlib-initiative
-/
import Mathlib
import RepresentationTheory.Alignment.Attribute

/-!
# Coordinate simple roots

The coordinate vector `αᵢ` has value one at `i` and zero at every other vertex.
-/

/-- The simple coordinate vector `αᵢ`: one at vertex `i`, zero elsewhere. -/
@[source_ref "Chapter6/Definition6.4.5" (role := supporting)]
def RepresentationTheory.AuxiliaryFiniteIndexIntegerFunction.auxiliaryValue (n : ℕ) (i : Fin n) :
    Fin n → ℤ :=
  Pi.single i 1
