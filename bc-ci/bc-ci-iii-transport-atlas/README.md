# BC-CI III certified transport atlas demo

This companion package illustrates the atlas logic introduced in

**Boundary Compensation - Compensated Islands III: Certified Transport Atlases and Reset Obstructions over Parameter Bases**.

The demo is not a physical geometry or spacetime simulation. It visualizes finite-dimensional certification statuses over a declared two-parameter base. The words `atlas`, `gluing`, and `reset obstruction` mean certification bookkeeping only.

## Demonstrated statuses

- `CHART_CERTIFIED`: local chart margins are positive.
- `OVERLAP_CERTIFIED`: adjacent charts have compatible local channel projectors.
- `RESET_EDGE`: no certified transition exists across an overlap.
- `TRIPLE_DEFECT`: pairwise transitions exist but composition fails on a triple overlap.
- `GLUING_CERTIFIED`: all chart, overlap, and triple checks pass.

## Files

```text
html/demo.html       Browser-only interactive atlas visualization
atlas_scan_demo.py   Deterministic toy scanner for chart/overlap/triple status
configs/*.json       Example tolerance settings
data/                Generated JSON output
figures/             Optional generated SVG sketches
```

## Run

```bash
python atlas_scan_demo.py
```

Open `html/demo.html` in a browser for the interactive demonstration.

## Non-claim note

The two-dimensional plane in the visualization is only a parameter base. It is not physical space, spacetime, phase space, or a causal diagram.
