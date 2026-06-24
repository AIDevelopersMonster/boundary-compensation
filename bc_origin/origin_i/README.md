# BC-Origin I software companion

This folder contains the canonical executable software companion for:

**Boundary Compensation Origin I: Oriented Winding Shadows, Structural Scale Selection, and Signed Spectral Localization**

Related DOI:

```text
https://doi.org/10.5281/zenodo.20822186
```

## Purpose

The software reproduces the computational and visual material for the BC-Origin I toy model. It is designed to make the algebraic mechanism in the article inspectable and reproducible.

The three core effects are:

1. **Orientation-controlled shadow localization**: same-oriented winding products shift inverse-scale denominators upward and compress observable shadows.
2. **Admissibility horizon**: a branch with denominator near zero loses localized observability because `ell/L -> infinity`.
3. **Coupling-induced shadow gap**: off-diagonal coupling separates the two observable branches.

## Repository role

This GitHub folder is not the article source of record. The article is published on Zenodo. This folder is the executable companion used to check the computational and visual part of the article.

## Standalone browser GUI

Open this file directly in a browser:

```text
bc_origin/origin_i/web/index.html
```

No Python server is required.

The GUI includes:

- sliders for `n1`, `n2`, `gamma`, `kappa`, `d1`, `d2`, and `mu`;
- live spectral display for `lambda_minus` and `lambda_plus`;
- scale-ratio diagnostics `ell/L`;
- admissibility status;
- `EN/RU` language switcher;
- FAQ, symbol explanations, and characteristic preset points.

## Python static visuals

Run from the repository root:

```bash
python bc_origin/origin_i/python/generate_visuals.py --out bc_origin/origin_i/outputs
```

This creates publication-style PNG diagrams:

```text
bc_origin/origin_i/outputs/spectrum_signed_shift.png
bc_origin/origin_i/outputs/admissibility_horizon.png
bc_origin/origin_i/outputs/phase_map.png
bc_origin/origin_i/outputs/model_scheme.png
```

## Optional Streamlit app

If Streamlit is installed:

```bash
python -m pip install -r bc_origin/origin_i/requirements.txt
streamlit run bc_origin/origin_i/streamlit_app.py
```

## One-click Windows launcher

From the repository root, run:

```text
START_BC_ORIGIN_WINDOWS.bat
```

The launcher creates a local virtual environment, installs dependencies, generates static visuals, opens the output folder, and opens the standalone browser GUI.

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

## Legacy path

The older path

```text
bc_origin/lab/
```

is kept temporarily for compatibility with early repository descriptions and external users. The canonical location is now:

```text
bc_origin/origin_i/
```

Future documentation should point to `origin_i`, not to `lab`.

## Software status

This software is a lightweight reproducible demonstration scaffold for the BC-Origin I toy model. It is not a general-purpose physics simulator, does not extract real constants, and does not claim empirical validation.
