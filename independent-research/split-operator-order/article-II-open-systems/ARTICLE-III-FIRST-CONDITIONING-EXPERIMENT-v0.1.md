# Article III — First Conditioning Experiment

**Author:** Malachevsky, A.A. / Малачевский А.А.  
**ORCID:** 0009-0008-6009-3196  
**Date:** 2026-09-06  
**Status:** `NUMERICAL_EVIDENCE / NORMALIZATION_DECLARED / THEOREM_PENDING`

## 0. Purpose

This note performs the first real singular-value experiment for the Coxeter measurement operators used in Article II. It is explicitly not a theorem. Its role is to test whether algebraically minimal designs are plausibly stable and whether small amounts of genuine geometric redundancy improve the lower frame bound.

The experiment reconstructs the Article-II real/complex measurement operator from the same qutrit and d=4 face specifications used in the exact rank certificates and from the same 12 engineered squares used in the d=5 certificate. The finite-field rank certificates are not themselves used for metric information.

---

## 1. Domain metric

Let `q=d^2-1` and let `F_a` be an orthonormal traceless-Hermitian basis for the normalized Hilbert-Schmidt product

\[
\tau(X^*Y)=\frac1d\operatorname{Tr}(X^*Y).
\]

A dissipative tangent is parametrized by a Hermitian Kossakowski matrix `C in Herm(q)`:

\[
\mathcal L_C(X)
=
\sum_{a,b} C_{ab}
\left(F_aXF_b-\frac12\{F_aF_b,X\}\right).
\]

For the real Frobenius geometry on `Herm(q)`, the superoperator Hilbert metric induced by normalized Hilbert-Schmidt geometry has Gram form

\[
\boxed{
G_d(C,D)
=
\operatorname{Tr}(CD)
+\operatorname{Tr}(C)\operatorname{Tr}(D)
+\frac12\,\tau(K_C^0K_D^0),
}
\]

where

\[
K_C=\sum_{a,b}C_{ab}F_aF_b,
\qquad
K_C^0=K_C-\operatorname{Tr}(C)I.
\]

Numerically, the Hamiltonian derivation sector is orthogonal to this dissipative parametrization in the chosen normalized superoperator Hilbert metric, so no further quotient correction is needed for the present Kossakowski coordinates.

The spectrum of `G_d` was found exactly to machine precision to be

\[
\boxed{
\operatorname{spec}(G_d)
=
\{1,\ d^2/2,\ d^2\}
}
\]

with multiplicities

\[
\boxed{
(d^2-1)^2-(d^2-1)-1=d^4-3d^2+1,
\quad d^2-1,
\quad 1.
}
\]

Checked numerically:

- `d=2`: `1^(x5), 2^(x3), 4^(x1)`;
- `d=3`: `1^(x55), 4.5^(x8), 9^(x1)`;
- `d=4`: `1^(x209), 8^(x15), 16^(x1)`;
- `d=5`: `1^(x551), 12.5^(x24), 25^(x1)`.

This spectral pattern is strong enough to deserve an analytic proof in the next theorem note.

---

## 2. Output metric

For a design with `L` matrix-valued faces, the output norm is

\[
\|(Y_f)\|^2
=
\frac1L\sum_f \frac1d\operatorname{Tr}(Y_f^*Y_f).
\]

Thus each stacked real/imaginary matrix block is scaled by `1/sqrt(dL)`, and the domain is whitened by `G_d^{-1/2}`.

No arbitrary row rescaling is used.

For the qutrit and d=4 Coxeter loops, all braid faces in the baseline designs have equal six-edge length except the one qutrit commuting-square face. Because condition number is invariant under a common scalar but not under heterogeneous face rescaling, the primary reported values below use the raw first-order face coefficient with equal face weight. A path-length-normalized diagnostic was also checked; it does not change the qualitative conclusion.

---

## 3. Baseline Article-II designs

### d=3

The four-face qutrit design from `qutrit_rank_certificate_v010.py` gives a real measurement matrix of shape

\[
72\times64
\]

and full numerical rank `64`.

After domain whitening and averaged normalized output scaling:

\[
\sigma_{\min}\approx0.1217388041,
\]

\[
\sigma_{\max}\approx4.5994104323,
\]

\[
\boxed{\kappa\approx37.78097},
\]

\[
A\approx1.48203\times10^{-2},
\qquad
B\approx21.15458.
\]

### d=4

The eight-face design from `exact_face_rank_certificate_d4_v010.py` gives shape

\[
256\times225
\]

and full numerical rank `225`.

Normalized singular data:

\[
\sigma_{\min}\approx0.0535512400,
\]

\[
\sigma_{\max}\approx4.3512436875,
\]

\[
\boxed{\kappa\approx81.25384},
\]

