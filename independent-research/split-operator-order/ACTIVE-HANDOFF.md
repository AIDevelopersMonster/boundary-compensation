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

Current release level: `PUBLICATION_READY`.

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
The first GitHub Actions render attempt failed before producing a PDF because of a C5 LaTeX source defect: the single `\mathscr D` use lacked a script-font definition. Mathematics was unaffected.

Repair:
- `publication-v0.2.1/article.tex` became the canonical build entrypoint;
- it defines `\mathscr` compatibly as `\mathcal` and inputs `main.tex`;
- workflow builds `article.tex`;
- workflow log gate rejects undefined references/citations, undefined control sequences, and fatal errors.

Repair commits:
- build entrypoint: `75538921b994d8a594b25dfbf10956623f9df404`;
- workflow/log gate: `26b2e9488b823b225f0c8312e78cb8c6c431c3e5`.

## Publication render audit checkpoint 9 — 2026-09-06
Post-repair workflow run `33995974451` completed successfully: build, LaTeX log gate, pdfinfo preflight, and artifact upload all passed.

Artifact:
- name `article-II-v0.2.1-pdf`;
- id `9978084171`;
- workflow head `26b2e9488b823b225f0c8312e78cb8c6c431c3e5`;
- SHA-256 digest `d474fa8cc1ab94aa7bf6a184d647fb2536597780ebbfbc693b4456aafc4c7488`.

PDF audit:
- 16 pages, PDF 1.5, unencrypted, openable, text-based;
- final log has no undefined references/citations, undefined control sequence, fatal error, overfull box, or underfull box warnings;
- all 16 pages rendered to PNG and inspected as a full montage;
- title page, appendix transition, and final bibliography/repository page additionally inspected at full-page resolution;
- no clipping, overlap, black boxes, broken glyphs, equation truncation, or bibliography-layout blocker found.

Two nonfatal hyperref bookmark warnings remain from math shifts in one appendix subsection title. They do not alter visible page rendering or mathematical content and are classified C6/nonblocking.

Publication README promotion commit: `a45c1ea4588f164411f6d308567828d40997bc41`.

## Current publication gate
Mathematical existence blockers: none currently identified.

Targeted related-work/claim-boundary audit: complete.

Author/ORCID: verified.

Repository licence: MIT at repository level.

Article-specific Zenodo DOI: not assigned; do not invent one.

Former even-dimensional typography defect is corrected as `((d-1)^2-1)/2 + d = d^2/2`.

Source compilation: passed.

PDF visual inspection: passed.

Current release state: `PUBLICATION_READY`.

## Next permitted attack
Do not reopen theorem existence unless a concrete mathematical defect is found. The next publication action is the article-specific Zenodo deposit package: finalize title/abstract/keywords/version/license/related identifiers, deposit the audited PDF and source bundle, record the assigned DOI in repository metadata, and only then update citation records. Conditioning/noise robustness remains a separate future research problem.
