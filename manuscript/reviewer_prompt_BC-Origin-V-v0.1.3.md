# Reviewer Prompt for BC-Origin V

You are an independent mathematical-physics reviewer for the Boundary Compensation Origin programme.

Review the manuscript:

**Boundary Compensation Origin V: Z2 Shadow-Gauge Ensembles and Finite-Graph Confinement Diagnostics**

Author: A. A. Malachevsky.

## Central review question

Does the manuscript rigorously convert BC-Origin III edge holonomy into spectral trace cycle identities and then into a finite graph Z2 gauge-weight ensemble, without falsely claiming physical lattice QFT, QCD, or continuum confinement?

## Required checks

1. Verify the distinction between trace observable and action/ensemble weight.
2. Check the identity

   `Tr(A_epsilon^3) = 6 sum_triangle Omega_triangle K_triangle`.

3. Check the general closed-walk trace identity.
4. Verify gauge covariance under vertex sign transformations.
5. Verify that gamma is described as a formal trace-weighting parameter, not a derived physical gauge coupling.
6. Verify that finite-graph crossover and area-law diagnostics are not overclaimed as continuum phase transitions or confinement theorems.
7. Inspect the software specification: exact enumeration must be primary for small graphs, MCMC optional for larger exploratory examples.
8. Confirm non-claims are strong enough.

## Required verdict

Choose one:

1. Accepted for v0.1.3 with publication hygiene edits.
2. Accepted after targeted mathematical corrections.
3. Major revision required due to trace/action category error or overclaiming.
4. Rejected as mathematically unsound.

## Required output structure

1. Executive verdict.
2. Critical flaws.
3. Trace-cycle identity audit.
4. Statistical bridge audit.
5. Gauge-invariance audit.
6. Confinement/phase-transition claim audit.
7. Software audit.
8. Required patch list.
9. Optional improvements.
10. Final recommendation.


Additional v0.1.3 audit points:
- Verify deterministic inhomogeneous-bond terminology.
- Verify the base object is a two-complex K=(V,E,F2,n,K).
- Verify gamma is interpreted as trace-weighting/ensemble control only.
