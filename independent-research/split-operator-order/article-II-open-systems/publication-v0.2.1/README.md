# Article II v0.2.1 publication package

**Title:** *Context Reduction in Open Quantum Systems: Multiplicativity Defects, Lindblad Order Holonomy, and Sharp Coxeter Tomography*  
**Author:** Malachevsky, A.A.  
**ORCID:** 0009-0008-6009-3196  
**Date:** 2026-09-06  
**Status:** `PUBLISHED`  
**Zenodo DOI:** https://doi.org/10.5281/zenodo.22421827

## Files

- `main.tex` — publication master;
- `article.tex` — canonical CI build entrypoint and compatibility shim;
- `sharp-proof-appendix.tex` — publication-compressed proof chain for the sharp Coxeter theorem;
- repository workflow `.github/workflows/article-ii-publication.yml` — deterministic PDF build, log gate, pdfinfo preflight, and artifact upload.

## Main theorem

In the bounded finite-dimensional matrix-valued first-order Coxeter-face measurement model,

\[
L_d^{\mathrm{Cox}}=\left\lfloor\frac{d^2}{2}\right\rfloor,
\qquad d\ge3.
\]

The theorem is intentionally not stated for `d=2`; the proved low-dimensional result there is an obstruction to **extension-readiness** of minimal two-face designs under scalar-one embedding, not a no-go theorem for native two-face tomography.

## Publication repairs incorporated

1. The binder-compatible transversality theorem is stated on the reverse-cycle-zero parameter space actually needed by the native-tilt proof.
2. The odd-to-even proof is written in exact centered scalar-one coordinates.
3. The invalid post hoc scalar determinant-normalization step is absent; all transfer witnesses are built directly in `SL_n(C)`.
4. The even-dimensional final face count is typeset correctly as

   \[
   \frac{(d-1)^2-1}{2}+d=\frac{d^2}{2}.
   \]
5. The literature boundary separates reduced order holonomy from Uhlmann/Jamiołkowski channel holonomy and separates the sharp Coxeter count from arbitrary process-tomography/Lindbladian-learning lower bounds.
6. The first CI render failure (`Undefined control sequence: \mathscr`) was repaired by the canonical `article.tex` entrypoint; no mathematical content changed.

## Build and render audit

The GitHub Actions workflow runs

```text
latexmk -pdf -interaction=nonstopmode -halt-on-error article.tex
```

and rejects undefined references/citations, undefined control sequences, and fatal LaTeX errors before uploading the artifact.

Successful audited run: `33995974451` at head `26b2e9488b823b225f0c8312e78cb8c6c431c3e5`.

Artifact: `article-II-v0.2.1-pdf`, artifact id `9978084171`, SHA-256 digest `d474fa8cc1ab94aa7bf6a184d647fb2536597780ebbfbc693b4456aafc4c7488`.

PDF preflight:

- 16 pages;
- PDF 1.5;
- unencrypted and openable;
- text PDF, not scan-like;
- no undefined references/citations or fatal LaTeX errors;
- no overfull/underfull box warnings in the final log;
- all 16 pages rendered to PNG and visually inspected as a montage, with targeted full-page inspection of the title page, appendix transition, and final bibliography/repository page;
- no clipping, overlap, black boxes, broken glyphs, or equation truncation found.

The log contains only two nonfatal `hyperref` bookmark warnings caused by math shifts in an appendix subsection title. They do not affect page rendering or mathematical content and are classified C6/nonblocking for this release.

## Publication record

Zenodo DOI: **10.5281/zenodo.22421827**  
Canonical DOI URL: https://doi.org/10.5281/zenodo.22421827

Mathematical proof audit: complete at the current theorem level.

Targeted literature/claim-boundary audit: complete.

Author/ORCID/repository metadata: checked.

Source compilation and PDF visual audit: complete.

**Release decision:** `PUBLISHED`.
