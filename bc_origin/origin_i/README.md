# BC-Origin Visual Lab

This folder contains visualization and interactive scripts for **BC-Origin I**.

The goal is to inspect the three core effects of the signed-shadow model:

1. **Orientation-controlled shadow localization**: same-oriented winding products shift inverse-scale denominators upward and compress observable shadows.
2. **Admissibility horizon**: a branch with denominator near zero loses localized observability because `ell/L -> infinity`.
3. **Coupling-induced shadow gap**: off-diagonal coupling separates the two observable branches.

## Standalone GUI

Open this file directly in a browser:

```text
bc_origin/lab/web/index.html
```

It has sliders for `n1`, `n2`, `gamma`, `kappa`, `d1`, and `d2`, plus live plots for eigen-denominators, scale ratios, and the admissibility horizon.

No Python server is required.

## Python static visuals

Run:

```bash
python bc_origin/lab/python/generate_visuals.py --out bc_origin/lab/outputs
```

This creates publication-style PNG diagrams:

```text
bc_origin/lab/outputs/spectrum_signed_shift.png
bc_origin/lab/outputs/admissibility_horizon.png
bc_origin/lab/outputs/phase_map.png
bc_origin/lab/outputs/model_scheme.png
```

## Optional Streamlit app

If Streamlit is installed:

```bash
pip install streamlit numpy matplotlib
streamlit run bc_origin/lab/streamlit_app.py
```

## Mathematical core

The signed common-shift model is

```text
D_signed = [[d1 + gamma*s, kappa],
            [kappa,        d2 + gamma*s]]

s = sign(n1*n2)
```

Eigen-denominators:

```text
lambda_pm = (d1+d2)/2 + gamma*s +/- sqrt(((d1-d2)/2)^2 + kappa^2)
```

Observable scale ratios:

```text
S_pm = mu_eff / lambda_pm
```

The branch is localized only if `lambda_pm > 0`.
