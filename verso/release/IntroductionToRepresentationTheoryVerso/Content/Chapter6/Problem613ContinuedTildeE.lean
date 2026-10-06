/-
Copyright (c) 2026 American Mathematical Society. All rights reserved.
-/

import VersoManual
import RepresentationTheory

open Verso.Genre Manual

namespace IntroductionToRepresentationTheoryVerso.Content.Chapter6.Problem613ContinuedTildeE

#doc (Manual) "Affine Dynkin diagrams" =>

# Affine Dynkin diagrams
%%%
tag := "Chapter6/Problem6.1.3_continued_tildeE"
number := false
%%%

- _$`\tilde{E}_6`:_

  $$`\begin{array}{ccccccccc}
  &&&& \overset{1}{\bullet} \\
  &&&& | \\
  &&&& \overset{2}{\bullet} \\
  &&&& | \\
  \overset{1}{\bullet} & \text{---} & \overset{2}{\bullet} & \text{---} & \overset{3}{\bullet} & \text{---} & \overset{2}{\bullet} & \text{---} & \overset{1}{\bullet}
  \end{array}`

- _$`\tilde{E}_7`:_

  $$`\begin{array}{ccccccccccccc}
  &&&&&& \overset{2}{\bullet} \\
  &&&&&& | \\
  \overset{1}{\bullet} & \text{---} & \overset{2}{\bullet} & \text{---} & \overset{3}{\bullet} & \text{---} & \overset{4}{\bullet} & \text{---} & \overset{3}{\bullet} & \text{---} & \overset{2}{\bullet} & \text{---} & \overset{1}{\bullet}
  \end{array}`

- _$`\tilde{E}_8`:_

  $$`\begin{array}{ccccccccccccccc}
  &&&&&&&&&& \overset{3}{\bullet} \\
  &&&&&&&&&& | \\
  \overset{1}{\bullet} & \text{---} & \overset{2}{\bullet} & \text{---} & \overset{3}{\bullet} & \text{---} & \overset{4}{\bullet} & \text{---} & \overset{5}{\bullet} & \text{---} & \overset{6}{\bullet} & \text{---} & \overset{4}{\bullet} & \text{---} & \overset{2}{\bullet}
  \end{array}`

_Hint for (c)-(e):_ What is the meaning of the numbers labeling the vertices of these graphs?

(f) Deduce from (a)—(e) the classification theorem for Dynkin diagrams.

(g) A (simply laced) *affine Dynkin diagram* is a connected graph without self-loops such that the quadratic form defined by $`A` is positive semidefinite but not positive definite. Classify affine Dynkin diagrams. (Show that they are exactly the forbidden diagrams from (c)—(e).)

## Formalization
%%%
tag := "Chapter6/Problem6.1.3_continued_tildeE/formalization"
number := false
%%%

### Supporting declarations

{Manual.docstring RepresentationTheory.DynkinDiagram.AffineClassification.AffineDynkinDiagram.adjacency_isAffineDynkinMatrix}

{Manual.docstring RepresentationTheory.DynkinDiagram.AffineClassification.AffineDynkinDiagram.det_two_smul_one_sub_adjacency_eq_zero}

{Manual.docstring RepresentationTheory.DynkinDiagram.AffineClassification.AffineDynkinDiagram.two_smul_one_sub_adjacency_mulVec_marks_eq_zero}

{Manual.docstring RepresentationTheory.DynkinDiagram.AffineClassification.isAffineDynkinMatrix_iff_exists_equiv}

{Manual.docstring RepresentationTheory.DynkinDiagram.AffineClassification.isFiniteDynkinMatrix_iff_exists_equiv}
