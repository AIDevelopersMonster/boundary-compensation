# P3-B-M12 Research Audit v0.1.0

**Verdict:** certified zero-fit analytic third-jet result on the declared independent new-label atlas.

## Scope

The module extends the exact finite q-6j differentiation chain from \(F''\) to \(F'''\) and evaluates the curvature of \(\log|\omega|\). It does not fit a representation model and does not interpret the deformation physically.

## Preregistration integrity

The formula, atlas rule, two reference steps and all thresholds were committed before evaluation in commit `d48fb3d811d8681d6823288af7e15a7efd800246`. No frozen field was changed after the numerical result.

## Mathematical audit

The third derivative of a positive factor represented by logarithmic jets uses

\[
f'''=f\bigl(\ell_1^3+3\ell_1\ell_2+\ell_3\bigr).
\]

The same rule is applied separately to q-factorials, triangle prefactors, each Racah summand and the channel-dimension amplitude. Product-rule coefficients in the q-6j and matrix third derivatives are explicit. The generator identity

\[
K''=F'''F^T+2F''F'^T+F'F''^T
\]

is used directly.

## Validation findings

The declared atlas contains 208 ordered carriers in 15 unseen external-spin families. The maximum relative residual against the refined reference is `8.562775171720663e-09`; the maximum disagreement between reference steps is `2.531584412895532e-08`.

Structural residuals are:

- orthogonality: `1.1371631099637045e-15`;
- generator skewness: `2.2177764877206478e-14`;
- first generator-derivative skewness: `1.585800223262612e-12`;
- second generator-derivative skewness: `2.2895394478573956e-10`.

All are below preregistered thresholds.

## Reproducibility

The exact repository-style test file was executed locally:

```text
10 passed in 2.03s
```

No GitHub Actions workflow was run in this step.

## Claim firewall

Certified: analytic third differentiation reproduces the log-speed curvature on the declared two-channel new-label atlas.

Not certified: low-dimensional compression, arbitrary-spin uniformity, physical q evolution, semiclassical interpretation, or higher derivatives.

No statement from the Gemini advisory report is used as evidence.
