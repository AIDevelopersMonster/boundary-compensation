# Mode-5 Gram Preflight

This directory contains the first executed response-independent diagnostic inside P5-UA01.

## Run

```bash
python p5_mode5_gram_geometry.py --dps 80 --output-dir results
```

Dependency:

```text
mpmath>=1.3
```

## Artifacts

- `REPORT.md` — scientific interpretation and claim ceiling.
- `p5_mode5_gram_geometry.py` — deterministic reconstruction and analysis.
- `results/P5_MODE5_GRAM_RESULTS.json` — machine-readable metrics and decisions.
- `results/GII.csv` — integer predictor Gram matrix.
- `results/GCC.csv` — control Gram matrix.
- `results/GIC.csv` — integer-control cross-Gram matrix.
- `results/MANIFEST.json` — SHA-256 file manifest.

No response data are read. This package does not reopen RC02.
