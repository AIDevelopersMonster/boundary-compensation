# BC-Spec L1-P04: exact kappa=2 raw-to-Wedderburn calculations

This directory is the reproducible calculation companion for **BC-Spec L1-P04 v0.1.4-r1 reviewed-clean**. It records an exact registered-gauge coordinate transform for the `SU(2)_2` / Ising tube algebra and a historical cross-audit against the basis registries shipped with v0.1.5.

## Exact scope

The package verifies:

- `A_2 ~= C^8 + M_2(C)` on the 12-dimensional regular carrier;
- the raw/Wedderburn support blocks `3 + 1 + 4 + 1 + 3`;
- an invertible registered-gauge matrix `U` with `[v]_raw = U [v]_lambda`;
- `det(U) = i/256` in the serialized `alpha = beta = 1` gauge;
- nine transported central projectors, including idempotence, orthogonality, and completeness;
- operator-space dimensions `12 < 24 < 72 < 144`;
- constraint ranks `120` for full-sector preservation and `72` for coarse preservation;
- compatibility with the historical v0.1.5 raw registry after the explicit permutation `[0,1,2,3,5,4,6,7,8,11,10,9]`.

## Claim boundary

The calculations are exact **inside the declared registered coordinate convention**. They do not prove that this coordinate Gram equals the still-unfrozen legacy v0.1.2 TQFT Gram normalization. They do not compute the nontrivial physical edge-star matrix and do not establish physical sector decoupling.

## Layout

```text
scripts/                  exact generator, independent checker, cross-audit
registries/               registered transform metadata
generated/                matrices, multiplication table, raw projectors
checks/                   exact and independent audit reports
historical-cross-audit/   v0.1.5 source registries and permutation bridge
```

## Reproduction

```bash
python -m pip install -r requirements.txt
python scripts/p04_kappa2_raw_wedderburn_transform.py
python scripts/p04_kappa2_raw_wedderburn_independent_check.py
python scripts/p04_historical_cross_audit_v015_vs_v014r1.py
```

Expected terminal status:

```text
INDEPENDENT CHECK PASS
```

The three scripts must finish without assertion failures. Generated files are deterministic symbolic outputs produced with SymPy.

## Historical-order bridge

The v0.1.5 and v0.1.4-r1 registries contain the same 12 raw basis elements but serialize four entries in a different order. The cross-audit constructs a permutation matrix `Q` with

```text
[v]_raw,v015 = Q [v]_raw,v014r1,
U_v015 = Q U_v014r1.
```

The corresponding inverse and central projectors are exported in `historical-cross-audit/`.
