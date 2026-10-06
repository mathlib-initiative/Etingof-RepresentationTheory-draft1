/-
Copyright (c) 2026 American Mathematical Society. All rights reserved.
-/

import VersoManual
import RepresentationTheory

open Verso.Genre Manual

namespace IntroductionToRepresentationTheoryVerso.Content.Chapter6.TheoremDynkinClassification

#doc (Manual) "Finite Dynkin diagrams" =>

# Finite Dynkin diagrams
%%%
tag := "Chapter6/Theorem_Dynkin_classification"
number := false
%%%

*Theorem.* _$`\Gamma` is a Dynkin diagram if and only if it is one of the following graphs:_

- _$`A_n`:_

  $$`\circ \text{---} \circ \text{---} \circ \text{-} \cdots \text{-} \circ \text{---} \circ \text{---} \circ`

- _$`D_n`:_

  $$`\begin{array}{ccccccccccc}
  \circ & \text{---} & \circ & \text{---} & \circ & \text{-} & \cdots & \text{-} & \circ & \text{---} & \circ \\
  &&&&&&&& | \\
  &&&&&&&& \circ
  \end{array}`

- _$`E_6`:_

  $$`\begin{array}{ccccccccc}
  \circ & \text{---} & \circ & \text{---} & \circ & \text{---} & \circ & \text{---} & \circ \\
  &&&& | \\
  &&&& \circ
  \end{array}`

## Formalization
%%%
tag := "Chapter6/Theorem_Dynkin_classification/formalization"
number := false
%%%

### Supporting declarations

{Manual.docstring RepresentationTheory.Matrix.BinaryAdjacencyClassification.Matrix.exists_adjacency_reindexing_iff}
