# Boundary Compensation

This repository collects reproducible companion materials, minimal software utilities, demonstrations, and publication-support files for the **Boundary Compensation** research programme.

Current repository tracks include:

- **BC-Origin** toy-model and software companions;
- **BC-Academy** educational and methodological demonstrations for the mathematical apparatus of Boundary Compensation.

## BC-Academy demonstration

The new `bc_academy/` folder introduces **BC-Academy I--V**, the curriculum track for the mathematical apparatus of Boundary Compensation.

BC-Academy organizes the BC corpus as a learning path:

```text
spectra
  -> Schur/Feshbach response operators
  -> finite-resolution access and sector weights
  -> inverse response and non-identifiability
  -> quotient representatives and certified atlases
```

Quick start:

```bash
cd bc_academy/demo
python bc_academy_linear_spectral_demo.py
```

The demo is dependency-free and illustrates a 2x2 avoided-crossing model: full gaps move, sector weights flow, and finite-resolution access depends on a declared threshold.

## BC-Origin IV v0.1.1 software patch

This package also preserves the Python software companion patch for:

**Boundary Compensation Origin IV: Lifted Phase Flow, Spectral Pumping and Horizon Events in Shadow Geometry**

It replaces risky terminology and ambiguous variable names from the reviewer draft:

- `Topological Spectral Pumping` -> `Lifted Phase Reindexing`;
- `w1`, `w2` -> phase-lift deformation coefficients;
- `kappa` as pairwise-looking constant -> structural overlap / global kernel normalization;
- rough grid zero-crossing -> linear interpolated horizon estimates;
- adds nonzero winding validation.

The code remains a deterministic finite-dimensional toy-model visualization layer. It does not claim physical time, physical transition probabilities, real particle creation, or empirical topological pumping.

## Claim boundary

Repository materials are finite-dimensional mathematical, computational, educational, or toy-model companions. They do not claim hidden-sector reconstruction, Standard Model derivation, empirical particle physics, physical time dynamics, continuum QFT, or cosmological prediction.
