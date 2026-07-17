# BC-IDPR P5-UA01-D0 — Response-Independent Mode-5 Gram Preflight

**Status:** `HIGH_PRECISION_DIAGNOSTIC_COMPLETE / INTERVAL_CERTIFICATION_PENDING`  
**Date:** 2026-07-17  
**Upstream object:** `BC-IDPR-P3-P1-RC02`  
**Response data loaded:** `false`

## 1. Question

Does the frozen cubic-residualized predictor/control dictionary already make integer mode `5` unique before any q-Racah carrier response is applied?

This diagnostic reconstructs only the frozen RC02 dictionary:

- `eta = 12 theta / pi` on `0.60,...,1.15` with step `0.0005`;
- cubic nuisance space `span{1,x,x^2,x^3}` in the affine coordinate `x in [-1,1]`;
- q-curvature atoms `Phi_m = -m^2 csc^2(m theta) + csc^2(theta)`;
- integer modes `2,...,10`;
- half-integer controls `1.5,...,9.5`;
- the frozen RC02 bijection.

No pilot, calibration, confirmatory, carrier-family, phase, or energy outcome is read by the computation.

## 2. Arithmetic and reproducibility

The calculation uses `mpmath` at 80 decimal digits. Cubic projection is solved in high precision and all Gram entries are recomputed from the 1101 residual samples.

This is stronger than a float64 exploratory calculation but is **not yet an interval proof**. The committed matrices and JSON result are accompanied by SHA-256 hashes in `results/MANIFEST.json`.

The maximum frozen paired overlap is reconstructed as

```text
0.9909657557889068551246253630853970...
```

which agrees with the frozen RC02 value `0.9909657558650774` to approximately ten decimal places. The small discrepancy is numerical-implementation scale and does not alter any ordering reported below.

## 3. Integer predictor Gram geometry

The eigenvalues of `GII` in ascending order begin

```text
1.6593540696e-17
4.1174292778e-14
3.5102412262e-11
1.3707547019e-8
2.7499115829e-6
2.9781970665e-4
1.6680739915e-2
3.7133875986e-1
8.6116799169
```

The condition number is approximately `5.1897784051e17`. Thus the normalized predictor dictionary is strongly concentrated near a low-dimensional curved family. At thresholds `1e-12`, `1e-10`, `1e-8`, and `1e-6`, the effective ranks are respectively `7`, `6`, `6`, and `5`.

### Mode-5 local position

For mode `5`:

```text
nearest integer mode              4
absolute overlap                  0.9994508815208706...
projective distance               0.0331351086787821...
leave-one-out distance            7.7251124840e-9
```

The leave-one-out distances, ordered from least to most independent, start with

```text
m=4   6.07538828696e-9
m=5   7.72511248402e-9
m=3   9.06808352265e-9
m=6   1.77522829754e-8
...
m=10  3.37206546770e-3
```

Therefore mode `5` is the **second least independent** integer atom under the full leave-one-out test. It is not an isolated predictor direction.

## 4. Integer-control cross geometry

The controls nearest to mode `5` are not its frozen control:

| control | absolute overlap with mode 5 | projective distance |
|---:|---:|---:|
| 4.5 | 0.9998487770883943 | 0.0173903121 |
| 5.5 | 0.9998107021708921 | 0.0194566139 |
| 3.5 | 0.9988690846596609 | 0.0475452596 |
| 9.5 (frozen) | 0.9126886234204259 | 0.4086556945 |

The frozen `5 -> 9.5` assignment is therefore not a nearest-neighbour relation. It arises from the global lexicographic minimax bijection.

For a frozen pair `(m,c)`, the maximum possible energy contrast over unit residuals is controlled by

```text
||P_psi_m - P_chi_c||_op = sqrt(1 - |<psi_m,chi_c>|^2).
```

The frozen pair capacities rank as follows:

| rank | integer mode | control | contrast capacity |
|---:|---:|---:|---:|
| 1 | 10 | 4.5 | 0.5942333897141773 |
| 2 | 5 | 9.5 | 0.4086556945387254 |
| 3 | 3 | 8.5 | 0.2879091857172718 |
| 4 | 9 | 5.5 | 0.2863366268309762 |
| 5 | 8 | 2.5 | 0.2458349306275308 |
| 6 | 4 | 7.5 | 0.1647584082333774 |
| 7 | 2 | 6.5 | 0.1500766573298192 |
| 8 | 7 | 3.5 | 0.1436406500439397 |
| 9 | 6 | 1.5 | 0.1341151402852065 |

Mode `5` has a large contrast capacity, but it is not the unique or maximal capacity. Mode `10` is larger. The bottleneck of the frozen minimax assignment is mode `6`, not mode `5`.

## 5. Reflection audit

For the integer reflection permutation `m -> 12-m`, the post-residualization Gram defect is

```text
||GII - Pi_R GII Pi_R^T||_op = 0.5191189932962168...
```

and the even/odd symmetry-sector mixing norm is `0.2595594966481084...`.

Hence the root reflection found at the pointwise q-number level does not become an exact or near-exact organizing symmetry of the complete normalized residual Gram geometry on the frozen asymmetric eta window.

## 6. Decision

```text
PREDICTOR_ONLY_MODE5_ISOLATION: NOT_SUPPORTED
MODE5_FROZEN_PAIR_CAPACITY: LARGE_BUT_SECOND_RANKED
MODE5_FROZEN_CONTROL_NEAREST_NEIGHBOUR: FALSE
FROZEN_ASSIGNMENT_BOTTLENECK: MODE_6
MECHANISM_LOCALIZATION:
    RESPONSE_ALIGNMENT_OR_ADDITIONAL_CARRIER_STRUCTURE_REQUIRED
```

The response-independent dictionary does not uniquely predict mode `5`.

This does **not** weaken the frozen RC02 outcome. It localizes the missing explanation: the selected mode cannot be derived from single-atom q-number symmetry, integer predictor isolation, nearest-control matching, or maximal paired contrast capacity alone. Any analytical account of the observed mode-5 advantage must include the orientation of the finite q-Racah carrier responses, or another carrier-dependent structural input.

## 7. Claim ceiling

This result concerns only the frozen finite RC02 dictionary and cubic residualization protocol. It is not:

- an arbitrary-level or arbitrary-label theorem;
- an interval-certified frame bound;
- a theorem about the 283-carrier response class;
- a physical coupling or dynamical mechanism;
- a reopening or rerun of RC02.

## 8. Next P5 action

The next response-independent calculation is not another predictor search. It is the construction of the operator-adapted measurement matrix required by `UA01-WP1`, followed by an E-optimal frame-design certificate. The mode-5 question then re-enters only through fixed contrast operators and response-alignment bounds, without retuning the frozen dictionary.
