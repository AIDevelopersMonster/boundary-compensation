# G2 and G2-R Response Matrix - v0.1.1 reviewed

**Manuscript:** `Recursive Jet Calculus and Rigorous Uniform Conditioning for Finite Quantum 6j Recoupling Matrices`  
**Version:** `v0.1.1 reviewed`  
**Date:** 2026-07-16  
**Verdict:** `ALL_G2_BLOCKERS_RESOLVED_IN_MANUSCRIPT`

## Critical error

| Audit item | Resolution | Location |
|---|---|---|
| CE-1 float64 computation overstated as a rigorous theorem | Replaced by the preregistered 192/256-bit Arb ball-arithmetic theorem with outward rounding, explicit Taylor-Cauchy envelope, conservative lower bound, and G2-R certificate | Abstract; Section 9; Theorem 9.3 |

## Missing assumptions

| Audit item | Resolution | Location |
|---|---|---|
| MA-1 exact q-6j convention | The scalar q-6j finite formula is now an explicit definition; phase and dimension factors are declared part of the matrix convention | Definition 3.1; Eq. (11) |
| MA-2 root-of-unity admissibility | The paper states `[12]_q=0` at the anchor, proves all used indices are at most 10, and treats the object as an explicitly defined finite trigonometric q-Racah model rather than silently importing a full modular category | Section 3; Proposition 2.3 |
| MA-3 orthogonality domain | Added a cited transpose-orthogonality proposition and analytic-continuation argument; explicitly distinguishes transpose orthogonality from unitarity | Proposition 4.2 |
| MA-4 class mixed with numerical filters | Replaced the former class by the exact algebraic class `A_6`; no tolerance or nonzero-speed filter enters its definition | Definition 2.2 |
| MA-5 analytic logarithm | Replaced complex-domain `log|omega|` language by the holomorphic branch `Log(s_J omega_J)`; real-axis derivatives are stated as a corollary | Lemma 6.2; Corollary 6.3; Theorem 9.3 |

## Proof gaps

| Audit item | Resolution | Location |
|---|---|---|
| PG-1 square-root branches | Added a holomorphic square-root continuation lemma and applied it to both triangle and dimension-amplitude radicands | Lemma 4.1 |
| PG-2 critical q-index bound | Added an exact integer-enumeration proposition with maxima 10, 10, 6, and 8 by occurrence; published the 283-carrier JSON list | Proposition 2.3; Appendix C; supplementary JSON |
| PG-3 Cauchy remainder | Displayed the exact order-50 remainder inequality, defined `R_out`, `R_cert`, `M_J`, and the lower envelope | Eqs. (37)-(39) |
| PG-4 complex orthogonality | Uses analytic transpose orthogonality and explicitly disclaims unitarity | Proposition 4.2 |
| PG-5 independence wording | Recast as a frozen new-label cross-validation using a different differentiation route but the same q-Racah evaluator | Section 8 |

## Wording corrections

All requested replacements were made:

- `matrix derivatives through order three`;
- `families excluded by the frozen label-1-to-4 split`;
- `given by a finite analytic expression and recursively evaluable`;
- q-number walls explicitly defined;
- pytest classified as implementation verification, not proof;
- no maximal-radius claim retained in the theorem.

## Publication enhancements

- theorem/claim dependency ledger added;
- exact carrier-enumeration pseudocode added;
- Arb Taylor-Cauchy pseudocode added;
- convention-to-code table added;
- exact 283-carrier supplementary JSON generated;
- finite-label versus unbounded-label limitation added;
- Arb primary reference added;
- PDF metadata populated.

## Residual obligations

The manuscript-level G2 cycle is closed. Remaining publication gates are external to theorem correctness:

1. clean-checkout reproducibility and hash equality;
2. final bibliography/DOI audit;
3. release metadata, license, Zenodo record and archive link;
4. final release PDF audit after clean build.

No statement from the Gemini advisory report is used as evidence.
