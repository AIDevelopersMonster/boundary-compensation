# BC-Academy I--V: Programme Charter overview

**Document type:** Programme Charter / Curriculum Syllabus  
**Current curriculum version:** v0.1.1  
**Purpose:** educational organization of the mathematical apparatus of Boundary Compensation  
**Status:** repository-facing condensed companion to the full Programme Charter

## Status

This overview summarizes the full document:

**BC-Academy I--V: Programme Charter for the Mathematical Apparatus of Boundary Compensation -- Curriculum Syllabus v0.1.1**

It is a lightweight repository overview, not a replacement for the complete LaTeX/PDF charter. Its purpose is to make the BC-Academy folder readable from the repository front door and to identify the educational scope of the demonstration files.

BC-Academy is not a new research module and does not introduce new physical claims. It is a curriculum and methodology layer for learning the existing Boundary Compensation mathematical apparatus.

## Central thesis

Finite-resolution data do not reconstruct hidden reality directly; they define certified layers of compatible response structure.

This is the guiding epistemic principle of the BC-Academy curriculum and of the BC-Core finite-resolution certification infrastructure.

## Why BC-Academy exists

The Boundary Compensation corpus contains several technical modules. BC-Academy reorganizes that corpus as a reproducible learning path. The ordering follows mathematical necessity rather than publication chronology:

```text
spectra -> Schur/Feshbach -> finite-resolution access -> inverse response -> quotient/certification
```

The complete teaching spine is:

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

## Module map

| BC-Academy module | Core BC sources | Learning purpose |
|---|---|---|
| I. Linear Spectral Entry | BC-I, optional TimeEntropy / Collapse | spectra, gaps, near-zero modes, sensitivity |
| II. Schur/Feshbach Response Operators | BC-III, BC-IV, partial BC-V--VI | induced gap operators and multi-channel mixing |
| III. Finite-Resolution Access and Sector Weights | BC-VII, VIII, IX, X | access windows, sector weights, parameter flow, forward atlas |
| IV. Inverse Response and Non-Identifiability | BC-XI, XII, XIII, XIV | inverse fibers, non-injectivity, selection rules, identifiability thresholds |
| V. Quotient Representatives and Certified Atlases | BC-XV--XXII, Overview I | quotient normal forms, walls, tubes, certification, reset, gluing, metrics |

## Methodological boundaries

1. **Module I isolates mathematics from cosmology.** The cosmological language in BC-I is used only as historical and motivational illustration. The mathematical core is spectral sensitivity of near-zero eigenvalues under declared assumptions. It is not a derivation of the observed cosmological constant.
2. **School analogies are outreach only.** They cannot replace definitions, proofs or mathematical statements in Research Syllabus and University Notes materials.
3. **BC-Origin is optional and separate.** It is a toy-model branch involving combinatorial, spectral and graph-like constructions. It is not part of the BC-Core certification infrastructure.
4. **BC-Academy is not a new research claim.** It is a curriculum and methodology charter for learning existing BC mathematics.

## Prerequisite layers

- **Engineering entry:** linear algebra, matrices, eigenvalues, eigenvectors, projectors, traces and basic operator intuition.
- **University / master's layer:** spectral projectors, finite-dimensional functional calculus, perturbation theory, Schur complement, Schur/Feshbach reduction, representation-theoretic decomposition and inverse problems.
- **Research layer:** functional analysis and spectral theory, matrix analysis and positive operators, differential geometry of local charts and Grassmannian-type structures, basic algebraic-topology intuition for cocycle consistency, compact-group representation theory, inverse-problem theory, quotient structures, gauge redundancy, rank stratification, perturbation tubes, local-to-global consistency and certification logic.

BC-Academy remains finite-dimensional at the BC-Core level. These prerequisites are needed to understand quotient, atlas, wall and certification structures, not to assert continuum QFT, RG flow or physical dynamics.

## Recommended reading route

```text
BC-I
  -> BC-III -> BC-IV
  -> BC-VII -> BC-VIII -> BC-IX -> BC-X
  -> BC-XI -> BC-XII -> BC-XIII -> BC-XIV
  -> BC-XV -> BC-XVI -> BC-XVII -> BC-XVIII
  -> BC-XIX -> BC-XX -> BC-XXI -> BC-XXII
  -> BC-Overview I
```

Optional branches:

- **BC-TimeEntropy:** optional spectral-counting, entropy and relational-reading branch.
- **BC-Collapse:** optional finite-resolution readout branch.
- **BC-Origin:** optional toy-model branch; not part of the BC-Core certification sequence.

## Teaching formats

Each future module should support four forms:

1. Research Syllabus
2. University Notes
3. Engineering Guide
4. Outreach Appendix / School Analogy Version

The outreach form may use analogies, but analogies must never replace mathematical definitions or proofs.

## Minimal demonstration

The demo in `demo/bc_academy_linear_spectral_demo.py` illustrates the BC-Academy I--III teaching spine using a 2x2 avoided-crossing model.

It shows:

- a finite-dimensional self-adjoint family;
- moving full gap branches;
- sector-weight flow across an avoided crossing;
- finite-resolution access under a declared threshold;
- no reconstruction of a unique hidden sector from the displayed response data.

## Controlled claims

BC-Academy claims only that the BC corpus can be organized as a reproducible learning trajectory for the mathematical apparatus of finite-resolution response analysis.

It supports a curriculum path from spectra and Schur/Feshbach operators to inverse response classes, quotient representatives, wall-stratified atlases, perturbation tubes, certification workflows, reset protocols, gluing diagnostics and layer-aware metrics.

## Non-claims

BC-Academy does not claim:

- derivation of the cosmological constant;
- reconstruction of a true hidden sector;
- identification of induced gaps with particle masses;
- a detector theory or empirical measurement model;
- continuum QFT, RG flow or physical time dynamics;
- physical meaning for certificate reset or atlas transitions;
- that school analogies are mathematical proofs;
- that BC-Origin is part of BC-Core XV--XXII.

## Next curriculum step

After the Programme Charter, the next educational document should be:

**BC-Academy I: Linear Spectral Entry -- Research Syllabus + University Notes**

Its first methodological rule is that the BC-I physical setting must remain illustrative, while the mathematical core is the spectral sensitivity of near-zero eigenvalues under declared assumptions.
