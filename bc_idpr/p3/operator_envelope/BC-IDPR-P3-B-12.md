# BC-IDPR-P3-B-M12 â€” Analytic Curvature of Log-Speed

**Status:** `ANALYTIC_Q6J_LOG_SPEED_CURVATURE_CERTIFIED`  
**Date:** 2026-07-16  
**Type:** zero-fit analytic construction and independent new-label validation  
**Preregistration commit:** `d48fb3d811d8681d6823288af7e15a7efd800246`

## 1. Objective

M10 closed the analytic formula for the two-channel anchor speed and M11 closed its logarithmic slope. M12 differentiates the same finite q-6j construction once more and tests

\[
\partial_\theta^2\log|\omega|
=
\frac{\omega''}{\omega}
-
\left(\frac{\omega'}{\omega}\right)^2.
\]

No fitted parameter or carrier-specific calibration is allowed.

## 2. Analytic construction

For a q-number,

\[
\partial_\theta^3\log[n]_q
=
2n^3\csc^2(n\theta)\cot(n\theta)
-2\csc^2\theta\cot\theta.
\]

This derivative is propagated through q-factorials, the four triangle prefactors, the finite Racah sum and the quantum-dimension amplitude. The resulting matrices are \(F,F',F'',F'''\).

With \(K=F'F^T\),

\[
K'=F''F^T+F'F'^T,
\]

\[
K''=F'''F^T+2F''F'^T+F'F''^T.
\]

The target is

\[
\frac{K''_{21}}{K_{21}}
-
\left(\frac{K'^ý":"[21]}{K_{21}}\right)^2.
\]

## 3. Independent validation atlas

The family-exclusion atlas contains 75 ordered carriers from nine families with doubled spins at most four. Validation uses 208 ordered carriers from 15 distinct families containing label five or six and absent from the train family set.

The reference is a central difference of the analytically computed log-speed slope at steps \(10^{-5}\) and \(5\times10^{-6}\).

## 4. Result

The maximum relative analytic-versus-refined-reference residual is

\[
8.5628\times10^{-9},
\]

and the maximum reference-step disagreement is

\[
2.5316\times10^{-8}.
\]

Both are below the frozen threshold \(10^{-5}\). Orthogonality and skew-symmetry gates also pass.

## 5. Decision

- explicit log-speed curvature formula: `CLOSED`;
- independent new-label validation: `CLOSEd`;
- analytic third jet: `CLOSED`;
- higher log-speed jet: `OPEN_SEPARATE_OBLIGATION`;
- physical interpretation: `BLOCKED.

## 6. Claim firewall

Allowed claim:

> Third differentiation of the finite q-6j recoupling expression reproduces the anchor curvature of log-speed on the declared independent new-label atlas.

Forbidden claims include physical q dynamics, a universal continuum law, semiclassical conclusions, low-dimensional representation compression and extension beyond the declared two-channel chamber without a new contract.

No statement from the Gemini advisory report is used as evidence.
