# Audit — BC-IDPR-P3-B-JET-RADIUS v0.1.0

## Scope

Audit of the order-50 Taylor–Cauchy radius certificate and its use in the preprint-readiness decision.

## Findings

1. The declared carrier class is unchanged: 283 ordered carriers in 24 sorted external-spin families.
2. The method-selection phase and confirmatory phase are separated by preregistration commit `a6148e37a3386bc4d6c65e168f919977de38317e`.
3. The confirmatory radius is fixed at exactly `0.1 * R_wall`; the proof-family extremal radius is reported separately and is not substituted for the safer confirmatory radius.
4. The first 50 signed-angular-speed Taylor coefficients preserve cancellations that are destroyed by termwise absolute Racah bounds.
5. The tail is bounded by an outer-disk Cauchy majorant. The resulting confirmatory lower bound for `abs(omega)` is positive on every declared carrier.
6. No fitted regression coefficient, carrier-specific threshold or post-evaluation exclusion is used.
7. The absolute maximal analytic radius remains open and is not required by the bounded preprint claim.
8. The preprint-readiness gate correctly separates mathematical-core readiness from manuscript, proof-audit, reproducibility, bibliography and metadata work.

## Test result

Local exact test command:

```text
pytest -q test_finite_q6j_sharp_radius.py
```

Result:

```text
10 passed in 22.05s
```

GitHub Actions was not run in this step.

## Verdict

`CERTIFIED_WITH_BOUNDED_CLAIM_SCOPE`

The mathematical core is ready for integration into a preprint. Upload remains blocked until the five packaging and audit gates in `PREPRINT_READINESS_GATE.md` are closed.

No statement from the Gemini advisory report is used as evidence.
