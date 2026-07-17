# BC-IDPR P5-UA01 WP3 — Spectral-Support and Conditioning Jet Theorem

**Contract:** `BC-IDPR-P5-UA01-WP3-H5B1`  
**Status:** `EXACT_SUPPORT_PROJECTOR_AND_CONDITIONING_JET_CALCULUS_CLOSED / N15_PRIMITIVE_INPUT_BOUNDS_OPEN`  
**Upstream:** `BC-IDPR-P5-UA01-WP3-H5A` physical measurement and whitening jet calculus.  
**Scope:** the thresholded positive-support construction used by the frozen N15 residual-frame protocol.

## 1. Physical support construction

Let `R(theta)` be the positive Hermitian target-overlap matrix used in N15, let `tau>0` be the frozen support threshold, and assume a chamber on which

\[
\operatorname{dist}(\tau,\sigma(R(\theta)))\ge \delta>0.
\]

The support projector and conditioned inverse square root are

\[
P(\theta)=\mathbf 1_{[\tau,\infty)}(R(\theta)),
\qquad
S(\theta)=P(\theta)R(\theta)^{-1/2}P(\theta).
\]

The conditioned target map is

\[
\mathcal C_R(V)=S V S.
\]

A threshold crossing is a support-rank wall. No derivative certificate may be continued through such a crossing.

## 2. Contour representation

Choose one fixed positively oriented contour `Gamma` enclosing the selected spectrum and excluding the rejected spectrum and zero. With

\[
G_z=(zI-R)^{-1},
\]

one has

\[
P=\frac{1}{2\pi i}\oint_\Gamma G_z\,dz,
\]

and, using the principal branch of `z^{-1/2}` on the contour domain,

\[
S=\frac{1}{2\pi i}\oint_\Gamma z^{-1/2}G_z\,dz.
\]

This formulation is gauge-free: it does not differentiate eigenvectors.

## 3. Exact first and second jets

For `f(z)=1` or `f(z)=z^{-1/2}`, define

\[
\mathfrak F_f(R)=\frac{1}{2\pi i}\oint_\Gamma f(z)(zI-R)^{-1}\,dz.
\]

Then

\[
\boxed{
\mathfrak F_f'(R)
=
\frac{1}{2\pi i}\oint_\Gamma
f(z)G_zR'G_z\,dz
}
\]

and

\[
\boxed{
\mathfrak F_f''(R)
=
\frac{1}{2\pi i}\oint_\Gamma
f(z)
\bigl(
G_zR''G_z+2G_zR'G_zR'G_z
\bigr)\,dz.
}
\]

Thus the formulas for `P',P''` are obtained with `f=1`, while those for `S',S''` use `f(z)=z^{-1/2}`.

## 4. Gap-conditioned bounds

Let

\[
\rho=\inf_{z\in\Gamma,\theta\in I}
\operatorname{dist}(z,\sigma(R(\theta)))>0,
\]

and let `ell(Gamma)` be the contour length. Put

\[
K_f=\frac{\ell(\Gamma)}{2\pi}
\sup_{z\in\Gamma}|f(z)|.
\]

Since `||G_z||<=rho^{-1}`,

\[
\boxed{
\|\mathfrak F_f'\|
\le K_f\rho^{-2}\|R'\|
}
\]

and

\[
\boxed{
\|\mathfrak F_f''\|
\le
K_f
\left(
\rho^{-2}\|R''\|
+2\rho^{-3}\|R'\|^2
\right).
}
\]

For a contour chosen at a fixed fraction of the spectral separation, these constants diverge polynomially as the support margin tends to zero. This is the exact support-wall amplification mechanism.

## 5. Jets of conditioned targets

For a twice differentiable Hermitian operator family `V(theta)`, define

\[
T=S V S.
\]

Then

\[
\boxed{
T'=S'VS+SV'S+SVS'
}
\]

and

\[
\boxed{
\begin{aligned}
T''={}&S''VS+SV''S+SVS''\\
&+2S'V'S+2S'VS'+2SV'S'.
\end{aligned}
}
\]

Hence all conditioned N15 target jets reduce to primitive bounds for

\[
R,R',R'',V,V',V''
\]

plus one certified support gap.

## 6. Normalization jets used by N15

For a nonzero matrix path `A(theta)` with

\[
n(\theta)=\|A(\theta)\|_{HS},
\qquad
\widehat A=A/n,
\]

one has

\[
n'=rac{\operatorname{Re}\langle A,A'\rangle_{HS}}{n},
\]

\[
n''=
\frac{\|A'\|_{HS}^2+
\operatorname{Re}\langle A,A''\rangle_{HS}}{n}
-
\frac{\bigl(\operatorname{Re}\langle A,A'\rangle_{HS}\bigr)^2}{n^3},
\]

and

\[
\boxed{
\widehat A'
=
\frac{A'}{n}-\frac{n'}{n}\widehat A
}
\]

\[
\boxed{
\widehat A''
=
\frac{A''}{n}
-2\frac{n'}{n^2}A'
+\left(
2\frac{(n')^2}{n^2}-\frac{n''}{n}
\right)\widehat A.
}
\]

Therefore the N15 residual generators

\[
R_{\rm bulk}=\widehat T_{\rm bulk}-\widehat A_{XY},
\qquad
W=T_{\rm wall}/\|T_{\rm full}\|_{HS}
\]

have explicit first and second jets once the conditioned target and XY candidate jets are supplied.

## 7. Executable verification

The companion script evaluates the contour formulas on a noncommuting four-dimensional synthetic path with moving selected and rejected eigenspaces. It compares the analytic jets against five-point finite differences.

The audit gave:

```text
support rank                       2
threshold gap                     0.4626153144
projector reconstruction error    4.63e-16
inverse-root reconstruction error 9.75e-16
P' relative error                 8.84e-12
P'' relative error                4.03e-7
S' relative error                 9.19e-12
S'' relative error                3.46e-7
conditioned T' relative error     9.20e-12
conditioned T'' relative error    5.52e-7
```

These are implementation checks, not N15 physical constants.

## 8. Gate consequence

```text
UA01-H5A MEASUREMENT/WHITENING CALCULUS: PASS
UA01-H5B1 SUPPORT/CONDITIONING CALCULUS: PASS
UA01-H5B2 N15 PRIMITIVE R,V JET BOUNDS: OPEN
UA01-G1A PHYSICAL MATRIX REPRODUCTION: OPEN
UA01-G2 LOCAL FRAME: BLOCKED
MODE-5 ANALYTIC UNIQUENESS: OPEN
P2 HANDOFF: BLOCKED
```

The next admissible step is to specialize these formulas to the actual N15 q-6j target-overlap matrix, exact XY operator, bulk/wall target matrices, and projected-torus coherent states on one frozen case, then certify the first support margin and primitive jet bounds.

## 9. Claim firewall

This document closes the finite-dimensional spectral-support calculus only. It does not prove that the N15 support rank is constant on the full deformation chamber, does not provide an N15 numerical support margin, does not establish a physical local frame theorem, does not select mode 5, and does not authorize P2.