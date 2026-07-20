# P2 Orientation-Reset Handoff

P2-E02 terminates with `ORIENTATION_UNIDENTIFIABLE` under the frozen positive
ordered basis `(R_bulk, W)`. The obstruction is localized to `U3 -> U4`, whose
certified polar factor has determinant `-1` and
`sigma_min_lower = 0.05918258018571901`.

The next authorized operation is an orientation-reset investigation, not
P2-E03 or P2-G3 positivity:

1. trace the U3/U4 bulk-wall ordering convention to the upstream N15/P5 chart
   embeddings;
2. decide whether a preregistered chart-orientation transition was omitted;
3. if and only if an upstream convention error is proved, issue
   `P2_CERTIFICATE_RESET` and rerun all five edges;
4. otherwise record a genuine non-orientable finite atlas and stop rotational
   cycle-angle propagation.

No post-hoc sign flip of U3 or U4 is authorized.
