# BC-Origin V v0.1.3 review package

Boundary Compensation Origin V: Simplicial Z2 Shadow-Gauge Ensembles.

This package contains the v0.1.3 review manuscript, LaTeX source, Python reproducibility layer, figures, and interactive HTML lab.

## v0.1.3 structural patch

- Replaces random-bond terminology with deterministic inhomogeneous-bond terminology.
- Moves triangular 2-cells F2 into the base object: K=(V,E,F2,n,K).
- Clarifies gamma as a trace-weighting / ensemble-control parameter, not physical time, temperature, or fundamental gauge coupling.
- Keeps the trace/action separation: Tr(A_epsilon^3) is a trace functional; Z(gamma) is the finite ensemble.
- Keeps the full shadow operator D_epsilon = Delta + eta A_epsilon only for horizon/admissibility diagnostics.

## Main files

- manuscript/BC-Origin-V-v0.1.3-review-manuscript.pdf
- manuscript/BC-Origin-V-v0.1.3-review-manuscript.tex
- manuscript/reviewer_prompt_BC-Origin-V-v0.1.3.md
- origin_v/software/bc_origin_v_gauge_ensemble_core.py
- origin_v/software/generate_bc_origin_v_figures.py
- origin_v/web/index.html

## Command

python origin_v/software/generate_bc_origin_v_figures.py --out origin_v/figures

## Claim boundary

This is a finite simplicial Z2 shadow-gauge ensemble and software lab. It is not a physical lattice-QFT simulator, not a QCD confinement simulator, and not an empirical spin-glass model.
