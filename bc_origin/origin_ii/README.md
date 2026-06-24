# BC-Origin II

**Boundary Compensation Origin II: Structural Coupling Kernels and Multi-Shadow Spectral Geometry**

Status: working module after BC-Origin I.

## Purpose
BC-Origin II replaces pairwise coupling constants with structural kernels on a hidden winding-index space:

```
kappa_ij = K(n_i, n_j)
```

or translationally invariant form:
```
K_ij = k(n_i - n_j)
```

## Model
- Hidden winding labels: n_i ∈ Z\{0}
- Sign structure: s_ij = sign(n_i n_j)
- Operator:
```
(D_N)_ii = d_i + γ Σ s_ij K_ij
(D_N)_ij = η K_ij
```

## GUI
Interactive kernel lab:
- Location: bc_origin/origin_ii/web/index.html
- Features:
  - Kernel heatmap
  - Sign matrix heatmap
  - Operator spectrum
  - Horizon diagnostic

## Interpretation
This module is a structural toy model. It does not claim physical reconstruction of fundamental couplings.
