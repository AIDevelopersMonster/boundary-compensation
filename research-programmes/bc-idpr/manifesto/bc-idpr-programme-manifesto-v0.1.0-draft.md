# Boundary Compensation — Independent Deformation and Phase-Resolved Response Programme

Canonical identifier: `BC-IDPR`
Document type: programme manifesto / branch charter
Version: `v0.1.0-draft`
Status: `internal-review`

## Executive thesis

Observed residual modulation along a parameter path generally mixes quantum deformation, normalized geometry, representation scale, sector composition, branch identity, and finite-resolution protocol. Phase structure cannot be attributed specifically to a deformation coordinate until an independent deformation model has been constructed and certified.

The dependency order is

`P3 independent deformation -> parameter-separation certification -> P1 phase-resolved response -> analytic synthesis or valid null result`.

## Central object

Use a typed family

`D(q, rho, xi; vartheta)`,

where `q` is the deformation coordinate, `rho` is representation scale, `xi` is normalized geometric data, and `vartheta` collects protocol, gauge/frame, branch-tracking, and finite-resolution choices.

For an observable `O`, distinguish

`dO/ds = partial_q O q_dot + partial_rho O rho_dot + D_xi O[xi_dot] + D_vartheta O[vartheta_dot]`.

The P3 contract is to construct paths for which contaminating terms vanish or are bounded strongly enough that the `q`-specific response is identifiable.

## Work packages

- `WP0` definitions, baselines, and anti-duplication audit.
- `WP1` independent deformation construction.
- `WP2` deformation and leakage certification.
- `WP3` signed, complex, and phase-sensitive observable design.
- `WP4` preregistered phase scan.
- `WP5` phase-law extraction and analytic interpretation.
- `WP6` robustness, wall, and certificate-reset analysis.
- `WP7` theorem, obstruction, and no-go layer.
- `WP8` reproducibility and publication package.

## Benchmark hierarchy

1. Minimal finite-dimensional family with exact separation.
2. Quantum-group or quantum-6j-inspired family with fixed normalized geometry.
3. Controlled asymptotic sequence with declared fixed ratios.
4. Deliberately confounded family as negative control.

## Failure states

- `NO_INDEPENDENT_DEFORMATION_FOUND`
- `GEOMETRY_LEAKAGE`
- `SCALE_LEAKAGE`
- `BRANCH_IDENTITY_FAILURE`
- `PHASE_SIGNAL_NOT_ROBUST`
- `MODEL_SELECTION_INCONCLUSIVE`
- `CERTIFICATE_RESET`
- `NULL_RESULT_WITH_VALID_PROTOCOL`

A valid null result is publishable.

## Publication sequence

A. Programme manifesto.
B. P3 technical foundation.
C. Certification and benchmark paper.
D. P1 preregistered experiment paper.
E. Synthesis, rigidity, universality, or principled no-go result only if supported.

## Claim firewall

The branch may establish mathematical deformation families, separation certificates, phase-sensitive response within those families, reproducible analytic or numerical structure, explicit obstructions, and null results. It may not infer fundamental dynamics, physical time, particle masses, spacetime geometry, or a unique microscopic hidden sector merely from stable modulation.

## Immediate milestone

Produce `BC-IDPR-P3-CONTRACT v0.1.0-draft` with exact definitions of `q`, `rho`, `xi`, and `vartheta`; one exact family; one confounded control; an independence certificate; candidate signed and complex observables; a P1 preregistration skeleton; and a theorem-obligation graph.
