# Article II v0.2.1 publication package

**Title:** *Context Reduction in Open Quantum Systems: Multiplicativity Defects, Lindblad Order Holonomy, and Sharp Coxeter Tomography*  
**Author:** Malachevsky, A.A.  
**ORCID:** 0009-0008-6009-3196  
**Date:** 2026-09-06  
**Status:** `PUBLICATION_READY_PENDING_RENDER_AUDIT`

## Files

- `main.tex` — publication master;
- `sharp-proof-appendix.tex` — publication-compressed proof chain for the sharp Coxeter theorem;
- repository workflow `.github/workflows/article-ii-publication.yml` — deterministic PDF build and artifact upload.

## Main theorem

In the bounded finite-dimensional matrix-valued first-order Coxeter-face measurement model,

\[
L_d^{\mathrm{Cox}}=\left\lfloor\frac{d^2}{2}\right\rfloor,
\qquad d\ge3.
\]

The theorem is intentionally not stated for `d=2`; the proved low-dimensional result there is an obstruction to **extension-readiness** of minimal two-face designs under scalar-one embedding, not a no-go theorem for native two-face tomography.

## Publication repairs already incorporated

1. The binder-compatible transversality theorem is stated on the reverse-cycle-zero parameter space actually needed by the native-tilt proof.
2. The odd-to-even proof is written in exact centered scalar-one coordinates.
3. The invalid post hoc scalar determinant-normalization step is absent; all transfer witnesses are built directly in `SL_n(C)`.
4. The even-dimensional final face count is typeset correctly as

   \[
   \frac{(d-1)^2-1}{2}+d=\frac{d^2}{2}.
   \]
5. The literature boundary separates reduced order holonomy from Uhlmann/Jamiołkowski channel holonomy and separates the sharp Coxeter count from arbitrary process-tomography/Lindbladian-learning lower bounds.

## Build

The GitHub Actions workflow installs a standard TeX Live toolchain and runs

```text
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

It then performs a basic nonempty-PDF/pdfinfo preflight and uploads `main.pdf`, `main.log`, and `pdfinfo.txt` as the `article-II-v0.2.1-pdf` artifact.

## Release gate

Mathematical proof audit: complete at the current theorem level.

Targeted literature/claim-boundary audit: complete.

Author/ORCID/repository metadata: checked.

Article-specific DOI: not assigned; do not invent one before Zenodo deposit.

Remaining mandatory gate: obtain the compiled PDF artifact, inspect all pages visually, clear any C5 rendering/LaTeX defects, then promote from `PUBLICATION_READY_PENDING_RENDER_AUDIT` to `PUBLICATION_READY`.
