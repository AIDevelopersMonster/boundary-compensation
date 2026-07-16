# BC-IDPR-P3-B-M6 — Representation-Normalized Recoupling Jacobian

**Status:** `RECOUPLING_JACOBIAN_FACTORIZATION_CERTIFIED_SCALAR_NORMALIZATION_INSUFFICIENT`  
**Date:** 2026-07-16

## 1. Purpose

P1-PILOT-03R showed that a fixed two-coefficient q-number model fits each two-channel carrier locally but does not transfer between carriers. M6 therefore asks a construction-level question:

> Which part of the differential response is forced by two-channel representation geometry, and can elementary Casimir-gap normalizations remove the remaining carrier dependence?

No cross-carrier law is fitted in this module.

## 2. Declared atlas

Five valid two-channel carriers are frozen:

- `A_M5`: doubled spins `(1,2,4,5)`;
- `B_PILOT03R`: `(1,1,2,2)`;
- `C_MINIMAL`: `(1,1,1,1)`;
- `D_BALANCED`: `(1,3,3,3)`;
- `E_ASYMMETRIC`: `(1,2,3,4)`.

All are evaluated on `theta in [pi/15,pi/10]` with anchor `pi/12`.

## 3. Representation Jacobian

For a real orthogonal two-channel recoupling matrix `F(theta)`, define

\[
K(\theta)=F'(\theta)F(\theta)^T.
\]

Differentiating `F F^T=I` gives

\[
K+K^T=0.
\]

Hence in dimension two

\[
K(\theta)=
\begin{pmatrix}
0&-\omega(\theta)\\
\omega(\theta)&0
\end{pmatrix}.
\]

The scalar `omega` is the carrier's recoupling angular speed.

## 4. Exact operator factorization

Let

\[
Y(\theta)=F(\theta) D F(\theta)^T,
\qquad D=\operatorname{diag}(d_1,d_2).
\]

Then

\[
Y'=[K,Y],
\]

and for a two-channel carrier

\[
\|Y'(\theta)\|_{HS}
=\sqrt{2}\,|d_2-d_1|\,|\omega(\theta)|.
\]

Across the five-carrier atlas, the maximum numerical relative residual of this identity is below `1.88e-10`. This closes the representation-Jacobian factorization gate.

## 5. Scalar normalization audit

At the anchor, the raw angular speeds have coefficient of variation

\[
CV(|\omega|)=0.5485453421.
\]

Two representation-computable candidates were tested:

\[
\frac{|\omega|}{\sqrt{\Delta C_E\Delta C_F}},
\qquad
\frac{|\omega|}{\Delta C_E\Delta C_F}.
\]

Their atlas CV values are respectively

\[
0.3612386192,
\qquad
0.1147239322.
\]

The preregistered collapse threshold is `0.10`; therefore neither candidate closes the carrier dependence. The product-gap normalization is close but remains outside the declared gate.

## 6. Shape audit

Removing the anchor scale alone gives

\[
\rho_C(\theta)=
\frac{|\omega_C(\theta)|}{|\omega_C(\theta_0)|}.
\]

The largest pairwise difference across the atlas is

\[
\max_{C,D,\theta}|\rho_C(\theta)-\rho_D(\theta)|
=0.3348046725,
\]

above the allowed `0.10`. Thus carrier dependence is present not only in amplitude but also in curve shape.

## 7. Decision

Closed:

- two-channel skew-generator structure;
- exact channel-gap/operator-response factorization;
- five-carrier numerical audit.

Rejected on the declared atlas:

- Casimir-gap-only scalar collapse;
- anchor-scale-only shape collapse.

The next cross-carrier pilot remains blocked pending a richer representation map, likely involving the full anchor matrix `F(theta0)`, its Jacobian, and channel-position data rather than a single scalar scale.

## 8. Claim firewall

Allowed claim:

> In the declared two-channel atlas, differential conjugation response factors exactly through the channel eigenvalue gap and the recoupling angular speed, but elementary Casimir-gap and anchor-scale normalizations do not remove carrier dependence.

Forbidden claims include a universal normalized phase law, impossibility of all representation-aware normalization, physical q dynamics, semiclassical interpretation, and extrapolation beyond the declared atlas.

No statement from the Gemini advisory report is used as evidence.
