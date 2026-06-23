# BC-Origin I Core Effects

This note fixes the three core effects of the signed winding-shadow model.

## Model

Let two hidden cyclic generators carry oriented winding numbers `n1`, `n2`. Define the orientation product

```text
s = sign(n1*n2)
```

and the signed common-shift operator

```text
D_signed = [[d1 + gamma*s, kappa],
            [kappa,        d2 + gamma*s]]
```

The eigen-denominators are

```text
lambda_pm = (d1+d2)/2 + gamma*s +/- sqrt(((d1-d2)/2)^2 + kappa^2)
```

Observable scale ratios are interpreted as

```text
ell_pm/L = mu_eff/lambda_pm
```

for positive `lambda_pm`.

## Effect 1: Orientation-controlled shadow localization

For `gamma > 0`:

```text
s = +1 -> lambda_pm increases -> ell_pm/L decreases
s = -1 -> lambda_pm decreases -> ell_pm/L increases
```

Therefore same-oriented winding products compress observable shadows, while opposite-oriented winding products delocalize them.

This is not a force law. It is a signed spectral displacement of the observable inverse-scale denominators.

## Effect 2: Admissibility horizon

A localized observable shadow requires

```text
lambda_pm > 0
```

If a branch reaches

```text
lambda_pm = 0
```

then

```text
ell_pm/L -> infinity
```

and that branch no longer defines a localized observable shadow.

For the lower opposite-orientation branch, with

```text
lambda_base = (d1+d2)/2
R = sqrt(((d1-d2)/2)^2 + kappa^2)
```

the horizon condition is

```text
gamma_c = lambda_base - R
```

and the branch is admissible only while

```text
gamma < gamma_c
```

when `gamma_c` is positive.

## Effect 3: Coupling-induced shadow gap

The branch separation is

```text
lambda_plus - lambda_minus = 2*sqrt(((d1-d2)/2)^2 + kappa^2)
```

The off-diagonal coupling `kappa` creates a reproducible branch gap. It does not automatically protect every branch from delocalization; instead it separates the branches, often keeping the upper branch localized while the lower branch approaches or crosses the admissibility horizon.

## Claim status

The three effects are theorems of the toy operator model. Their physical interpretation is structural: hidden winding orientation can be projected into observable scale localization through a signed spectral operator.

The model does not require the observed layer to be fundamental. It gives a concrete mechanism by which a shadow layer can have scale selection, orientation dependence, and admissibility transitions.
