# BC-Origin VI v0.1.2: Spectral Admissibility Collapse and Projection Failure

This package contains the review manuscript and software companion for:

**Boundary Compensation Origin VI: Spectral Admissibility Collapse and Projection Failure in Frustrated Shadow-Gauge Ensembles**

Author: A. A. Malachevsky  
ORCID: 0009-0008-6009-3196  
Programme: Boundary Compensation Origin Program (BC-Origin / BC-O)  
Version: v0.1.2 review package, June 2026

Software repository pointer: https://github.com/AIDevelopersMonster/boundary-compensation

## What changed in v0.1.2

v0.1.2 preserves the ensemble-driven correction of v0.1.1 and adds three reviewer refinements: the finite-resolution threshold delta is conceptually grounded as readout resolution; the scalar-diagonal case is explained as a homogeneous closure background; and the figures are integrated into the main mathematical narrative rather than listed only as a final gallery. Holonomies remain sampled or enumerated according to the finite simplicial Z2 shadow-gauge ensemble introduced in BC-Origin V.

## Contents

```text
manuscript/
  BC-Origin-VI-v0.1.2-review-manuscript.pdf
  BC-Origin-VI-v0.1.2-review-manuscript.tex
  reviewer_prompt_BC-Origin-VI-v0.1.2.md
origin_vi/
  README.md
  software/
    bc_origin_vi_projection_core.py
    generate_bc_origin_vi_figures.py
  web/
    index.html
  figures/
    p_fail_vs_gamma.png
    frustration_density_vs_gamma.png
    lambda_min_distribution_vs_gamma.png
    frustration_vs_lambda_min_ensemble.png
    gershgorin_vs_spectral_margin.png
    wilson_loop_vs_projection_failure.png
    mcmc_trace_diagnostics.png
    exact_vs_mcmc_validation.png
    scalar_diagonal_collapse_boundary.png
    hidden_graph_projection_failure_lab.png
  data/
    single_triangle.json
    two_triangles_shared_edge.json
    triangulated_disk.json
    smoke_test_output.txt
docs/
  article_description_no_formulas_ru.md
  article_description_no_formulas_en.md
  github_repository_note.md
  zenodo_metadata_draft.txt
bibliography/
  bibliography.md
  references.bib
```

## Rebuild figures

```bash
cd origin_vi/software
python generate_bc_origin_vi_figures.py --out ../figures
```

## Smoke test

```bash
cd origin_vi/software
python bc_origin_vi_projection_core.py
```

## Claim boundary

This is a finite-dimensional BC-Origin projection-failure laboratory. It does not simulate physical particle annihilation, quantum measurement collapse, empirical vacuum dynamics, or continuum QFT.
