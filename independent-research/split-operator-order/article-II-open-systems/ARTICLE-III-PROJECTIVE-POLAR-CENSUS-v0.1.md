# Article III — Projective and Polar Support-Frame Census

**Author:** Malachevsky, A.A. / Малачевский А.А.  
**ORCID:** 0009-0008-6009-3196  
**Date:** 2026-09-06  
**Status:** `NUMERICAL_EVIDENCE / GEOMETRY-ONLY NORMALIZATION / NEW SUBSPACE-OVERLAP WALL`

## 0. Purpose

This census executes the normalization hierarchy proved in
`ARTICLE-III-PROJECTIVE-POLAR-FUSION-FRAME-v0.1.md`.

The hierarchy is

\[
\boxed{
\text{exact quotient whitening}
\to
\text{projective face normalization}
\to
\text{polar support normalization}.
}
\]

The first step removes domain-coordinate distortion. The second removes total face amplitude. The third also removes within-face singular-value weighting, leaving only the geometry of the measured subspaces in the dissipative quotient.

The calculations below use the same fixed 72-face Coxeter pool for `d=3,4` as the earlier conditioning experiments. They are finite-pool numerical evidence only.

---

## 1. Projective normalization removes the amplitude ambiguity

For every nonzero face,

\[
Q_f=\frac{C_f^*C_f}{\operatorname{Tr}(C_f^*C_f)},
\qquad
\operatorname{Tr}Q_f=1.
\]

For a design `D`,

\[
\widehat S_D=\frac1L\sum_fQ_f,
\qquad
\operatorname{Tr}\widehat S_D=1.
\]

Thus

\[
\widehat\eta_D=N\lambda_{\min}(\widehat S_D)
\]

is insensitive to total face energy.

### d=3

The original four-face Article-II witness, after projective normalization, has approximately

\[
\widehat\eta\approx0.00455,
\qquad
\widehat\kappa\approx35.47.
\]

The previously sampled four-face sharp redesign gives approximately

\[
\widehat\eta\approx0.01059,
\qquad
\widehat\kappa\approx20.90.
\]

A fresh 5000-sample projective sharp search found

\[
\boxed{
\widehat\eta\approx0.01182,
\qquad
\widehat\kappa\approx19.68.
}
\]

One representative design is

- `((0,3,1,2), c02)`;
- `((1,2,0,3), b01)`;
- `((2,3,1,0), c02)`;
- `((3,1,0,2), c02)`.

Therefore the sharp-design improvement survives after all scalar face-amplitude differences are removed.

### d=4

The original eight-face Article-II witness has approximately

\[
\widehat\eta\approx0.001139,
\qquad
\widehat\kappa\approx80.11.
\]

The known one-face replacement

`((1,0,2,3),b12) -> ((1,2,0,3),c02)`

raises this to

\[
\boxed{
\widehat\eta\approx0.002305,
\qquad
\widehat\kappa\approx55.31.
}
\]

Again, the improvement survives projective normalization.

This closes the simplest amplitude objection: the observed redesign gains are not artifacts of selecting faces with larger total response norms.

---

## 2. Polar support normalization reveals a second hidden variable

For each face let

\[
P_f=\operatorname{proj}_{(\ker C_f)^\perp},
\qquad
R_f=P_f/r_f,
\qquad
r_f=\operatorname{rank}C_f.
\]

This removes not only total energy, but also the singular-value weighting inside the measured subspace.

The remaining design operator is

\[
S_D^{\mathrm{supp}}
=
\frac1L\sum_f\frac{P_f}{r_f}.
\]

### Face ranks in the fixed pool

For `d=3`, every one of the 72 pool faces has rank

\[
\boxed{r_f=18.}
\]

For `d=4`:

- all 48 braid faces have rank `32`;
- 16 commuting-square faces have rank `32`;
- 8 commuting-square faces have rank `16`.

Thus even the support dimensions are not completely uniform in the `d=4` pool.

---

## 3. Geometry-only redundancy survives polar normalization

### d=3

Using the four-face projective sharp seed above, its polar support frame has

\[
\eta_{\mathrm{supp}}\approx0.02628,
\qquad
\kappa_{\mathrm{supp}}\approx10.36,
\qquad
\delta_{\mathrm{supp}}\approx0.8220.
\]

A greedy lower-frame search over genuinely new support subspaces gives:

\[
\begin{array}{c|c|c|c}
L & \eta_{\mathrm{supp}} & \kappa_{\mathrm{supp}} & \delta_{\mathrm{supp}}\\
\hline
4 & 0.02628 & 10.36 & 0.8220\\
5 & 0.05588 & 6.95 & 0.7489\\
6 & 0.09174 & 5.32 & 0.6853\\
7 & 0.14929 & 4.03 & 0.6195\\
8 & 0.17319 & 3.69 & 0.5909\\
9 & 0.19339 & 3.44 & 0.5608\\
10 & 0.22535 & 3.13 & 0.5390\\
11 & 0.23851 & 3.04 & 0.5285\\
12 & 0.24911 & 2.97 & 0.5135
\end{array}
\]

This is strong geometry-only evidence: the gain persists after both face amplitude and within-face singular-value shape are removed.

### d=4

For the one-swap sharp seed, the polar support frame has

\[
\eta_{\mathrm{supp}}\approx0.002691,
\qquad
\kappa_{\mathrm{supp}}\approx39.39,
\qquad
\delta_{\mathrm{supp}}\approx1.0865.
\]

A greedy lower-frame extension gives approximately

