/-
Copyright (c) 2026 American Mathematical Society. All rights reserved.
-/

import VersoManual
import RepresentationTheory

open Verso.Genre Manual

namespace IntroductionToRepresentationTheoryVerso.Content.Chapter9.Theorem964

#doc (Manual) "Finite abelian categories as module categories" =>

# Finite abelian categories as module categories
%%%
tag := "Chapter9/Theorem9.6.4"
number := false
%%%

*Theorem 9.6.4.* _The functor $`F` is an equivalence of categories. Thus, any finite abelian category over a field $`k` is equivalent to the category of modules over a finite dimensional $`k`-algebra._

The proof of Theorem 9.6.4 is contained in the following problem.

## Formalization
%%%
tag := "Chapter9/Theorem9.6.4/formalization"
number := false
%%%

### Primary declarations

{Manual.docstring RepresentationTheory.CategoryTheory.Preadditive.FGModuleEquivalence.fgModuleFunctor_isEquivalence}

{Manual.docstring RepresentationTheory.CategoryTheory.Preadditive.FGModuleEquivalence.fgModuleFunctor_isEquivalence_of_noetherian}

{Manual.docstring RepresentationTheory.CategoryTheory.Preadditive.FGModuleEquivalence.nonempty_fgModuleEquivalence}

{Manual.docstring RepresentationTheory.CategoryTheory.Preadditive.FGModuleEquivalence.nonempty_fgModuleEquivalence_of_noetherian}

### Supporting declarations

{Manual.docstring RepresentationTheory.CategoryTheory.Preadditive.FGModuleEquivalence.opEnd_isNoetherian}

{Manual.docstring RepresentationTheory.CategoryTheory.ProjectiveEpiProperties.HasProjectiveEpiWitnesses.fgModuleFunctor}

{Manual.docstring RepresentationTheory.CategoryTheory.ProjectiveEpiProperties.HasProjectiveEpiWitnesses.fgModuleFunctor_essentiallySurjective}

{Manual.docstring RepresentationTheory.CategoryTheory.ProjectiveEpiProperties.HasProjectiveEpiWitnesses.hasAssociatedProperty}

{Manual.docstring RepresentationTheory.CategoryTheory.ProjectiveEpiProperties.HasProjectiveEpiWitnesses.hom_finite}

{Manual.docstring RepresentationTheory.CategoryTheory.ProjectiveEpiProperties.HasProjectiveEpiWitnesses.isSeparator}

{Manual.docstring RepresentationTheory.CategoryTheory.ProjectiveEpiProperties.HasProjectiveEpiWitnesses.preadditiveCoyonedaObj_faithful}

{Manual.docstring RepresentationTheory.CategoryTheory.ProjectiveEpiProperties.HasProjectiveEpiWitnesses.preadditiveCoyonedaObj_full}

{Manual.docstring RepresentationTheory.CategoryTheory.SubobjectFiniteDimensional.SubobjectFiniteDimensional.hasFiniteBiproducts}
