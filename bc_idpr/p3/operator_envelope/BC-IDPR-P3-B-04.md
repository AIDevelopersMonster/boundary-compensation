# BC-IDPR-P3-B-04

## Geometry-to-Operator Coherent Symbol Bridge

**Programme:** Boundary Compensation — Independent Deformation and Phase-Resolved Response (BC-IDPR)  
**Track:** P3-B — generic-q operator envelope  
**Milestone:** P3-B-M4  
**Status:** `EUCLIDEAN_COHERENT_SYMBOL_BRIDGE_CERTIFIED`  
**Date:** 2026-07-16  
**Upstream:** `BC-IDPR-P3-B-03`, `BC-IDPR-P3-B-02`  
**Downstream:** protocol-relative CERT only

---

## 1. Purpose

M3 fixed a complete Euclidean tetrahedral geometry and proved zero forbidden external leakage, but it did not supply a semantic map from the tetrahedron to the q-Racah operator package. M4 closes that interface for one explicit finite-spin protocol.

The claim is deliberately restricted:

> A declared spin-one coherent-intertwiner lower-symbol protocol maps two classical normal-Gram coordinates of a fixed tetrahedron to two channel-Casimir operators. After a frozen anchor calibration, the resulting symbol has quantified finite-j mismatch and a nonzero q-response at fixed external geometry.

This is not a unique quantization theorem and not a semiclassical theorem at `j=1`.

---

## 2. Classical observable package

For outward unit face normals `n_i`, select

\[
g_{12}=n_1\cdot n_2,
\qquad
g_{23}=n_2\cdot n_3.
\]

These are entries of the normal Gram matrix and therefore genuine shape observables of the declared Euclidean tetrahedron.

---

## 3. Three-channel carrier and coherent state

Use four external spin-one representations and total spin zero. In the `(12)(34)` coupling scheme the invariant carrier has channels

\[
e\in\{0,1,2\}.
\]

For each normal `n_i`, form the spin-one SU(2) coherent state `|1,n_i>`. Project the tensor product

\[
\bigotimes_{i=1}^4 |1,n_i\rangle
\]

onto the invariant carrier and normalize. The resulting coefficient vector is denoted

\[
c(n_1,n_2,n_3,n_4)\in\mathbb C^3.
\]

The implementation constructs the invariant basis independently from Clebsch--Gordan coefficients and verifies its Gram matrix against the identity.

---

## 4. Operator package

In the first channel define the pairwise Casimir operator

\[
C_{12}=\operatorname{diag}(-2,-1,1),
\]

because

\[
\mathbf J_1\cdot\mathbf J_2
=\frac12\left(e(e+1)-2j(j+1)\right),
\qquad j=1.
\]

Normalize by `j(j+1)=2`:

\[
G_{12}=\frac12 C_{12}.
\]

For the second channel use the direct q-Racah matrix from M2:

\[
G_{23}(\theta)
=\frac12 F(\theta)C_{12}F(\theta)^T.
\]

The raw lower symbol is

\[
S_\theta(n)=
\left(
\langle c,G_{12}c\rangle,
\langle c,G_{23}(\theta)c\rangle
\right).
\]

---

## 5. Frozen anchor calibration

At

\[
\theta_0=\frac\pi8
\]

use the regular tetrahedron from M3 as the sole calibration geometry. Freeze two additive channel offsets

\[
b=g^{\mathrm{reg}}-S_{\theta_0}(n^{\mathrm{reg}}).
\]

Numerically,

\[
b_1=-1.67\times10^{-16},
\qquad
b_2=0.00837124074102752.
\]

The calibrated symbol is

\[
\widetilde S_\theta=S_\theta+b.
\]

The offsets are frozen before the interval scan and holdout evaluation. No holdout datum is used in calibration.

---

## 6. Holdout geometry

The same equal-spin carrier cannot faithfully encode unequal face areas. Therefore the first independent holdout is an anisotropic **equifacial disphenoid**, not a generic unequal-area tetrahedron.

Its four face areas are equal, so it is compatible with the fixed spin-one external labels, while its edge lengths and normal Gram entries differ strongly from the regular tetrahedron. The edge-length spread is approximately

\[
2.16319848054031.
\]

A genuinely unequal-area scalene holdout is deferred to a larger nonuniform-spin carrier.

---

## 7. Anchor results

The regular calibration mismatch is zero by construction:

\[
\|\widetilde S_{\theta_0}^{\mathrm{reg}}-g^{\mathrm{reg}}\|=0.
\]

For the anisotropic equifacial holdout,

\[
\|\widetilde S_{\theta_0}^{\mathrm{hold}}-g^{\mathrm{hold}}\|
=0.10211910127354808.
\]

The q-response at fixed coherent state is nonzero:

\[
\partial_\theta \widetilde S_{23}^{\mathrm{reg}}(\theta_0)
=-0.10729829427735815,
\]

\[
\partial_\theta \widetilde S_{23}^{\mathrm{hold}}(\theta_0)
=0.4463919038855124.
\]

The first channel is theta-independent by construction and functions as a negative control.

---

## 8. Compact-interval audit

On the preregistered interval

\[
I=\left[\frac\pi{10},\frac{3\pi}{20}\right]
\]

with 33 samples:

\[
\max_I \|\widetilde S^{\mathrm{reg}}-g^{\mathrm{reg}}\|
=0.013713613923774015,
\]

\[
0.07819043294294023
\le
\|\widetilde S^{\mathrm{hold}}-g^{\mathrm{hold}}\|
\le
0.1491999657742081.
\]

The second-channel derivatives retain fixed nonzero sign on the grid:

\[
-0.2656513939935934
\le
\partial_\theta\widetilde S_{23}^{\mathrm{reg}}
\le
-0.04207254733490373,
\]

\[
0.25967920647129716
\le
\partial_\theta\widetilde S_{23}^{\mathrm{hold}}
\le
0.8999946229382161.
\]

These are grid bounds, not continuum extrema.

---

## 9. Error ledger

The protocol separates four terms:

1. **External leakage:** zero by the exact M3 certificate.
2. **Symbol mismatch:** reported separately for calibration and holdout geometries.
3. **q-response:** derivative of the frozen calibrated lower symbol at fixed coherent state and fixed external geometry.
4. **Wall error:** absent on the declared compact interval; the distance to the `pi/5` wall is at least `pi/20`.

No symbol mismatch is subtracted from the q-response claim.

---

## 10. Certified status

Assign

`EUCLIDEAN_COHERENT_SYMBOL_BRIDGE_CERTIFIED`.

The allowed statement is:

> Under the declared spin-one coherent-intertwiner protocol, a calibrated pair of normal-Gram lower symbols exhibits a nonzero q-response while the complete external tetrahedral geometry remains fixed, and the finite-j symbol mismatch is explicitly bounded on one calibration geometry and one independent anisotropic equifacial holdout.

---

## 11. Claim firewall

M4 does not establish:

- uniqueness of the operator assignment;
- exact quantization of tetrahedral shape;
- semiclassical accuracy at spin one;
- a universal symbol map for all tetrahedra;
- a continuous family of standard `SU(2)_k` TQFTs;
- physical dynamics of q;
- a confirmatory P1 phase law;
- unequal-area holdout robustness.

---

## 12. Gate decision

The semantic bridge is no longer empty. CERT may now open only in a **protocol-relative** form:

- observable package fixed to `(g12,g23)`;
- coherent-state preparation fixed;
- anchor offsets frozen;
- finite-j mismatch retained in the uncertainty budget;
- external leakage inherited as zero from M3;
- no physical interpretation.

The next document is `BC-IDPR-CERT-01`, not P1 itself.
