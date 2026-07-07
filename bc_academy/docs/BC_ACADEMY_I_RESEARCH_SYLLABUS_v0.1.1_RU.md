# BC-Academy I: Linear Spectral Entry

**Research Syllabus v0.1.1 — Russian repository companion**  
**Subtitle:** Matrices, Spectra, Gaps and the First Boundary Compensation Mechanism  
**Author:** A. A. Malachevsky  
**Programme:** Boundary Compensation / BC-Academy  
**Recommended Zenodo type:** Publication / Project deliverable

## Status

This document is the repository-facing Markdown companion to the Russian Zenodo-ready syllabus **BC-Academy I: Linear Spectral Entry — Research Syllabus v0.1.1**.

It fixes the structure of the first BC-Academy module before expansion into University Notes and Engineering Guide materials.

## Methodological boundary

BC-Academy I teaches a **spectral mechanism**, not a cosmological theory.

The BC-I physical context — cosmological constant, microboundary language, monopole sphere, gauge-covariant Dirac operator and topological zero modes — is used only as historical and motivational background.

The mathematical core is finite-dimensional spectral sensitivity of small eigenvalues and near-zero modes under declared assumptions.

The BC-I-style formula

```text
gamma = |n| beta_epsilon + O((epsilon R_Sigma)^2)
```

must be read as a conditional spectral amplification mechanism, not as a derivation of the observed cosmological constant.

## Local learning chain

```text
operator
  -> spectrum
  -> zero / near-zero modes
  -> gap
  -> logarithmic sensitivity
  -> multiplicity amplification
  -> finite-resolution access preview
```

## Official module title

**BC-Academy I: Linear Spectral Entry — Matrices, Spectra, Gaps and the First Boundary Compensation Mechanism**

Russian working title:

**BC-Academy I: Линейный спектральный вход — матрицы, спектры, зазоры и первый механизм Boundary Compensation**

## Main source

**BC-I: Spectral Sensitivity of the Cosmological Constant**

BC-I supplies the motivating spectral mechanism in which protected zero modes are lifted through a small effective compensation gap, schematically `epsilon(alpha, phi)`, and the leading sensitivity is read through a multiplicity factor.

Optional orientation sources:

- BC-TimeEntropy — spectral counting and relational reading branch;
- BC-Collapse — finite-resolution readout branch;
- BC-Overview I — later consolidation of finite-resolution response infrastructure.

## Pedagogical simplification

In BC-I the effective compensation gap may depend on more than one parameter:

```text
epsilon = epsilon(alpha, phi)
```

For the first educational module this is reduced to a one-parameter teaching model:

```text
epsilon(alpha, phi) -> epsilon(alpha)
```

This permits a clean introduction of logarithmic sensitivity:

```text
beta_epsilon = d ln epsilon / d ln alpha
```

This is only a pedagogical reduction. It does not assert that the full BC-I setting has only one parameter.

## Main topics

1. Vector space and operator.
2. Self-adjoint matrix.
3. Eigenvalues and eigenvectors.
4. Spectrum of an operator.
5. Zero mode and near-zero mode.
6. Gap and near-zero sector.
7. Trace, determinant and spectral count.
8. Spectral sensitivity.
9. Toy form of `gamma ~ |n| beta_epsilon`.
10. Controlled claims and non-claims of BC-I.

## Learning outcomes

After BC-Academy I the reader should understand:

- what a spectral gap is;
- why zero and near-zero modes may have special status in a spectral response mechanism;
- how a small gap may carry logarithmic sensitivity to a declared parameter;
- why BC-I is a conditional spectral mechanism rather than a first-principles calculation of the cosmological constant.

## Notation table

| Symbol | Meaning |
|---|---|
| `H` | finite-dimensional complex Hilbert space |
| `A : H -> H` | linear operator, usually represented by a matrix |
| `A = A^*` | self-adjoint / Hermitian operator |
| `sigma(A)` | spectrum of `A` |
| `lambda_j(A)` | eigenvalues of `A` |
| `Pi_j` | spectral projector associated with a spectral branch or cluster |
| `ker A` | kernel / nullspace of `A` |
| `Tr A` | trace of `A` |
| `epsilon` | small spectral gap scale |
| `alpha` | external parameter of the educational model |
| `phi` | additional parameter in the original BC-I motivation |
| `beta_epsilon` | logarithmic sensitivity of `epsilon` |
| `m` | multiplicity of near-zero branches in the toy model |
| `|n|` | BC-I multiplicity count |
| `gamma` | leading sensitivity coefficient |
| `W_delta` | finite-resolution spectral window |
| `N_eff` | effective finite-resolution spectral count |

## Eight lecture-articles

| No. | Lecture-article | Central topic | Output |
|---|---|---|---|
| 1 | Operator, Matrix, Spectrum | operator as matrix and spectral object | spectrum as course language |
| 2 | Hermitian Operators and Projectors | self-adjointness, projectors, spectral decomposition | `A = A^*`, `lambda_j`, `Pi_j` |
| 3 | Zero Modes and Kernels | kernel and zero modes | `ker A`, protected zero subspace |
| 4 | Near-Zero Modes and Gap Scale | near-zero branches and small gap scale | `epsilon` as spectral scale |
| 5 | Logarithmic Sensitivity | gap sensitivity to parameter | `beta_epsilon` |
| 6 | Multiplicity Amplification | amplification through near-zero branch multiplicity | toy sensitivity lemma |
| 7 | BC-I Specialization: From `m` to `|n|` | connection to BC-I formula | conditional mechanism |
| 8 | Finite-Resolution Preview | bridge to finite-resolution access | `W_delta`, `N_eff` |

