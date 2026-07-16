# BC-IDPR P3→P1 Research Contract 02

**Title:** Identifiable q-Curvature Predictors for Phase-Resolved Residual Modulation  
**Status:** `PREDICTOR_GEOMETRY_CERTIFIED / PILOT_AUTHORIZED / CALIBRATION_SEALED`  
**Date:** 2026-07-17

RC02 replaces the unreachable predictor/control geometry of RC01 without using calibration or confirmatory carrier responses. The new dictionary is built from the exact q-number curvature atom

\[
\Phi_m(\eta)
=-m^2\csc^2(m\theta(\eta))+\csc^2\theta(\eta),
\qquad \theta(\eta)=\frac{\pi\eta}{12},
\]

which equals the second \(\theta\)-derivative of \(\log[m]_q\). Integer q-modes are paired with a bijective half-integer control pool by an exhaustive response-independent minimax assignment.

## Certified design geometry

- candidate pairings searched: `9! = 362880`;
- maximum paired absolute overlap: `0.9909657558650774`;
- minimum projector-difference norm: `0.1341151397223887`;
- frozen energy threshold: `0.02`;
- reachability safety factor: `6.705756986119435`;
- response data used for design: `false`;
- calibration results present: `false`;
- confirmatory results present: `false`.

## Stage state

```text
RC01: CLOSED_AT_PILOT_DESIGN_FAILURE
RC02_PREDICTOR_GEOMETRY: CERTIFIED
RC02_PILOT: AUTHORIZED_ON_FOUR_PRIOR_PILOT_FAMILIES
RC02_CALIBRATION: SEALED
RC02_CONFIRMATORY: SEALED_AND_UNTOUCHED
```

## Files

- `RC02_PREREGISTRATION_v0.1.0.json` — machine-readable contract;
- `RESEARCH_CONTRACT_02.md` — scientific design contract;
- `PREDICTOR_GEOMETRY_AUDIT.md` — reachability and optimal-pairing audit;
- `PREDICTOR_GEOMETRY_CERTIFICATE.json` — machine-readable geometry certificate;
- `predictor_geometry_audit.py` — executable exhaustive audit;
- `test_predictor_geometry.py` — geometry tests;
- `PILOT_AUTHORIZATION.md` — permitted pilot operations;
- `CHANGE_CONTROL.md` — post-freeze modification rules;
- `validate_rc02.py` — package validator;
- `RC02_CERTIFICATE.json` — freeze certificate;
- `SHA256SUMS.txt` — checksum ledger.

No statement from the Gemini advisory report is used as evidence.