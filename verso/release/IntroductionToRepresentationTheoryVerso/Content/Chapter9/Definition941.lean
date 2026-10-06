/-
Copyright (c) 2026 American Mathematical Society. All rights reserved.
-/

import VersoManual
import RepresentationTheory

open Verso.Genre Manual

namespace IntroductionToRepresentationTheoryVerso.Content.Chapter9.Definition941

#doc (Manual) "Projective dimension" =>

# Projective dimension
%%%
tag := "Chapter9/Definition9.4.1"
number := false
%%%

*Definition 9.4.1.* The *projective dimension* $`\operatorname{pd}(M)` of $`M` is the length of the shortest finite projective resolution of $`M` (where we agree that the length of $`0 \to P_d \to \cdots \to P_0` is $`d`). If a finite projective resolution of $`M` does not exist, then the projective dimension of $`M` is infinite.

For instance, the projective modules are the modules of projective dimension 0.

## Formalization
%%%
tag := "Chapter9/Definition9.4.1/formalization"
number := false
%%%

### Primary declarations

{Manual.docstring RepresentationTheory.ProjectiveDimension.projectiveDimension}

### Supporting declarations

{Manual.docstring RepresentationTheory.ProjectiveDimension.projectiveDimensionAux}

{Manual.docstring RepresentationTheory.ProjectiveDimension.projectiveDimension_eq_projectiveDimensionAux}

{Manual.docstring RepresentationTheory.ProjectiveDimension.projectiveDimension_eq_zero_iff_projective}

{Manual.docstring RepresentationTheory.ProjectiveDimension.projectiveDimension_eq_zero_of_isZero}

{Manual.docstring RepresentationTheory.ProjectiveDimension.projectiveDimension_le_iff}

{Manual.docstring RepresentationTheory.ProjectiveDimension.zero_le_projectiveDimension}

{Manual.docstring RepresentationTheory.ProjectiveDimension.zero_le_projectiveDimensionAux}
