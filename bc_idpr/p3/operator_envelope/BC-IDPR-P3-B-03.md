# BC-IDPR-P3-B-03

## Complete External Tetrahedral Geometry and Explicit q-Leakage Ledger

**Programme:** Boundary Compensation — Independent Deformation and Phase-Resolved Response (BC-IDPR)  
**Track:** P3-B — generic-q operator envelope  
**Milestone:** P3-B-M3  
**Status:** `COMPLETE_EXTERNAL_GEOMETRY_AND_ZERO_LEAKAGE_CERTIFIED`  
**Date:** 2026-07-16  
**Upstream:** `BC-IDPR-P3-B-02`  
**Downstream:** semantic geometry-to-operator bridge, then CERT

---

## 1. Purpose

M2 established a nonzero intrinsic derivative for a three-channel direct q-Racah operator envelope, but its external control was only an equal-label ray. M3 replaces that weak control by a complete externally declared tetrahedral geometry and separates:

1. **forbidden external leakage** — unintended change of geometry, representation scale or protocol while `theta` varies;
2. **allowed internal response** — q-dependent change of q-numbers, q-Racah recoupling, channel operators and quotient invariants.

M3 is a parameter-separation result. It does not yet identify the operator package as a calibrated quantization of the selected tetrahedron.

---

## 2. Complete external geometry

The fixed external datum is the convex Euclidean regular tetrahedron with ordered vertices

\[
v_0=\frac{(1,1,1)}{2\sqrt2},\quad
v_1=\frac{(1,-1,-1)}{2\sqrt2},\quad
v_2=\frac{(-1,1,-1)}{2\sqrt2},\quad
v_3=\frac{(-1,-1,1)}{2\sqrt2}.
\]

It has:

\[
\ell_{ij}=1\quad(i<j),
\qquad
A_i=\frac{\sqrt3}{4},
\qquad
V=\frac{\sqrt2}{12}.
\]

The outward unit-normal Gram matrix is

\[
G_N=
\begin{pmatrix}
1&-1/3&-1/3&-1/3\\
-1/3&1&-1/3&-1/3\\
-1/3&-1/3&1&-1/3\\
-1/3&-1/3&-1/3&1
\end{pmatrix},
\]

with

\[
\operatorname{rank}G_N=3,
\qquad
G_N(1,1,1,1)^T=0.
\]

The area vectors satisfy exact closure:

\[
\sum_{i=1}^{4}A_i n_i=0.
\]

The explicit vertices already determine the tetrahedron. Areas and non-coplanar outward normals provide a redundant closed Minkowski datum and an independent consistency audit.

---

## 3. External label calibration

The fixed representation labels are

\[
(j_1,j_2,j_3,j_4)=(1,1,1,1).
\]

For this anchor only, the external q-independent calibration is declared as

\[
A_i=\frac{\sqrt3}{4}j_i.
\]

This calibration fixes scale and areas. Equal labels alone are not used as a proof of shape; shape is fixed independently by the vertex and normal data.

---

## 4. Independent path

The active path is

\[
\theta\in
\left[\frac{\pi}{10},\frac{3\pi}{20}\right]
\subset
\left(0,\frac{\pi}{5}\right),
\]

with anchor

\[
\theta_0=\frac{\pi}{8}.
\]

The exact external path conditions are

\[
\dot\theta=1,
\qquad
\dot R=0,
\qquad
\dot X_{\mathrm{ext}}=0,
\qquad
\dot\Theta=0.
\]

The forbidden external leakage norm is therefore

\[
E_{\mathrm{ext}}=0.
\]

This is exact by construction, not estimated from finite differences.

---

## 5. Leakage ledger

The following channels are fixed exactly:

- vertices;
- all six edge lengths;
- face areas;
- outward normals;
- normal Gram matrix;
- volume;
- representation labels;
- external label-to-area calibration;
- observation protocol.

The following channels are allowed to respond internally to `theta`:

- q-numbers `[2]` through `[5]`;
- the direct q-Racah matrix `F(theta)`;
- channel operators `X(theta)` and `Y(theta)`;
- centered mixed orientation correlation;
- affine spectral-shape invariant.

At the anchor the internal response norm is

\[
\|V_{\mathrm{int}}\|=20.3533745130361\ldots>0.
\]

The M2 nuisance-quotient margin remains

\[
m_{\mathrm{int}}(\theta_0)=2.5422533772484\ldots
\]

and the operator-norm dual lower bound is

\[
m_{\mathrm{op}}^{\mathrm{dual}}(\theta_0)
=1.1028627901322\ldots.
\]

---

## 6. Compact-interval persistence

On the preregistered 33-point grid:

\[
\min m_{\mathrm{int}}
=1.2292366584592\ldots,
\]

\[
\min \widehat m_{\mathrm{int}}
=0.07776396080238\ldots,
\]

\[
\min m_{\mathrm{op}}^{\mathrm{dual}}
=0.53229704247649\ldots.
\]

The q-Racah orthogonality residual remains below

\[
1.36\times10^{-80},
\]

and the nuisance Gram matrix stays nonsingular throughout the grid.

These are grid bounds. Continuum nontriviality remains supplied by the exact invariant sign certificate of M2.

---

## 7. What M3 establishes

M3 establishes, relative to the declared model:

\[
\dot X_{\mathrm{ext}}=0,
\qquad
E_{\mathrm{ext}}=0,
\qquad
P_{\mathcal N^\perp}\partial_\theta\mathcal D_J\neq0.
\]

Thus the previously observed intrinsic q-response is not caused by changing the externally declared tetrahedral geometry, label scale or protocol.

---

## 8. Semantic bridge remains open

M3 does **not** yet prove that

\[
\mathcal D_J(\theta)
\]

is a calibrated quantization of a specified classical observable of the fixed tetrahedron. A fully fixed geometry and a q-dependent operator package can coexist without a proved semantic map between them.

The next obligation is therefore:

> construct a coherent-state, lower-symbol or other declared classical-symbol map from the fixed tetrahedron to the q-Racah operator package, and bound the symbol mismatch over the compact interval.

Until that bridge is closed, CERT remains blocked.

---

## 9. Claim firewall

This module does not establish:

- a quantum-volume operator;
- physical meaning of `theta`;
- a deformation of a fixed fusion category;
- a continuous family of standard `SU(2)_k` TQFTs;
- observable identifiability;
- correctness for arbitrary tetrahedra;
- global persistence in label size;
- wall crossing;
- a classical-symbol correspondence.

---

## 10. Status

`P3_B_M3_GEOMETRY_CONTROL_CLOSED_CERT_SEMANTIC_BRIDGE_OPEN`
