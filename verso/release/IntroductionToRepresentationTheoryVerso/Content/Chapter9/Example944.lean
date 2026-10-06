/-
Copyright (c) 2026 American Mathematical Society. All rights reserved.
-/

import VersoManual
import RepresentationTheory

open Verso.Genre Manual

namespace IntroductionToRepresentationTheoryVerso.Content.Chapter9.Example944

#doc (Manual) "Global dimension of a polynomial algebra" =>

# Global dimension of a polynomial algebra
%%%
tag := "Chapter9/Example9.4.4"
number := false
%%%

*Example 9.4.4.* By the Hilbert syzygies theorem (see Problem 8.2.10(iv)), the homological dimension of the polynomial algebra $`k[x_1, \ldots, x_n]` is $`n`.

## Formalization
%%%
tag := "Chapter9/Example9.4.4/formalization"
number := false
%%%

### Primary declarations

{Manual.docstring RepresentationTheory.Auxiliary.RingAndCategoryProperties.Auxiliary.mvPolynomial_value_eq_natCast}

### Supporting declarations

{Manual.docstring RepresentationTheory.Auxiliary.RingAndCategoryProperties.Auxiliary.property_mvPolynomial_variable_count}

{Manual.docstring RepresentationTheory.Auxiliary.RingAndCategoryProperties.Auxiliary.property_of_ringEquiv}

{Manual.docstring RepresentationTheory.Auxiliary.RingAndCategoryProperties.Auxiliary.property_polynomial_succ}

{Manual.docstring RepresentationTheory.Auxiliary.RingAndCategoryProperties.Auxiliary.property_zero_of_isSemisimpleRing}

{Manual.docstring RepresentationTheory.Auxiliary.RingAndCategoryProperties.Auxiliary.variable_count_le_of_property}

{Manual.docstring RepresentationTheory.Auxiliary.RingAndCategoryProperties.CategoryTheory.HasProjectiveDimensionLT.ofEquivalence}