\[
A\approx2.86774\times10^{-3},
\qquad
B\approx18.93332.
\]

### d=5

The twelve engineered squares from `exact_face_rank_certificate_d5_v010.py` reconstruct a real matrix of shape

\[
600\times576
\]

and full numerical rank `576`.

Normalized singular data:

\[
\sigma_{\min}\approx0.0397866513,
\]

\[
\sigma_{\max}\approx4.8436282258,
\]

\[
\boxed{\kappa\approx121.74003},
\]

\[
A\approx1.58298\times10^{-3},
\qquad
B\approx23.46073.
\]

These three data points are consistent with deterioration of the baseline construction with dimension, but they are far too few to support an asymptotic claim.

---

## 4. Sharp-design search inside a fixed d=3/d=4 Coxeter pool

For `d=3,4` a deterministic pool of 72 Coxeter faces was generated from all 24 permutations of four fixed gates and three loop types:

- braid word `[0,1]^3`;
- braid word `[1,2]^3`;
- commuting square `[0,2,0,2]`.

The baseline designs were then compared with local one-face exchange and random sharp-design search.

### d=3

Baseline four-face condition number:

\[
\kappa\approx37.78.
\]

A local exchange search raised the lower frame bound from

\[
A\approx0.01482
\]

to

\[
A\approx0.03585
\]

and reduced the condition number to about

\[
\kappa\approx26.16.
\]

A 3000-sample random search found a four-face design with

\[
\boxed{
A\approx0.03980,
\qquad
\kappa\approx21.52.
}
\]

Thus the original Article-II qutrit rank witness is not even close to an apparent conditioning optimum inside this small pool.

### d=4

Baseline eight-face condition number:

\[
\kappa\approx81.25.
\]

A single local face exchange produced

\[
A\approx0.00559249,
\qquad
\boxed{\kappa\approx56.45}.
\]

A 1200-sample random sharp-design search did not beat that local result.

Again, the Article-II rank witness is not conditioning-optimal.

---

## 5. Redundancy experiment

Because the output norm is averaged over faces, simple replication gives no gain. The following improvements therefore come from genuinely new face geometry.

Starting from the locally improved sharp design:

### d=3

- `L=4`: `A≈0.03585`, `kappa≈26.16`;
- `L=5`: `A≈0.11742`, `kappa≈13.48`;
- `L=6`: `A≈0.23446`, `kappa≈9.17`;
- `L=7`: `A≈0.33024`, `kappa≈7.37`.

### d=4

- `L=8`: `A≈0.005592`, `kappa≈56.45`;
- `L=9`: `A≈0.015484`, `kappa≈33.98`;
- `L=10`: `A≈0.026052`, `kappa≈26.14`;
- `L=11`: `A≈0.031720`, `kappa≈23.99`.

This is the first numerical evidence in the programme for a possible **robustness gap**: a small amount of genuine oversampling can improve the lower frame bound by factors much larger than would be explained by measurement duplication.

No theorem is claimed yet.

---

## 6. Immediate mathematical consequence

The most important finding is not the numerical value of any one condition number. It is the structural separation

\[
\boxed{
\text{rank-optimal design}
\neq
\text{conditioning-optimal design}
}
\]

already visible at `d=3` and `d=4` inside the fixed gate pool.

Article II therefore solved only the injectivity threshold. Article III has a genuinely new optimization problem even before statistical noise and sample complexity are introduced.

---

## 7. Next theorem target

The Gram-spectrum experiment suggests the exact statement

\[
\boxed{
\operatorname{spec}(G_d)
=
\{1,d^2/2,d^2\}
}
\]

with multiplicities

\[
d^4-3d^2+1,\qquad d^2-1,\qquad1.
\]

The next analytic task is to prove this by decomposing `Herm(su(d))` under the adjoint `SU(d)` action and identifying the scalar, adjoint, and orthogonal sectors of the map

\[
C\mapsto K_C^0.
\]

A proof would remove the remaining numerical whitening step and give a closed-form canonical domain normalization for all dimensions.

After that, the next computational task is to construct dimension-scalable normalized face pools and determine whether

\[
\kappa_d^{\rm sharp}
\]

remains polynomial, and whether a bounded redundancy ratio can enforce a dimension-independent or polynomial lower frame bound.

---

## 8. Claim firewall

The present evidence does **not** prove:

- asymptotic ill-conditioning of all sharp designs;
- optimality of the local or random-search designs;
- existence of a universal redundancy threshold;
- noise robustness or sample-complexity bounds;
- experimental practicality;
- any process-tensor or non-Markovian extension.

It does establish a reproducible and mathematically normalized conditioning problem, and it provides the first evidence that redundancy can materially improve stable injectivity.
