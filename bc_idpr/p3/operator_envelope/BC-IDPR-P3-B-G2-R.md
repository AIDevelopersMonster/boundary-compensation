# BC-IDPR-P3-B-G2-R — Rigorous Interval Conditioning

**Status:** `RIGOROUS_ARB_UNIFORM_CONDITIONING_CERTIFIED`  
**Date:** 2026-07-16  
**Preregistration commit:** `535de38c4f0ed4393747510b7c15ccd6dd1fd977`

## Objective

Close the single publication blocker identified by the G2 theorem audit: replace the ordinary `float64` radius calculation by a rigorous outward-rounded enclosure proving that the angular speed does not vanish on a common complex disk.

## Arithmetic

The implementation uses `python-flint` Arb ball arithmetic. The confirmatory calculation is run at 192 bits and repeated at 256 bits. Arb propagates midpoint-radius enclosures with outward rounding through all arithmetic and transcendental operations.

The frozen proof family is

\[
\theta_0=\frac{\pi}{12},\qquad
R_{\rm out}=\frac{\pi}{120},\qquad
R_{\rm cert}=\frac{\pi}{1200},\qquad N=50.
\]

For each canonical carrier, the program encloses the normalized Taylor coefficients

\[
\omega(\theta_0+h)=\sum_{k=0}^{50}\omega_k h^k+\mathcal R_{51}(h)
\]

and proves

\[
|\omega(h)|\ge
\underline{|\omega_0|}
-\sum_{k=1}^{50}\overline{|\omega_k|}R_{\rm cert}^k
-\overline M\frac{q^{51}}{1-q},
\qquad q=R_{\rm cert}/R_{\rm out}=0.1.
\]

## Algebraic carrier class and symmetry reduction

The carrier class is generated only from exact doubled-spin admissibility rules. No orthogonality tolerance or floating-point nonzero-speed filter is used. It contains 283 ordered carriers in 24 unordered external-label families.

The tetrahedral symmetries of the quantum 6j symbol transform recoupling matrices associated with permutations of the four external labels by constant signed row/column permutation matrices and, in some cases, transpose. These operations preserve the absolute angular speed and its zero set. Therefore one Arb calculation for each of the 24 canonical families rigorously covers all 283 ordered carriers.

## Result

At both 192 and 256 bits, every certified lower bound is strictly positive. The worst carrier is

\[
J=(1,1,1,1),
\]

with

\[
\inf_{|z-\theta_0|\le \pi/1200}|\omega_J(z)|
\ge 0.16025264148217666.
\]

Its bound decomposes as

\[
\underline{|\omega_0|}=0.16210935083709735,
\]

\[
\overline{\sum_{k=1}^{50}|\omega_k|R_{\rm cert}^k}
=0.0018567093549206992,
\]

\[
\overline{|\mathcal R_{51}|}
=4.6169853384256\times10^{-33}.
\]

## Decision

- `float64_blocker`: `CLOSED`;
- `uniform_nonvanishing_theorem`: `RIGOROUSLY_CERTIFIED`;
- `holomorphic_logarithm_on_common_disk`: `CLOSED`;
- `G2_overall`: `PASS`.

The result does not claim an absolute maximal radius, unbounded-label uniformity, semiclassical geometry or physical dynamics.

No statement from the Gemini advisory report is used as evidence.
