# BC-Origin II

**Full title:** Boundary Compensation Origin II: Structural Coupling Kernels and Multi-Shadow Spectral Geometry

**Status:** working module after published BC-Origin I.

BC-Origin II does not modify BC-Origin I. The published first module remains the baseline for oriented winding shadows, structural scale selection, and signed two-shadow localization.

## Purpose

BC-Origin II addresses the coupling problem left open by BC-Origin I. The two-shadow model used an explicit pairwise coupling parameter `kappa`. BC-Origin II replaces pairwise fitted constants by structural kernel values on a hidden winding-index space:

```text
kappa_ij = K(n_i, n_j)
```

For translation-invariant kernels this becomes:

```text
K_ij = k(n_i - n_j)
```

The resulting `N x N` multi-shadow operator has spectra, admissibility horizons, and localization patterns determined by winding labels and a declared kernel rule.

## Main objects

Hidden winding labels:

```text
I_N = {n_1, ..., n_N} subset Z \ {0}
```

Sign rule:

```text
s_ij = sign(n_i n_j)
```

Closure denominators:

```text
d_i = 2*pi*|n_i| - theta(|q_i|)
```

Baseline structural multi-shadow operator:

```text
(D_N)_ii = d_i + gamma * sum_{j != i} s_ij K_ij
(D_N)_ij = eta * K_ij,  i != j
```

A signed-offdiagonal diagnostic variant is also implemented in software, but it should be marked as a variant unless adopted in the manuscript.

## Software

Run from the repository root:

```bash
python bc_origin/origin_ii/software/generate_bc_origin_ii_figures.py --out bc_origin/origin_ii/figures
```

Expected outputs:

```text
kernel_decay_profile.png
kernel_matrix_heatmap.png
n_body_spectrum.png
lambda_min_horizon_map.png
constant_vs_structural_coupling.png
balanced_sign_graph_check.png
```

## Claim discipline

BC-Origin II may claim structural replacement of pairwise coupling constants inside the toy model. It must not claim derivation of physical couplings, gravity, particle spectra, genuine spin-glass frustration, or empirical validation.

The baseline sign rule is balanced:

```text
s_ij = sigma_i sigma_j
s_ij s_jk s_ki = +1
```

Genuine frustration requires a non-factorizable edge holonomy and is reserved for a later module.
