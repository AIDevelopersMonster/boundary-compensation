# BC-Origin Shadow Lab Experiment Protocol

## Goal

The practical calculation protocol tests whether the BC-Origin model produces a reproducible transition:

```text
hidden residual generator -> observable elementary shadow
```

with observable scale data selected by equations rather than assigned as free parameters.

## Experiment 1: One-generator resonant shadow

### Inputs

```text
q: nonzero integer index-like charge
c: integer cyclic closure number
alpha: positive dimensionless scale coefficient
L: positive macro-scale, used only as ratio reference
theta(q): structural phase function
f(|q|): positive spectral weight function
```

### Definitions

```text
mu_q = alpha*f(|q|)
lambda_q(ell) = mu_q/ell
closure: lambda_q(ell)*L + theta(q) = 2*pi*c
```

### Output

```text
S(q,c) = ell/L = mu_q/(2*pi*c - theta(q))
```

### Required checks

1. denominator positivity: `2*pi*c - theta(q) > 0`;
2. scale positivity: `S(q,c) > 0`;
3. discreteness over integer `c`;
4. sensitivity to `q` through `mu_q` and/or `theta(q)`;
5. no manual cutoff for `ell`.

### Expected minimal result

A discrete hyperbolic family of admissible observable scale ratios.

## Experiment 2: Two-generator coupled shadow splitting

### Inputs

```text
h_1 = (q_1, c_1)
h_2 = (q_2, c_2)
kappa: coupling coefficient
```

### Definitions

```text
d_i = 2*pi*c_i - theta(q_i)
g = kappa*q_1*q_2
D = [[d_1, g], [g, d_2]]
```

### Output

The eigen-denominators of `D`:

```text
delta_pm = (d_1+d_2)/2 +/- sqrt(((d_1-d_2)/2)^2 + g^2)
```

and split scale ratios:

```text
S_pm = mu_eff/delta_pm
```

### Required checks

1. eigen-denominator positivity;
2. reduction to uncoupled denominators when `kappa=0`;
3. splitting magnitude increases with `|q_1*q_2|` for fixed `kappa`;
4. symmetric real matrix does not retain sign of `q_1*q_2` in eigenvalue magnitudes;
5. sign-sensitive extensions require oriented projection, asymmetric coupling, or phase coupling.

## Experiment 3: Sign-sensitive extension candidate

Experiment 2 exposes a technical node: symmetric real coupling loses charge-sign information in eigenvalue magnitudes. Therefore a stronger model should test one of the following extensions:

1. oriented observable functional:

```text
O(D, v) = <v, D v>
```

with signed orientation vector `v`;

2. asymmetric coupling:

```text
D = [[d_1, kappa_12*q_1*q_2], [kappa_21*q_1*q_2, d_2]]
```

3. complex phase coupling:

```text
g = |g| exp(i*phi(q_1,q_2))
```

4. signed denominator correction after eigenmode projection.

## Success condition for the lab

The lab succeeds if it produces:

1. reproducible CSV/JSON tables;
2. symbolic formulas matching numerical outputs;
3. a clear separation between model theorem, computational result, and speculative interpretation;
4. an identified next technical node rather than vague expansion.
