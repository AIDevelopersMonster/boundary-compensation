# BC-Academy I--V

**Учебно-методическая программа математического аппарата Boundary Compensation**  
**От линейного спектрального входа к сертифицированным атласам отклика конечного разрешения**  
**Programme Charter / Curriculum Syllabus v0.1.1**  
**Author:** A. A. Malachevsky  
**Programme:** Boundary Compensation research programme

## Status

This is the repository-facing Russian Markdown companion to the full **BC-Academy I--V Programme Charter v0.1.1**.

BC-Academy is the educational and methodological layer of the Boundary Compensation programme. It translates the BC corpus from a sequence of research modules into a reproducible learning trajectory.

It introduces no new physical claims and does not claim to reconstruct a hidden sector.

## Central methodological thesis

```text
Finite-resolution data do not reconstruct hidden reality directly;
they define certified layers of compatible response structure.
```

Russian formulation:

```text
Данные конечного разрешения не реконструируют скрытую реальность напрямую;
они задают сертифицированные слои совместимой структуры отклика.
```

## Purpose of BC-Academy

BC-Academy is created to:

1. separate the strict mathematical apparatus of BC from physical-philosophical motivation;
2. provide an entry point through linear algebra, spectra and projectors;
3. explain the transition from a scalar gap to induced response operators;
4. show why finite resolution leads to compatible classes rather than unique reconstruction;
5. teach the language of quotient representatives, wall stratification, hidden-lift dictionaries, perturbation tubes and certification workflows;
6. prepare the basis for future textbooks, university notes, problem sets, engineering guides and outreach appendices.

## General structure

The programme is divided into five educational modules:

1. **BC-Academy I: Linear Spectral Entry**
2. **BC-Academy II: Schur/Feshbach Response Operators**
3. **BC-Academy III: Finite-Resolution Access and Sector Weights**
4. **BC-Academy IV: Inverse Response and Non-Identifiability**
5. **BC-Academy V: Quotient Representatives and Certified Atlases**

The ordering follows mathematical necessity rather than publication chronology:

```text
spectra
  -> Schur/Feshbach
  -> finite-resolution access
  -> inverse non-identifiability
  -> quotient/certification infrastructure
```

## Module map

| Module | Main BC corpus | Central educational task |
|---|---|---|
| I. Linear Spectral Entry | BC-I; optional TimeEntropy and Collapse branches | Introduce spectra, near-zero modes, gaps, traces, projectors and spectral sensitivity. |
| II. Schur/Feshbach Response Operators | BC-III, BC-IV, partly BC-V--VI | Explain how a scalar gap becomes an induced finite-dimensional response operator. |
| III. Finite-Resolution Access and Sector Weights | BC-VII, BC-VIII, BC-IX, BC-X | Teach finite-resolution access, spectral windows, sector weights, parameter flow, isotypic structure and forward response atlases. |
| IV. Inverse Response and Non-Identifiability | BC-XI, BC-XII, BC-XIII, BC-XIV | Move from forward response models to inverse classes, admissible fibers, refinement and identifiability thresholds. |
| V. Quotient Representatives and Certified Atlases | BC-XV--BC-XXII; BC-Overview I | Develop quotient geometry, walls, atlases, perturbation tubes, certification, reset, gluing and layer-aware metrics. |

## BC-Academy I: Linear Spectral Entry

Full title:

**BC-Academy I: Linear Spectral Entry — Matrices, Spectra, Gaps and the First Boundary Compensation Mechanism**

Main sources:

- BC-I: Spectral Sensitivity of the Cosmological Constant;
- optional: BC-TimeEntropy;
- optional: BC-Collapse.

The physical context of BC-I is used only as historical and motivational illustration. The mathematical core of Module I is spectral sensitivity of small eigenvalues and near-zero modes under declared assumptions.

Learning outcome:

```text
spectral gap -> near-zero modes -> small-gap response channel
```

The reader should understand why BC-I is a conditional spectral mechanism rather than a first-principles calculation of the cosmological constant.

## BC-Academy II: Schur/Feshbach Response Operators

Full title:

**BC-Academy II: Schur/Feshbach Response Operators — From Scalar Compensation Gaps to Induced Gap Spectra**

Main sources:

