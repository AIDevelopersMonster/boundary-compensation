# BC-IDPR-CERT-03 — Nonuniform-Carrier Affine-Quotient Separation Certificate

**Status:** `NONUNIFORM_AFFINE_QUOTIENT_SEPARATION_CERTIFIED`  
**Date:** 2026-07-16  
**Upstream:** `BC-IDPR-P3-B-M5`

## 1. Certified scope

For the fixed nonuniform-spin carrier

\[
(j_1,j_2,j_3,j_4)=\left(\frac12,1,2,\frac52\right)
\]

and the fixed unequal-area tetrahedron with face-area ratios

\[
1:2:4:5,
\]

the varying lower-symbol channel is strictly ordered and grid-separated on

\[
\theta\in\left[\frac{\pi}{15},\frac{\pi}{10}\right]
\]

after quotienting every constant positive affine calibration

\[
y(\theta)\mapsto a y(\theta)+b,\qquad a>0.
\]

The quotient coordinate is

\[
u(\theta)=\frac{y(\theta)-y(\theta_{\rm lo})}{y(\theta_{\rm hi})-y(\theta_{\rm lo})}.
\]

## 2. Preregistration

The grid, interval, nuisance group, thresholds, uncertainty budget and stopping rule were frozen before evaluation in commit

`be415393641808a84759de04293ee5ae9e1a9e87`.

One 129-point evaluation was then performed. No post-result changes were made to the quotient, thresholds or exclusion rules.

## 3. Decision results

- negative-control maximum numerical derivative: `3.552713678800501e-15`;
- endpoint denominator: `0.008715842540636967`;
- affine-invariance residual: `1.0974554598419672e-13`;
- uncertainty-adjusted monotonicity margin: `0.01652385241081851`;
- minimum adjacent quotient separation: `0.0015734158353453054`;
- uncertainty-adjusted adjacent margin: `0.0015733855065317558`.

Every preregistered decision inequality is satisfied.

## 4. Gate split

- nonuniform affine-quotient differential pilot: `OPEN`;
- absolute lower-symbol accuracy: `OPEN`;
- confirmatory phase law: `BLOCKED`;
- physical interpretation of q: `BLOCKED`.

## 5. Controlled claim

The declared nonuniform carrier admits an affine-calibration-invariant differential observable that preserves strict parameter ordering and positive adjacent separation on the frozen compact grid.

## 6. Non-claims

This document does not certify:

- absolute agreement between lower symbols and classical face geometry;
- invariance under negative, nonlinear or theta-dependent recalibration;
- a sinusoidal or q-phase law;
- universal behavior for other spins, geometries, intervals or observables;
- physical q dynamics, matter, mass or curvature.

## 7. Next admissible action

A second P1 pilot may now be preregistered on the M5 carrier, using only the affine-quotient coordinate frozen here. The previous equal-spin pilot remains a separate negative model-selection result and must not be overwritten.
