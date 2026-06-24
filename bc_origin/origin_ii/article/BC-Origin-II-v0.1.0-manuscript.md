# Boundary Compensation Origin II
## Structural Coupling Kernels and Multi-Shadow Spectral Geometry

**Author:** A. A. Malachevsky

## Abstract
BC-Origin II replaces pairwise coupling constants with structural kernels on a hidden winding-index space. Coupling coefficients become functions of index separation rather than fitted parameters.

## Core Idea
Replace:
\[ \kappa_{ij} \rightarrow K(n_i, n_j) \]

with:
\[ K_{ij} = k(n_i - n_j) \]

This yields a multi-shadow spectral operator whose spectrum is determined by kernel geometry.

## Key Claim
- BC-Origin I: finite 2-shadow signed operator
- BC-Origin II: N-shadow kernel operator

## Next Step
- derive admissibility maps
- compare constant vs structural coupling
- extend to non-factorizable holonomy (BC-Origin III)

## Software
See `software/` for computational companion.
