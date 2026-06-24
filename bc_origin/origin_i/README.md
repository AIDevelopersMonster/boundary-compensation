# BC-Origin I software companion

This folder is the canonical software location for the published BC-Origin I module:

**Boundary Compensation Origin I: Oriented Winding Shadows, Structural Scale Selection, and Signed Spectral Localization**

DOI: https://doi.org/10.5281/zenodo.20822186

## Purpose

The programs reproduce the computational and visual companion to BC-Origin I. They inspect the signed two-shadow model and its three core effects:

1. orientation-controlled shadow localization;
2. admissibility-horizon crossing;
3. coupling-induced branch separation.

## Standalone browser GUI

Open directly in a browser:

```text
bc_origin/origin_i/web/index.html
```

No Python server is required.

## Python static figures

Run from the repository root:

```bash
python bc_origin/origin_i/python/generate_visuals.py --out bc_origin/origin_i/outputs
```

Expected outputs:

```text
spectrum_signed_shift.png
admissibility_horizon.png
phase_map.png
model_scheme.png
```

## Optional Streamlit GUI

```bash
python -m pip install -r bc_origin/origin_i/requirements.txt
streamlit run bc_origin/origin_i/streamlit_app.py
```

## Legacy path

The earlier path

```text
bc_origin/lab/
```

is kept temporarily for compatibility with early BC-Origin I repository descriptions and external users. The canonical location is now `bc_origin/origin_i/`.

## Software status

This is a lightweight reproducible demonstration scaffold for the BC-Origin I toy model. It is not a general-purpose physics simulator and does not claim empirical validation.
