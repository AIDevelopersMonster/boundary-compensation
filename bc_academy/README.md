# BC-Academy I--V demonstration package

**Programme:** Boundary Compensation / BC-Academy  
**Status:** educational and methodological demonstration layer  
**Version:** v0.1.1 repository package  
**Author:** A. A. Malachevsky  
**ORCID:** 0009-0008-6009-3196

This folder introduces **BC-Academy**, the educational track for the mathematical apparatus of Boundary Compensation. It is not a new physics branch and not a hidden-sector reconstruction claim. It is a reproducible teaching layer that turns the BC corpus into a curriculum path.

## Central thesis

Finite-resolution data do not reconstruct hidden reality directly; they define certified layers of compatible response structure.

The BC-Academy teaching spine is:

```text
near-zero spectrum
  -> D_gap
  -> A_gap
  -> (epsilon_kappa, omega_kappa,s)
  -> R_delta[A]
  -> Phi^{-1}(R_obs)/~
  -> F_adm
  -> B = W^* W
  -> sr(B)
  -> D_C^{(eta,tau)}(B)
  -> certified atlas / reset / gluing / metrics
```

## Curriculum modules

1. **BC-Academy I: Linear Spectral Entry**  
   Matrices, spectra, near-zero modes, gaps and spectral sensitivity.

2. **BC-Academy II: Schur/Feshbach Response Operators**  
   From scalar compensation gaps to induced finite-dimensional gap operators.

3. **BC-Academy III: Finite-Resolution Access and Sector Weights**  
   Spectral windows, projectors, sector weights, parameter flow and forward atlases.

4. **BC-Academy IV: Inverse Response and Non-Identifiability**  
   Response-equivalence classes, admissible inverse fibers and identifiability thresholds.

5. **BC-Academy V: Quotient Representatives and Certified Atlases**  
   Normal forms, rank walls, dictionary tubes, certification, reset, gluing and metrics.

## Folder contents

```text
bc_academy/
  README.md
  PROGRAMME_CHARTER_OVERVIEW.md
  demo/
    README.md
    bc_academy_linear_spectral_demo.py
    sample_output.txt
  docs/
    README.md
    BC_ACADEMY_I_V_PROGRAMME_CHARTER_v0.1.1_RU.md
    BC_ACADEMY_I_RESEARCH_SYLLABUS_v0.1.1_RU.md
    zenodo_metadata_draft.txt
```

## Documents

- `docs/BC_ACADEMY_I_V_PROGRAMME_CHARTER_v0.1.1_RU.md` — repository-facing companion to the Programme Charter / Curriculum Syllabus v0.1.1.
- `docs/BC_ACADEMY_I_RESEARCH_SYLLABUS_v0.1.1_RU.md` — repository-facing companion to BC-Academy I: Linear Spectral Entry — Research Syllabus v0.1.1.
- `PROGRAMME_CHARTER_OVERVIEW.md` — compact English overview for the repository front door.

## Quick start

Run the dependency-free demonstration:

```bash
cd bc_academy/demo
python bc_academy_linear_spectral_demo.py
```

The script demonstrates a minimal avoided-crossing model where full gaps move, sector weights flow, and finite-resolution access depends on a declared threshold.

## Claim boundary

BC-Academy is a curriculum and methodology layer. It does not claim:

- derivation of the cosmological constant;
- reconstruction of a true hidden sector;
- identification of induced gaps with particle masses;
- a detector model or empirical measurement theory;
- continuum QFT, RG flow or physical time dynamics;
- physical meaning for certificate reset or atlas transitions.

## Relation to BC-Core and BC-Origin

BC-Academy teaches the **BC-Core** mathematical infrastructure, especially the BC-XV--BC-XXII finite-resolution certification layer. BC-Origin remains a separate optional toy-model branch and should not be merged into the BC-Core certification track.
