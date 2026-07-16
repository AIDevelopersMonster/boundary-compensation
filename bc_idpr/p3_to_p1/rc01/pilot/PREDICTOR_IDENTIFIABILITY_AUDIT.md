# RC01 predictor-identifiability audit

**Contract:** `BC-IDPR-P3-P1-RC01`  
**Audit date:** 2026-07-17  
**Status:** `EXACT_PROTOCOL_REACHABILITY_FAILURE / CALIBRATION_BLOCKED`  
**Scope:** frozen grid and frozen predictor dictionary only; no calibration or confirmatory data were evaluated.

## 1. Finding

The preregistered integer q modes and their matched half-integer controls are almost collinear after projection away from the frozen cubic baseline. For every registered mode `n=2,...,10`,

\[
|\langle\psi_n,\chi_n\rangle|>0.9999932.
\]

This makes the frozen confirmatory energy threshold mathematically unreachable.

## 2. Exact projector bound

Let `u` and `v` be unit vectors and let `r` be any unit residual. Define

\[
\rho_u=|\langle r,u\rangle|^2,
\qquad
\rho_v=|\langle r,v\rangle|^2.
\]

Writing `P_u=uu^*` and `P_v=vv^*`,

\[
|\rho_u-\rho_v|
=|\langle r,(P_u-P_v)r\rangle|
\le \|P_u-P_v\|_{\operatorname{op}}
=\sqrt{1-|\langle u,v\rangle|^2}.
\]

Therefore every ordered-carrier advantage

\[
\Delta_{J,n}=\rho_{J,n}^{q}-\rho_{J,n}^{c}
\]

obeys the same absolute bound. A family median cannot exceed that bound either.

## 3. Frozen-mode bounds

| `n` | `|<psi_n,chi_n>|` | exact operator-norm bound on `|Delta_{J,n}|` |
|---:|---:|---:|
| 2 | 0.9999934351299474 | 0.0036234923771990 |
| 3 | 0.9999934257955784 | 0.0036260675149603 |
| 4 | 0.9999934130408109 | 0.0036295833080553 |
| 5 | 0.9999933968414608 | 0.0036340436811730 |
| 6 | 0.9999933771667401 | 0.0036394536207953 |
| 7 | 0.9999933539791421 | 0.0036458191872586 |
| 8 | 0.9999933272343166 | 0.0036531475252261 |
| 9 | 0.9999932968809018 | 0.0036614468813053 |
| 10 | 0.9999932628603475 | 0.0036707266196157 |

The largest possible family-level absolute advantage under the frozen dictionary is therefore at most

\[
0.003670726619615724.
\]

The preregistered confirmatory criterion requires

\[
\operatorname{median}_f\Delta_{f,n_*}\ge 0.02.
\]

Since

\[
0.003670726619615724 < 0.02,
\]

the criterion is impossible for every registered mode and for every possible carrier residual, independently of the data.

## 4. Additional conditioning diagnostic

The combined 18-column integer/control dictionary has numerical condition number

\[
\kappa_2\approx 2.2834\times 10^{13}.
\]

This is a secondary warning. The exact projector bound above is already sufficient to block the protocol and does not depend on a floating-point condition-number threshold.

## 5. Consequences

1. Outcome `A_UNIVERSAL_PHASE_LOCK` cannot be reached under RC01.
2. Outcome `B_PHASE_CLASSES` also cannot be reached because it inherits the same energy criterion.
3. Proceeding to calibration would create a confirmatory experiment whose positive outcomes are excluded by construction.
4. Lowering the threshold or replacing controls inside RC01 would be a post-preregistration scientific change.
5. Under `CHANGE_CONTROL.md`, RC01 must stop before calibration and a new contract identifier must be issued.

## 6. Decision

```text
RC01_PILOT: COMPLETED
RC01_CALIBRATION: NOT_AUTHORIZED
RC01_CONFIRMATORY: SEALED_AND_UNTOUCHED
NEXT_REQUIRED_ARTIFACT: RC02_PREDICTOR_DESIGN_CONTRACT
```

This is a protocol-design result, not evidence for or against physical phase modulation.

No statement from the Gemini advisory report is used as evidence.