\[
\begin{array}{c|c|c|c}
L & \eta_{\mathrm{supp}} & \kappa_{\mathrm{supp}} & \delta_{\mathrm{supp}}\\
\hline
8 & 0.002691 & 39.39 & 1.0865\\
9 & 0.006899 & 24.05 & 1.0296\\
10 & 0.012223 & 17.77 & 1.0003\\
11 & 0.014427 & 16.33 & 0.9757\\
12 & 0.015814 & 15.78 & 0.9695\\
13 & 0.016146 & 15.58 & 0.9727\\
14 & 0.016474 & 15.54 & 0.9855
\end{array}
\]

The large jump from `L=8` to `L=10` again survives complete polar normalization.

However, the improvement saturates rapidly in this fixed pool: unlike `d=3`, the support efficiency remains very small even after six additional faces.

This is the new obstruction.

---

## 4. The next door: pairwise subspace overlap

Once every face has been replaced by its normalized support projector, there is no amplitude left and no within-face singular spectrum left. The only remaining variables are:

- support dimensions `r_f`;
- relative subspace positions, equivalently principal angles;
- higher-order arrangement of the family of supports.

For equal-rank faces the support frame potential is

\[
\operatorname{Tr}[(S_D^{\mathrm{supp}})^2]
=
\frac1{Lr}
+
\frac{L-1}{L}\bar c,
\]

where

\[
\bar c
=
\frac{2}{L(L-1)}
\sum_{f<g}\frac{\operatorname{Tr}(P_fP_g)}{r^2}.
\]

For the `d=3` polar sequence, all faces have rank `18`. The mean normalized cross-overlap stays surprisingly close to the tight-frame lower scale `1/N=1/64`:

- `L=4`: `cross ≈ 0.016393`, ratio to `1/N ≈ 1.049`;
- `L=7`: `cross ≈ 0.015965`, ratio `≈1.022`;
- `L=12`: `cross ≈ 0.016490`, ratio `≈1.055`.

Yet the lower frame efficiency changes by almost an order of magnitude.

Therefore the arithmetic mean of pairwise overlap is not enough to control the weakest direction.

For `d=4`, with the rank-32 part of the greedy sequence, the mean normalized cross-overlap is much higher relative to `1/N=1/225`:

- `L=8`: ratio `≈1.49`;
- `L=9`: ratio `≈1.44`;
- `L=10`: ratio `≈1.44`.

This is consistent with stronger geometric crowding, but it still does not by itself determine `lambda_min`.

Hence the next barrier is no longer merely a frame-energy or pairwise-coherence problem.

It is a **spectral subspace-arrangement problem**.

---

## 5. Frame potential and lower-frame bound are distinct objectives

A separate greedy experiment minimizing the tightness defect rather than maximizing the lower frame bound confirms the distinction.

For `d=3`, at several face counts the defect-minimizing design has a smaller `delta_supp` but also a smaller `eta_supp` than the lower-bound-optimized design. For example at `L=5`:

- `A`-optimized: `eta_supp≈0.05588`, `delta_supp≈0.74887`;
- `delta`-optimized: `eta_supp≈0.04286`, `delta_supp≈0.71461`.

For `d=4` the same split becomes visible around `L=11` and beyond.

Therefore

\[
\boxed{
\text{second-moment isotropy}
\neq
\text{worst-direction robustness}.
}
\]

A theorem based only on frame potential or average pairwise overlap will generally be insufficient to prove a lower bound on `lambda_min`.

---

## 6. New theorem target

The next mathematical target should be stated directly in terms of the smallest eigenvalue of a normalized sum of support projectors:

\[
\boxed{
\lambda_{\min}
\left(
\frac1L\sum_{f\in D}\frac{P_f}{r_f}
\right).
}
\]

The finite-pool evidence suggests two competing possibilities:

1. there exist dimension-scalable Coxeter support families whose normalized projector sums have polynomially controlled spectral gaps;
2. Coxeter support geometry develops increasingly large almost-common blind sectors, forcing a genuine redundancy barrier.

The next structural invariant to inspect is not merely the scalar overlap `Tr(P_fP_g)`, but the spectrum of products and sums of support projectors, including principal-angle distributions and incremental kernel/intersection decay.

A particularly useful exact/combinatorial target is the codimension profile

\[
\boxed{
K_j
=
\dim\bigcap_{f\in D_j}\ker C_f
}
\tag{6.1}
\]

along an ordered family of faces, together with quantitative principal-angle separation once `K_j=0`.

Rank tomography only detects the endpoint `K_L=0`; robust tomography must control how transversely the successive kernels are eliminated.

This is the new door opened by the polar experiment.

---

## 7. Reproducibility

Script:

`examples/article_iii_projective_polar_census_v010.py`

The script rebuilds the 72-face `d=3,4` pools from real/complex Coxeter data, applies the exact theorem-level quotient whitener, constructs projective operators `Q_f`, polar support projectors `P_f/r_f`, and prints sharp/oversampled metrics.

---

## 8. Claim firewall

The census does not prove:

- asymptotic decay of sharp Coxeter support efficiency;
- optimality of any sampled/greedy design;
- that the fixed 72-face pool is representative of all admissible Coxeter geometry;
- a universal redundancy threshold;
- a physical resource interpretation of support normalization;
- sample-complexity or experimental-noise bounds.

What it does show is narrower and useful:

\[
\boxed{
\text{the observed redundancy gain survives removal of amplitude and within-face spectral weighting.}
}
\]

Therefore the remaining obstruction is genuinely geometric at the level of measured quotient subspaces.
