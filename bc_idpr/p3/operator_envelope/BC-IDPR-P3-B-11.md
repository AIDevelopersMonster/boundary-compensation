# BC-IDPR-P3-B-M11 — Analytic Log-Speed Slope

**Status:** `ANALYTIC_Q6J_LOG_SPEED_SLOPE_CERTIFIED`  
**Date:** 2026-07-16  
**Preregistration commit:** `b39e6456b9af0ad8f5bed738c3e03751a64b19e6`

## 1. Objective

Construct, without regression, the anchor quantity

\[
\frac{\omega'(\theta_0)}{\omega(\theta_0)}
=\partial_\theta\log|\omega(\theta)|\big|_{\theta_0}
\]

from the second derivative of the finite q-6j recoupling formula.

## 2. Analytic construction

For a q-number,

\[
\partial_\theta^2\log[n]_q
=-n^2\csc^2(n\theta)+\csc^2\theta.
\]

This identity is propagated through q-factorials, the four Delta prefactors, the finite Racah sum, and the quantum-dimension amplitude to obtain `F''`.

With

\[
K=F'F^T,
\]

the differentiated generator is

\[
K'=F''F^T+F'F'^T.
\]

In a two-channel carrier,

\[
\frac{\omega'}{\omega}=\frac{K'_{21}}{K_{21}}.
\]

No fitted parameters are used.

## 3. Frozen validation

The validation atlas is inherited from M10: 208 ordered carriers in 15 representation families containing labels 5 or 6 and absent from the label-1-to-4 family set.

The analytic result is compared with central differences of the analytically evaluated angular speed using frozen steps `1e-5` and `5e-6`.

## 4. Result

The maximum relative analytic-versus-refined-reference residual is

\[
1.84\times10^{-9},
\]

against a preregistered threshold of `1e-6`.

The maximum disagreement between the two reference steps is

\[
5.49\times10^{-9}.
\]

Orthogonality, generator skewness, and differentiated-generator skewness gates also pass.

## 5. Claim firewall

Allowed claim:

> The second derivative of the declared finite q-6j recoupling formula reproduces the anchor log-speed slope on the frozen independent new-label atlas.

Not allowed: a compact representation-only formula, a universal physical phase law, a third-jet formula, semiclassical interpretation, or conclusions beyond the declared finite chamber.

No statement from the Gemini advisory report is used as evidence.
