# BC-CI IV certification-cost selection demo

This companion package illustrates the finite-dimensional status logic used in

**Boundary Compensation - Compensated Islands IV: Externally Anchored Hidden Sections and Certification-Cost Selection**.

The demo is not a physical simulation. It does not implement time evolution, Hamiltonian dynamics, Lagrangian dynamics, photons, waves, fields, spacetime geometry, or a physical action principle.

It visualizes the BC-CI IV transition from an unconstrained scaffold to externally anchored hidden-section selection:

```text
all declared hidden sections  ->  externally anchored admissible class  ->  cost-selected class
```

The central margins are:

```text
readout margin:     q(p) = ||R_p(Xi)|| - delta_read
variation cost:     sum_edges ||Xi_q - Xi_p||^2
leakage cost:       sum_p ||(I-Pi_p)L_p Xi_p||^2
balance residual:   ||sum_p W_p L_p Xi_p||
```

## Contents

```text
configs/default_selection.json
certification_cost_demo.py
html/demo.html
figures/*.svg
data/cost_demo_output.json
```

## Run

From this directory:

```bash
python certification_cost_demo.py
```

Open the interactive HTML demonstration directly in a browser:

```text
html/demo.html
```

No network access and no external JavaScript libraries are required.


## Weight status and anti-tuning note

The weights in the demo are certification-policy parameters, not physical constants or fitted couplings. A single hand-tuned weight vector does not carry theorem-level significance. Robust conclusions should be checked over declared admissible weight classes or Pareto-stable selections, as deferred to BC-CI V.

## Claim hygiene

The selected section is not a physical trajectory and the cost is not an action, energy, entropy, or Lagrangian. The demo only illustrates finite-dimensional certification-cost selection under externally declared anchors.
