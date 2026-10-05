/-
Copyright (c) 2026 American Mathematical Society. All rights reserved.
-/

import VersoManual
import RepresentationTheory

open Verso.Genre Manual

namespace IntroductionToRepresentationTheoryVerso.Content.Chapter9.Definition943

#doc (Manual) "Left and right global dimension" =>

# Left and right global dimension
%%%
tag := "Chapter9/Definition9.4.3"
number := false
%%%

*Definition 9.4.3.* One says that a ring $`A` has left (respectively, right) *homological dimension* $`\leq d` if every left (respectively, right) $`A`-module $`M` has projective dimension $`\leq d`. The homological dimension of $`A` is exactly $`d` if it is $`\leq d` but not $`\leq d - 1`. If such a $`d` does not exist, one says that $`A` has infinite homological dimension.

## Formalization
%%%
tag := "Chapter9/Definition9.4.3/formalization"
number := false
%%%

### Primary declarations

{Manual.docstring RepresentationTheory.Auxiliary.RingData.auxiliaryRingENatInvariant}

{Manual.docstring RepresentationTheory.Auxiliary.RingData.auxiliaryRingENatInvariantAux}

{Manual.docstring RepresentationTheory.Auxiliary.RingData.auxiliaryRingENatInvariantThird}

### Supporting declarations

{Manual.docstring RepresentationTheory.Auxiliary.RingData.auxiliaryRingENatInvariantThird_opposite}

{Manual.docstring RepresentationTheory.Auxiliary.RingData.auxiliaryRingNatProperty}

{Manual.docstring RepresentationTheory.Auxiliary.RingData.auxiliaryRingNatPropertyAux}

{Manual.docstring RepresentationTheory.Auxiliary.RingData.auxiliaryRingNatPropertyThird}

{Manual.docstring RepresentationTheory.Auxiliary.RingData.auxiliaryRingNatPropertyThird_opposite_iff}
