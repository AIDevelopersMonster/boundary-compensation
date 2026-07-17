# BC-IDPR-P3-B-04 — Coherent Symbol Bridge M4 Research Audit

**Status:** internal mathematical and computational review, v0.1.0  
**Date:** 2026-07-16  
**Scope:** protocol-relative geometry-to-operator bridge; no uniqueness or physical interpretation.

## 1. Reviewed claim

The reviewed claim is:

> For the declared spin-one coherent-intertwiner preparation and the declared pair of normal-Gram observables, the frozen calibrated lower-symbol protocol has nonzero q-response at fixed complete external geometry, while finite-j symbol mismatch is quantified on one calibration geometry and one independent anisotropic equifacial holdout.

This is a protocol-relative claim. It is not a theorem that the selected operators are the unique or exact quantization of tetrahedral shape.

## 2. Construction audit

The carrier is the three-dimensional invariant subspace of four spin-one representations. The implementation constructs an orthonormal `(12)(34)` coupling basis directly from Clebsch--Gordan coefficients. The basis Gram residual is

\[
5.99\times10^{-16}.
\]

The projected coherent state is obtained by projecting the tensor product of four spin-one SU(2) coherent states onto this invariant basis and normalizing.

The classical observables are

\[
g_{12}=n_1\cdot n_2,
\qquad
g_{23}=n_2\cdot n_3.
\]

The corresponding operator protocol is

\[
G_{12}=\frac{\mathbf J_1\cdot\mathbf J_2}{j(j+1)},
\qquad
G_{23}(\theta)=F(\theta)G_{12}F(\theta)^T.
\]

This is a standard angular-momentum functional calculus combined with the direct q-Racah recoupling block from M2.

## 3. Calibration and holdout discipline

Only the regular tetrahedron is used for calibration. Two additive channel offsets are frozen at `theta=pi/8` before interval and holdout evaluation.

The first channel offset is numerically zero. The second is

\[
0.00837124074102752.
\]

The independent holdout is not used in calibration.

A generic unequal-area scalene tetrahedron was not used because the current carrier fixes all four external spins to one. Such a geometry would introduce a known area/label mismatch. The holdout is therefore an anisotropic equifacial disphenoid: it preserves equal face areas but changes edge lengths and normal-Gram coordinates substantially. Its edge spread is approximately

\[
2.16319848054031.
\]

This is a scientifically necessary restriction, not a cosmetic change of terminology.

## 4. Quantitative findings

At the anchor, regular mismatch is zero by the declared calibration. The independent holdout mismatch is

\[
0.10211910127354808.
\]

The fixed-geometry q-response is nonzero:

\[
\partial_\theta \widetilde S_{23}^{\mathrm{reg}}(\pi/8)
=-0.10729829427735815,
\]

\[
\partial_\theta \widetilde S_{23}^{\mathrm{hold}}(\pi/8)
=0.4463919038855124.
\]

On the 33-point compact grid, the maximum regular mismatch is

\[
0.013713613923774015,
\]

and the holdout mismatch remains between

\[
0.07819043294294023
\quad\text{and}\quad
0.1491999657742081.
\]

The second-channel derivative keeps a fixed nonzero sign for each geometry on the grid. These are grid statements, not continuum extrema.

## 5. Error separation

The audit accepts the following ledger:

- external geometry leakage: exactly zero, inherited from M3;
- symbol mismatch: explicitly retained and reported;
- q-response: derivative of the frozen calibrated lower symbol;
- wall error: absent on the compact interval, whose distance from the `pi/5` wall is at least `pi/20`.

The response is not declared significant merely because it exceeds zero. CERT must compare response size with the complete mismatch and numerical uncertainty budget.

## 6. Literature consultation

The mathematical ingredients are consistent with established primary literature:

1. E. Livine and S. Speziale, *A new spinfoam vertex for quantum gravity*, arXiv:0705.0674 — coherent intertwiners and semiclassical polyhedral data.
2. E. Bianchi, P. Dona and S. Speziale, *Polyhedra in loop quantum gravity*, arXiv:1009.3402 — face normals, areas, closure and polyhedral interpretation.
3. Y. U. Taylor and C. T. Woodward, *6j symbols for U_q(sl_2) and non-Euclidean tetrahedra*, arXiv:math/0305113 — q-6j recoupling and geometric asymptotics.

These references justify the use of coherent intertwiners, flux scalar products and q-Racah recoupling. They do not prove the BC calibration, mismatch bounds or independent-q certificate.

No statement from the Gemini advisory report is used as evidence.

## 7. Reviewer concerns

### Concern A — anchor calibration guarantees success

**Assessment:** it guarantees zero mismatch only for the regular anchor. It does not determine the holdout result or the interval response. The holdout mismatch is nonzero and explicitly reported.

### Concern B — two additive offsets are arbitrary

**Assessment:** they are protocol choices and therefore remain inside the claim. CERT must stress-test alternative calibration families. M4 does not claim canonicality.

### Concern C — spin one is not semiclassical

**Correct.** No semiclassical accuracy claim is permitted. The mismatch is a finite-spin protocol error, not a small-parameter asymptotic remainder.

### Concern D — the holdout is not fully scalene

**Correct and explicitly recorded.** A generic unequal-area tetrahedron requires nonuniform external spins and a different carrier. The present disphenoid is an anisotropic equal-area holdout compatible with the current carrier.

### Concern E — only two Gram coordinates are used

**Correct.** The bridge is an observable-package certificate, not complete shape reconstruction. Later work must enlarge the observable package.

### Concern F — the nonzero response may be smaller than model mismatch

**Valid.** This is exactly why the programme must enter CERT rather than P1. CERT must establish distinguishability relative to the symbol-error budget.

## 8. Verdict

**Accept P3-B-M4 with a restricted protocol-relative claim.**

Assign status:

`EUCLIDEAN_COHERENT_SYMBOL_BRIDGE_CERTIFIED`.

The semantic bridge is no longer empty: a complete external geometry now enters a declared coherent-state preparation, a declared operator package and a measurable lower symbol. The result is sufficient to open CERT, but not sufficient to authorize confirmatory P1 analysis.

## 9. Publication firewall

Do not infer from M4:

- unique or exact quantization;
- semiclassical convergence;
- complete tetrahedral reconstruction;
- robustness for unequal areas or large labels;
- physical dynamics of q;
- standard `SU(2)_k` away from the anchor;
- a confirmed phase-residual law.

## 10. Required next step

Proceed to `BC-IDPR-CERT-01 / Protocol-Relative Observable Separation Certificate`.

It must compare the observed q-response against:

1. calibration mismatch;
2. independent holdout mismatch;
3. finite-difference and arithmetic uncertainty;
4. protocol variation under alternative frozen calibrations;
5. wall margin;
6. nuisance-equivalence margin inherited from M2/M3.

Only a positive net separation margin may authorize a preregistered P1 pilot.
