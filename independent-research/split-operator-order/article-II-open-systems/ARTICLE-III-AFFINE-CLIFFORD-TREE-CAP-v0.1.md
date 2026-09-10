# Article III — Affine Clifford Spanning Tree and One-Cycle Cap

**Author:** Malachevsky, A.A. / Малачевский А.А.  
**ORCID:** 0009-0008-6009-3196  
**Date:** 2026-09-10  
**Status:** `PROVED COMBINATORIAL TREE / EXACT FOREST ELIMINATION / DETERMINISTIC SHARP CANDIDATE / ALL-PRIME CYCLE GAP OPEN`

## 0. Purpose

The quadratic-phase forest theorem solved the block-compatible core problem for every odd prime dimension but left `p-1` dense completion faces unspecified.

A much more rigid architecture is now visible. For every odd prime `p`, one can write down **one deterministic sharp-count Clifford face set** consisting of

1. a vertical quadratic-shear forest;
2. a horizontal quadratic-shear tree connecting the remaining components;
3. one Fourier face closing exactly one cycle.

The first two layers contain exactly `|Omega_p|-1` faces, where

\[
\Omega_p=(\mathbb F_p^2\setminus\{0\})/\{\pm1\}.
\]

At the label level they form a spanning tree on `Omega_p`; the Fourier face adds a single cycle. Thus the sharp problem has been reduced to a **one-cycle holonomy problem** on a residual real space of dimension `2p^2`.

The tree/cycle combinatorics and the exact forest elimination are proved here. Floating-point computations certify the predicted rank pattern for `p=3,5,7,11,13`. The all-prime spectral theorem for the final cycle is not yet claimed.

---

## 1. Symmetric Weyl gauge

Let

\[
\omega=e^{2\pi i/p},
\qquad
2^{-1}\in\mathbb F_p
\]

and use symmetric Weyl operators

\[
\boxed{
W_{a,b}=\omega^{ab/2}X^aZ^b.
}
\tag{1.1}
\]

Then

\[
W_{a,b}^*=W_{-a,-b}.
\]

Changing from this gauge to `X^aZ^b` only multiplies individual transports by central phases. Such phases cancel from the engineered-square first-order coefficient, so rank and singular values are unchanged.

Let

\[
F_{jk}=p^{-1/2}\omega^{jk}
\]

be the discrete Fourier transform. Then exactly

\[
\boxed{
F^*W_{a,b}F=W_{b,-a}.
}
\tag{1.2}
\]

Write

\[
J(a,b)=(b,-a).
\]

---

## 2. Affine quadratic phase family

For `tau in F_p`, define

\[
\boxed{
P_\tau
=\operatorname{diag}
\left(\omega^{(j^2+\tau j)/2}\right)_{j\in\mathbb F_p}.
}
\tag{2.1}
\]

The quadratic-phase anchor used in the earlier forest note is the noncentered member `tau=-1`.

A direct calculation gives

\[
\boxed{
P_\tau^*W_{a,b}P_\tau
=\omega^{-\tau a/2}W_{a,b-a}.
}
\tag{2.2}
\]

Thus the projective label action is the shear

\[
S(a,b)=(a,b-a).
\]

Define the Fourier-conjugate chirp

\[
\boxed{
Q_\tau=FP_\tau F^*.
}
\tag{2.3}
\]

Then

\[
\boxed{
Q_\tau^*W_{a,b}Q_\tau
=\omega^{-\tau b/2}W_{a+b,b},
}
\tag{2.4}
\]

with projective label action

\[
T(a,b)=(a+b,b).
\]

Multiplying `P_tau,Q_tau,F,W_g` by determinant-correcting scalar phases places every transport in `SU(p)` and leaves every engineered-square coefficient unchanged.

---

## 3. The vertical shear forest

Put

\[
m=\frac{p-1}{2},
\qquad
A_p=\{1,\ldots,m\}.
\]

For each

\[
a\in A_p,
\qquad
k=1,\ldots,p-1,
\]

use the face

\[
\boxed{(P_\tau,W_{a,ka}).}
\tag{3.1}
\]

The projective phase in (2.2) changes only unitary row gauges, so the proof of `ARTICLE-III-QUADRATIC-PHASE-FOREST-CORE-v0.1.md` applies verbatim to every `tau`.

