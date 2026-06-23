# BC-Origin Program Definition

## Canonical name

**BC-Origin** / **BC-O**  
**Boundary Compensation Origin Program**

## Core question

Can an observed elementary structure be modeled as a non-fundamental shadow of a hidden residual generator, with its admissible scale and initial data selected by structural compatibility equations?

The question is not whether this toy model is already the true physics of the world. The question is whether there exists a mathematically controlled class of models in which an observed layer is generated as a shadow layer rather than postulated as fundamental.

## Minimal positive thesis

A minimal hidden generator may have two structural components:

```text
h = (q, c)
```

where:

- `q` is an index-like residual charge;
- `c` is a cyclic or phase-closure number.

An observable elementary shadow is a projected object

```text
s = Pi(h)
```

whose scale ratio is not inserted as a cutoff but selected from a closure equation.

## First model class

The first model class uses a spectral closure equation:

```text
lambda_q(ell) * L + theta(q) = 2*pi*c
lambda_q(ell) = mu_q / ell
```

The selected observable scale is

```text
ell / L = mu_q / (2*pi*c - theta(q))
```

This produces a discrete family of admissible observable scales for fixed structural data.

## Second model class

For two generators, the goal is to introduce a coupled spectral problem rather than inserting a correction by hand:

```text
D = [[d1, g],
     [g,  d2]]

d_i = 2*pi*c_i - theta(q_i)
g   = kappa*q_1*q_2
```

The positive eigenvalues of `D` define split denominators and therefore split observable shadow scales.

## Strong-result principle

The project should not be written as an apologetic list of non-claims. Instead it should separate levels of assertion:

1. theorem inside the toy model;
2. structural interpretation;
3. computational experiment;
4. physics-motivated analogy;
5. speculative extension;
6. explicit critic target.

The aim is the strongest valid version of the model, not the safest weak restatement.

## Immediate success criterion

BC-Origin I succeeds if it proves and computes the following:

1. a hidden index-cycle generator maps to an observable shadow;
2. the observable scale is selected by closure, not by manual cutoff;
3. two generators produce coupled shadows;
4. coupling produces a reproducible scale-splitting rule;
5. the result is strong enough to serve as the first practical BC-Origin building block.
