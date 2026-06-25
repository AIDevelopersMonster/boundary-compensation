# BC-Origin IV v0.1.1 software patch

This package patches the Python software companion for:

**Boundary Compensation Origin IV: Lifted Phase Flow, Spectral Pumping and Horizon Events in Shadow Geometry**

It replaces risky terminology and ambiguous variable names from the reviewer draft:

- `Topological Spectral Pumping` -> `Lifted Phase Reindexing`;
- `w1`, `w2` -> phase-lift deformation coefficients;
- `kappa` as pairwise-looking constant -> structural overlap / global kernel normalization;
- rough grid zero-crossing -> linear interpolated horizon estimates;
- adds nonzero winding validation.

The code remains a deterministic finite-dimensional toy-model visualization layer. It does not
claim physical time, physical transition probabilities, real particle creation, or empirical topological pumping.
