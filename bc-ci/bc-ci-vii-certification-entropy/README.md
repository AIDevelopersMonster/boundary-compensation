# BC-CI VII Certification Entropy Demo

Companion supplement for:

**Boundary Compensation - Compensated Islands VII: Certification Entropy and Macrostate Ambiguity of Robust Reachability**  
Version v0.1.1 clean

This folder contains a minimal finite-graph audit companion. The demo computes certification-support multiplicities for robust reachability under declared finite-resolution conventions.

## What the demo audits

The demo reports:

- `reachability_matrix`
- `path_support_table`
- `section_support` witnesses for each robust path
- `weight_fraction_proxy` values declared in the config
- `macrostate_support_counts`
- `macrostate_entropy_table`
- `entropy_dominant_macrostates`
- `measure_status`
- `status_protocol`
- `reset_contamination` and tuning flags when present

All path budgets, measure conventions, robust edge statuses, section supports, and macrostate recording rules are declared inputs.

## Logarithm convention

The manuscript uses `log` as the natural logarithm, or any fixed base `b > 1`. Changing the base only rescales entropy values and does not affect ordering, maximizer existence, or protocol statuses.

## Non-claim boundary

This is a finite certification audit only. Certification entropy measures epistemic breadth of declared support. It is not thermodynamic entropy, not von Neumann entropy, not entropy production, not physical probability, not a path integral, not dynamics, not a simulation of causality, not a physical irreversibility statement, and not an arrow of time.

A measure or weight-fraction convention must be declared before the audit. If a measure is retrofitted after the desired outcome is known, the correct status is `MEASURE_TUNING_ARTIFACT`.

## Run

```bash
python certification_entropy_demo.py --config configs/default_entropy.json --out data/certification_entropy_audit.json
```

The default configuration intentionally includes a fragile loop-like support route and a reset-contaminated route to demonstrate why the entropy layer must preserve reset and tuning flags.
