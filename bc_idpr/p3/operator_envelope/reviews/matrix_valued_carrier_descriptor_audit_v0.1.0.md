# P3-B-M7 Research Audit v0.1.0

**Verdict:** negative certification result with a positive exploratory signal.

## Scope

The module tests whether a frozen representation descriptor predicts the local two-channel recoupling jet across a deterministic atlas of 75 wall-safe carriers. Derivatives of \(F\) are excluded from the predictor and used only to construct targets.

## Validation design

The baseline descriptor contains normalized external and channel Casimirs. The augmented descriptor adds the four entries of \(F(\theta_0)\). Both are evaluated by leave-one-carrier-out ridge regression with fixed \(\alpha=1\).

Targets are

\[
\log|\omega|,\qquad \omega'/\omega,\qquad \omega''/\omega.
\]

The frozen certification requirement is NRMSE at most `0.25` for every target, together with improvement over the baseline.

## Findings

Baseline NRMSE is

`(0.509846, 0.491628, 0.569295)`.

Matrix-augmented NRMSE is

`(0.304711, 0.406176, 0.466017)`.

Thus adding \(F(\theta_0)\) improves all three targets, but every error remains above the certification threshold. The result is informative but not sufficient to open another cross-carrier pilot.

Halving the jet-extraction step changes the raw jet by at most `1.08e-5` relatively, so the negative decision is not explained by the finite-difference scale.

## Claim firewall

Allowed: the anchor recoupling matrix contains predictive information beyond normalized Casimir data on the declared atlas.

Not allowed: certified prediction of \(\omega\), a universal representation law, higher-jet transfer, physical interpretation, or post-hoc enlargement of the descriptor on the same atlas.

## Next obligation

The next module must introduce an independently motivated nonlinear or equivariant representation map and test it on a held-out carrier family or a separately frozen atlas. Reusing the same 75 carriers to search arbitrary feature combinations would be exploratory only.

No statement from the Gemini advisory report is used as evidence.
