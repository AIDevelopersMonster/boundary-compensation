# Build Audit - finite q-6j jet calculus v0.1.1 reviewed

**Date:** 2026-07-16  
**Status:** `REVIEWED_PDF_COMPILED_AND_VISUALLY_VERIFIED`

## Environment

- pdfTeX: `3.141592653-2.6-1.40.26`;
- TeX Live: `2025/dev`;
- page format: A4;
- manuscript source: sectioned LaTeX;
- bibliography: directly compiled `references.tex` plus machine-readable `.bib`.

## Deterministic build

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

## Result

- pages: `15`;
- PDF size: `344597` bytes;
- unresolved references: `0`;
- undefined citations: `0`;
- overfull boxes: `0`;
- underfull boxes: `0`;
- fatal errors: `0`.

## PDF checks

- openable with PyMuPDF: yes;
- encrypted: no;
- likely scanned: no;
- fonts embedded: yes;
- outline items: 28;
- title/author/subject/keywords metadata: present;
- rendered at 180 dpi: 15 pages;
- visual defects found: none.

## Artifact hashes

See `SHA256SUMS.txt` generated after the final two-pass build.

No statement from the Gemini advisory report is used as evidence.
