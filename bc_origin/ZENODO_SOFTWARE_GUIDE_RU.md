# BC-Origin Shadow Lab — краткое руководство для пользователей Zenodo

**Project repository:** https://github.com/AIDevelopersMonster/boundary-compensation  
**Current BC-Origin branch:** https://github.com/AIDevelopersMonster/boundary-compensation/tree/codex/bc-origin  
**Current draft pull request:** https://github.com/AIDevelopersMonster/boundary-compensation/pull/5  
**BC-Origin folder:** https://github.com/AIDevelopersMonster/boundary-compensation/tree/codex/bc-origin/bc_origin  
**Visual Lab folder:** https://github.com/AIDevelopersMonster/boundary-compensation/tree/codex/bc-origin/bc_origin/lab  
**Standalone GUI source:** https://github.com/AIDevelopersMonster/boundary-compensation/blob/codex/bc-origin/bc_origin/lab/web/index.html

> Note: until PR #5 is merged, the active BC-Origin files are in the `codex/bc-origin` branch. After merge, the same materials will be available from the repository `main` branch.

---

## 1. What is included

This Zenodo release is accompanied by the **BC-Origin Shadow Lab**, a small visual and computational environment for exploring the first BC-Origin model:

```text
hidden oriented winding -> scale channel + sign channel -> observable shadow
```

The lab demonstrates three effects of the signed-shadow model:

1. **Orientation-controlled shadow localization** — the sign of the winding product shifts the observable inverse-scale spectrum.
2. **Admissibility horizon** — a branch with `lambda = 0` loses localized observability because `ell/L -> infinity`.
3. **Coupling-induced shadow gap** — off-diagonal coupling separates the two spectral branches.

The programs are intentionally simple and visual. They are designed as a reproducible research scaffold rather than a large software package.

---

## 2. Quick start for users

### Option A — one-click Windows launcher

Clone the repository, switch to the active branch, and run:

```bat
START_BC_ORIGIN_WINDOWS.bat
```

The launcher creates a local virtual environment, installs dependencies, generates figures, and opens the visual output folder and browser GUI.

Direct file link:

https://github.com/AIDevelopersMonster/boundary-compensation/blob/codex/bc-origin/START_BC_ORIGIN_WINDOWS.bat

### Option B — browser GUI without Python

Open this file after cloning/downloading the repository:

```text
bc_origin/lab/web/index.html
```

This interface runs locally in the browser. It provides sliders for:

```text
n1, n2, gamma, kappa, d1, d2, mu
```

and visualizes the signed matrix, eigen-denominators, observable scale ratios, and horizon crossing.

GitHub source link:

https://github.com/AIDevelopersMonster/boundary-compensation/blob/codex/bc-origin/bc_origin/lab/web/index.html

### Option C — Python static figures

Install dependencies:

```bash
python -m pip install -r bc_origin/lab/requirements.txt
```

Generate figures:

```bash
python bc_origin/lab/python/generate_visuals.py --out bc_origin/lab/outputs
```

Expected outputs:

```text
bc_origin/lab/outputs/spectrum_signed_shift.png
bc_origin/lab/outputs/admissibility_horizon.png
bc_origin/lab/outputs/phase_map.png
bc_origin/lab/outputs/model_scheme.png
```

Python source links:

- Core calculations: https://github.com/AIDevelopersMonster/boundary-compensation/blob/codex/bc-origin/bc_origin/lab/python/bc_origin_visual_core.py
- Figure generator: https://github.com/AIDevelopersMonster/boundary-compensation/blob/codex/bc-origin/bc_origin/lab/python/generate_visuals.py
- Requirements: https://github.com/AIDevelopersMonster/boundary-compensation/blob/codex/bc-origin/bc_origin/lab/requirements.txt

### Option D — Streamlit interface

If Streamlit is installed:

```bash
streamlit run bc_origin/lab/streamlit_app.py
```

Source link:

https://github.com/AIDevelopersMonster/boundary-compensation/blob/codex/bc-origin/bc_origin/lab/streamlit_app.py

---

## 3. Repository layout

```text
bc_origin/
  README.md
  ZENODO_SOFTWARE_GUIDE_RU.md
  USER_GUIDE_RU.md
  article/
    BC-Origin-I-v0.1.0-draft.md
  docs/
    00_program_definition.md
    01_article_skeleton.md
    02_experiment_protocol.md
    03_core_effects.md
    04_structural_coupling_and_multishadow_branch.md
  lab/
    README.md
    requirements.txt
    run_windows.bat
    run_windows.ps1
    web/
      index.html
    python/
      bc_origin_visual_core.py
      generate_visuals.py
    streamlit_app.py
  prompts/
    01_strong_theory_builder.md
    02_adversarial_reviewer.md
    03_formal_math_reviewer.md
    04_computational_experimenter.md
    05_publication_auditor.md
```

---

## 4. What the figures show

### `spectrum_signed_shift.png`

Shows how same-oriented and opposite-oriented winding products shift the two spectral branches `lambda+` and `lambda-` in opposite directions.

### `admissibility_horizon.png`

Shows the critical curve `gamma_c(kappa)` where the lower opposite-orientation branch reaches `lambda- = 0`.

### `phase_map.png`

Shows the parameter regions where the lower branch is localized or horizon-crossed.

### `model_scheme.png`

Summarizes the architecture:

```text
hidden winding n
  -> |n| scale channel
  -> sign(n) orientation channel
  -> closure equation and signed operator
  -> observable shadow
```

---

## 5. Minimal mathematical model

Hidden generator:

```text
h = (q, n)
```

where `q` is an index-like residual type and `n in Z` is an oriented winding number.

Scale channel:

```text
|n|
```

Sign channel:

```text
sign(n)
```

Two-shadow sign product:

```text
s = sign(n1*n2)
```

Signed operator:

```text
D_signed = [[d1 + gamma*s, kappa],
            [kappa,        d2 + gamma*s]]
```

Eigen-denominators:

```text
lambda_pm = (d1+d2)/2 + gamma*s +/- sqrt(((d1-d2)/2)^2 + kappa^2)
```

Localized observable branches require:

```text
lambda_pm > 0
```

---

## 6. Suggested Zenodo description paragraph

This release includes the first BC-Origin preprint and the accompanying BC-Origin Shadow Lab. The lab is a lightweight visual/computational environment for exploring oriented winding shadows, signed spectral localization, admissibility horizons, and coupling-induced branch gaps. It includes a standalone browser GUI, Python figure-generation scripts, optional Streamlit interface, reproducibility notes, and role prompts for theory building and review. Source code and updated materials are available on GitHub: https://github.com/AIDevelopersMonster/boundary-compensation . The active development branch for this release is `codex/bc-origin`: https://github.com/AIDevelopersMonster/boundary-compensation/tree/codex/bc-origin .

---

## 7. Suggested Zenodo keywords

```text
Boundary Compensation; BC-Origin; resonant shadows; emergent geometry; winding number; spectral geometry; signed operator; admissibility horizon; computational toy model; mathematical physics; visualization; Python; Streamlit; interactive model
```

---

## 8. Suggested citation note

If using the software or figures, cite the Zenodo record and refer to the GitHub repository for the latest executable version:

```text
A. A. Malachevsky, Boundary Compensation Origin I: Oriented Winding Shadows, Structural Scale Selection, and Signed Spectral Localization, v0.1.0, Zenodo, 2026.
```

Repository:

```text
https://github.com/AIDevelopersMonster/boundary-compensation
```
