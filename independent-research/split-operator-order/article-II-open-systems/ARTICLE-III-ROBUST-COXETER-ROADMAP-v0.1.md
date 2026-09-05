# Article III research seed — Robust Minimal Coxeter Tomography

**Date:** 2026-09-06  
**Status:** `RESEARCH_SEED / NEXT_ACTIVE_PROBLEM`  
**Parent result:** Article II v0.2.1, `L_d^Cox=floor(d^2/2)` for `d>=3` in the declared first-order matrix-valued Coxeter-face model.

## Core question

Among algebraically minimal full-rank Coxeter designs, can one achieve quantitatively stable inversion as `d` grows?

For a design `D`, move from the rank-only condition

`rank M_D=(d^2-1)^2`

to its smallest singular value and condition number:

`sigma_min(M_D)` and `kappa(M_D)=sigma_max(M_D)/sigma_min(M_D)`.

Define the optimal minimal-design conditioning problem schematically by

`kappa_d^Cox = inf { kappa(M_D) : |D|=floor(d^2/2), rank M_D=(d^2-1)^2 }`,

with an explicit normalization of the quotient basis and measurement coordinates to be fixed before quantitative claims are made.

## First mathematical fork

### Stable-minimal regime

If there exists a normalized family of minimal designs with polynomially controlled `kappa(M_D)` (equivalently a polynomial lower bound on normalized `sigma_min`), then Article II's sharp algebraic count can plausibly be converted into a robust first-order reconstruction protocol. The next layer is sample complexity / POVM / randomized-measurement implementation.

### Robustness gap

If every minimal family becomes badly conditioned with dimension, then sharp algebraic minimality and robust tomography separate. Introduce oversampled designs

`L > floor(d^2/2)`

and seek the smallest redundancy factor required for a prescribed stability threshold.

## Immediate proof obligations

1. Fix a basis-independent or canonically normalized metric on the dissipative quotient.
2. Fix normalization of each matrix-valued Coxeter face so singular values are physically/mathematically comparable across designs and dimensions.
3. Compute exact/numerical `sigma_min` and `kappa` for the existing certified `d=3,4,5` minimal designs.
4. Test whether the existing all-d existence proof gives any quantitative lower bound on the decisive minors; Zariski-open existence alone is insufficient for stability.
5. Separate unavoidable dimensional scaling from construction-induced ill-conditioning.
6. If minimal conditioning degrades, formulate and test oversampling laws.
7. Only after a stable linear inverse is established, translate matrix-valued first-order coefficients into state preparation + observables/POVM/shadow measurements and derive statistical error bounds.

## Claim firewall

Do not infer robustness from full rank. Do not infer sample complexity from face count. Do not claim diamond-norm reconstruction before an operational channel/generator norm conversion is proved. Do not treat generic/Zariski-open existence as quantitative conditioning.

## Deferred branch

Non-Markovian process tensors remain a plausible later programme motivated by the nested-reduction composition law, but are intentionally deferred so that the sharp Coxeter theorem first receives a quantitative stability theory.
