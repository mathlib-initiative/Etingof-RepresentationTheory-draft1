/-
Copyright (c) 2026 mathlib-initiative. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: mathlib-initiative
-/

import RepresentationTheory.LinearAlgebra.ExteriorAlgebra.Contraction
import RepresentationTheory.Algebra.Homology.BasisSymmetricAlgebraComplex
import RepresentationTheory.LinearAlgebra.ExteriorPower.DegreeZero
import RepresentationTheory.LinearAlgebra.SymmetricExteriorBasis
import RepresentationTheory.SymmetricAlgebra.ProjectiveResolution
import RepresentationTheory.Algebra.Homology.SymmetricAlgebra.ProductResolution
import RepresentationTheory.Algebra.Homology.SymmetricAlgebraResolution
import RepresentationTheory.Alignment.Attribute

universe u v w

namespace RepresentationTheory.Algebra.Homology.ProjectiveResolutionAuxiliary

/-- The free Koszul resolution of the trivial module over a symmetric algebra, constructed from a finite basis. -/
@[source_ref "Chapter8/Problem8.2.10" (role := supporting)]
noncomputable def basisProjectiveResolutionAuxiliary {k : Type u} [CommRing k] {V : Type v}
    [AddCommGroup V] [Module k V] {κ : Type w} [LinearOrder κ] [Fintype κ]
    (b : Module.Basis κ k V) :
    CategoryTheory.ProjectiveResolution
      (ModuleCat.of (SymmetricAlgebra k V)
        (RepresentationTheory.LinearAlgebra.ExteriorPower.DegreeZero.degreeZero k V)) :=
  RepresentationTheory.SymmetricAlgebra.ProjectiveResolution.projectiveResolutionOfBasis b

section

variable {k : Type u} [CommRing k] {V : Type v} [AddCommGroup V] [Module k V]
variable {κ : Type w} [LinearOrder κ] [Fintype κ] (b : Module.Basis κ k V)

/-- The complex underlying the basis-indexed auxiliary projective resolution equals the displayed complex. -/
theorem basisProjectiveResolutionAuxiliary_complex_eq :
    (basisProjectiveResolutionAuxiliary b).complex =
      RepresentationTheory.Algebra.Homology.BasisSymmetricAlgebraComplex.basisSymmetricAlgebraComplex b := rfl

/-- Every term S(V) ⊗ ΛⁱV of the basis-indexed Koszul resolution is free over S(V). -/
@[source_ref "Chapter8/Problem8.2.10" (role := supporting)]
theorem basisProjectiveResolutionAuxiliary_free (i : ℕ) :
    Module.Free (SymmetricAlgebra k V) ((basisProjectiveResolutionAuxiliary b).complex.X i) :=
  RepresentationTheory.SymmetricAlgebra.ProjectiveResolution.projectiveResolutionOfBasis_X_free b i

/-- The degree-zero component of the augmentation of the basis-indexed auxiliary projective resolution equals the displayed module morphism. -/
theorem basisProjectiveResolutionAuxiliary_pi_f_zero_eq :
    (basisProjectiveResolutionAuxiliary b).π.f 0 =
      ModuleCat.ofHom
        (RepresentationTheory.LinearAlgebra.ExteriorPower.DegreeZero.tensorToDegreeZero k V) :=
  RepresentationTheory.SymmetricAlgebra.ProjectiveResolution.basisComplexToSingleZero_f_zero b

end

section

variable (k U W : Type u) [Field k]
  [AddCommGroup U] [Module k U] [FiniteDimensional k U]
  [AddCommGroup W] [Module k W]

/-- Resolve S(W) as an S(U × W)-module with U acting by zero, by tensoring the Koszul resolution for U with S(W). -/
@[source_ref "Chapter8/Problem8.2.10" (role := supporting)]
noncomputable def finiteDimensionalProjectiveResolutionAuxiliary :
    CategoryTheory.ProjectiveResolution
      (RepresentationTheory.Algebra.Homology.SymmetricAlgebra.ProductResolution.productSymmetricAlgebraModule k U W) :=
  RepresentationTheory.Algebra.Homology.SymmetricAlgebra.ProductResolution.productSymmetricAlgebraProjectiveResolution k U W

