# BC-Origin III software companion

Article: **Boundary Compensation Origin III: Non-Factorizable Holonomy and Frustrated Multi-Shadow Spectral Geometry**

Status: draft software companion for the BC-Origin III manuscript.

## Purpose

The software checks the finite-dimensional graph-holonomy examples used in the article:

- Z2 edge holonomy signs `epsilon_ij`;
- vertex-gauge transformations and cycle products;
- balanced versus frustrated triangle spectral types;
- horizon diagnostics for toy eigen-denominators;
- companion avoided-crossing geometry for the Flow Lab.

This is a demonstration/calculation scaffold, not a physical simulator.

## Run

From the repository root or from this folder:

```bash
python software/generate_bc_origin_iii_figures.py --out figures
```

Expected outputs:

```text
triangle_holonomy_spectra.png
balanced_vs_frustrated_heatmaps.png
cycle_holonomy_product.png
flow_avoided_crossing_horizon.png
```

## Claim discipline

Allowed: finite-dimensional toy-model statements about graph holonomy, cycle products, spectral splitting, and admissibility-horizon diagnostics.

Not allowed: claims that the software derives real gauge fields, real spin glasses, particle masses, physical annihilation, empirical predictions, or a completed hidden-sector theory.
