# Split Operator Order — active handoff

**Branch:** `research/split-operator-order-article-II-v0.1`  
**Checkpoint date:** 2026-09-06  
**Author:** Malachevsky, A.A.  
**ORCID:** 0009-0008-6009-3196

## Rule for future chats
Read this file first, then the cited control notes. Do not reconstruct the programme from chat memory. After every nontrivial theorem, obstruction, audit repair, manuscript promotion, source-build change, or publication-status change, update this file before continuing.

## Article I
The published Article-I core is frozen. Post-publication research established the sharp first-order Coxeter tomography theorem. Do not rewrite the frozen Article-I publication core.

## Article II — published
Directory: `article-II-open-systems/`.

Publication source package: `article-II-open-systems/publication-v0.2.1/`.

Title: *Context Reduction in Open Quantum Systems: Multiplicativity Defects, Lindblad Order Holonomy, and Sharp Coxeter Tomography*.

**Zenodo DOI:** `10.5281/zenodo.22421827`  
**Canonical URL:** https://doi.org/10.5281/zenodo.22421827  
**Publication status:** `PUBLISHED`.

The audited publication package contains `main.tex`, `sharp-proof-appendix.tex`, canonical build entrypoint `article.tex`, and release-control `README.md`. Workflow: `.github/workflows/article-ii-publication.yml`.

## Main theorem
In the bounded finite-dimensional matrix-valued first-order Coxeter-face measurement model,

`L_d^Cox=floor(d^2/2)` for every `d>=3`.

The quotient dimension is `N_d=(d^2-1)^2`; one matrix-valued face supplies at most `2d^2` real coordinates. The theorem is algebraic and does not extrapolate from low-dimensional numerical ranks.

## Audited proof chain
1. Structural scalar-one restriction quotient `R_res(d)=(d^2-1)(d+1)^2+2`.
2. Extension-ready minimal-design criterion and parity ceiling.
3. Centered odd-dimensional tangent formulas.
4. Complete one-anchor regular kernel and finite H-anchor compression.
5. Cycle factorization of compressed dependency determinant `D_n`.
6. Binder-compatible transversality inside the reverse-cycle-zero subspace.
7. Exact no-go for the old one-parameter native tilt.
8. Reverse-cycle transverse detector and finite reconstruction coefficient.
9. Extension-ready minimal designs in every odd dimension.
10. Odd-to-even transfer rebuilt directly in centered scalar-one coordinates and directly in `SL_n(C)`.
11. Return to genuine unitary Coxeter faces by `SU(n)` Zariski density and engineered contextual-square realization.

Critical proof repairs remain recorded in `article-I/research/BINDER-COMPATIBLE-TRANSVERSALITY-REPAIR-v0.1.md` and `article-I/research/ODD-TO-EVEN-TRANSFER-AUDIT-REPAIR-v0.1.md`. The invalid post hoc determinant normalization is withdrawn and is not used in the publication source.

## d=2 boundary
No two-face design is extension-ready under scalar-one embedding `M_2 -> M_3`. This does not prove native two-face tomography impossible. The sharp theorem is intentionally `d>=3`.

## Claim firewall
Do not inflate the result into finite-time arbitrary UCP-channel identifiability, conditioning/noise robustness, universal CP-reduction monotonicity, entropy/decoherence monotones, infinite-dimensional unbounded GKSL results, non-Markovian process-tensor results, or established physical spacetime/gauge curvature.

The physical motivation and explicitly speculative programme are kept in `article-II-open-systems/PHYSICAL-INTERPRETATION-SUPPLEMENT-v0.1.md`, where theorem-level statements, supported interpretation, and conjectural targets are separated.

## Reproducibility
The `d=5` builder was independently re-executed during consolidation:

`prime=1000033 shape=600x576 rank=576`

`CERTIFIED_FULL_COLUMN_RANK_OVER_Q`.

This is an independent reproducibility check, not part of the all-dimensional proof.

## Publication audit
Successful audited workflow run: `33995974451` at head `26b2e9488b823b225f0c8312e78cb8c6c431c3e5`.

Artifact:
- `article-II-v0.2.1-pdf`;
- id `9978084171`;
- SHA-256 `d474fa8cc1ab94aa7bf6a184d647fb2536597780ebbfbc693b4456aafc4c7488`.

PDF audit: 16 pages, PDF 1.5, text-based, unencrypted; no undefined references/citations, undefined control sequences, fatal errors, overfull/underfull boxes, clipping, overlap, black boxes, broken glyphs, equation truncation, or bibliography-layout blocker. Two nonfatal hyperref bookmark warnings remain and do not affect visible content.

## Publication checkpoint 10 — 2026-09-06
Article II has been deposited/published on Zenodo with DOI:

`https://doi.org/10.5281/zenodo.22421827`

Repository metadata must use this DOI for Article II from this checkpoint onward. Do not replace it with a guessed or future DOI.

## Next research/publication direction
Article II is frozen as the published theorem paper except for genuine errata.

A separate transition/perspective article should connect Article I and Article II to the next strict programme while explicitly separating proven mathematics from physically motivated speculation. The strict next mathematical target remains stable/robust Coxeter tomography: singular values, conditioning, oversampling, noise amplification, and ultimately operational measurement protocols.
