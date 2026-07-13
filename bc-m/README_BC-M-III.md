# BC-M III v0.1.1 reviewed — English package

## Manuscript

**Title:** *BC-M III: Exclusion Geometry, Descriptor Boundaries, and Certified Excluded Regions*  
**Author:** A. A. Malachevsky, Independent Researcher  
**Version:** v0.1.1 reviewed  
**Programme:** Boundary Compensation / BC-M  
**License:** CC BY 4.0

The manuscript develops a carrier-neutral framework for realizable images, excluded regions, descriptor boundaries, quotient-aware exclusion, convex and nonconvex certificates, finite-resolution margins, and machine-readable failure states.

## Files

- `BC-M-III-v0.1.1-reviewed-en.pdf` — compiled reviewed manuscript.
- `BC-M-III-v0.1.1-reviewed-en.tex` — XeLaTeX source.
- `BC-M-III-Exclusion-Geometry-Lab-v0.1.1-en.html` — standalone interactive demonstration.
- `BC-M-III-v0.1.1-review-integration-note-en.md` — record of the two-review integration.
- `BC-M-III-v0.1.1-pdf-preflight-en.txt` — PDF structural preflight.

## Interactive lab

Open the HTML file in a modern browser. It has no external dependencies and works offline.

The lab contains:

1. four canonical regimes: interior realizability, realized boundary, closure-only compatibility, and strict exterior exclusion;
2. metric projection and a convex separating certificate;
3. the unit-circle counterexample showing failure of linear separation for a nonconvex image;
4. a 3x3 correlation-elliptope PSD audit;
5. an admissibility-relaxation gap laboratory;
6. live export of an educational `BCM3Report` JSON record.

The demonstration is an explanatory companion. It is not a formal proof verifier and does not promote numerical failure to mathematical exclusion.

## Build

Compile the source with XeLaTeX twice:

```bash
xelatex -interaction=nonstopmode -halt-on-error BC-M-III-v0.1.1-reviewed-en.tex
xelatex -interaction=nonstopmode -halt-on-error BC-M-III-v0.1.1-reviewed-en.tex
```
