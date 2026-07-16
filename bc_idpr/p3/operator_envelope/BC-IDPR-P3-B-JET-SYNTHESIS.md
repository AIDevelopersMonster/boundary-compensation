# BC-IDPR P3-B Jet Calculus Synthesis

**Status:** `FINITE_Q6J_RECURSIVE_JET_CALCULUS_CERTIFIED_THROUGH_LOG_ORDER_2`  
**Date:** 2026-07-16  
**Type:** synthesis theorem, recursive implementation, and regression certificate

## 1. Purpose

M10–M12 separately differentiated the finite q-6j Racah expression through first, second, and third matrix order. This synthesis replaces those hand-expanded chains by one truncated-Taylor algebra.

The coefficient convention is

\[
a_r(f;\theta_0)=\frac{f^{(r)}(\theta_0)}{r!}.
\]

Products, quotients, square roots, and finite sums are propagated in the truncated series ring. Since every q-6j expression in the declared chamber is a finite composition of these operations, its jet exists to every finite order as long as the denominators and chosen square-root branches remain regular.

## 2. General finite-order lemma

Let the q-number, q-factorials, triangle prefactors, and every summand of the finite Racah sum be regular at \(\theta_0\). Then, for every finite order \(N\), the jet

\[
J_NF(\theta_0)=\sum_{r=0}^N F_r(\theta-\theta_0)^r
\]

is obtained exactly in truncated Taylor algebra.

For

\[
K(\theta)=F'(\theta)F(\theta)^T,
\]

the normalized coefficients satisfy

\[
K_r=\sum_{a=0}^{r}(a+1)F_{a+1}F_{r-a}^{T}.
\]

In a two-channel regular chamber, the signed local angular speed is the \((2,1)\) entry of \(K\). After freezing its local sign, the jet of \(\log|\omega|\) follows from the formal logarithm recurrence.

This is a finite-order algebraic lemma, not a physical law and not a low-dimensional representation compression.

## 3. Implemented validation ceiling

The implementation is general in requested finite order, but the present regression certificate intentionally stops at:

- matrix derivative order 3;
- log-speed derivative order 2;
- the three obligations already certified in M10–M12.

Orders above this ceiling require a new validation contract rather than automatic claim extension.

## 4. Unified validation

The engine was evaluated on the inherited independent new-label atlas:

\[
208\ \text{ordered carriers in}\ 15\ \text{representation families}.
\]

Maximum relative residuals were

\[
2.03\times10^{-9}
\]

for anchor speed,

\[
1.85\times10^{-9}
\]

for the first derivative of \(\log|\omega|\), and

\[
8.64\times10^{-9}
\]

for its second derivative.

All inherited M10–M12 thresholds pass.

## 5. Decision

Closed:

- general finite-order truncated-Taylor lemma in the declared regular chamber;
- a single recursive implementation reproducing M10–M12;
- independent new-label regression through log order 2.

Open:

- software validation above log order 2;
- uniform conditioning bounds near q-number walls;
- low-dimensional representation compression.

Blocked:

- physical interpretation;
- extrapolation outside the declared chamber;
- claims that arbitrary-order numerical stability has already been proved.

## 6. Claim firewall

Allowed claim:

> Truncated Taylor algebra gives a general finite-order construction for the finite q-6j recoupling jet in a regular chamber, and one recursive implementation reproduces the M10–M12 anchor-speed, log-slope, and log-curvature certificates on the declared independent atlas.

No statement from the Gemini advisory report is used as evidence.
