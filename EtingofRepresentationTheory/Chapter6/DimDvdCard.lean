import Mathlib
import EtingofRepresentationTheory.Infrastructure.CharacterOrthogonalityCompat

/-!
# The dimension of a complex irreducible representation divides `|G|`

This file proves the classical theorem of Frobenius: the dimension of a
complex irreducible representation of a finite group `G` divides the order of
`G`. It is the general ingredient behind the odd-order case of
Problem 6.1.6(c) (`isCyclic_of_odd_card`): a group of odd order has no
`2`-dimensional irreducible representation, because `2 ∤ |G|`.

The main theorem `finrank_dvd_card_of_irreducible` is proved here in full, together
with its two central-character ingredients (`FDRep.isIntegral_character` and
`FDRep.isIntegral_classSum_scalar`).

## Main results

* `isIntegral_int_of_pow_eq_one`: a complex root of unity is an algebraic
  integer (root of the monic `X ^ n - 1`).
* `FDRep.isIntegral_character` (from Mathlib): **character values are algebraic
  integers.**
* `FDRep.isIntegral_classSum_scalar`: **the central-character value on a class
  sum is an algebraic integer.**
* `finrank_dvd_card_of_irreducible`: the Frobenius divisibility theorem itself
  (deduced from `isIntegral_classSum_scalar` and `isIntegral_character` via
  Schur orthogonality and integral closure of `ℤ` in `ℚ`).

## References

Etingof et al., *Introduction to Representation Theory*; the theorem is standard
(Frobenius). Building blocks used: `Matrix.trace_eq_sum_roots_charpoly`,
`Matrix.eval_charpoly`, `Matrix.exists_mulVec_eq_zero_iff`,
`IsIntegrallyClosed`/`Niven` (rational algebraic integers are integers),
`FDRep.scalar_product_char_eq_finrank_equivariant`.
-/

open Polynomial Matrix Module CategoryTheory

/-- A complex number `r` with `r ^ n = 1` for some `0 < n` is integral over `ℤ`:
it is a root of the monic integer polynomial `X ^ n - 1`. -/
theorem isIntegral_int_of_pow_eq_one {r : ℂ} {n : ℕ} (hn : 0 < n) (h : r ^ n = 1) :
    IsIntegral ℤ r := by
  refine ⟨X ^ n - C 1, monic_X_pow_sub_C 1 hn.ne', ?_⟩
  simp [h]

namespace FDRep

variable {G : Type*} [Group G] [Finite G]

/-- **Central character integrality (Frobenius, step 2).**

For an irreducible `V` and a conjugacy class with representative `g₀` and size
`c`, the scalar `ω = c · χ_V(g₀) / d` by which the class sum acts on `V` is
integral over `ℤ`.