- BC-III: Induced Zero-Mode Splitting and the Microscopic Origin of the Compensation Gap;
- BC-IV: Multi-Channel Compensation Mixing and Induced Gap Spectra;
- partly: BC-V--BC-VI.

Central transition:

```text
epsilon -> D_gap -> {epsilon_a} -> finite induced gap spectrum
```

Key formula:

```text
D_gap = - P_0 V^* M^{-1} V P_0 + ...
```

Learning outcome: the gap is no longer treated as an inserted scalar; it becomes an induced finite-dimensional operator arising from a declared block structure.

## BC-Academy III: Finite-Resolution Access and Sector Weights

Full title:

**BC-Academy III: Finite-Resolution Access and Sector Weights — Spectral Windows, Projectors, Transport and Forward Atlases**

Main sources:

- BC-VII: Coarse-Grained Spectral Access;
- BC-VIII: Parameter Flow of Induced Gap Spectra and Sector-Weight Transport;
- BC-IX: Isotypic Sector Transport;
- BC-X: Toy Hidden-Sector Response Models.

Key objects:

```text
A_gap = |D_gap| / M_*
N_eff(delta) = Tr W_delta(A)
epsilon_{a,s} -> (epsilon_kappa, omega_kappa,s)
```

Learning outcome:

```text
full gaps define access; sector weights define interpretation
```

## BC-Academy IV: Inverse Response and Non-Identifiability

Full title:

**BC-Academy IV: Inverse Response and Non-Identifiability — Response Equivalence Classes, Selection Rules and Identifiability Thresholds**

Main sources:

- BC-XI: The Inverse Isotypic Gap Problem;
- BC-XII: Selection Rules and Admissible Representatives;
- BC-XIII: Rigidity and Refinement;
- BC-XIV: Structural Identifiability Thresholds.

The central epistemological turn is that finite-resolution data generally do not identify a unique hidden operator.

Learning outcome:

```text
finite-resolution response => compatible class, not unique hidden sector
```

## BC-Academy V: Quotient Representatives and Certified Atlases

Full title:

**BC-Academy V: Quotient Representatives and Certified Atlases — Normal Forms, Walls, Dictionary Tubes, Certification and Gluing**

Main sources:

- BC-XV: Canonical Representatives and Gauge Quotients;
- BC-XVI: Stratified Response Quotients and Cluster-Merger Walls;
- BC-XVII: Hidden-Lift Atlases and Response-Compatible Dictionaries;
- BC-XVIII: Stability under Finite-Resolution Perturbations;
- BC-XIX: Algorithmic Construction of Hidden-Lift Dictionaries;
- BC-XX: Certified Atlas Transitions;
- BC-XXI: Certified Gluing Obstructions;
- BC-XXII: Metrics and Stability Distances;
- BC-Overview I.

Key formulas:

```text
B = -D_gap = V^* M^{-1} V >= 0
W = M^{-1/2} V
B = W^* W
support-valued representative: (supp B, I, B^{1/2})
```

Learning outcome:

```text
hidden ambiguity
  -> quotient representative
  -> wall-stratified atlas
  -> perturbation tube
  -> certificate
  -> gluing / metrics
```

## Prerequisite layers

| Layer | Required knowledge | Appropriate modules |
|---|---|---|
| Engineering entry | matrices, eigenvalues, basic linear algebra, complex vectors, elementary operator intuition | BC-Academy I--II |
| University / master's level | spectral projectors, functional calculus, perturbation theory, Schur complement, representation theory, inverse problems | BC-Academy III--IV |
| Research level | functional analysis, matrix analysis, differential geometry, algebraic-topology intuition, representation theory, inverse problems, quotient geometry | BC-Academy V |

BC-Academy remains finite-dimensional at the BC-Core level. These disciplines are needed to understand quotient, atlas, wall and certification structures correctly, not to assert continuum QFT.

## Recommended core reading route

```text
BC-I
  -> BC-III
  -> BC-IV
  -> BC-VII
  -> BC-VIII
  -> BC-IX
  -> BC-X
  -> BC-XI
  -> BC-XII
  -> BC-XIII
  -> BC-XIV
  -> BC-XV
  -> BC-XVI
  -> BC-XVII
  -> BC-XVIII
  -> BC-XIX
  -> BC-XX
  -> BC-XXI
  -> BC-XXII
  -> BC-Overview I
```

