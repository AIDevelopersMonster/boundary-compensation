# BC-CI V: Weight-Robust Certification Demo

This folder is a GitHub-ready computational supplement for:

**Boundary Compensation -- Compensated Islands V: Weight-Robust Certification and Pareto-Stable Hidden Sections**

It demonstrates a finite-dimensional audit of hidden-section candidates under uncertainty in certification-policy weights.

## Claim hygiene

This supplement is **not** a physical simulation. It does not model spacetime, fields, particles, photons, dynamics, action, energy, entropy, or causality. The weights are certification-policy parameters, not physical constants. The admissible weight domain is a declared input protocol object and must not be retrofitted after observing a preferred winner.

A candidate selected by one hand-tuned vector is not treated as structurally meaningful. The demo reports:

- `PARETO_STABLE`
- `EXACT_WEIGHT_ROBUST`
- `FACET_ROBUST`
- `EPSILON_ROBUST`
- `MINIMAX_ROBUST`
- `WEIGHT_FRAGILE`
- `DOMINATED`
- `TUNING_ARTIFACT`
- `NONUNIQUE_SELECTION` where applicable

## Files

```text
bc-ci/bc-ci-v-weight-robust-selection/
├── README.md
├── weight_robust_selection_demo.py
├── configs/
│   └── default_weight_simplex.json
├── html/
│   └── demo.html
├── data/
│   └── weight_chambers.json
└── figures/
    ├── pareto_frontier.svg
    ├── weight_simplex_chambers.svg
    └── fragile_vs_robust_selection.svg
```

## Run

```bash
python weight_robust_selection_demo.py
```

The default configuration samples the 6-dimensional normalized weight simplex and estimates exact, facet-style, and epsilon robustness fractions for finite candidate sections. Epsilon robustness is the primary finite-resolution audit; exact/facet chambers are strong special cases.

## Browser demo

Open `html/demo.html` in a browser. It visualizes a 3-component simplex slice for readability. The picture is an audit visualization, not a spacetime diagram, not causality, and not a physical arrow of time.
