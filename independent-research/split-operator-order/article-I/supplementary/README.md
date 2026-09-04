# Supplementary Material S1 — reproducibility manifest

The reviewed Article I release uses deterministic scripts and frozen benchmark tables for the operator-order reordering experiments.

Expected source assets:

- `operator_order_benchmarks_v020.py`
- `operator_order_benchmark_environment_v020.json`
- `operator_order_benchmarks_v020_run.log`
- `operator_order_fixed_target_benchmark_v020.csv`
- `operator_order_precedence_benchmark_v020.csv`
- `operator_order_scaling_v020.csv`
- `heisenberg_xyz_filtration_v020.csv`
- `ma_qaoa_filtration_v020.csv`

The publication figures are generated from these frozen data. Final binary figures and PDF/ZIP release assets should be attached to the GitHub release / Zenodo record rather than duplicated as ordinary Git blobs.

Benchmark scope: timings concern the classical reordering stage after pairwise weights `c_ij = 1/2 ||[U_i,U_j]||` are available. They are not benchmarks of a complete hardware-aware quantum compiler.
