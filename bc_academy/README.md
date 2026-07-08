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

## Canonical resources

- Full course charter DOI: [10.5281/zenodo.21199133](https://doi.org/10.5281/zenodo.21199133)
- BC-Academy I block syllabus DOI: [10.5281/zenodo.21205935](https://doi.org/10.5281/zenodo.21205935)

## BC-Academy I lecture resources

**Lecture 1: Operator, Matrix, Spectrum**

- Article DOI: [10.5281/zenodo.21251960](https://doi.org/10.5281/zenodo.21251960)
- Video lecture: [YouTube](https://youtu.be/O_ZId9dZT3c)
- NotebookLM companion: [NotebookLM](https://notebooklm.google.com/notebook/28b52381-5032-447f-9f49-e83641c7ac07)
- HTML demonstrations: [`BC-Academy-I-LA01-Demos/`](BC-Academy-I-LA01-Demos/)

## Folder contents

```text
bc_academy/
  README.md
  PROGRAMME_CHARTER_OVERVIEW.md
  BC-Academy-I-LA01-Demos/
    README.md
    index.html
    demos/
      demo_01_diagonal_spectrum.html
      demo_02_basis_change_same_spectrum.html
      demo_03_eigenvector_detector.html
      demo_04_same_spectrum_different_operator.html
      demo_05_near_zero_preview.html
      demo_06_what_spectrum_reads.html
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

Run the dependency-free Python demonstration:

```bash
cd bc_academy/demo
python bc_academy_linear_spectral_demo.py
```

Open the Lecture-Article 1 browser demonstrations:

```bash
cd bc_academy/BC-Academy-I-LA01-Demos
# then open index.html in a modern browser
```

The Python script demonstrates a minimal avoided-crossing model where full gaps move, sector weights flow, and finite-resolution access depends on a declared threshold. The LA01 HTML package demonstrates the first route: space → operator → matrix → spectrum.

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
