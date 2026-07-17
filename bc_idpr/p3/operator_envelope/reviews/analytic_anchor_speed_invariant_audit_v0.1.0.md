# P3-B-M10 Research Audit v0.1.0

**Verdict:** positive analytic construction certificate with a strict claim ceiling.

## Scope

The module closes only the anchor angular-speed obligation for real orthogonal two-channel q-recoupling matrices. It does not attempt higher-jet prediction or a low-dimensional representation law.

## Analytic construction

The derivative is obtained term by term from

\[
[n]_q=\frac{\sin(n\theta)}{\sin\theta},
\qquad
\partial_\theta\log[n]_q=n\cot(n\theta)-\cot\theta,
\]

then propagated through q-factorials, the four Delta prefactors and the finite q-Racah sum. The recoupling derivative includes the derivative of the quantum-dimension amplitude.

The certified invariant is

\[
I_C(\theta_0)=\frac{\|F'_C(\theta_0)F_C(\theta_0)^T\|_{HS}}{\sqrt2}=|\omega_C(\theta_0)|.
\]

No fitted coefficient or target-dependent feature choice is present.

## Independent validation

The family-exclusion atlas contains 75 ordered carriers from nine label-1-to-4 families. Validation uses 208 ordered carriers from fifteen families absent from that set and containing a doubled-spin label 5 or 6.

Against central finite differences with steps `1e-5` and `5e-6`:

- maximum analytic-versus-refined relative residual: `2.0283e-9`;
- maximum reference-step disagreement: `6.0882e-9`;
- maximum orthogonality residual: `1.1372e-15`;
- maximum generator-skew residual: `2.3855e-14`.

All preregistered thresholds pass by substantial margins.

## Integrity audit

The initially uploaded source file was truncated during a connector write. It was replaced before tests and before publication of the certificate by the complete locally executed source. The repaired source is the one associated with the reported ten passing tests.

Local execution:

```text
10 passed in 1.46s
```

## Claim firewall

Allowed:

> The explicit termwise derivative of the declared finite q-6j recoupling formula reproduces the two-channel anchor angular speed on the independent new-label atlas.

Not allowed:

- a compressed carrier-neutral formula using only a few Casimir invariants;
- prediction of \(\omega'/\omega\) or \(\omega''/\omega\);
- validity outside the declared real regular chamber or outside two-channel carriers;
- physical interpretation of the deformation parameter.

## Next obligation

The next admissible construction is an analytic second-derivative module for the logarithmic angular-speed slope, with a new preregistration and no inference from the successful first derivative.

No statement from the Gemini advisory report is used as evidence.
