# BC-CI Engineering Guide I - reference supplement v0.1.1 clean

This folder accompanies:

**Boundary Compensation - Compensated Islands Engineering Guide I: A Step-by-Step Certification Pipeline**

The supplement demonstrates a deterministic finite-dimensional status-returning audit. It does not implement physical dynamics, physical causality, thermodynamics, quantum measurement, gravity, or spacetime geometry.

## Data ingestion

The pipeline ingests finite-dimensional positive response matrices `B_theta` from a declared preprocessing protocol. They may come from covariance-like summaries, reduced response operators, finite-dimensional signal projections, sensor-derived matrices, or other declared finite-dimensional residual data. The supplement does not prescribe a physical origin for `B_theta` and does not reconstruct a hidden generator from it.

## Files

Source/configuration files:

- `README.md` - this file.
- `requirements.txt` - Python dependencies.
- `bc_ci_audit.py` - reference Python script for the toy protocol.
- `configs/toy_protocol_config.json` - minimal declared protocol package.
- `manifest.json` - generated package manifest with file hashes.

Generated outputs:

- `outputs/response_status.csv` - threshold/readout status at each diagnostic node.
- `outputs/section_status.csv` - Pareto and epsilon-robust section audit.
- `outputs/edge_status.csv` - robust edge / reset / endpoint-failure / fragile edge statuses.
- `outputs/reachability_matrix.csv` - certified reachability relation under path budget.
- `outputs/distance_depth.csv` - minimum certified depth diagnostics.
- `outputs/distance_cost.csv` - additive audit cost diagnostics.
- `outputs/bottleneck_margin.csv` - best bottleneck margin diagnostics.
- `outputs/path_count_matrix.csv` - certified path counts under path budget.
- `outputs/certification_entropy.csv` - log path-count entropy where support is nonempty.
- `outputs/run_summary.json` - top-level status summary, config hash, output hashes, and claim-firewall flags.
- `outputs/manifest.json` - copy of generated manifest for output-only workflows.
- `figures/diagnostic_graph.svg` - graph view of certified and reset/failed edges.
- `figures/status_tree.svg` - status-returning audit flow.

## Setup

```bash
python3 -m pip install -r requirements.txt
```

## Run

From this directory:

```bash
python3 bc_ci_audit.py --config configs/toy_protocol_config.json --out outputs --figures figures
```

The core CSV outputs are deterministic for a fixed config and dependency stack. `run_summary.json` and manifest files include a generation timestamp and hashes for release auditing.

## Floating-point guardrail

The config declares `fp_tol`. The response threshold logic is:

```text
margin > fp_tol        -> CHANNEL_CERTIFIED
margin < -fp_tol       -> READOUT_BELOW_THRESHOLD
abs(margin) <= fp_tol  -> MARGIN_AMBIGUOUS
```

`MARGIN_AMBIGUOUS` means that the point lies too close to a declared threshold wall to force a reliable pass/fail decision.

## INF / UNDEFINED convention

Matrix-shaped CSV outputs may use `INF` when no finite certified path exists and `UNDEFINED` when no supported bottleneck or entropy value exists. These are computational placeholders only.

`INF` is not infinite physical distance. `RESET_BLOCKED` is a logical certification failure under the declared protocol, not a distance value.

## Claim firewall

The output statuses are audit statuses. They are not physical statuses.

- `TRANSPORT_NONPHYSICAL`: parameter continuation is not physical propagation.
- `CAUSALITY_NONCLAIM`: certified reachability is not physical causality.
- `THERMODYNAMIC_ENTROPY_NONCLAIM`: certification entropy is not thermodynamic entropy.
- `METRIC_TENSOR_NONCLAIM`: certified distances are not spacetime metric tensors.

## Reproducibility contract

A valid BC-CI run must declare thresholds and protocol choices before reading the desired output. Retrofitting thresholds, measures, weights, or distance costs after observing the output must be flagged as a tuning artifact.
