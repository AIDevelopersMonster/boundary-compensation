# BC-IDPR P5-UA01 Appendix A — Exact Ideal-Projective Two-Channel Frame Benchmark

**Artifact:** `BC-IDPR-P5-UA01-AUX-IDEAL-PROJECTIVE-FRAME`  
**Status:** `EXACT_AUXILIARY_BENCHMARK_CERTIFIED / PHYSICAL_P5_GATE_OPEN`  
**Scope:** arbitrary real pure states acting on `Sym_0(2,R)`; not the inherited N15 projected-torus coherent-state protocol.

## 1. Benchmark space

Let

\[
V=\operatorname{Sym}_0(2,\mathbb R)
\]

with Hilbert--Schmidt orthonormal basis

\[
E_z=\frac1{\sqrt2}\begin{pmatrix}1&0\\0&-1\end{pmatrix},
\qquad
E_x=\frac1{\sqrt2}\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]

For a real unit vector `z`, define

\[
v(z)=\bigl(z^TE_z z,\ z^TE_x z\bigr)^T.
\]

## 2. Exact E-optimal theorem

Use

\[
z_+=(1,0)^T,\quad z_-=(0,1)^T,
\quad x_\pm=2^{-1/2}(1,\pm1)^T
\]

with equal weights `1/4`. Their frame operator is

\[
F_*=\sum_a w_av_av_a^T=\frac14I_2.
\]

### Theorem

Among all probability designs supported on real pure states in this coefficient space,

\[
\boxed{\max\lambda_{\min}(F)=\frac14}.
\]

### Proof

Writing `z=(cos alpha,sin alpha)^T` gives

\[
v(z)=\frac1{\sqrt2}(\cos2\alpha,\sin2\alpha)^T,
\qquad \|v(z)\|^2=\frac12.
\]

Thus every probability design has `tr F=1/2`, hence `lambda_min(F)<=1/4`. The four-state design attains equality. ∎

A dual/KKT certificate is

\[
Z_*=\frac12I_2,
\qquad \operatorname{tr}Z_*=1,
\qquad v(z)^TZ_*v(z)=\frac14.
\]

## 3. Coordinate-transfer identity

For an operator basis `B_alpha=sum_j C_{j alpha}E_j`, the same ideal design gives

\[
F_B=\frac14C^TC,
\qquad
\lambda_{\min}(F_B)=\frac14\sigma_{\min}(C)^2.
\]

This is an exact coefficient-space benchmark.

## 4. Programme role after scope correction

The physical P5 observation map inherited from N15 is different: it uses projected torus coherent states on a frozen chart, quadrature weights, and the residual plane `span{R_bulk,W}`. Its frame constant is the smallest generalized eigenvalue of the physical symbol-Gram/HS-Gram pair.

Therefore:

- `1/4` is a sharp ideal upper-reference value;
- it is useful for synthetic tests and normalization audits;
- it does not certify the N15 physical frame;
- no UA01 physical gate is closed by this theorem;
- P2 remains blocked.

The gate-closing matrix is defined in `PHYSICAL_RESIDUAL_FRAME_PROTOCOL.md`.

## 5. Claim firewall

The theorem is exact but applies only to arbitrary real pure states in a two-dimensional coefficient model. It does not establish that those states belong to the registered physical coherent-state family, and it proves no uniform physical lower bound, global gluing, continuum limit, or dynamics.
