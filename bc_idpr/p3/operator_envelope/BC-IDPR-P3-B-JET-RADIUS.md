# BC-IDPR-P3-B-JET-RADIUS — Sharp Conditioning and Radius Optimization

**Status:** `TAYLOR_CAUCHY_UNIFORM_RADIUS_CERTIFIED`  
**Date:** 2026-07-16  
**Preregistration:** `a6148e37a3386bc4d6c65e168f919977de38317e`

## 1. Objective

Improve the conservative common conditioning radius without changing the declared class of 283 two-channel ordered carriers in 24 representation families.

The module distinguishes the q-wall-safe outer radius from a smaller radius on which nonvanishing of the recoupling angular speed is certified uniformly.

## 2. Frozen proof family

The direct absolute-value majorant of every Racah summand was rejected during exploratory method selection because it destroys cancellations and produces unusably large bounds.

The confirmatory method preserves cancellation in the first 50 Taylor coefficients of the signed angular speed,

\[
\omega(z)=\sum_{k=0}^{50}\omega_k(z-\theta_0)^k+\mathcal R_{51}(z),
\]

and bounds the remainder using an analytic Cauchy majorant on the outer q-wall-safe disk.

No fitted parameter is used.

## 3. Radius certificate

The outer wall-safe radius is

\[
R_{\rm wall}=2.617993877991496\times10^{-2}.
\]

The frozen confirmatory radius is

\[
R_{\rm cert}=0.1R_{\rm wall}
=2.617993877991496\times10^{-3}.
\]

This is 1.6 times the earlier conservative radius \(R_{\rm wall}/16\).

The maximum radius inside the frozen order-50 Taylor–Cauchy proof family is

\[
R_{50}^{\rm ext}=2.639397419804555\times10^{-3}
=0.10081755507501339R_{\rm wall}.
\]

The confirmatory radius deliberately stays below this proof-family boundary.

## 4. Uniform margins

At the confirmatory radius,

\[
\inf_C\inf_{|z-\theta_0|\le R_{\rm cert}}|\omega_C(z)|
\ge 0.16025264148217636.
\]

The worst carrier for this bound is the symmetric carrier \((1,1,1,1)\).

The minimum q-number lower bound is

\[
\min_{1\le n\le10}\inf_{|z-\theta_0|\le R_{\rm cert}}|[n]_q(z)|
\ge0.25628849484566973.
\]

## 5. Decision

Closed:

- uniform radius optimization within the frozen order-50 Taylor–Cauchy proof family;
- uniform nonvanishing of the signed angular speed at the confirmatory radius;
- mathematical core required for the planned preprint.

Open but not publication-blocking:

- proof of the absolute maximal analytic radius;
- sharper all-order constants;
- low-dimensional representation compression.

Blocked:

- physical interpretation;
- claims outside the declared finite two-channel chamber.

No statement from the Gemini advisory report is used as evidence.
