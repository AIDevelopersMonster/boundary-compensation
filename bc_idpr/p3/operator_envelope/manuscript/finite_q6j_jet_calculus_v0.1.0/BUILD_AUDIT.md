# Integrated manuscript build audit - v0.1.0 draft

**Date:** 2026-07-16  
**Manuscript:** `Recursive Jet Calculus and Uniform Conditioning for Finite Quantum 6j Recoupling Matrices`  
**Status:** `INTEGRATED_DRAFT_COMPILED`

## Source architecture

The manuscript is stored as a sectioned LaTeX project:

- `main.tex`;
- seven section files under `sections/`;
- `references.tex` for the directly compiled bibliography;
- `finite_q6j_jet_calculus.bib` as machine-readable bibliography metadata.

The paper integrates M10, M11, M12, the recursive jet synthesis, the uniform-conditioning contract and the sharp-radius certificate into one bounded article.

## Build environment

- pdfTeX: `3.141592653-2.6-1.40.26`;
- TeX Live: `2025/dev`;
- Python: `3.13.5`;
- NumPy: `2.3.5`.

## Build command

From the manuscript directory:

```bash
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex
```

The directly compiled `references.tex` removes a BibTeX runtime dependency while the `.bib` file remains available for later publication tooling.

## Build result

- PDF pages: `12`;
- output size: `300660` bytes;
- unresolved references: `0`;
- undefined citations: `0`;
- overfull boxes: `0`;
- underfull boxes: `0`;
- LaTeX fatal errors: `0`.

## SHA-256 hashes of locally compiled monolithic source artifacts

- manuscript source: `36a37854bba66d1556b9aa6bc11839937c12ca898b3ac4b3160d3e32d9add602`;
- bibliography metadata: `18f8f5bb350df23b9ff4214517491c09bff95658d1a01fcf8d4685a650822763`;
- compiled PDF: `29d8e80739c033d7de2614a954396d2001990ddca1257f67e25c265b41605e32`.

The repository uses a sectioned source layout, so a release-cycle hash manifest must be regenerated from a clean checkout rather than reusing the monolithic-source hash above.

## Visual audit

The 12-page PDF was rendered at 150 dpi and reviewed as a contact sheet. No clipped equations, overlapping text, broken glyphs or page-layout failures were observed.

## Current readiness impact

- `G1 Integrated manuscript`: `CLOSED_AT_V0.1.0_DRAFT`;
- `G2 Theorem-level proof audit`: `OPEN`;
- `G3 Clean-checkout reproducibility package`: `OPEN`;
- `G4 Bibliography and related-work boundary`: `PARTIALLY_CLOSED_INITIAL_PRIMARY_SET`;
- `G5 Publication hygiene`: `PARTIALLY_CLOSED_DRAFT_COMPILED`.

The draft is suitable for theorem-level review. It is not yet the upload-ready preprint.

No statement from the Gemini advisory report is used as evidence.