The number of these faces is

\[
K_P=m(p-1)=\frac{(p-1)^2}{2}.
\tag{3.2}
\]

They form `m` disjoint paths through all sign classes with nonzero first coordinate. The surviving component representatives are

\[
H_a=[(a,0)],
\qquad a\in A_p,
\]

together with the isolated vertical classes

\[
V_a=[(0,a)],
\qquad a\in A_p.
\]

Hence after contracting the `P_tau` forest there are exactly

\[
2m=p-1
\]
components.

---

## 4. The horizontal-shear component tree

Use the following `Q_tau` faces.

### Vertical leaves

For every `a in A_p`, take

\[
\boxed{q_a=(-a,a).}
\tag{4.1}
\]

Since

\[
T(-a,a)=(0,a),
\]

the corresponding face joins the `H_a` component to `V_a`.

### Horizontal chain

For

\[
a=1,\ldots,m-1,
\]

take

\[
\boxed{h_a=(a,1).}
\tag{4.2}
\]

Because

\[
T(a,1)=(a+1,1),
\]
this face joins the `H_a` and `H_{a+1}` components.

Thus the component graph is

\[
V_1-H_1-H_2-\cdots-H_m-V_m
\]

with each remaining `V_a` attached as a leaf to `H_a`.

The number of `Q_tau` faces is

\[
K_Q=m+(m-1)=p-2.
\tag{4.3}
\]

### Theorem 4.1 — two-shear spanning tree

The union of the `P_tau` faces (3.1) and the `Q_tau` faces (4.1)--(4.2) is a spanning tree on `Omega_p`.

#### Proof

The `P_tau` forest contracts `Omega_p` to the `2m=p-1` components `H_a,V_a`. The `m` edges (4.1) attach each `V_a` to `H_a`; the `m-1` edges (4.2) connect all `H_a` in a path. Hence the contracted graph is connected and has

\[
m+(m-1)=2m-1
\]

edges on `2m` vertices, so it is a tree. Expanding each contracted `P_tau` component, itself a tree, preserves acyclicity and connectivity. The total number of edges is

\[
\frac{(p-1)^2}{2}+p-2
=\frac{p^2-3}{2}
=|\Omega_p|-1.
\]
QED.

---

## 5. One Fourier cap

Set

\[
\boxed{
g_*=(-1,m).}
\tag{5.1}
\]

Use one final engineered square

\[
\boxed{(F,W_{g_*}).}
\tag{5.2}
\]

Since

\[
Jg_*=(m,1),
\]
its endpoints lie in the `H_1` and `H_m` components. Therefore this face adds exactly one graph cycle to the spanning tree of Theorem 4.1: it closes the horizontal chain

\[
H_1-H_2-\cdots-H_m.
\]

For `p=3` this is a loop on the single `H_1` component; for `p=5` it is a parallel closure of the unique horizontal tree edge; for `p>=7` it is an ordinary cycle.

The total number of faces is

