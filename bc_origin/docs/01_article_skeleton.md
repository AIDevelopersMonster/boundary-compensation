# BC-Origin I Article Skeleton

# Boundary Compensation Origin I: Resonant Shadows, Structural Scale Selection, and Index-Dependent Splitting

## Abstract draft

This note introduces the first toy model of the BC-Origin program. The model studies hidden residual generators carrying an index-like charge and a cyclic closure number. Observable elementary shadows are defined as solutions of a structural closure equation. In the one-generator case, the closure equation selects a discrete family of observable scale ratios. In the two-generator case, a coupled denominator matrix produces index-dependent spectral splitting. The result is a structural-existence model for a non-fundamental observed layer: observed scale data are selected by hidden compatibility equations rather than assigned as free cutoffs.

## 1. Introduction

- Explain the move from BC-Certification to BC-Origin.
- State the target: not reconstructing the true hidden sector, but constructing a minimal hidden-to-observed shadow model.
- Introduce the central problem: structural selection of observable initial data.
- State the first result: resonant shadow scales.
- State the second result: index-dependent splitting for coupled shadows.

## 2. Hidden residual generators and observable shadows

Define:

```text
R_hid = Z e_q + Z e_c
h = (q, c)
```

where `q` is an index-like charge and `c` is a cyclic closure number.

Define the shadow map:

```text
Pi(h) = (Q(h), S(h))
```

with

```text
Q(h) = q
S(h) = ell_h / L
```

## 3. One-generator closure model

Spectral function:

```text
lambda_q(ell) = mu_q / ell
mu_q = alpha*f(|q|) > 0
```

Closure equation:

```text
lambda_q(ell)*L + theta(q) = 2*pi*c
```

Admissibility condition:

```text
2*pi*c - theta(q) > 0
```

Scale relation:

```text
ell_h/L = mu_q/(2*pi*c - theta(q))
```

### Proposition 1: Structural scale selection

For fixed structural data `(q, c)` satisfying the admissibility condition, the observable scale ratio is uniquely selected by the closure equation.

### Proposition 2: Discrete shadow scale family

For fixed `q`, the admissible scale ratios form a discrete family indexed by `c`.

## 4. Two-generator coupled shadow model

For two generators:

```text
h_1 = (q_1, c_1)
h_2 = (q_2, c_2)
```

Define denominators:

```text
d_i = 2*pi*c_i - theta(q_i)
g = kappa*q_1*q_2
```

Coupled denominator matrix:

```text
D = [[d_1, g],
     [g,   d_2]]
```

Eigen-denominators:

```text
delta_pm = (d_1+d_2)/2 +/- sqrt(((d_1-d_2)/2)^2 + g^2)
```

Split observable scales:

```text
S_pm = mu_eff / delta_pm
```

### Proposition 3: Index-dependent splitting

If `g != 0`, the coupled model splits the denominator spectrum. The splitting magnitude depends on `|kappa*q_1*q_2|` in the symmetric two-generator model.

### Remark: sign-sensitive extension

A symmetric real 2x2 matrix makes eigenvalue splitting depend on `g^2`. Therefore the sign of `q_1*q_2` is not visible in eigenvalue magnitudes unless one adds oriented projection, asymmetric coupling, complex phase coupling, or a signed observable functional.

## 5. Computational experiments

Experiment 1:

- enumerate `q`, `c`;
- compute `theta(q)`, `mu_q`, `ell/L`;
- verify discreteness and admissibility.

Experiment 2:

- enumerate pairs `(q_1,c_1)`, `(q_2,c_2)`;
- build coupled matrices;
- compute eigen-denominators and split scales;
- verify coupling vanishes when `kappa=0`;
- test whether sign-sensitive information survives chosen projection.

## 6. Interpretation

The model demonstrates a possible mechanism by which observed elementary structures may be scale-selected shadows of hidden residual generators. It is a structural-existence model, not an identification of the physical hidden sector.

## 7. Critic targets

- Is the closure condition physically motivated or merely imposed?
- Does the model produce anything beyond standard resonator quantization?
- Does the two-generator model require a nontrivial projection to retain sign information?
- Can the next model produce a rule over a family of shadows, not only a two-generator example?

## 8. Conclusion

BC-Origin I establishes the first practical BC-Origin building block: resonant observable shadows and index-dependent splitting from hidden index-cycle generators.
