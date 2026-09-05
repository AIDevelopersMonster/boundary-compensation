# Split Operator Order — active handoff

**Branch:** `research/split-operator-order-article-II-v0.1`  
**Checkpoint date:** 2026-09-06  
**Author:** Malachevsky, A.A.  
**ORCID:** 0009-0008-6009-3196

## Rule for future chats
Read this file first, then the cited control notes. Do not reconstruct the programme from chat memory. After every nontrivial theorem, obstruction, audit repair, manuscript promotion, source-build change, or publication-status change, update this file before continuing.

## Article I
The published Article-I core is frozen. Post-publication research established the sharp first-order Coxeter tomography theorem. Do not rewrite the frozen Article-I publication core.

## Article II — current state
Directory: `article-II-open-systems/`.

Publication manuscript: `article-II-open-systems/manuscript-v0.2.0-en.md`.

Publication source package: `article-II-open-systems/publication-v0.2.1/` with:
- `main.tex` — publication master;
- `sharp-proof-appendix.tex` — publication-compressed sharp-proof chain;
- `article.tex` — canonical build entrypoint and compatibility shim;
- `README.md` — release control.

Workflow: `.github/workflows/article-ii-publication.yml`.

Working title: *Context Reduction in Open Quantum Systems: Multiplicativity Defects, Lindblad Order Holonomy, and Sharp Coxeter Tomography*.

Current release level: `PUBLICATION_READY_PENDING_RENDER_AUDIT`.

## Main theorem
In the bounded finite-dimensional matrix-valued first-order Coxeter-face measurement model,

`L_d^Cox=floor(d^2/2)` for every `d>=3`.

The quotient dimension is `N_d=(d^2-1)^2`; one matrix-valued face supplies at most `2d^2` real coordinates. The all-dimensional theorem is algebraic and does not extrapolate from low-dimensional numerical ranks.

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

Critical proof repairs remain recorded in:
- `article-I/research/BINDER-COMPATIBLE-TRANSVERSALITY-REPAIR-v0.1.md`;
- `article-I/research/ODD-TO-EVEN-TRANSFER-AUDIT-REPAIR-v0.1.md`.

The invalid post hoc determinant normalization is withdrawn and is not used in the publication source.

## d=2 boundary
No two-face design is extension-ready under scalar-one embedding `M_2 -> M_3`. This does not prove native two-face tomography impossible. The sharp theorem is intentionally `d>=3`.

## Claim firewall
Do not inflate the result into finite-time arbitrary UCP-channel identifiability, conditioning/noise robustness, universal CP-reduction monotonicity, entropy/decoherence monotones, infinite-dimensional unbounded GKSL results, non-Markovian process-tensor results, or physical spacetime/gauge curvature.

Related-work/novelty control: `article-II-open-systems/LITERATURE-NOVELTY-AUDIT-v0.2.md`.
Legacy status map: `article-II-open-systems/LEGACY-STATUS-v0.2.md`.
Proof obligations: `article-II-open-systems/PROOF-OBLIGATIONS.md`.

## Reproducibility
The `d=5` builder was independently re-executed during consolidation:

`prime=1000033 shape=600x576 rank=576`

`CERTIFIED_FULL_COLUMN_RANK_OVER_Q`.

This is an independent reproducibility check, not part of the all-dimensional proof.

## Publication-source audit checkpoint 8 — 2026-09-06
The first GitHub Actions render attempt failed before producing a PDF. The failure was isolated to a C5 LaTeX source defect, not mathematics:

`! Undefined control sequence.`

at the single use of `\mathscr D` in `main.tex` because the source did not load a script-font package.

Repair:
- added `publication-v0.2.1/article.tex` as the canonical build entrypoint;
- the entrypoint defines `\mathscr` compatibly as `\mathcal` and inputs `main.tex`;
- workflow now builds `article.tex` rather than `main.tex`;
- workflow now includes a log gate rejecting undefined references/citations, undefined control sequences, and fatal errors before artifact upload.

Repair commits:
- build entrypoint: `75538921b994d8a594b25dfbf10956623f9df404`;
- workflow/log gate: `26b2e9488b823b225f0c8312e78cb8c6c431c3e5`.

The failed run proves only that the old source did not compile; it does not change any theorem or claim. No compiled PDF has yet passed the render gate in this control session.

## Current publication gate
Mathematical existence blockers: none currently identified.

Targeted related-work/claim-boundary audit: complete.

Author/ORCID: verified.

Repository licence: MIT at repository level.

Article-specific Zenodo DOI: not assigned; do not invent one.

Former even-dimensional typography defect is corrected as `((d-1)^2-1)/2 + d = d^2/2`.

Source-build defect discovered by CI: repaired as above.

Compiled PDF artifact after repair: pending successful workflow run.

PDF visual inspection: pending.

Therefore status remains exactly `PUBLICATION_READY_PENDING_RENDER_AUDIT`.

## Next permitted attack
Do not reopen theorem existence unless a concrete mathematical defect is found. Next publication gate only:
1. obtain a successful post-repair `article-ii-publication` workflow build;
2. inspect `article.log` and `pdfinfo.txt`;
3. download `article-II-v0.2.1-pdf` artifact;
4. render every page and inspect clipping, overfull equations, broken glyphs, orphan headings, reference failures, and bibliography layout;
5. repair any C5 defects and rebuild;
6. only after clean visual inspection promote to `PUBLICATION_READY`;
7. then prepare the article-specific Zenodo metadata/deposit package.
