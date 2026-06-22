# boundary-compensation

Public reproducibility layer for the Boundary Compensation finite-resolution certification programme.

This repository provides minimal Python utilities and scripts for reproducible finite-dimensional certification experiments. Its first external demonstrator is **BC-Gateway I**: finite-resolution certification of non-identifiability in reduced open quantum system models.

## Gateway I publication

**Finite-Resolution Certification of Non-Identifiability in Reduced Open Quantum System Models: Boundary Compensation Gateway I**  
A. A. Malachevsky  
Version: v0.1.0 manuscript  
DOI: https://doi.org/10.5281/zenodo.20801748

Manuscript-support material is stored in `papers/gateway_i/`.

## Gateway I demonstrator

The initial demonstrator uses an exactly solvable two-spin pure-dephasing model. The reproducibility script computes

```text
|Gamma(t)| = |cos(t) cos(1.4 t)|
lambda_minus(t) = (1 - |Gamma(t)|) / 2
D_coarse(t) = 0.5 * ||Gamma(t)| - exp(-0.4 t)|
```

with certification parameters

```text
tau = 0.05
eta = 0.02
```

The expected reference output is approximately

```text
level=0.030, t=0.203304, lambda_minus=0.030000, D_coarse=0.009052
level=0.050, t=0.264226, lambda_minus=0.050000, D_coarse=0.000148
level=0.070, t=0.314799, lambda_minus=0.070000, D_coarse=0.010843
max D_coarse before threshold: 0.012928110761649347
```

## Quick start

```bash
python -m pip install -e .[dev]
python scripts/reproduce_gateway_i.py
pytest
```

To generate figures:

```bash
python scripts/reproduce_gateway_i.py --save-figures
```

## Claim boundary

This repository does **not** reconstruct physical baths, identify true hidden environments, or claim that certificate reset is a physical event. It provides deterministic finite-dimensional certification diagnostics for reduced quantum channels under declared thresholds and tolerances.

## License

Code is released under the MIT License. Scientific interpretation remains bounded by the controlled-claims documentation in `docs/controlled_claims.md`.
