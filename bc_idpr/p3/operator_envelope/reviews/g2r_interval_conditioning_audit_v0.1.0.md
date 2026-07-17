# G2-R Rigorous Interval Conditioning Audit v0.1.0

**Date:** 2026-07-16  
**Status:** `PASS`

## Audit scope

The audit checks whether the G2 float64 objection is actually closed rather than merely hidden behind higher precision.

## Arithmetic audit

- Backend: `python-flint` 0.9.0 / Arb.
- Primary precision: 192 bits.
- Control precision: 256 bits.
- Pi, trigonometric values, square roots, reciprocals, Taylor coefficients and Cauchy majorants are Arb balls.
- Acceptance uses the lower endpoint of the final Arb enclosure.
- Ordinary binary floats appear only when serializing already certified interval endpoints to JSON.

Result: `PASS`.

## Class audit

The generator uses exact integer rules only:

- labels 1 through 6;
- even external-label sum;
- exactly two channels in each scheme;
- nonnegative finite-Racah factorial arguments;
- required q-number index at most 10.

It produces 283 ordered carriers in 24 families. No numerical orthogonality or nonzero-speed filter is used.

Result: `PASS`.

## Symmetry audit

The reduction from 283 ordered carriers to 24 canonical external-label families relies on the tetrahedral symmetries of the q-6j symbol. External permutations induce constant signed row/column permutations and optional transpose of the two-channel recoupling matrix. For constant signed permutation matrices, the generator is transformed by conjugation; under transpose its scalar skew generator changes at most by sign. Therefore `abs(omega)` and the zero set of `omega` are invariant.

Result: `PASS`, subject to adding the symmetry lemma and a primary citation to the manuscript.

## Remainder audit

The proof uses the frozen order-50 expansion and the geometric Cauchy tail

`M q^(N+1)/(1-q)` with `q=Rcert/Rout=0.1`.

All quantities entering the lower bound are outward-rounded Arb enclosures. The primary and control runs agree on the worst carrier and preserve strict positivity.

Result: `PASS`.

## Confirmatory results

- ordered carriers covered: 283;
- canonical families evaluated: 24;
- worst carrier: `(1,1,1,1)`;
- rigorous minimum lower bound: `0.16025264148217666`;
- primary precision: positive;
- control precision: positive;
- frozen radius: `pi/1200`;
- radius changed after evaluation: no.

## Remaining manuscript corrections

G2-R closes the critical arithmetic blocker. The manuscript still requires the noncritical G2 clarifications:

1. state the exact q-6j normalization;
2. add the tetrahedral-symmetry reduction lemma and citation;
3. distinguish algebraic and certified carrier classes;
4. state the holomorphic square-root lemma;
5. derive the critical q-index bound 10;
6. print the exact Cauchy-tail formula;
7. replace ambiguous `log abs(omega(z))` language by a holomorphic logarithm statement on the complex disk;
8. call the finite-difference comparison an independent differentiation route.

## Gate decision

- G2-R: `CLOSED`;
- G2 critical blocker: `CLOSED`;
- G2 theorem audit: `PASS_WITH_MANUSCRIPT_CORRECTIONS`;
- next blocking task: corrected manuscript cycle followed by clean reproducibility.

No statement from the Gemini advisory report is used as evidence.
