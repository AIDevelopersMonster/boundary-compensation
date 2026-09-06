# Article III checkpoint — unitary five-defect carrier closed

**Date:** 2026-09-06  
**Branch:** `research/split-operator-order-article-II-v0.1`  
**Author:** Malachevsky, A.A.  
**ORCID:** 0009-0008-6009-3196

## New theorem

See:

`article-II-open-systems/ARTICLE-III-UNITARY-FIVE-DEFECT-CARRIER-v0.1.md`

Commit:

`0430d0b677fba34a2860c24bf6aa859c4950c597`

Status:

`PROVED / EXPLICIT UNITARY CARRIER / INVERSE-POLYNOMIAL LOCAL GAP / NO ZARISKI RETURN FOR CARRIER`

## Result

For every odd `d>=3`, the isolated five-defect carrier in the repaired odd-to-even extension-ready transfer admits a direct unitary realization.

The carrier transports can be chosen explicitly in `SU(d+1)` using a scalar phase anchor

`c_d=exp(i*pi/[4(d+1)])`

and small traceless-Hermitian unitary perturbations.

The pure relative `R` block has a forward singular gap at least `c/(d+1)` after removing the two exact tail-gauge directions.

A separability-idempotent contraction proves that every normalized non-derivation regular defect has a bounded bilinear Leibniz-defect witness. The paired-branch mismatch phase is uniformly separated from `+/-1`, so the missing regular class is detected on the unitary family.

The four scalar defect copies are simultaneously separated by one additional traceless-Hermitian detector direction and a one-parameter avoidance argument.

With a polynomial perturbation scale `delta_d=c*d^-12`, the five-defect Schur block has an inverse-polynomial gap. The theorem note records the deliberately crude bounds

`sigma_min(S_E5) >= c d^-24`

and for the full isolated carrier

`sigma_min^+(C_d) >= c d^-28`,

with condition estimate `kappa=O(d^30)` in the stated normalized coordinates.

No exponent is claimed optimal.

## Consequence

The five-defect carrier is not the odd-to-even superpolynomial wall. The Zariski-density return used in the old repaired proof is no longer needed for the carrier stage.

## Next strict target

Attack the first two-tail binding scale directly on the unitary locus:

`beta_j=r`, `delta_j=s`.

Replace the old determinant-one diagonal perturbation `mu=1+epsilon` by a unitary phase perturbation and prove an inverse-polynomial finite-parameter gap. Then combine it with the already established unitary cross-plane graph binding and prove simultaneous two-scale remainder control.

Do not claim the complete odd-to-even transfer polynomially conditioned until those layers are closed.
