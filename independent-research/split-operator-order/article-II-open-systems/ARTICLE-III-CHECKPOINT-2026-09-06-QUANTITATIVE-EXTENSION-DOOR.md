# Article III checkpoint — quantitative sharp-extension narrowing

**Date:** 2026-09-06  
**Status:** `ACTIVE / QUANTITATIVE UNITARY CROSS-PLANE WALL`

This checkpoint records the latest Article-III narrowing after the Schur-transversality stage.

## New proved results

1. `ARTICLE-III-SHARP-RANK-SLACK-THEOREM-v0.1.md`
   - every sharp full-rank design is a near-direct-sum support geometry;
   - total exact overlap budget is at most `2 d^2 - 1` for even `d` and `d^2 - 1` for odd `d`;
   - average exact overlap per sharp face is bounded by a constant (`<4` even, `<=2` odd);
   - therefore severe instability, if present, must come from near intersections / weak spectral directions, not large exact intersections.

2. `ARTICLE-III-BINDING-GRAPH-SPECTRAL-GAP-v0.1.md`
   - the residual graph-binding matrix is the incidence matrix of the bipartite double cover of the triangle-with-leaves graph;
   - the double-cover Laplacian splits into the Laplacian and signless-Laplacian spectra of the base graph;
   - its smallest nonzero eigenvalue satisfies `1/d < lambda_2 < 2/d` for `d>=4`;
   - the unweighted binding matrix has `sigma_min^+ > d^{-1/2}` and condition number `< sqrt(2) d`.

3. `ARTICLE-III-POLYNOMIAL-SIDON-PHASES-v0.1.md`
   - explicit polynomial Sidon exponents `e_j=j+(2n+1)j^2`;
   - unit-circle phases `lambda_j=exp(i e_j/(12 n^3))` are multiplicatively Sidon with inverse-polynomial separation;
   - local determinant gaps are at least order `n^{-6}`;
   - graph edge weights lie in a polynomial window, yielding a crude `O(d^7)` weighted combinatorial condition-number bound.

4. `ARTICLE-III-UNITARY-LOCAL-FACE-REPLACEMENT-v0.1.md`
   - the nonunitary local `[[1,1],[1,2]]` block is unnecessary;
   - any nontrivial `SU(2)` Givens rotation gives the same local kernel and multiplicative-Sidon determinant up to row signs/scales;
   - choosing `theta=pi/4` removes any small local angular parameter;
   - the full unperturbed local reduction layer is now explicit on the unitary locus.

## Current wall

The remaining quantitative unitary gap in the even-to-odd sharp extension is the cross-plane perturbation used for global binding.

The old complex witness uses

`B_jk(t)=Lambda [I+t(E_kn+E_nk)]`,

which is not unitary.

The natural replacement is

`B_jk^u(t)=Lambda exp(t(E_kn-E_nk))`.

The next strict theorem target is to rederive the second-order reduced Schur map for this unitary perturbation and prove that it produces the same edge relations

`alpha_j+gamma_k=0`, `alpha_k+gamma_j=0`

up to inverse-polynomial nonzero weights.

If successful, the even-to-odd local/binding construction can be made quantitatively unitary without the qualitative Zariski-density return. After that, the remaining issues are finite-`t` remainder control and accumulated Schur coupling, followed by the two-scale odd-to-even transfer.
