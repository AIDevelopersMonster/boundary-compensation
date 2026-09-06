# Article III checkpoint — Schur transversality door

**Date:** 2026-09-06  
**Branch:** `research/split-operator-order-article-II-v0.1`  
**Status:** `ACTIVE / SUPPORT-GEOMETRY LAYER / NEXT PROOF STRUCTURAL`

## New proved layer

The face-side normalization hierarchy is now:

`exact quotient whitening -> projective face normalization -> polar support normalization`.

Control note:

`ARTICLE-III-PROJECTIVE-POLAR-FUSION-FRAME-v0.1.md`

The polar layer replaces each nonzero face by its normalized support projector

`R_f=P_f/r_f`,

so amplitude and within-face singular weighting are both removed. The remaining problem is normalized fusion-frame geometry of measured quotient subspaces.

## Numerical census

Control note:

`ARTICLE-III-PROJECTIVE-POLAR-CENSUS-v0.1.md`

Reproducibility script:

`examples/article_iii_projective_polar_census_v010.py`.

The observed redundancy gain survives both projective and polar normalization.

For d=3, polar support efficiency rises from about `0.0263` at L=4 to about `0.2491` at L=12 in the greedy sequence.

For d=4, it rises from about `0.00269` at L=8 to about `0.0165` at L=14, but saturates much earlier and remains small.

## New exact theorem

Control note:

`ARTICLE-III-SCHUR-TRANSVERSALITY-THEOREM-v0.1.md`.

For an accumulated positive semidefinite frame operator `A` with blind space `K=ker A`, and a new positive face contribution `R`, decompose relative to `K direct-sum K^perp` and set

`D=A_+ + R_11`,

`Sigma_A(R)=R_00-R_01 D^{-1} R_10`.

Then

`A+R>0 iff Sigma_A(R)>0`.

Moreover the exact congruence factorization gives a quantitative lower-frame bound in terms of the Schur transversality coefficient, the weakest already-observed direction, and triangular coupling distortion.

## Sharp-completion census

Control note:

`ARTICLE-III-SCHUR-TRANSVERSALITY-CENSUS-v0.1.md`.

For the d=3 sharp support sequence, blind dimensions evolve

`46, 28, 10, 0`.

For d=4 they evolve

`193, 161, 129, 97, 65, 33, 1, 0`.

The d=4 design is therefore almost maximally efficient in algebraic rank growth: the first seven rank-32 faces reach rank 224 in a 225-dimensional quotient. Nevertheless the smallest positive unaveraged frame eigenvalue before the last face is only about `4.29e-7`.

The last face has raw projector coverage about `0.0955` of the final blind direction, but the effective Schur transversality is only about `3.32e-4`, and the final averaged lower support-frame eigenvalue is about `1.20e-5`.

Thus the new structural separation is

`maximal rank growth != stable transversality`.

## Next strict task

Do not return to generic random search first.

Return to the all-dimensional Article-II extension-ready construction and analyze its ordered support/kernel geometry. Track:

`K_j = ker A_j`,

`gamma_j = lambda_min^+(A_j)`,

`theta_j = lambda_min(Sigma_{A_j}(R_{j+1}))`,

and coupling distortion `chi_j`.

The next theorem target is either:

1. polynomial control of these quantities along a scalable sharp/mildly redundant Coxeter construction; or
2. a forced small-Schur step yielding a genuine stable-minimality / redundancy obstruction.

This is now the active Article-III front.
