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

## Experiment 2: Two-generator symmetric splitting baseline

### Inputs

```text
h_1 = (q_1, c_1)
h_2 = (q_2, c_2)
kappa: coupling coefficient
Q = q_1*q_2
```

### Definitions

```text
d_i = 2*pi*c_i - theta(q_i)
g = kappa*Q
D_sym = [[d_1, g], [g, d_2]]
```

### Output

The eigen-denominators of `D_sym`:

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
3. splitting magnitude increases with `|Q|` for fixed `kappa`;
4. symmetric real matrix does not retain the sign of `Q` in eigenvalue magnitudes because the characteristic equation contains `g^2`.

### Expected minimal result

The symmetric baseline gives index-dependent splitting magnitude, but it loses the sign of the topological product in eigenvalue magnitudes.

## Experiment 3: Signed common-shift correction

The sign-loss problem in Experiment 2 is caused by the characteristic equation. To preserve the topological sign of the interaction at the observable-shadow level, introduce a charge-dependent diagonal shift.

### Definitions

```text
Q = q_1*q_2
D_signed = [[d_1 + gamma*Q, kappa],
            [kappa,         d_2 + gamma*Q]]
```

### Eigen-denominators

```text
delta_pm(Q) = gamma*Q + (d_1+d_2)/2 +/- sqrt(((d_1-d_2)/2)^2 + kappa^2)
```

### Interpretation

This model preserves the sign of `Q` as a signed common displacement of the observable denominator spectrum. The splitting gap itself is unchanged:

```text
delta_plus - delta_minus = 2*sqrt(((d_1-d_2)/2)^2 + kappa^2)
```

but the absolute scale positions depend linearly on `Q`:

```text
S_pm(Q) = mu_eff/delta_pm(Q)
```

Therefore same-sign and opposite-sign charge products generate different observable shadow scales.

### Required checks

1. `Q > 0` and `Q < 0` produce opposite signed shifts of the denominator spectrum;
2. the splitting gap is independent of the sign of `Q`;
3. admissibility requires both `delta_pm(Q) > 0`;
4. this is a sign-sensitive global scale-shift model, not a sign-sensitive relative splitting model.

## Experiment 4: Oriented signed-shift extension

For a stronger sign-sensitive model, introduce opposite diagonal shifts:

```text
D_oriented = [[d_1 + gamma*Q, kappa],
              [kappa,         d_2 - gamma*Q]]
```

The eigen-denominators are

```text
delta_pm(Q) = (d_1+d_2)/2 +/- sqrt(((d_1-d_2 + 2*gamma*Q)/2)^2 + kappa^2)
```

This model lets the sign of `Q` enter the relative diagonal imbalance. It can change mode orientation, mixing balance, and component weights, not only the common position of the spectrum.

### Required checks

1. sign of `Q` changes the relative imbalance term;
2. eigenvalue magnitudes may still be even in special symmetric cases, so eigenvectors and projected observables must also be inspected;
3. define a signed observable functional if the sign is not visible in eigenvalues alone;
4. compare against Experiment 3 to separate global signed shift from oriented signed deformation.

## Success condition for the lab

The lab succeeds if it produces:

1. reproducible CSV/JSON tables;
2. symbolic formulas matching numerical outputs;
3. a clear separation between model theorem, computational result, and speculative interpretation;
4. an identified next technical node rather than vague expansion;
5. an explicit distinction between symmetric splitting, signed common shift, and oriented signed deformation.
