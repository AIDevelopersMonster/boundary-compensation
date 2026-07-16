# P3-B-M11 Research Audit v0.1.0

**Verdict:** analytic second-jet certificate accepted within the declared two-channel finite q-6j chamber.

## Scope

M11 extends M10 from the anchor speed `|omega|` to the logarithmic slope `omega'/omega`. The construction differentiates the finite q-6j expression twice and uses no learned coefficients.

## Independence and leakage control

The preregistration was committed before evaluation. The test atlas is the same independent new-label atlas frozen in M10: 208 ordered carriers in 15 families containing doubled-spin labels 5 or 6 and excluded from the label-1-to-4 family set.

The finite-difference references are used only to validate the analytic expression. They do not enter its construction.

## Findings

The maximum relative residual against the refined reference is `1.8376e-9`; the preregistered limit is `1e-6`.

The maximum disagreement between reference steps is `5.4944e-9`. Orthogonality residual is `1.1372e-15`, generator skew residual is `2.2178e-14`, and differentiated-generator skew residual is `1.5858e-12`.

All frozen gates pass.

## Reproducibility

A local autonomous implementation of the same formulas was executed successfully and produced the recorded certificate values. The repository test suite contains ten specialized tests. The exact repository pytest file was not executed through GitHub Actions in this step; the certificate therefore reports the specialized test design and locally reproduced computation, not an observed CI run.

## Claim firewall

Allowed: the analytic second derivative of the finite q-6j recoupling formula reproduces the anchor logarithmic angular-speed slope on the declared independent atlas.

Forbidden: third-jet closure, low-dimensional representation compression, universal phase dynamics, physical interpretation, or extrapolation beyond the declared chamber.

## Next obligation

The next admissible analytic step is a separately preregistered third-derivative module for `omega''/omega`, including the subtraction needed to distinguish it from the second derivative of `log|omega|`.

No statement from the Gemini advisory report is used as evidence.
