/-
Copyright (c) 2026 American Mathematical Society. All rights reserved.
-/

import VersoManual
import RepresentationTheory

open Verso.Genre Manual

namespace IntroductionToRepresentationTheoryVerso.Content.Chapter9.Definition962

#doc (Manual) "Projective generators" =>

# Projective generators
%%%
tag := "Chapter9/Definition9.6.2"
number := false
%%%

*Definition 9.6.2.* An object $`P` of an abelian category $`\mathcal{C}` is said to be a *projective generator* (or *progenerator*) if it is projective and every object is a quotient of a multiple of $`P`.
For example, in the category of modules over a ring $`A`, the free module $`A` is a projective generator.

## Formalization
%%%
tag := "Chapter9/Definition9.6.2/formalization"
number := false
%%%

### Primary declarations

{Manual.docstring RepresentationTheory.CategoryTheory.ProjectiveEpiProperties.HasProjectiveEpiWitnesses}

{Manual.docstring RepresentationTheory.CategoryTheory.ProjectiveEpiProperties.IsProjectiveEpiSigmaDesc}

### Supporting declarations

{Manual.docstring RepresentationTheory.CategoryTheory.ProjectiveEpiProperties.HasProjectiveEpiWitnesses.exists_epi}

{Manual.docstring RepresentationTheory.CategoryTheory.ProjectiveEpiProperties.HasProjectiveEpiWitnesses.toProjective}

{Manual.docstring RepresentationTheory.CategoryTheory.ProjectiveEpiProperties.IsProjectiveEpiSigmaDesc.iff_projective_and_epi_sigma_desc}

{Manual.docstring RepresentationTheory.CategoryTheory.ProjectiveEpiProperties.IsProjectiveEpiSigmaDesc.isSeparator}

{Manual.docstring RepresentationTheory.CategoryTheory.ProjectiveEpiProperties.IsProjectiveEpiSigmaDesc.projective}
