/-
Copyright (c) 2026 American Mathematical Society. All rights reserved.
-/

import VersoManual
import RepresentationTheory

open Verso.Genre Manual

namespace IntroductionToRepresentationTheoryVerso.Content.Chapter9.Definition931

#doc (Manual) "Definition and entries of the Cartan matrix" =>

# Definition and entries of the Cartan matrix
%%%
tag := "Chapter9/Definition9.3.1"
number := false
%%%

*Definition 9.3.1.* The matrix $`C = (c_{ij})` is called the *Cartan matrix* of $`A`.

Obviously, the Cartan matrix of $`A` is a matrix with nonnegative entries, whose diagonal entries are positive.

## Formalization
%%%
tag := "Chapter9/Definition9.3.1/formalization"
number := false
%%%

### Primary declarations

{Manual.docstring RepresentationTheory.ModuleFamilyNatMatrix.ModuleFamilyNatMatrix.matrix}

### Supporting declarations

{Manual.docstring RepresentationTheory.ModuleFamilyNatMatrix.ModuleFamilyNatMatrix.matrix_diagonal_pos}

{Manual.docstring RepresentationTheory.ModuleFamilyNatMatrix.ModuleFamilyNatMatrix.matrix_diagonal_pos_of_auxiliary}

{Manual.docstring RepresentationTheory.ModuleFamilyNatMatrix.ModuleFamilyNatMatrix.matrix_natCast_diagonal_pos}

{Manual.docstring RepresentationTheory.ModuleFamilyNatMatrix.ModuleFamilyNatMatrix.matrix_natCast_nonneg}

{Manual.docstring RepresentationTheory.ModuleFamilyNatMatrix.ModuleFamilyNatMatrix.matrix_nonneg}