/-- Identify the degree-i complementary resolution term with S(U × W) ⊗ ΛⁱU. -/
@[source_ref "Chapter8/Problem8.2.10" (role := supporting)]
noncomputable def finiteDimensionalProjectiveResolutionAuxiliary_componentIso (i : ℕ) :
    (finiteDimensionalProjectiveResolutionAuxiliary k U W).complex.X i ≅
      ModuleCat.of (SymmetricAlgebra k (U × W))
        (RepresentationTheory.Algebra.Homology.SymmetricAlgebra.ProductResolution.productResolutionTerm k U W i) :=
  RepresentationTheory.Algebra.Homology.SymmetricAlgebra.ProductResolution.productResolutionComponentIso k U W i

/-- Every degree of the finite-dimensional auxiliary projective resolution is free over the symmetric algebra on the product module. -/
theorem finiteDimensionalProjectiveResolutionAuxiliary_free (i : ℕ) :
    Module.Free (SymmetricAlgebra k (U × W))
      ((finiteDimensionalProjectiveResolutionAuxiliary k U W).complex.X i) :=
  RepresentationTheory.Algebra.Homology.SymmetricAlgebra.ProductResolution.productResolutionComponent_free k U W i

/-- The augmentation of the finite-dimensional auxiliary projective resolution is a quasi-isomorphism. -/
@[source_ref "Chapter8/Problem8.2.10" (role := supporting)]
theorem finiteDimensionalProjectiveResolutionAuxiliary_pi_quasiIso :
    QuasiIso (finiteDimensionalProjectiveResolutionAuxiliary k U W).π :=
  RepresentationTheory.Algebra.Homology.SymmetricAlgebra.ProductResolution.productResolution_augmentation_quasiIso k U W

end


section PartV

variable {k V κ : Type u} [Field k] [AddCommGroup V] [Module k V]
variable [LinearOrder κ] [Fintype κ] (b : Module.Basis κ k V)

/-- For the trivial S(V)-module k, Ext in degree i is the k-linear dual of ΛⁱV. -/
@[source_ref "Chapter8/Problem8.2.10" (role := supporting)]
noncomputable def basisIndexedDualExteriorPowerIsoAuxiliary (i : ℕ) :
    RepresentationTheory.Algebra.Homology.LinearYoneda.ModuleCat.linearYonedaHomology k
        (SymmetricAlgebra k V)
        (ModuleCat.of (SymmetricAlgebra k V)
          (RepresentationTheory.LinearAlgebra.ExteriorPower.DegreeZero.degreeZero k V))
        (ModuleCat.of (SymmetricAlgebra k V)
          (RepresentationTheory.LinearAlgebra.ExteriorPower.DegreeZero.degreeZero k V)) i ≅
      ModuleCat.of k (Module.Dual k (⋀[k]^i V)) :=
  RepresentationTheory.Algebra.Homology.SymmetricAlgebraResolution.SymmetricAlgebra.indexedObjectIsoExteriorPowerDual k V b i

/-- For the trivial S(V)-module k, Tor in degree i is the exterior power ΛⁱV. -/
@[source_ref "Chapter8/Problem8.2.10" (role := supporting)]
noncomputable def basisIndexedExteriorPowerIsoAuxiliary (i : ℕ) :
    RepresentationTheory.ModuleCat.RightTensor.auxiliaryIndexedModuleFunctorObj k
        (SymmetricAlgebra k V)
        (RepresentationTheory.LinearAlgebra.ExteriorPower.DegreeZero.degreeZero k V)
        ((RepresentationTheory.Algebra.Module.DirectSumData.commRingModuleToOpposite
          (SymmetricAlgebra k V)).obj
          (ModuleCat.of (SymmetricAlgebra k V)
            (RepresentationTheory.LinearAlgebra.ExteriorPower.DegreeZero.degreeZero k V))) i ≅
      ModuleCat.of k (⋀[k]^i V) :=
  RepresentationTheory.Algebra.Homology.SymmetricAlgebraResolution.SymmetricAlgebra.indexedObjectIsoExteriorPower k V b i

end PartV

end RepresentationTheory.Algebra.Homology.ProjectiveResolutionAuxiliary
