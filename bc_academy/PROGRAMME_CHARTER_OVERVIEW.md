# BC-Academy I--V: Programme Charter overview

**Document type:** Programme Charter / Curriculum Syllabus  
**Current curriculum version:** v0.1.1  
**Purpose:** educational organization of the mathematical apparatus of Boundary Compensation

## Status

This overview summarizes the BC-Academy Programme Charter. The complete PDF/LaTeX charter may be released separately on Zenodo or added to the repository in a later publication package. This repository folder is a lightweight demonstration layer.

## Why BC-Academy exists

The Boundary Compensation corpus contains several technical modules. BC-Academy reorganizes that corpus as a reproducible learning path. The ordering follows mathematical necessity rather than publication chronology:

```text
spectra -> Schur/Feshbach -> finite-resolution access -> inverse response -> quotient/certification
```

## Module map

| BC-Academy module | Core BC sources | Learning purpose |
|---|---|---|
| I. Linear Spectral Entry | BC-I, optional TimeEntropy / Collapse | spectra, gaps, near-zero modes, sensitivity |
| II. Schur/Feshbach Response Operators | BC-III, BC-IV, partial BC-V--VI | induced gap operators and multi-channel mixing |
| III. Finite-Resolution Access and Sector Weights | BC-VII, VIII, IX, X | access windows, sector weights, parameter flow, forward atlas |
| IV. Inverse Response and Non-Identifiability | BC-XI, XII, XIII, XIV | inverse fibers, non-injectivity, selection rules, identifiability thresholds |
| V. Quotient Representatives and Certified Atlases | BC-XV--XXII, Overview I | quotient normal forms, walls, tubes, certification, reset, gluing, metrics |

## Methodological boundaries

1. **Module I isolates mathematics from cosmology.** The cosmological language in BC-I is used only as motivation. The mathematical core is spectral sensitivity of near-zero eigenvalues under declared assumptions.
2. **School analogies are outreach only.** They cannot replace definitions, proofs or mathematical statements in research syllabus and university notes.
3. **BC-Origin is optional and separate.** It is a toy-model branch, not part of the BC-Core certification infrastructure.
4. **BC-Academy is not a new research claim.** It is a curriculum and methodology charter.

## Prerequisite layers

- **Engineering entry:** matrices, eigenvalues, projectors, traces.
- **University / master's layer:** spectral projectors, perturbation theory, Schur complement, representation-theoretic decomposition, inverse problems.
- **Research layer:** quotient structures, gauge redundancy, rank stratification, atlas language, perturbation tubes, local-to-global consistency and certification logic.

## Teaching formats

Each future module should support four forms:

1. Research Syllabus
2. University Notes
3. Engineering Guide
4. Outreach Appendix / School Analogy Version

## Minimal demonstration

The demo in `demo/bc_academy_linear_spectral_demo.py` illustrates the BC-Academy I--III teaching spine using a 2x2 avoided-crossing model.
