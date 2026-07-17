# Mode-5 Gram Preflight

This directory contains the first executed response-independent diagnostic inside P5-UA01.

## Run

```bash
python p5_mode5_gram_geometry.py --dps 80 --output results.json
```

Dependency: `mpmath>=1.3`.

## Artifacts

- `REPORT.md` — scientific interpretation and claim ceiling.
- `p5_mode5_gram_geometry.py` — deterministic reconstruction and analysis.
- `P5_MODE5_GRAM_RESULTS.json` — machine-readable principal results.

The calculation reconstructs the frozen RC02 grid, cubic nuisance projection, integer predictor modes, half-integer control pool, and frozen bijection. It does not load pilot, calibration, confirmatory, carrier-family, phase, or energy data. It does not reopen RC02.
