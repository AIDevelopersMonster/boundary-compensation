# BC-IDPR P3→P1 Research Contract 02

## Identifiable q-Curvature Predictors for Phase-Resolved Residual Modulation

**Contract ID:** `BC-IDPR-P3-P1-RC02`  
**Version:** `v0.1.0`  
**Date:** 2026-07-17  
**Status:** `PREDICTOR_GEOMETRY_CERTIFIED_PILOT_AUTHORIZED`

## 1. Reason for a new contract

RC01 stopped correctly before calibration. Its integer exponential predictors and paired half-integer controls became almost collinear after cubic baseline removal. The largest response-independent projector difference was about `0.00367`, below the frozen positive threshold `0.02`. Changing the dictionary inside RC01 would have violated preregistration; therefore RC02 receives a new identifier.

RC02 uses no calibration or confirmatory response data in predictor design.

## 2. Frozen deformation domain

\[
\eta=\frac{12\theta}{\pi},\qquad
\eta\in[0.60,1.15],\qquad
\Delta\eta=5\times10^{-4},
\]

with 1101 grid points and anchor \(\eta=1\).

## 3. Observable interface

The primary response remains the anchored complex recoupling-column observable

\[
Z_J(\eta)=
\frac{F_{11,J}(\eta)+iF_{21,J}(\eta)}
     {F_{11,J}(1)+iF_{21,J}(1)}.
\]

The replication response remains the sign-aligned angular speed. Both are residualized against the frozen cubic baseline in the affine coordinate \(x\in[-1,1]\).

## 4. q-curvature predictor family

For real or half-integer \(m>0\), define

\[
\Phi_m(\eta)
=\partial_\theta^2\log[m]_q
=-m^2\csc^2(m\theta(\eta))+\csc^2\theta(\eta).
\]

Let \(P_3\) be the discrete orthogonal projector onto \(\operatorname{span}\{1,x,x^2,x^3\}\). The normalized atom is

\[
\psi_m=\frac{(I-P_3)\Phi_m}{\|(I-P_3)\Phi_m\|_2}.
\]

The q-predictor modes are integers `2,...,10`. The control pool is `{1.5,2.5,...,9.5}`. All atoms are finite on the frozen grid.

## 5. Frozen pairing

A control frequency is used exactly once. Among all `9! = 362880` bijections, the pairing minimizes lexicographically the maximum, then median, then mean paired absolute overlap.

| q mode | control | overlap | projector difference |
|---:|---:|---:|---:|
| 2 | 6.5 | 0.9886743634484192 | 0.1500766572784159 |
| 3 | 8.5 | 0.9576577158773160 | 0.2879091857177225 |
| 4 | 7.5 | 0.9863339530385055 | 0.1647584082328888 |
| 5 | 9.5 | 0.9126886234204216 | 0.4086556945387350 |
| 6 | 1.5 | 0.9909657558650774 | 0.1341151397223887 |
| 7 | 3.5 | 0.9896299124699062 | 0.1436406500431053 |
| 8 | 2.5 | 0.9693117078074397 | 0.2458349306087819 |
| 9 | 5.5 | 0.9581290811446330 | 0.2863366268309753 |
| 10 | 4.5 | 0.8042926572764700 | 0.5942333897141381 |

## 6. Reachability qualification

For unit residual \(r\) and unit atoms \(u,v\),

\[
\left||\langle r,u\rangle|^2-|\langle r,v\rangle|^2\right|
\le \|uu^*-vv^*\|_{op}
=\sqrt{1-|\langle u,v\rangle|^2}.
\]

RC02 does not claim that a positive effect exists. It requires only that the registered threshold not be excluded by predictor geometry. The smallest paired projector difference is `0.1341151397223887`, exceeding the frozen threshold `0.02` by the safety factor `6.705756986119435`.

## 7. Frozen split and stage discipline

The RC01 family split is carried forward by hash. The four prior pilot families may be reused because they are permanently excluded from calibration and confirmation. The 12 calibration and 8 confirmatory families remain unopened.

Pilot is limited to software, numerical stability, residual degeneracy and effect-scale diagnostics. Calibration requires a committed pilot certificate. Confirmation requires a later committed calibration freeze certificate.

## 8. Inference rule retained

Calibration selects `n_star` by maximum median family q-versus-control energy advantage, with the smallest `n` resolving ties within `1e-12`. The confirmatory threshold remains `0.02`; it was not lowered to repair RC01.

## 9. Non-claims

Geometry qualification is not evidence for phase modulation. RC02 makes no claim about physical oscillations, time evolution, matter, defects, gravity, global gluing, full modular-category coherence, continuum limits or universality outside the frozen finite atlas.

No statement from the Gemini advisory report is used as evidence.