\[
\boxed{
K_P+K_Q+1
=\frac{(p-1)^2}{2}+p-1
=\frac{p^2-1}{2}
=L_p^\sharp.
}
\tag{5.3}

Thus the construction is exactly at the information-theoretic sharp count for every odd prime.

---

## 6. Exact forest-elimination recurrence

Let `D` be a normalized complex-linear `*`-preserving map and put

\[
X_g=D(W_g).
\]

Because of the symmetric Weyl gauge,

\[
X_{-g}=X_g^*.
\tag{6.1}
\]

For a `P_tau` face with label `g`, write

\[
C_g=P_\tau^*W_g^*P_\tau.
\]

The exact first-order square coefficient is

\[
\begin{aligned}
K_D(P_\tau,W_g)
={}&C_gP_\tau^*W_gD(P_\tau)
+C_gP_\tau^*X_gP_\tau\\
&+C_gD(P_\tau^*)W_gP_\tau
+D(C_g)P_\tau^*W_gP_\tau.
\end{aligned}
\tag{6.2}
\]

The first term simplifies to

\[
P_\tau^*D(P_\tau).
\]

Therefore, on the zero set of this face, the child value `X_g` is given explicitly by

\[
\boxed{
\begin{aligned}
X_g=-W_gP_\tau\Bigl[
&P_\tau^*D(P_\tau)
+C_gD(P_\tau^*)W_gP_\tau\\
&+D(C_g)P_\tau^*W_gP_\tau
\Bigr]P_\tau^*.
\end{aligned}}
\tag{6.3}
\]

For the forest label

\[
g=(a,ka),
\]
we have

\[
Sg=(a,(k-1)a),
\]
so `D(C_g)` is a unit-modulus multiple of `X_{-Sg}=X_{Sg}^*`. Hence (6.3) is a genuine one-step recurrence from the parent `k-1` to the child `k`.

Starting from the axis data

\[
\boxed{
\{X_{(a,0)},X_{(0,a)}:a\in A_p\},
}
\tag{6.4}

it reconstructs every nonzero Weyl input value of `D` satisfying all `P_tau` forest equations.

Thus the `P_tau`-forest kernel is parametrized exactly by

\[
\boxed{2p^2(p-1)}
\]
real axis coordinates.

---

## 7. Exact reduced completion matrix

Let

\[
\mathcal E_{p,\tau}
\]

denote the linear extension operator defined by recurrence (6.3): it takes the axis data (6.4) to the full normalized `*`-preserving map in the `P_tau`-forest kernel.

Let

\[
\mathcal R_{p,\tau}
\]
be the stacked first-order measurement map of the `p-2` `Q_tau` faces and the final Fourier face, restricted through `E_{p,tau}`.

Then

\[
\boxed{
\mathcal R_{p,\tau}:
\mathbb R^{2p^2(p-1)}
\longrightarrow
\mathbb R^{2p^2(p-1)}.
}
\tag{7.1}

Hamiltonian derivations give a kernel of dimension `p^2-1`. Consequently the deterministic sharp design is universally identifying iff

\[
\boxed{
\operatorname{rank}\mathcal R_{p,\tau}
=2p^2(p-1)-(p^2-1)
=2p^3-3p^2+1.
}
\tag{7.2}

This is an exact reduction from the original ambient normalized-map dimension `Theta(p^4)` to a structured `Theta(p^3)` square residual matrix.

If the `Q_tau` tree block has full row rank, its rank is exactly

\[
\boxed{2p^2(p-2),}
\tag{7.3}

leaving a real kernel of dimension `2p^2`. The final Fourier face must then contribute exactly

\[
\boxed{p^2+1}
\tag{7.4}

new directions, leaving precisely the `p^2-1` Hamiltonian gauge.

Thus the old `p-1`-face Fourier-completion problem has collapsed to a **single-face cycle problem after a spanning tree**.

---

## 8. Polynomial conditioning of the forest elimination

The recurrence itself does not hide a superpolynomial loss.

The nonidentity Weyl coefficients of the quadratic chirp have modulus `p^{-1/2}`. Hence, in the natural sign-class Hilbert norm, the evaluation map

\[
(X_{(0,a)})_a\mapsto D(P_\tau)
\]

has operator norm `O(1)`.

Each recurrence step (6.3) consists of unitary left/right multiplications plus at most three terms involving `D(P_tau)` or the parent value. Therefore along a path of length at most `p-1`,

\[
\|X_{a,ka}\|
\le
\|X_{a,0}\|+Cp\|D(P_\tau)\|.
\tag{8.1}
\]

Summing over all `O(p^2)` reconstructed fibers gives the crude but sufficient bound

\[
\boxed{
\|\mathcal E_{p,\tau}\|\le Cp^2.
}
\tag{8.2}

The axis restriction is a left inverse of `E_{p,tau}`, so

\[
\|\mathcal E_{p,\tau}^{-1}\|\le1
\]

on its range in the corresponding coordinate normalization.

Therefore any inverse-polynomial lower gap for the reduced tree/cap map lifts to an inverse-polynomial lower gap for the full sharp design. No recursive-in-dimension multiplication appears.

---

## 9. Deterministic reduced census

The recurrence (6.3) was implemented directly, without first constructing the full `Theta(p^4)` domain matrix. For the canonical noncentered choice `tau=1`, the deterministic label set of Sections 3--5 gives:

| `p` | residual size `2p^2(p-1)` | `Q`-tree rank | final total rank | target | reduced `sigma_min^+` |
|---:|---:|---:|---:|---:|---:|
| 3 | 36 | 18 | 28 | 28 | 0.413546 |
| 5 | 200 | 150 | 176 | 176 | 0.140523 |
| 7 | 588 | 490 | 540 | 540 | 0.076482 |
| 11 | 2420 | 2178 | 2300 | 2300 | 0.045451 |
| 13 | 4056 | 3718 | 3888 | 3888 | 0.038233 |

For `p=5,7,11,13`, the `Q`-tree smallest singular values observed were respectively approximately

\[
0.11987,\ 0.07413,\ 0.03359,\ 0.02624,
\]

consistent with an `Omega(p^{-2})` scale.

After projecting the final Fourier face off the `Q`-tree rowspace, its nonzero rank is exactly `p^2+1` in every tested prime, with smallest positive singular values approximately

\[
0.3199,\ 0.2357,\ 0.1529,\ 0.1474
\]

for `p=5,7,11,13`, consistent with an `Omega(p^{-1})` scale.

These are floating-point diagnostics, not all-prime proofs.

A direct full ambient calculation independently confirms the sharp quotient rank for `p=3,5,7`.

---

## 10. Why the affine shift matters

Let

\[
\Pi=F^2
\]

be parity, `Pi|j>=|-j>`.

For the centered chirp `tau=0`,

\[
\Pi P_0\Pi=P_0,
\qquad
\Pi Q_0\Pi=Q_0,
\qquad
\Pi F=F\Pi.
\tag{10.1}
\]

More generally,

\[
\boxed{
\Pi P_\tau\Pi=P_{-\tau},
\qquad
\Pi Q_\tau\Pi=Q_{-\tau}.
}
\tag{10.2}

Thus `tau=0` has an exact global parity symmetry, while every nonzero affine shift breaks that symmetry inside the chosen one-cycle design.

In the deterministic full matrix census, the centered design has extra quotient nullity `1` at `p=5` and `2` at `p=7`, whereas every tested nonzero `tau` gives full sharp rank. This strongly suggests that the missing final determinant contains an affine-flux factor and that the centered obstruction has dimension `(p-3)/2`.

The exact `(p-3)/2` nullity formula is a research target here, not yet a theorem.

---

## 11. New strict theorem target — tree plus affine flux

The sharp odd-prime problem is now reduced to two explicit statements about `R_{p,tau}`.

### Target A — horizontal tree gap

For every odd prime `p` and every nonzero `tau`, prove

\[
\boxed{
\sigma_{\min}^{+}(\mathcal R^{Q}_{p,\tau})
\ge cp^{-2},
}
\tag{11.1}

where `R^Q` is the first `p-2` face block.

### Target B — one-cycle Fourier cap

On the `2p^2`-dimensional kernel left by Target A, prove that the final face `(F,W_{(-1,m)})` has

\[
\boxed{
\operatorname{rank}=p^2+1
}
\tag{11.2}

and

\[
\boxed{
\sigma_{\min}^{+}\ge cp^{-1}.
}
\tag{11.3}

Its kernel must then be exactly the `p^2-1` dimensional Hamiltonian derivation space.

Together with (8.2), these two estimates would prove a fresh explicit sharp robust Coxeter theorem for every odd prime dimension.

The geometry is now sufficiently rigid that the remaining proof should be sought as a **cycle-holonomy / twisted-incidence factorization**, not as generic restricted invertibility.

---

## 12. Claim firewall

This note proves:

- the exact affine Clifford actions (2.2) and (2.4);
- the deterministic two-shear spanning-tree theorem on Weyl sign classes;
- the exact sharp face count after adding one Fourier cap;
- the exact forest-elimination recurrence;
- the reduction of the completion problem to a structured `Theta(p^3)` residual matrix and, conditionally on tree rank, a single `2p^2` cycle block;
- polynomial conditioning of the forest parameterization.

It records numerical, not symbolic, certificates for the `Q`-tree full-row-rank and one-cycle cap ranks at `p=3,5,7,11,13`.

It does **not** yet claim:

- Target A for every odd prime;
- Target B for every odd prime;
- the centered-nullity formula `(p-3)/2`;
- sharp polynomial robustness in arbitrary odd prime dimension;
- an even/composite analogue.