Compact course chain:

```text
A = A^* -> sigma(A) -> ker A -> |lambda| << 1 -> epsilon(alpha)
-> beta_epsilon -> m beta_epsilon -> |n| beta_epsilon -> N_eff(delta)
```

## Lecture-article 1: Operator, Matrix, Spectrum

Goal: introduce finite-dimensional space, operator, matrix and spectrum.

Minimal formula:

```text
A u = lambda u
```

Learning result: the reader understands that BC-Academy I begins with the question of what can be read from the spectrum of an operator.

## Lecture-article 2: Hermitian Operators and Projectors

Central formulas:

```text
A = A^*,  lambda_j(A) in R,  Pi_j
A = sum_j lambda_j Pi_j,  Pi_j^2 = Pi_j,  Pi_j^* = Pi_j
```

Learning result: the reader can read an operator as a structured combination of eigenvalues and projectors.

## Lecture-article 3: Zero Modes and Kernels

Central formula:

```text
ker A = { u in H : A u = 0 }
```

Learning result: the reader treats `0 in sigma(A)` as a structural spectral event, not as a metaphorical nothing.

## Lecture-article 4: Near-Zero Modes and Gap Scale

Central formula:

```text
A(epsilon) u_j(epsilon) = lambda_j(epsilon) u_j(epsilon),
|lambda_j(epsilon)| << 1
```

Learning result: `epsilon` is read as a small spectral scale, not as a particle mass or empirical physical quantity.

## Lecture-article 5: Logarithmic Sensitivity

Central formula:

```text
beta_epsilon = d ln epsilon / d ln alpha
```

If

```text
epsilon(alpha) = epsilon_* (alpha / alpha_*)^beta,
```

then

```text
beta_epsilon = beta.
```

## Lecture-article 6: Multiplicity Amplification

Toy sensitivity lemma:

If `m` near-zero branches share a common small scale `epsilon(alpha)`, then

```text
sum_{j=1}^m ln epsilon(alpha) = m ln epsilon(alpha)
```

and therefore

```text
d/d ln alpha sum_{j=1}^m ln epsilon(alpha)
  = m d ln epsilon / d ln alpha.
```

Equivalently:

```text
gamma_toy = m beta_epsilon.
```

Learning result: the amplification in the first BC mechanism comes from a spectral multiplicity factor.

## Lecture-article 7: BC-I Specialization: From `m` to `|n|`

Specialization:

```text
m = |n|,
gamma = |n| beta_epsilon + O((epsilon R_Sigma)^2).
```

Correct reading:

```text
multiplicity + small gap sensitivity => amplified spectral response
```

This does not imply derivation of `Lambda`, proof of a vacuum model, hidden-sector reconstruction or a Standard Model claim.

## Lecture-article 8: Finite-Resolution Preview

Preview formulas:

```text
N_eff(delta) = Tr W_delta(A)
A_gap = |D_gap| / M_*
```

Learning result: the reader understands the first BC transition from exact spectrum to finite-resolution spectral access.

## Controlled claims

BC-Academy I claims only that:

1. the spectral language of BC can be introduced through finite-dimensional linear algebra;
2. near-zero modes are a natural entry point into the first BC mechanism;
3. a small spectral gap scale can carry logarithmic sensitivity to a declared parameter;
4. multiplicity of near-zero branches can amplify leading logarithmic response;
5. the BC-I formula can be taught as a conditional spectral amplification mechanism;
6. finite-resolution reading is a natural next step after exact spectral reading.

## Non-claims

BC-Academy I does not claim:

1. calculation of the observed cosmological constant;
2. derivation of the Standard Model;
3. reconstruction of a true hidden sector;
4. particle-mass interpretation of `epsilon`;
5. physical detector theory;
6. physical time evolution;
7. renormalization-group flow;
8. continuum QFT dynamics;
9. empirical prediction;
10. that school analogies replace definitions or proofs.

## Exercises and mini-projects

Basic:

1. Find eigenvalues of `diag(epsilon, 1)`.
2. Find `ker A` at `epsilon = 0`.
3. Compute trace and determinant for a diagonal near-zero matrix.
4. Verify `beta_epsilon` for `epsilon(alpha) = alpha^beta`.

Intermediate:

1. For `A_m(epsilon) = diag(epsilon, ..., epsilon, 1, ..., 1)`, show `log det A_m = m log epsilon + regular terms`.
2. Prove the toy sensitivity lemma.
3. Explain why `m beta_epsilon` is a multiplicity amplification factor.

Advanced:

1. For `A(t) = [[t, epsilon], [epsilon, -t]]`, find `lambda_+(t)` and `lambda_-(t)`.
2. Find the minimal gap.
3. Introduce threshold `delta` and compute `N_eff(delta; t)`.

Mini-project: build a table for avoided crossing with `t`, `lambda_-(t)`, `lambda_+(t)`, `gap(t)` and `N_eff(delta; t)`.

## Final formula

```text
near-zero modes + small gap + multiplicity => amplified logarithmic response
```

Main boundary: BC-Academy I teaches a spectral mechanism, not a cosmological theory.
