# BC-IDPR-P1-PILOT-03R — Corrected Cross-Carrier q-Number Prediction of the Recoupling Angle

**Status:** `PREREGISTERED_CROSS_CARRIER_TRANSFER_CRITERIA_NOT_MET`  
**Date:** 2026-07-16  
**Preregistration commit:** `6642887b79b0df1c16fc11a58d1f31830ea26e5f`

## 1. Question

Can one frozen two-parameter q-number model for

\[
\Delta\phi(\theta)=\phi(\theta)-\phi(\theta_0)
\]

transfer between two different valid two-channel recoupling carriers without any target-carrier refit?

## 2. Carriers

Carrier A uses doubled spins `(1,2,4,5)`, channels `E=(1,3)`, `F=(4,6)`.

Carrier B uses doubled spins `(1,1,2,2)`, channels `E=(0,2)`, `F=(1,3)`.

Both pass the frozen orthogonality and nonzero-angle-span gates.

## 3. Frozen models

The q-number predictor basis is

\[
\log\frac{[2]_q}{[2]_{q_0}},\qquad
\log\frac{[3]_q}{[3]_{q_0}}.
\]

The equal-complexity smooth null is

\[
\theta-\theta_0,\qquad (\theta-\theta_0)^2.
\]

Coefficients are fitted on one source carrier and applied unchanged to the other carrier.

## 4. Result

Both models fit each source carrier accurately. The q-number basis is the better source interpolant in both cases. However, neither coefficient vector transfers to the other carrier.

For A to B:

\[
E_q^{A\to B}=2.83459,\qquad E_0^{A\to B}=2.83439.
\]

For B to A:

\[
E_q^{B\to A}=0.739807,\qquad E_0^{B\to A}=0.739812.
\]

Both exceed the preregistered target threshold `0.15`, and neither achieves the required ten-percent advantage over the smooth null.

## 5. Interpretation

The declared q-number coordinates provide efficient carrier-specific local fits, but the fitted coefficients are not carrier-neutral. Therefore this pilot does not support an independent cross-carrier q-number phase law.

This negative result does not refute q-number structure inside a fixed recoupling problem. It rejects only the frozen two-predictor coefficient-transfer claim for the two declared carriers and interval.

## 6. Claim firewall

Allowed claim:

> The two-predictor q-number basis fits each declared source carrier, but its coefficients do not transfer between the two frozen carriers under the preregistered no-refit protocol.

Forbidden claims include universal phase laws, all-carrier non-transfer, physical q dynamics, semiclassical conclusions and post-hoc predictor replacement.

No statement from the Gemini advisory report is used as evidence.
