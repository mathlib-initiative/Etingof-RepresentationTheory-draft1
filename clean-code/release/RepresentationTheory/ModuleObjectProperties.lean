/-
Copyright (c) 2026 mathlib-initiative. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Kim Morrison
-/
import Mathlib
import RepresentationTheory.Alignment.Attribute

namespace RepresentationTheory.ModuleObjectProperties

open CategoryTheory Limits

namespace ModuleCat

/-- The property of being a finitely generated module over A. -/
def moduleObjectProperty (A : Type*) [CommRing A] : ObjectProperty (ModuleCat.{0} A) :=
  fun M => Module.Finite A M

namespace moduleObjectPropertyFullSubcategoryHasAbelianStructure

variable {A : Type} [CommRing A]

/-- Over a Noetherian commutative ring, submodules of finitely generated modules are finitely generated. -/
instance isClosedUnderSubobjects [IsNoetherianRing A] :
    (moduleObjectProperty A).IsClosedUnderSubobjects where
  prop_of_mono {X Y} f _ hY := by
    haveI : Module.Finite A Y := hY
    haveI : IsNoetherian A Y := isNoetherian_of_isNoetherianRing_of_finite A Y
    exact Module.Finite.of_injective f.hom ((ModuleCat.mono_iff_injective f).mp inferInstance)

/-- Quotients of finitely generated modules are finitely generated. -/
instance isClosedUnderQuotients : (moduleObjectProperty A).IsClosedUnderQuotients where
  prop_of_epi {X Y} f _ hX := by
    haveI : Module.Finite A X := hX
    exact Module.Finite.of_surjective f.hom ((ModuleCat.epi_iff_surjective f).mp inferInstance)

/-- The zero module is finitely generated. -/
instance containsZero : (moduleObjectProperty A).ContainsZero where
  exists_zero :=
    ⟨ModuleCat.of A PUnit, ModuleCat.isZero_of_subsingleton _,
      Module.Finite.of_surjective (0 : A →ₗ[A] PUnit) fun _ => ⟨0, Subsingleton.elim _ _⟩⟩

/-- Finite products of finitely generated modules are finitely generated. -/
instance isClosedUnderFiniteProducts : (moduleObjectProperty A).IsClosedUnderFiniteProducts := by
  apply ObjectProperty.IsClosedUnderFiniteProducts.of_isClosedUnderLimitsOfShape.{0}
  intro J _
  apply ObjectProperty.IsClosedUnderLimitsOfShape.mk'
  rintro _ ⟨F, hF⟩
  haveI : ∀ j : J, Module.Finite A (F.obj ⟨j⟩) := fun j => hF ⟨j⟩
  haveI : Module.Finite A (ModuleCat.of A (∀ j : J, (F.obj ⟨j⟩ : Type))) := Module.Finite.pi
  exact (moduleObjectProperty A).prop_of_iso
    (Iso.symm (HasLimit.isoOfNatIso Discrete.natIsoFunctor ≪≫ ModuleCat.piIsoPi _)) this

end moduleObjectPropertyFullSubcategoryHasAbelianStructure

/-- Finitely generated modules over a commutative ring of finite type over the integers form an abelian category. Hilbert's basis theorem supplies Noetherianity. -/
@[source_ref "Chapter7/Problem7.7.3" (role := primary)]
theorem moduleObjectPropertyFullSubcategoryHasAbelianStructure (A : Type) [CommRing A]
    [Algebra ℤ A] [Algebra.FiniteType ℤ A] :
    Nonempty (Abelian (moduleObjectProperty A).FullSubcategory) := by
  haveI : IsNoetherianRing A := Algebra.FiniteType.isNoetherianRing ℤ A
  exact ⟨inferInstance⟩

end ModuleCat

end RepresentationTheory.ModuleObjectProperties
