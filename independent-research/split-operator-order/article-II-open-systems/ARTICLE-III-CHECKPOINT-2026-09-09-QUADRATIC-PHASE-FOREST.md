# Article III checkpoint — quadratic-phase forest core

**Date:** 2026-09-09  
**Branch:** `research/split-operator-order-article-II-v0.1`

## New theorem

Created:

`ARTICLE-III-QUADRATIC-PHASE-FOREST-CORE-v0.1.md`

The theorem closes the block-compatible core problem for every odd prime dimension `p`.

## Exact construction

Let

`P=diag(omega^(j(j-1)/2))`

be the quadratic phase anchor, and use engineered Coxeter squares

`(P,W_(a,ka))`

for

`a=1,...,(p-1)/2`, `k=1,...,p-1`.

The selected labels form `(p-1)/2` disjoint paths through the quadratic-shear sign-class cycles.

Number of faces:

`K_p=(p-1)^2/2`.

## Closed

Each selected face contributes its full real rank `2p^2`.

Total core rank:

`R_forest=p^2(p-1)^2`.

Equal-face lower singular gap:

`sigma_min^+ >= p/(p-1)^2 >= 1/p`.

Hence the forest lower frame bound satisfies

`A_forest >= p^-2`.

The remaining quotient dimension is exactly

`(p^2-1)^2-p^2(p-1)^2=(p-1)^2(2p+1)`.

The exact number of faces still available at the sharp count is

`L_p^sharp-K_p=p-1`.

Their scalar capacity exceeds the residual dimension by exactly

`p^2-1`,

which is the odd sharp rank slack.

## Interpretation

The generic block-compatible restricted-invertibility barrier is no longer active on the odd-prime line. A concrete polynomially conditioned near-direct-sum core is explicit.

The sharp theorem is now reduced to a structured `p-1`-face dense completion problem.

## Strict next target

Prove a Fourier completion theorem: choose explicit labels `h_1,...,h_(p-1)` such that the squares

`(F_p,W_(h_j))`

complete the forest to full quotient rank with polynomial Schur gap.

Strong target suggested by the verified p=3,5 census:

- first `p-2` Fourier faces add full rank `2p^2` each;
- the last adds exactly `p^2+1` new directions;
- hence all sharp overlap `p^2-1` is concentrated in the final face.

Do not yet claim the all-prime Fourier completion theorem.
