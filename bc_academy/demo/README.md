# BC-Academy demo: finite-resolution spectral access

This demo is a minimal, dependency-free Python illustration for the first BC-Academy modules.

It demonstrates the educational chain:

```text
near-zero spectrum -> finite-dimensional operator -> finite-resolution access -> sector weights
```

## Model

The script uses a two-dimensional self-adjoint avoided-crossing family

```text
A(t) = [[t, eps], [eps, -t]]
```

with two fixed coordinate-sector projectors. As `t` changes, the eigenvalues move and the positive-branch sector weights flow between the two sectors.

A simple finite-resolution access rule counts branches satisfying:

```text
|lambda| <= delta
```

## Run

```bash
python bc_academy_linear_spectral_demo.py
```

## What it shows

- full gap branches move with the parameter;
- sector weights flow across the avoided crossing;
- finite-resolution access depends on the declared threshold;
- response data do not reconstruct a unique hidden sector.

## Claim boundary

This is a curriculum demonstration. It is not a physical time evolution, quantum dynamics, detector model, RG flow, particle-mass model, or hidden-sector reconstruction.
