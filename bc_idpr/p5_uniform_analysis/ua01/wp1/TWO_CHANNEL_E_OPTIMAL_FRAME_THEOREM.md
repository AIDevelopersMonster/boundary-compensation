# BC-IDPR P5-UA01 WP1/WP2 — Exact Two-Channel E-Optimal Frame Theorem

**Contract:** `BC-IDPR-P5-UA01-WP1-WP2`  
**Status:** `EXACT_TWO_CHANNEL_E_OPTIMAL_FRAME_CERTIFIED`  
**Scope:** real traceless symmetric residual operators on a two-channel carrier.

## 1. Residual space

Let

\[
V=\operatorname{Sym}_0(2,\mathbb R)
\]

with Hilbert--Schmidt inner product and orthonormal basis

\[
E_z=\frac1{\sqrt2}
\begin{pmatrix}1&0\\0&-1\end{pmatrix},
\qquad
E_x=\frac1{\sqrt2}
\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]

For a real unit vector \(z\in\mathbb R^2\), define its lower-symbol measurement vector

\[
v(z)=\bigl(z^TE_z z,\ z^TE_x z\bigr)^T.
\]

## 2. Frozen candidate design

Use the four projective directions

\[
z_+=(1,0)^T,
\quad z_-=(0,1)^T,
\quad x_+=2^{-1/2}(1,1)^T,
\quad x_-=2^{-1/2}(1,-1)^T,
\]

with equal weights \(w_a=1/4\).

Their measurement vectors are

\[
v(z_\pm)=\left(\pm\frac1{\sqrt2},0\right)^T,
\qquad
v(x_\pm)=\left(0,\pm\frac1{\sqrt2}\right)^T.
\]

Hence the frame operator is exactly

\[
F_*=\sum_a w_av_av_a^T=\frac14 I_2.
\]

Therefore

\[
\lambda_{\min}(F_*)=\frac14.
\]

## 3. Theorem

**Theorem 1 — Exact E-optimal design on the two-channel real residual space.**  
Among all probability designs supported on real pure channel states, the largest possible lower frame value is

\[
\boxed{t_*=\frac14}.
\]

The four-state equal-weight design above attains this optimum.

### Proof

Every real unit state has the form \(z=(\cos\alpha,\sin\alpha)^T\), and

\[
v(z)=\frac1{\sqrt2}(\cos2\alpha,\sin2\alpha)^T.
\]

Consequently

\[
\|v(z)\|^2=\frac12
\]

for every admissible candidate. For any probability design,

\[
\operatorname{tr}F
=
\sum_a w_a\|v_a\|^2
=
\frac12.
\]

Since \(F\) is a positive \(2\times2\) matrix,

\[
\lambda_{\min}(F)\le\frac{\operatorname{tr}F}{2}=\frac14.
\]

The declared four-state design gives \(F_*=I_2/4\), so the upper bound is attained. ∎

## 4. Dual/KKT certificate

Take

\[
Z_*=\frac12I_2,
\qquad \operatorname{tr}Z_*=1.
\]

For every real pure-state candidate,

\[
v(z)^TZ_*v(z)=\frac14.
\]

Thus the dual value is \(1/4\), equal to the primal value. Every candidate is a contact point; the primal--dual gap is exactly zero.

## 5. Operator-adapted transfer

Let an operator-adapted basis be related to the canonical basis by

\[
B_\alpha=\sum_{j=1}^2 C_{j\alpha}E_j.
\]

The same design has frame matrix

\[
F_B=C^TF_*C=\frac14C^TC.
\]

Therefore

\[
\boxed{
 c_{\mathrm{frame}}(B)
 =\lambda_{\min}(F_B)
 =\frac14\sigma_{\min}(C)^2.
}
\]

This identifies the first exact P5 mechanism:

\[
\text{coherent-state design constant }\frac14
\quad\times\quad
\text{operator-basis conditioning }\sigma_{\min}(C)^2.
\]

The frame wall is precisely

\[
\sigma_{\min}(C)=0.
\]

## 6. Consequence for UA01

The coherent-state design problem is solved exactly for the real two-channel residual sector. The remaining nontrivial P5 work is not to optimize this canonical design again, but to construct and bound the operator-adapted coordinate map \(C_J(\theta)\) on the declared carrier chamber:

\[
\inf_{J,\theta}\sigma_{\min}(C_J(\theta))>0.
\]

A positive bound immediately yields

\[
\underline c_{\mathrm{frame}}
\ge
\frac14
\inf_{J,\theta}\sigma_{\min}(C_J(\theta))^2.
\]

## 7. Claim firewall

This theorem establishes an exact finite-dimensional design result only for the declared real two-channel residual space. It does not establish an arbitrary-channel frame theorem, global gluing, a continuum limit, or physical dynamics.
