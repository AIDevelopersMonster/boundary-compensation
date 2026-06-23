# DC-O Shadow Lab

**DC-O working name:** *Discrete Closure / Observable-shadow toy program*.

This repository contains a practical calculation skeleton for a minimal hidden-to-observed shadow model:

1. one hidden index-cycle generator produces one observable scale-selected shadow;
2. two hidden generators produce coupled observable shadows with index-dependent splitting;
3. admissible observable scale ratios are selected by closure equations, not inserted as manual cutoffs.

The project is intentionally modest: it is a computational toy program and article skeleton for testing whether a non-fundamental observed layer can arise as a projected shadow of hidden structural generators. It does not identify this toy hidden layer with real physics.

## Core equations

One-generator closure:

```text
(mu_q / ell) * L + theta(q) = 2*pi*c
```

Scale relation:

```text
ell / L = mu_q / (2*pi*c - theta(q))
```

Two-generator spectral denominator matrix:

```text
D = [[d1, g],
     [g,  d2]]

where d_i = 2*pi*c_i - theta(q_i), g = kappa*q1*q2.
```

Split shadow scales use the positive eigenvalues of `D`.

## Quick start

```bash
python scripts/run_experiment_1.py
python scripts/run_experiment_2.py
python scripts/run_all.py
python -m pytest tests
```

Outputs are written to `results/`.

## Repository structure

```text
article/    article skeleton and research protocol
scripts/    executable experiments
src/        Python package dco_shadow
tests/      validation tests
results/    generated CSV/JSON results
```
