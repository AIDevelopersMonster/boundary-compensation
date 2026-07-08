# BC-Academy I — Lecture-Article 1 HTML Demonstrations

**Module:** BC-Academy I: Linear Spectral Entry  
**Lecture-Article:** Operator, Matrix, Spectrum  
**Version:** v0.1.2  

This folder contains standalone browser demonstrations for the first BC-Academy lecture-article.

## Lecture resources

- Article DOI: [10.5281/zenodo.21251960](https://doi.org/10.5281/zenodo.21251960)
- Video lecture: [YouTube](https://youtu.be/O_ZId9dZT3c)
- NotebookLM companion: [NotebookLM](https://notebooklm.google.com/notebook/28b52381-5032-447f-9f49-e83641c7ac07)

## Run locally

Open `index.html` in any modern browser. No external libraries are required.

## Demonstrations

1. `index.html` — main route: space → operator → matrix → spectrum.
2. `demos/demo_01_diagonal_spectrum.html` — diagonal matrix and direct spectral reading.
3. `demos/demo_02_basis_change_same_spectrum.html` — same operator, different matrix representation, same spectrum.
4. `demos/demo_03_eigenvector_detector.html` — vector direction test for `Au = λu`.
5. `demos/demo_04_same_spectrum_different_operator.html` — spectrum is informative, not complete.
6. `demos/demo_05_near_zero_preview.html` — preview of a near-zero spectral point using `diag(ε, 1)`.
7. `demos/demo_06_what_spectrum_reads.html` — what spectral reading extracts from an operator: eigenvalue scales, zero / near-zero events, gap-to-zero, multiplicity / cluster status, trace, determinant, and the non-completeness of spectrum as full reconstruction.

## Claim boundary

These demonstrations are finite-dimensional educational visualizations. They do not introduce new physical claims, do not reconstruct a hidden sector, and do not replace formal definitions and proofs in the lecture article.

## Suggested GitHub Pages publication

Upload this folder to a repository and enable GitHub Pages from the repository root or `/docs` folder.
