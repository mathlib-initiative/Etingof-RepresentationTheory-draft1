# Representation Theory in Lean

This Lean 4 and Mathlib library formalizes material from *Introduction to
Representation Theory* by Pavel Etingof, Oleg Golberg, Sebastian Hensel,
Tiankai Liu, Alex Schwendner, Dmitry Vaintrob, and Elena Yudovina (AMS,
2011; [catalogue entry](https://bookstore.ams.org/stml-59/)).

## Start reading

- [Finite-group characters and class functions](RepresentationTheory/FiniteGroup/ClassFunctions.lean)
- [Character column orthogonality](RepresentationTheory/FiniteGroup/CharacterColumnOrthogonality.lean)
- [Burnside's theorem and algebra density](RepresentationTheory/Representation/AlgebraDensity.lean)
- [Young diagrams and partition formulas](RepresentationTheory/YoungDiagram/PartitionFormulas.lean)
- [Morita equivalence](RepresentationTheory/MoritaEquivalence.lean)
- [Three-dimensional Lie algebras](RepresentationTheory/Algebra/Lie/ThreeDimensional.lean)
- [Finite simply-laced Dynkin diagrams](RepresentationTheory/DynkinDiagram/FiniteSimplyLaced.lean)

The [root module](RepresentationTheory.lean) gives the complete import graph.

## Book cross-reference

The Lean code and proofs were written independently and do not quote or
reproduce the book's prose. Machine-readable `source_ref` metadata provides
scholarly cross-references to numbered results, discussions, introductions,
and section headings; these citations allow aspects of the book's numbering
and organization to be inferred.

[Read the aligned Verso
edition](https://mathlib-initiative.github.io/EtingofRepresentationTheory-verso-pages/),
which places the formalization beside the corresponding book text.

## Building

```text
lake update
lake exe cache get
lake build
```

## License

Copyright 2026 mathlib-initiative. Licensed under the
[Apache License, Version 2.0](LICENSE); see [NOTICE](NOTICE).
