# Research Audit — BC-IDPR-P1-PILOT-02

**Version:** v0.1.0  
**Date:** 2026-07-16  
**Verdict:** restricted positive pilot.

## 1. Procedural audit

The predictor family, equal-dimensional cubic null, 129-point grid, eight blocked folds, thresholds and stopping rule were committed before evaluation in commit `8ee32533dc7991707b3e2e78c43c0096c459da27`. No post-result basis or threshold change is used.

## 2. Numerical verdict

All frozen criteria pass:

- negative-control excursion: `0.0`;
- quotient signal excursion: `0.7695395230687915`;
- recoupling-angle blocked-CV normalized RMSE: `1.7315748008431413e-14`;
- recoupling-angle coefficient instability: `1.1811137319095956e-13`;
- cubic-null blocked-CV normalized RMSE: `0.02411018093919437`;
- relative CV advantage: `0.9999999999992818`.

Nine decision tests are declared and pass.

## 3. Structural interpretation audit

The near-machine-precision fit is not evidence of a newly discovered universal oscillatory law. On a real two-dimensional invariant carrier, the frozen orthogonal recoupling matrix has one angular degree of freedom. Conjugation of a diagonal two-channel observable therefore produces matrix elements built from second harmonics of that angle. The coherent-state expectation inherits that structure.

Accordingly, the positive result certifies internal consistency and model discrimination relative to a cubic in the external parameter. It does not independently predict the angular deformation law.

The preregistered third basis element `sin(4*dphi)` receives coefficient approximately `9.8e-13`, so the observed response is effectively resolved by the first two second-harmonic components. This strengthens the two-channel kinematic reading and weakens any claim of a richer empirical harmonic discovery.

## 4. Relation to P1-PILOT-01

There is no contradiction with the negative first pilot. P1-PILOT-01 attempted to model lower-symbol response directly with fixed harmonics of the external parameter theta and did not outperform a cubic null. P1-PILOT-02 first passes through the internal recoupling angle phi(theta). The excellent fit then follows from the operator structure of a two-channel rotation.

Thus:

- direct external-parameter phase-law evidence remains absent;
- internal recoupling-angle structure is supported;
- the confirmatory phase-law gate remains blocked.

## 5. Claim firewall

### Supported

`TWO_CHANNEL_AFFINE_QUOTIENT_RESPONSE_RESOLVED_BY_PREREGISTERED_RECOUPLING_ANGLE_BASIS`.

### Not supported

- a universal formula for phi(theta);
- carrier-independent phase modulation;
- physical q dynamics;
- absolute-symbol accuracy;
- extrapolation to higher-dimensional carriers.

## 6. Next research obligation

A genuinely informative next pilot must move the prediction target from the lower symbol to the recoupling angle itself. It should preregister q-number-derived predictors for phi(theta), compare them against equal-complexity smooth nulls, and include at least two independently constructed carriers. Reusing the current response-versus-angle identity would be circular.

No statement from the Gemini advisory report is used as evidence.