Proof: let `z = ∑_{x ∼ g₀} x` be the class sum inside the integral group ring
`ℤ[G]`. Since `G` is finite, `ℤ[G]` is module-finite over `ℤ`, so `z` is integral
over `ℤ` (`IsIntegral.of_finite`). Let `Φ : ℤ[G] →ₐ[ℤ] End ℂ V` extend the
representation. As conjugation permutes the class, `Φ z = ∑_{x ∼ g₀} ρ x` commutes
with every `ρ g`, hence is a `V`-endomorphism; by Schur's lemma over the
algebraically closed field `ℂ` it is a scalar `Φ z = c • id`. Taking traces,
`c · d = tr(Φ z) = ∑_{x ∼ g₀} χ_V(x) = |C| · χ_V(g₀)`, so `c = ω`. Finally `Φ z`
is integral over `ℤ` (`IsIntegral.map`), and `Φ z = c • id = algebraMap ℂ ω`,
so `ω` is integral over `ℤ` (`isIntegral_algebraMap_iff`, the algebra map being
injective on the nonzero space `V`). -/
theorem isIntegral_classSum_scalar (V : FDRep ℂ G) [Simple V] (g₀ : G) :
    IsIntegral ℤ ((Nat.card {x // IsConj g₀ x} : ℂ) * V.character g₀ / (finrank ℂ V : ℂ)) := by
  classical
  have : Fintype G := Fintype.ofFinite G
  -- `V` is nonzero, hence has positive dimension and a nonzero-scalar-faithful action.
  have hpos : 0 < finrank ℂ V := by
    by_contra h
    have h0 : finrank ℂ V = 0 := by omega
    have hsub : Subsingleton (V : Type) := Module.finrank_zero_iff.mp h0
    have hsub2 : Subsingleton (V ⟶ V) :=
      ⟨fun f g => Action.Hom.ext (FGModuleCat.hom_ext (LinearMap.ext fun x => hsub.elim _ _))⟩
    have hSS : finrank ℂ (V ⟶ V) = 1 := by rw [FDRep.finrank_hom_simple_simple]; simp
    have : finrank ℂ (V ⟶ V) = 0 := Module.finrank_zero_of_subsingleton
    omega
  have : Nontrivial (V : Type) := (finrank_pos_iff (R := ℂ)).mp hpos
  have hfr0 : (finrank ℂ V : ℂ) ≠ 0 := by exact_mod_cast hpos.ne'
  -- The conjugacy class of `g₀`, as a finset, and its class sum in `ℤ[G]`.
  set C : Finset G := Finset.univ.filter (fun x => IsConj g₀ x) with hC
  set z : MonoidAlgebra ℤ G := ∑ x ∈ C, MonoidAlgebra.single x 1 with hz
  -- The algebra hom `ℤ[G] →ₐ[ℤ] End ℂ V` extending the representation.
  set Φ : MonoidAlgebra ℤ G →ₐ[ℤ] Module.End ℂ (V : Type) :=
    MonoidAlgebra.lift ℤ (Module.End ℂ V) G V.ρ with hΦ
  have hΦz : Φ z = ∑ x ∈ C, V.ρ x := by
    rw [hz, map_sum]
    refine Finset.sum_congr rfl fun x _ => ?_
    rw [hΦ, MonoidAlgebra.lift_single, one_smul]
  -- `Φ z` commutes with every `V.ρ g`: conjugation permutes the class.
  have hcomm : ∀ g : G, V.ρ g * Φ z = Φ z * V.ρ g := by
    intro g
    rw [hΦz, Finset.mul_sum, Finset.sum_mul]
    refine Finset.sum_nbij' (fun x => g * x * g⁻¹) (fun x => g⁻¹ * x * g) ?_ ?_ ?_ ?_ ?_
    · intro a ha
      simp only [hC, Finset.mem_filter, Finset.mem_univ, true_and] at ha ⊢
      exact ha.trans (isConj_iff.mpr ⟨g, rfl⟩)
    · intro a ha
      simp only [hC, Finset.mem_filter, Finset.mem_univ, true_and] at ha ⊢
      exact ha.trans (isConj_iff.mpr ⟨g⁻¹, by group⟩)
    · intro a _; group
    · intro a _; group
    · intro a _
      simp only [← MonoidHom.map_mul]
      congr 1
      group
  -- Package `Φ z` as an endomorphism of `V` in `FDRep ℂ G`, then apply Schur's lemma.
  have hf : ∀ g : G, (Φ z) ∘ₗ V.ρ g = V.ρ g ∘ₗ (Φ z) := fun g => (hcomm g).symm
  let φ : V ⟶ V :=
    { hom := FGModuleCat.ofHom (Φ z)
      comm := fun g => by ext v; exact LinearMap.congr_fun (hf g) v }
  obtain ⟨c, hc⟩ := CategoryTheory.endomorphism_simple_eq_smul_id ℂ φ
  -- Extract the underlying scalar identity `Φ z = c • id`.
  have hΦz_scalar : Φ z = c • LinearMap.id := by
    have key : (FGModuleCat.ofHom (Φ z)).hom.hom = (c • 𝟙 V).hom.hom.hom :=
      congrArg (fun ψ : V ⟶ V => ψ.hom.hom.hom) hc.symm
    rw [show (FGModuleCat.ofHom (Φ z)).hom.hom = Φ z from rfl] at key
    rw [key, Action.smul_hom, Action.id_hom]
    rfl
  -- Compute the scalar via the trace: `tr (Φ z) = |C| · χ(g₀)` and `tr (c • id) = c · d`.
  have htr : LinearMap.trace ℂ (V : Type) (Φ z) = (C.card : ℂ) * V.character g₀ := by
    rw [hΦz, map_sum]
    have hconst : ∀ x ∈ C, LinearMap.trace ℂ (V : Type) (V.ρ x) = V.character g₀ := by
      intro x hx
      simp only [hC, Finset.mem_filter, Finset.mem_univ, true_and] at hx
      obtain ⟨h, rfl⟩ := isConj_iff.mp hx
      exact V.char_conj g₀ h
    rw [Finset.sum_congr rfl hconst, Finset.sum_const, nsmul_eq_mul]
  have htr2 : LinearMap.trace ℂ (V : Type) (Φ z) = c * (finrank ℂ V : ℂ) := by
    rw [hΦz_scalar, map_smul, LinearMap.trace_id, smul_eq_mul]
  have hcd : (C.card : ℂ) * V.character g₀ = c * (finrank ℂ V : ℂ) := htr.symm.trans htr2
  -- Identify the target scalar with `c`.
  have hcard : Nat.card {x // IsConj g₀ x} = C.card := by
    rw [Nat.card_eq_fintype_card, hC, Fintype.card_subtype]
  have hω : (Nat.card {x // IsConj g₀ x} : ℂ) * V.character g₀ / (finrank ℂ V : ℂ) = c := by
    rw [show ((Nat.card {x // IsConj g₀ x} : ℕ) : ℂ) = (C.card : ℂ) by rw [hcard]]
    rw [hcd, mul_div_assoc, div_self hfr0, mul_one]
  rw [hω]
  -- `z` is integral over `ℤ` (`ℤ[G]` is module-finite over `ℤ`), so `Φ z = c • id` is too.
  have hz_int : IsIntegral ℤ z := by
    have : Module.Finite ℤ (MonoidAlgebra ℤ G) :=
      Module.Finite.of_basis (MonoidAlgebra.basis G ℤ)
    exact IsIntegral.of_finite ℤ z
  have hΦz_int : IsIntegral ℤ (Φ z) := IsIntegral.map Φ hz_int
  rw [hΦz_scalar, ← Module.algebraMap_end_eq_smul_id] at hΦz_int
  -- Descend integrality of `c • id = algebraMap c` to integrality of `c`.
  have hinj : Function.Injective (algebraMap ℂ (Module.End ℂ (V : Type))) := by
    rw [injective_iff_map_eq_zero]
    intro r hr
    by_contra hr0
    have hk := Module.ker_algebraMap_end ℂ (V : Type) r hr0
    rw [hr, LinearMap.ker_zero] at hk
    exact absurd hk top_ne_bot
  exact (isIntegral_algHom_iff (IsScalarTower.toAlgHom ℤ ℂ _) hinj).mp hΦz_int

end FDRep

/-- **Frobenius' theorem: the dimension of a complex irreducible representation of
a finite group divides the group order.**

Proof: with `d = finrank ℂ V` and `χ = V.character`, Schur
orthogonality `⟨χ, χ⟩ = 1` gives `|G| = ∑_C c · |χ(g_C)|²`, so
`|G| / d = ∑_C ω_C · conj(χ(g_C))` with `ω_C = c · χ(g_C) / d`. Each `ω_C`
(`FDRep.isIntegral_classSum_scalar`) and each `conj(χ(g_C))`
(`FDRep.isIntegral_character`, closed under complex conjugation) is an algebraic
integer, so `|G| / d ∈ ℚ` is an algebraic integer, hence an integer
(`ℤ` is integrally closed in `ℚ`); therefore `d ∣ |G|`. -/
theorem finrank_dvd_card_of_irreducible {G : Type*} [Group G] [Fintype G]
    (V : FDRep ℂ G) [Simple V] : Module.finrank ℂ V ∣ Fintype.card G := by
  classical
  have : Nonempty G := ⟨1⟩
  have hNne : (Fintype.card G : ℂ) ≠ 0 := Nat.cast_ne_zero.mpr Fintype.card_ne_zero
  have hinv : Invertible (Fintype.card G : ℂ) := invertibleOfNonzero hNne
  set d : ℕ := Module.finrank ℂ V with hd_def
  -- `V` is simple, hence a nonzero object, so `0 < d`.
  have hd0 : 0 < d := by
    rcases Nat.eq_zero_or_pos d with h0 | h0
    · exfalso
      have hsub : Subsingleton V := Module.finrank_zero_iff.mp h0
      have hsub2 : Subsingleton (V ⟶ V) := by
        refine ⟨fun f g => ?_⟩
        exact Action.Hom.ext (FGModuleCat.hom_ext (LinearMap.ext (fun x => hsub.elim _ _)))
      have h1 : Module.finrank ℂ (V ⟶ V) = 1 := by rw [FDRep.finrank_hom_simple_simple]; simp
      have h2 : Module.finrank ℂ (V ⟶ V) = 0 := Module.finrank_zero_of_subsingleton
      omega
    · exact h0
  have hdℂ : (d : ℂ) ≠ 0 := Nat.cast_ne_zero.mpr hd0.ne'
  -- Schur orthogonality gives `∑_g χ(g) χ(g⁻¹) = |G|`.
  have hnorm : ∑ g : G, V.character g * V.character g⁻¹ = (Fintype.card G : ℂ) := by
    have hco := FDRep.char_orthonormal_fintype V V
    rw [ite_eq_left ⟨Iso.refl V⟩] at hco
    have h2 : (Fintype.card G : ℂ) * (⅟(Fintype.card G : ℂ) •
        ∑ g : G, V.character g * V.character g⁻¹) = (Fintype.card G : ℂ) * (↑1 : ℂ) :=
      congrArg _ hco
    rw [smul_eq_mul, ← mul_assoc, mul_invOf_self, one_mul] at h2
    rw [h2]; norm_num
  -- The character is a class function, on `g` and on `g⁻¹`.
  have hconj : ∀ {a b : G}, IsConj a b → V.character a = V.character b := by
    intro a b hab
    obtain ⟨c, hc⟩ := isConj_iff.mp hab
    rw [← hc]; exact (FDRep.char_conj V a c).symm
  have hconj_inv : ∀ {a b : G}, IsConj a b → IsConj a⁻¹ b⁻¹ := by
    intro a b hab
    obtain ⟨c, hc⟩ := isConj_iff.mp hab
    exact isConj_iff.mpr ⟨c, by rw [← hc]; group⟩
  -- Reindex the sum over `G` by conjugacy classes.
  have hmaps : ∀ g ∈ (Finset.univ : Finset G),
      ConjClasses.mk g ∈ (Finset.univ : Finset (ConjClasses G)) := fun g _ => Finset.mem_univ _
  have hreindex :
      ∑ g : G, V.character g * V.character g⁻¹
        = ∑ C : ConjClasses G, ∑ g ∈ Finset.univ.filter (fun g => ConjClasses.mk g = C),
            V.character g * V.character g⁻¹ :=
    (Finset.sum_fiberwise_of_maps_to hmaps _).symm
  -- Each conjugacy-class fiber sum is `|C| · χ(g_C) χ(g_C⁻¹)`.
  have hinner : ∀ C : ConjClasses G,
      ∑ g ∈ Finset.univ.filter (fun g => ConjClasses.mk g = C),
        V.character g * V.character g⁻¹
        = (Nat.card {x // IsConj (Quotient.out C) x} : ℂ) *
            (V.character (Quotient.out C) * V.character (Quotient.out C)⁻¹) := by
    intro C
    have : DecidablePred (fun g : G => IsConj (Quotient.out C) g) := Classical.decPred _
    have hmkout : ConjClasses.mk (Quotient.out C) = C := by
      rw [← ConjClasses.quotient_mk_eq_mk]; exact Quotient.out_eq C
    -- membership in the `mk`-fiber is the same as being conjugate to the representative
    have hmem : ∀ g : G, ConjClasses.mk g = C ↔ IsConj (Quotient.out C) g := by
      intro g
      constructor
      · intro hg
        rw [← hmkout, ConjClasses.mk_eq_mk_iff_isConj] at hg
        exact hg.symm
      · intro hg
        rw [← hmkout, ConjClasses.mk_eq_mk_iff_isConj]
        exact hg.symm
    -- the summand is constant on the fiber
    have hconst : ∀ g ∈ Finset.univ.filter (fun g => ConjClasses.mk g = C),
        V.character g * V.character g⁻¹
          = V.character (Quotient.out C) * V.character (Quotient.out C)⁻¹ := by
      intro g hg
      rw [Finset.mem_filter] at hg
      have hcg : IsConj (Quotient.out C) g := (hmem g).mp hg.2
      rw [← hconj hcg, ← hconj (hconj_inv hcg)]
    -- the fiber has cardinality equal to the size of the conjugacy class
    have hcard : (Finset.univ.filter (fun g => ConjClasses.mk g = C)).card
        = Nat.card {x // IsConj (Quotient.out C) x} := by
      rw [Nat.card_eq_fintype_card, Fintype.card_subtype]
      exact congrArg Finset.card (Finset.filter_congr (fun g _ => hmem g))
    rw [Finset.sum_congr rfl hconst, Finset.sum_const, hcard, nsmul_eq_mul]
  -- Collect: `|G| = ∑_C |C| · χ(g_C) χ(g_C⁻¹)`.
  have hclasssum : (Fintype.card G : ℂ)
      = ∑ C : ConjClasses G,
          (Nat.card {x // IsConj (Quotient.out C) x} : ℂ) *
            (V.character (Quotient.out C) * V.character (Quotient.out C)⁻¹) := by
    rw [← hnorm, hreindex]
    exact Finset.sum_congr rfl (fun C _ => hinner C)
  -- `|G|/d = ∑_C ω_C · χ(g_C⁻¹)` is a sum of products of algebraic integers.
  have hα_int : IsIntegral ℤ ((Fintype.card G : ℂ) / (d : ℂ)) := by
    rw [hclasssum, Finset.sum_div]
    apply IsIntegral.sum
    intro C _
    have hrw : (Nat.card {x // IsConj (Quotient.out C) x} : ℂ) *
          (V.character (Quotient.out C) * V.character (Quotient.out C)⁻¹) / (d : ℂ)
        = ((Nat.card {x // IsConj (Quotient.out C) x} : ℂ) * V.character (Quotient.out C)
            / (d : ℂ)) * V.character (Quotient.out C)⁻¹ := by
      rw [← mul_assoc, mul_div_right_comm]
    rw [hrw]
    exact (FDRep.isIntegral_classSum_scalar V (Quotient.out C)).mul
      (FDRep.isIntegral_character V (Quotient.out C)⁻¹)
  -- A rational algebraic integer is an integer (`ℤ` is integrally closed in `ℚ`).
  have hqmap : (algebraMap ℚ ℂ) ((Fintype.card G : ℚ) / (d : ℚ))
      = (Fintype.card G : ℂ) / (d : ℂ) := by
    rw [map_div₀, map_natCast, map_natCast]
  have hq_int : IsIntegral ℤ ((Fintype.card G : ℚ) / (d : ℚ)) := by
    apply (isIntegral_algebraMap_iff (B := ℂ)).mp
    rw [hqmap]; exact hα_int
  obtain ⟨n, hn⟩ := IsIntegrallyClosed.isIntegral_iff.mp hq_int
  -- `n = |G|/d` as rationals, so `n · d = |G|`, hence `d ∣ |G|`.
  have hdℚ : (d : ℚ) ≠ 0 := Nat.cast_ne_zero.mpr hd0.ne'
  rw [eq_div_iff hdℚ] at hn
  have hnn : (n : ℚ) * (d : ℚ) = (Fintype.card G : ℚ) := by
    simpa using hn
  have hZ : (n : ℤ) * (d : ℤ) = (Fintype.card G : ℤ) := by exact_mod_cast hnn
  have hdvd : (d : ℤ) ∣ (Fintype.card G : ℤ) := ⟨n, by rw [← hZ]; ring⟩
  exact Int.natCast_dvd_natCast.mp hdvd
