# BC-CI-VIII v0.1.1: Certified Local Distances Supplement

This directory contains a finite-graph demonstration for **Boundary Compensation - Compensated Islands VIII: Finite-Resolution Atlas Metrics and Certified Local Distances**.

The supplement computes audit diagnostics only:

- `depth_distance_matrix`
- `cost_distance_matrix`
- `bottleneck_margin_matrix`
- `entropy_support_distance`
- `reset_barrier_report`
- `status_table`
- optional `quotient_component_distances`

These outputs are **certified distance diagnostics, not spacetime geometry**. They are not physical distances, causal intervals, geodesics, proper times, Lorentzian metrics, Riemannian metrics, metric tensors, curvature tensors, or field equations. The `entropy_support_distance` field is an entropy-support distance (`-log` of a support-fraction) table, where declared.

## Files

```text
bc-ci/bc-ci-viii-certified-local-distances/
├── README.md
├── certified_local_distances_demo.py
├── configs/default_distances.json
├── data/certified_local_distances_audit.json
├── html/demo.html
└── figures/
    ├── certified_distance_graph.svg
    └── distance_matrix.svg
```

## Run

```bash
python certified_local_distances_demo.py
```

The script has no non-standard dependencies.

## Status meanings

- `CERTIFIED_DISTANCE`: pair has a robust reset-free path under the declared protocol.
- `UNREACHABLE`: no robust certified path exists.
- `RESET_BLOCKED`: graph connectivity exists only through reset barriers; this is undefined certified continuation under the declared atlas protocol, not an infinite physical distance.
- `MARGIN_LOW`: reachable, but bottleneck margin is below the declared margin warning threshold.
- `ENTROPY_DISTANCE_NONMETRIC`: entropy-support diagnostic is present but no triangle law has been declared.
- `METRIC_TENSOR_NONCLAIM`: explicit reminder that no metric-tensor interpretation is made.

## Version note

This v0.1.1 supplement matches the clean manuscript. It preserves the finite-graph audit scope and adds the reset-barrier and support-fraction wording requested during review.
