/-
Copyright (c) 2026 American Mathematical Society. All rights reserved.
-/

import VersoManual
import RepresentationTheory

open Verso.Genre Manual

namespace IntroductionToRepresentationTheoryVerso.Content.Chapter3.Remark386

#doc (Manual) "Krull-Schmidt for modules of finite length" =>

# Krull-Schmidt for modules of finite length
%%%
tag := "Chapter3/Remark3.8.6"
number := false
%%%
*Remark 3.8.6.* Thus, we see that, in general, the Krull-Schmidt theorem fails for infinite dimensional modules. However, it still holds for modules of *finite length*, i.e., modules $`M` such that any filtration of $`M` has length bounded above by a certain constant $`l = l(M)`.

## Formalization
%%%
tag := "Chapter3/Remark3.8.6/formalization"
number := false
%%%

### Primary declarations

{Manual.docstring RepresentationTheory.Algebra.Module.InternalFamilyDecomposition.exists_internalFamily}

{Manual.docstring RepresentationTheory.Algebra.Module.InternalFamilyDecomposition.internalFamily_unique_up_to_permutation}

### Supporting declarations

Declaration: Module.length

Alignment metadata: book-ref=Chapter3/Remark3.8.6/Derived2; role=supporting

Declaration: Order.LTSeries.length\_le\_krullDim

Alignment metadata: book-ref=Chapter3/Remark3.8.6/Derived2; role=supporting

{Manual.docstring RepresentationTheory.Analysis.ContinuousMap.StableModuleEquivalence.auxiliaryProperty_auxiliaryFunctionAlgebra}

{Manual.docstring RepresentationTheory.Analysis.ContinuousMap.StableModuleEquivalence.auxiliaryProperty_auxiliaryFunctionModule}

{Manual.docstring RepresentationTheory.Analysis.ContinuousMap.StableModuleEquivalence.isEmpty_linearEquiv_auxiliaryFunctionModule}

{Manual.docstring RepresentationTheory.Analysis.ContinuousMap.StableModuleEquivalence.nonempty_prod_linearEquiv}

Declaration: isFiniteLength\_iff\_isNoetherian\_isArtinian

Alignment metadata: book-ref=Chapter3/Remark3.8.6/Derived2; role=supporting
