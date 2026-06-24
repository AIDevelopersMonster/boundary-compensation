# BC-Origin Flow Lab

Standalone browser GUI for the BC-Origin flow companion direction.

This GUI illustrates a two-shadow parameter-flow toy model:

```text
D(lambda) = [[d0 - v1*lambda, kappa],
             [kappa, d0 - v2*lambda]]
```

It visualizes avoided-crossing geometry, the spectral gap, and the admissibility horizon `lambda_min = 0`.

## Important claim-status note

The flow parameter is a controlled deformation parameter. It is not automatically physical time.

The display is Landau-Zener-type avoided-crossing geometry only. It does not compute Landau-Zener transition probabilities and does not define a physical dynamics.

## Open

Open directly in a browser:

```text
web/index.html
```