Optional branches:

- **BC-TimeEntropy** — spectral counting, compensation entropy and relational internal time.
- **BC-Collapse** — finite-resolution readout applied to stable pointer channels and measurement language.
- **BC-Origin** — optional toy-model branch; it must not be merged with BC-Core XV--XXII certification infrastructure.

## Format of teaching materials

Each BC-Academy module should eventually have four types of material:

1. **Research Syllabus** — strict programme with formulas, definitions, claim boundaries and references.
2. **University Notes** — expanded explanation for advanced undergraduate, master's and doctoral readers.
3. **Engineering Guide** — applied entry through matrices, algorithms, diagrams and computational examples.
4. **Outreach Appendix / School Analogy Version** — popular explanation through analogies, without proof-level rigor.

Additional desirable elements:

- exercises;
- solved problems;
- minimal computational examples;
- notation table;
- glossary;
- controlled claims / non-claims;
- source map;
- final mini-project.

## Restriction on school analogies

School analogies are outreach appendices. They are not definitions, proofs or strict mathematical formulations.

In Research Syllabus and University Notes, images such as "shadow", "map", "wall", "corridor", "lock" or "fingerprint" may be used only after the mathematical objects have been defined strictly, such as projector, quotient class, wall stratum, local chart, perturbation tube, certificate or response-equivalence class.

## Basic notation

| Symbol | Meaning |
|---|---|
| `H` | finite-dimensional complex Hilbert space |
| `Herm(H)` | real vector space of self-adjoint operators on `H` |
| `Herm_+(H)` | cone of positive semidefinite self-adjoint operators |
| `D_gap` | effective Schur/Feshbach gap operator |
| `A_gap` | positive finite-resolution access operator |
| `M` | positive hidden block, `M = M^* > 0` |
| `V` | coupling map between accessible and hidden sectors |
| `B` | positive response operator, `B = -D_gap` |
| `W` | whitened coupling, `W = M^{-1/2} V` |
| `B = W^* W` | Gram factorization |
| `P_s` | sector projector |
| `P_rho` | isotypic projector |
| `Pi_kappa` | spectral cluster projector |
| `W_delta` | finite-resolution spectral window |
| `N_eff` | effective accessible spectral count |
| `omega_kappa,s` | sector weight |
| `Phi^R` | response map for protocol `R` |
| `F_adm` | admissible inverse fiber |
| `sr(B)` | support-valued representative |
| `eta` | deterministic operator-norm perturbation tolerance |
| `tau` | finite-resolution accessibility threshold |
| `r_tau(B)` | threshold effective rank |
| `D_C^{(eta,tau)}(B)` | thresholded perturbation dictionary tube |
| `CERTIFICATE_RESET` | status of failed certificate continuation |

## Controlled claims

BC-Academy claims that:

1. the BC corpus can be organized into a reproducible educational trajectory;
2. the mathematical apparatus has a natural five-step structure: spectra, Schur/Feshbach operators, finite-resolution access, inverse response and quotient/certification infrastructure;
3. finite-resolution data define compatible classes rather than a unique hidden sector;
4. BC-Academy can serve as a basis for syllabi, university notes, engineering guides and outreach appendices;
5. BC-Academy does not replace original research manuscripts but provides a route for studying them.

## Non-claims

BC-Academy does not claim:

1. that BC has proved a physical theory of the cosmological constant;
2. that BC reconstructs a true hidden sector;
3. that induced gap spectra are particle masses;
4. that finite-resolution response is a detector model;
5. that BC-Core XV--XXII is a quantum field theory;
6. that certified atlases are physical state spaces;
7. that `CERTIFICATE_RESET` is a physical event;
8. that school analogies are proofs;
9. that BC-Origin belongs to BC-Core;
10. that Programme Charter v0.1.1 introduces a new technical theorem.

## Final formula of the programme

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

This chain is the educational skeleton of the mathematical apparatus of Boundary Compensation.

## Conclusion

BC-Academy teaches not how to "see hidden reality", but how to work rigorously with what is available at finite resolution: compatible classes, admissible representatives, factor forms, walls, perturbation tubes and certificates.
