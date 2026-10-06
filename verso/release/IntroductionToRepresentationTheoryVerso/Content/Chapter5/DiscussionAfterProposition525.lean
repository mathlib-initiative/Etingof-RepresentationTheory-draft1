/-
Copyright (c) 2026 American Mathematical Society. All rights reserved.
-/

import VersoManual
import RepresentationTheory

open Verso.Genre Manual

namespace IntroductionToRepresentationTheoryVerso.Content.Chapter5.DiscussionAfterProposition525

#doc (Manual) "Minimal polynomials and conjugates" =>

# Minimal polynomials and conjugates
%%%
tag := "Chapter5/Discussion_after_Proposition5.2.5"
number := false
%%%
Every algebraic number $`\alpha` has a *minimal polynomial* $`p(x)` which is the monic polynomial with rational coefficients of the smallest degree such that $`p(\alpha) = 0`. Any other polynomial $`q(x)` with rational coefficients such that $`q(\alpha) = 0` is divisible by $`p(x)`. Roots of $`p(x)` are called the *algebraic conjugates* of $`\alpha`; they are roots of any polynomial $`q` with rational coefficients such that $`q(\alpha) = 0`.

Note that any algebraic conjugate of an algebraic integer is obviously also an algebraic integer. Therefore, by the Vieta theorem, the minimal polynomial of an algebraic integer has integer coefficients.

Below we will need the following lemma:

## Formalization
%%%
tag := "Chapter5/Discussion_after_Proposition5.2.5/formalization"
number := false
%%%

### Supporting declarations

Declaration: IsConjRoot

Alignment metadata: book-ref=Chapter5/Discussion\_after\_Proposition5.2.5/Derived2; role=supporting

Declaration: IsConjRoot.aeval\_eq\_zero

Alignment metadata: book-ref=Chapter5/Discussion\_after\_Proposition5.2.5/Derived2; role=supporting

Declaration: IsConjRoot.isIntegral

Alignment metadata: book-ref=Chapter5/Discussion\_after\_Proposition5.2.5/Derived3; role=supporting

Declaration: minpoly

Alignment metadata: book-ref=Chapter5/Discussion\_after\_Proposition5.2.5; role=supporting

Declaration: minpoly.aeval

Alignment metadata: book-ref=Chapter5/Discussion\_after\_Proposition5.2.5; role=supporting

Declaration: minpoly.dvd

Alignment metadata: book-ref=Chapter5/Discussion\_after\_Proposition5.2.5; role=supporting

Alignment metadata: book-ref=Chapter5/Discussion\_after\_Proposition5.2.5/Derived2; role=supporting

Declaration: minpoly.isIntegrallyClosed\_eq\_field\_fractions'

Alignment metadata: book-ref=Chapter5/Discussion\_after\_Proposition5.2.5/Derived3; role=supporting

Declaration: minpoly.min

Alignment metadata: book-ref=Chapter5/Discussion\_after\_Proposition5.2.5; role=supporting

Declaration: minpoly.monic

Alignment metadata: book-ref=Chapter5/Discussion\_after\_Proposition5.2.5; role=supporting
