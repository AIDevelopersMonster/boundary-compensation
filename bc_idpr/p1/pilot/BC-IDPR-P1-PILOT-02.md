# BC-IDPR-P1-PILOT-02 — Nonuniform Affine-Quotient Recoupling-Angle Discrimination

**Status:** completed frozen exploratory pilot  
**Date:** 2026-07-16  
**Dependencies:** BC-IDPR-P3-B-M5; BC-IDPR-CERT-03  
**Preregistration commit:** `8ee32533dc7991707b3e2e78c43c0096c459da27`

## 1. Question

Does the affine-calibration-invariant response on the nonuniform two-channel carrier follow the preregistered internal recoupling-angle structure more faithfully than an equal-dimensional generic cubic smooth model?

This is not a test of a universal phase law. It is a model-internal discrimination test.

## 2. Frozen data and observable

External spins:

\[
(j_1,j_2,j_3,j_4)=\left(\frac12,1,2,\frac52\right).
\]

The fixed tetrahedron has face-area ratios `1:2:4:5`. On the interval

\[
\theta\in[\pi/15,\pi/10]
\]

with anchor \(\theta_0=\pi/12\), define

\[
u(\theta)=\frac{y(\theta)-y(\theta_{\rm lo})}{y(\theta_{\rm hi})-y(\theta_{\rm lo})},
\qquad z(\theta)=u(\theta)-u(\theta_0),
\]

where \(y\) is the varying \(G_{23}\) lower symbol. The \(G_{12}\) lower symbol is the frozen negative control.

## 3. Preregistered model

Because the carrier dimension is two and the frozen real orthogonal recoupling matrix is a rotation up to fixed signs, define

\[
\phi(\theta)=\operatorname{atan2}(F_{21}(\theta),F_{11}(\theta)),
\qquad \Delta\phi=\phi(\theta)-\phi(\theta_0).
\]

The preregistered structural design is

\[
\operatorname{span}\{\sin(2\Delta\phi),\;1-\cos(2\Delta\phi),\;\sin(4\Delta\phi)\}.
\]

The equal-dimensional smooth null is

\[
\operatorname{span}\{x,x^2,x^3\},
\qquad x=\theta-\theta_0.
\]

Both were evaluated with eight blocked folds on the frozen 129-point grid.

## 4. Frozen criteria

A positive pilot requires all of:

- negative-control excursion at most `1e-12`;
- quotient signal excursion at least `0.1`;
- structural blocked-CV normalized RMSE at most `0.05`;
- relative CV advantage over the cubic null at least `0.10`;
- structural coefficient instability at most `0.25`.

## 5. Result

The negative control is exactly zero at displayed precision. The quotient excursion is

\[
0.7695395230687915.
\]

The recoupling angle spans

\[
0.11266507359546996.
\]

The preregistered structural model gives

\[
E_{\rm rec}=1.7315748008431413\times10^{-14},
\]

with coefficient instability

\[
1.1811137319095956\times10^{-13}.
\]

The cubic null gives

\[
E_{\rm cubic}=0.02411018093919437.
\]

Hence the relative blocked-CV advantage is

\[
0.9999999999992818.
\]

All preregistered criteria are met.

## 6. Interpretation

Assign

`PREREGISTERED_RECOUPLING_ANGLE_CRITERIA_MET`.

The result is strong but structurally narrow. In a real two-dimensional carrier, conjugating a diagonal observable by an orthogonal recoupling matrix makes its matrix elements trigonometric functions of one rotation angle. The pilot verifies that the computed affine-quotient lower-symbol response obeys this preregistered internal structure and that a cubic in the external parameter is inferior under blocked validation.

It does not independently establish that the angle itself follows a universal phase law, nor does it identify physical dynamics.

## 7. Claim firewall

### Allowed

The declared nonuniform two-channel affine-quotient response is resolved by the preregistered recoupling-angle basis and outperforms an equal-dimensional cubic smooth null on the frozen interval.

### Forbidden

- universal or carrier-independent phase law;
- independent confirmation of a q-phase predictor for \(\phi(\theta)\);
- physical interpretation of \(q\) or \(\theta\);
- absolute lower-symbol accuracy;
- extrapolation outside the frozen carrier and interval.

No statement from the Gemini advisory report is used as evidence.

## 8. Next obligation

The next scientifically independent question is not another fit of \(u\) against functions of \(\phi\). That relation is now recognized as internal two-channel kinematics. The next module must test the deformation law of \(\phi(\theta)\) itself against preregistered q-number predictors and equal-complexity smooth nulls, preferably across more than one carrier.
