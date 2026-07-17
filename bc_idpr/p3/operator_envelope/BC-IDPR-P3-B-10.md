# BC-IDPR-P3-B-M10 — Analytic Anchor-Speed Invariant

**Status:** `ANALYTIC_Q6J_ANCHOR_SPEED_INVARIANT_CERTIFIED`  
**Date:** 2026-07-16  
**Preregistration:** `1f2d9f8ccbaae9273987cc8686627f6ef9cfdae6`

## 1. Objective

M9R showed that permutation-equivariant descriptors improve out-of-range prediction but do not predict the full local jet accurately enough. M10 narrows the obligation to the anchor angular speed only and replaces learned prediction by an explicit analytic derivative of the finite q-Racah formula.

For a real orthogonal two-channel recoupling matrix,

\[
K(\theta)=F'(\theta)F(\theta)^T
\]

is skew symmetric. Therefore

\[
I_C(\theta)=\frac{\|K(\theta)\|_{HS}}{\sqrt2}=|\omega_C(\theta)|.
\]

## 2. Analytic derivative

For the trigonometric q-number

\[
[n]_q=\frac{\sin(n\theta)}{\sin\theta},
\]

M10 uses

\[
\partial_\theta\log[n]_q=n\cot(n\theta)-\cot\theta.
\]

The logarithmic derivative of a q-factorial is the corresponding finite sum. Each Delta prefactor and every summand of the finite q-6j Racah sum is differentiated term by term. This gives an explicit matrix derivative \(F'_{\mathrm{analytic}}(\theta_0)\) with no fitted parameters.

## 3. Independent validation atlas

The label-1-to-4 atlas is used only to exclude previously represented families. The primary test atlas contains every valid two-channel ordered carrier with labels up to 6 whose unordered external-spin family contains a label 5 or 6 and is absent from the old atlas.

The resulting test contains 208 ordered carriers in 15 independent representation families.

## 4. Result

Across the full test atlas:

\[
\max \frac{|I_{\mathrm{analytic}}-I_{\mathrm{FD,refined}}|}{\max(I_{\mathrm{analytic}},I_{\mathrm{FD,refined}})}
=2.03\times10^{-9},
\]

while the preregistered limit was \(10^{-7}\).

The disagreement between finite-difference steps \(10^{-5}\) and \(5\times10^{-6}\) is at most

\[
6.09\times10^{-9}.
\]

Maximum orthogonality and generator-skew residuals are

\[
1.14\times10^{-15},\qquad 2.39\times10^{-14}.
\]

All frozen criteria pass.

## 5. Decision

Closed:

- explicit analytic anchor-speed formula;
- independent new-label validation for the declared two-channel regular chamber.

Still open:

- low-dimensional compression of the finite derivative formula into a small representation invariant;
- analytic formulas and transfer claims for \(\omega'\) and \(\omega''\).

Blocked:

- physical interpretation;
- extrapolation beyond the declared chamber and two-channel class.

## 6. Allowed claim

> The termwise analytic derivative of the finite q-6j Racah expression reproduces the two-channel anchor-speed invariant on all 208 declared new-label ordered carriers, with maximum relative residual below \(2.1\times10^{-9}\).

This is an explicit evaluation formula, not a learned universal representation law.

No statement from the Gemini advisory report is used as evidence.
