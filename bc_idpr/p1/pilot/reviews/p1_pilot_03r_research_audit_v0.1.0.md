# Research Audit — BC-IDPR-P1-PILOT-03R

**Version:** v0.1.0  
**Date:** 2026-07-16  
**Verdict:** valid negative transfer result.

## 1. Preregistration integrity

The corrected protocol was committed before evaluation as `6642887b79b0df1c16fc11a58d1f31830ea26e5f`. The carriers, interval, predictor bases, error metrics, thresholds and no-refit rule were frozen there.

The earlier `P1-PILOT-03` was not silently repaired. It was separately marked `FRONTIER_INVALIDATED` because its second carrier failed the declared orthogonality gate.

## 2. Carrier validity

Carrier A has angle span `0.1126650736` and maximum orthogonality residual below `3.17e-16`.

Carrier B has angle span `0.02929218949` and maximum orthogonality residual below `3.16e-16`.

Both satisfy the corrected preregistered validity gates.

## 3. Source fits

The q-number source NRMSE values are approximately `0.0034243` on A and `4.80e-5` on B. Both pass the source-fit threshold `0.05` and both improve on their equal-complexity smooth-null source fits.

Thus the transfer failure cannot be attributed to a failure to fit either source carrier.

## 4. No-refit transfer

Applying A coefficients unchanged to B gives q-number target NRMSE `2.83459`, slightly worse than the smooth-null value `2.83439`.

Applying B coefficients unchanged to A gives q-number target NRMSE `0.739807`, only negligibly better than the smooth-null value `0.739812`.

Neither direction passes the maximum target NRMSE `0.15` or the minimum relative advantage `0.10`.

## 5. Scientific interpretation

The result distinguishes carrier-specific interpolation from carrier-neutral prediction. The selected q-number variables are useful coordinates inside each carrier, but their coefficients encode substantial carrier dependence.

The evidence does not establish that no alternative representation-aware normalization can transfer. It only rejects the frozen raw coefficient-transfer hypothesis.

## 6. Claim firewall

Supported:

- both declared carriers are valid two-channel carriers;
- the q-number basis fits each source carrier;
- raw fitted coefficients fail to transfer under the frozen protocol.

Not supported:

- universal non-transfer;
- universal q-number phase law;
- physical interpretation of q;
- semiclassical accuracy;
- a conclusion about predictors not tested here.

No statement from the Gemini advisory report is used as evidence.

## 7. Recommended next step

Do not add more q-number predictors on the same two curves. The next admissible construction is a representation-aware normalization audit: derive coefficient scalings from channel Casimirs or local q-Racah Jacobians before any new transfer test, then preregister that normalization on at least three carriers.
