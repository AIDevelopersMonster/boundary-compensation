#!/usr/bin/env python3
"""Exact linearization of the Ising pentagon system over Q(sqrt(2))."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any, Iterable

import sympy as sp

from build_pentagon_residuals import f_table, instance, load, dump, outs


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def variable_keys(fusion: dict[str, Any], baseline_table: dict[tuple[str, ...], sp.Expr]) -> list[tuple[str, ...]]:
    unit = fusion["tensor_unit"]
    objs = fusion["objects"]
    rules = fusion["fusion_rules"]
    keys: list[tuple[str, ...]] = []
    for a in objs:
        for b in objs:
            for c in objs:
                for d in objs:
                    left = [e for e in outs(rules, a, b) if d in outs(rules, e, c)]
                    right = [f for f in outs(rules, b, c) if d in outs(rules, a, f)]
                    if unit in (a, b, c):
                        continue
                    for e in left:
                        for f in right:
                            key = (a, b, c, d, e, f)
                            if key not in baseline_table:
                                raise KeyError(key)
                            keys.append(key)
    return keys


def variable_id(key: tuple[str, ...]) -> str:
    a, b, c, d, e, f = key
    return f"dF[{a},{b},{c}->{d};{e}->{f}]"


def symbolic_table(
    baseline_table: dict[tuple[str, ...], sp.Expr],
    keys: list[tuple[str, ...]],
) -> tuple[dict[tuple[str, ...], sp.Expr], tuple[sp.Symbol, ...]]:
    symbols = sp.symbols(f"x0:{len(keys)}")
    table = dict(baseline_table)
    for key, symbol in zip(keys, symbols, strict=True):
        table[key] = sp.simplify(table[key] + symbol)
    return table, symbols


def residual_registry(fusion: dict[str, Any], table: dict[tuple[str, ...], sp.Expr]) -> list[dict[str, Any]]:
    objs = fusion["objects"]
    registry: list[dict[str, Any]] = []
    for a in objs:
        for b in objs:
            for c in objs:
                for d in objs:
                    for z in objs:
                        result = instance(fusion, table, a, b, c, d, z)
                        if result is None:
                            continue
                        _, _, residual = result
                        for row in range(residual.rows):
                            for col in range(residual.cols):
                                registry.append({
                                    "raw_index": len(registry),
                                    "external": [a, b, c, d],
                                    "total": z,
                                    "row": row,
                                    "col": col,
                                    "expression": sp.expand(residual[row, col]),
                                })
    return registry


def encode_expr(expr: sp.Expr) -> str:
    return sp.sstr(sp.simplify(expr))


def encode_vector(vector: Iterable[sp.Expr]) -> list[str]:
    return [encode_expr(value) for value in vector]


def first_nonzero(row: list[sp.Expr]) -> sp.Expr | None:
    for value in row:
        value = sp.simplify(value)
        if value != 0:
            return value
    return None


def projective_key(row: list[sp.Expr]) -> tuple[str, ...] | None:
    pivot = first_nonzero(row)
    if pivot is None:
        return None
    normalized = [sp.simplify(value / pivot) for value in row]
    return tuple(sp.sstr(value) for value in normalized)


def exact_jacobian(
    registry: list[dict[str, Any]], symbols: tuple[sp.Symbol, ...]
) -> tuple[sp.Matrix, list[dict[str, Any]]]:
    zero_subs = {symbol: 0 for symbol in symbols}
    rows: list[list[sp.Expr]] = []
    metadata: list[dict[str, Any]] = []
    for item in registry:
        expression = item["expression"]
        baseline = sp.simplify(expression.subs(zero_subs))
        if baseline != 0:
            raise ValueError(
                f"Baseline residual is nonzero at raw row {item['raw_index']}: {baseline}"
            )
        row = [sp.simplify(sp.diff(expression, symbol).subs(zero_subs)) for symbol in symbols]
        rows.append(row)
        metadata.append({key: item[key] for key in ("raw_index", "external", "total", "row", "col")})
    return sp.Matrix(rows), metadata


def independent_directional_audit(
    registry: list[dict[str, Any]],
    symbols: tuple[sp.Symbol, ...],
    jacobian: sp.Matrix,
) -> dict[str, Any]:
    eps = sp.Symbol("eps")
    direction = sp.Matrix([sp.Integer((index % 5) - 2) for index in range(len(symbols))])
    substitutions = {symbol: eps * direction[index] for index, symbol in enumerate(symbols)}
    direct = sp.Matrix([
        sp.expand(item["expression"].subs(substitutions)).coeff(eps, 1)
        for item in registry
    ])
    predicted = jacobian * direction
    discrepancy = sp.simplify(direct - predicted)
    nonzero = [index for index, value in enumerate(discrepancy) if sp.simplify(value) != 0]
    return {
        "method": "independent epsilon-direction coefficient extraction",
        "direction": [int(value) for value in direction],
        "verified": not nonzero,
        "nonzero_discrepancy_rows": nonzero,
    }


def build(fusion_path: Path, baseline_path: Path) -> dict[str, Any]:
    fusion = load(fusion_path)
    baseline = load(baseline_path)
    baseline_table = f_table(fusion, baseline)
    keys = variable_keys(fusion, baseline_table)
    table, symbols = symbolic_table(baseline_table, keys)
    registry = residual_registry(fusion, table)
    jacobian, row_metadata = exact_jacobian(registry, symbols)

    nonzero_raw_indices = [
        index for index in range(jacobian.rows)
        if any(sp.simplify(jacobian[index, col]) != 0 for col in range(jacobian.cols))
    ]
    nonzero_matrix = jacobian[nonzero_raw_indices, :] if nonzero_raw_indices else sp.zeros(0, jacobian.cols)

    projective_seen: dict[tuple[str, ...], int] = {}
    projective_indices: list[int] = []
    duplicate_map: list[dict[str, int]] = []
    for raw_index in nonzero_raw_indices:
        row = [jacobian[raw_index, col] for col in range(jacobian.cols)]
        key = projective_key(row)
        assert key is not None
        if key not in projective_seen:
            projective_seen[key] = raw_index
            projective_indices.append(raw_index)
        else:
            duplicate_map.append({
                "raw_index": raw_index,
                "representative_raw_index": projective_seen[key],
            })
    reduced = jacobian[projective_indices, :] if projective_indices else sp.zeros(0, jacobian.cols)

    rank_raw = int(jacobian.rank())
    rank_nonzero = int(nonzero_matrix.rank())
    rank_reduced = int(reduced.rank())
    if not (rank_raw == rank_nonzero == rank_reduced):
        raise ValueError("Rank changed during exact row reduction")

    nullspace = jacobian.nullspace()
    audit = independent_directional_audit(registry, symbols, jacobian)
    if not audit["verified"]:
        raise ValueError("Independent directional audit failed")

    variables = [
        {
            "index": index,
            "symbol": str(symbols[index]),
            "variable_id": variable_id(key),
            "key": list(key),
            "baseline_value": encode_expr(baseline_table[key]),
        }
        for index, key in enumerate(keys)
    ]

    return {
        "schema_version": "1.0",
        "contract": fusion["contract"],
        "category_id": fusion["category_id"],
        "status": "LINEARIZED_PENTAGON_JACOBIAN_CERTIFIED",
        "arithmetic": "exact symbolic over Q(sqrt(2))",
        "provenance": {
            "fusion_datum_sha256": sha256(fusion_path),
            "baseline_F_sha256": sha256(baseline_path),
        },
        "counts": {
            "n_variables": len(keys),
            "n_raw_residual_rows": jacobian.rows,
            "n_zero_linearized_rows": jacobian.rows - len(nonzero_raw_indices),
            "n_nonzero_linearized_rows": len(nonzero_raw_indices),
            "n_projectively_unique_rows": len(projective_indices),
            "n_projective_duplicates": len(duplicate_map),
        },
        "rank": {
            "raw": rank_raw,
            "nonzero": rank_nonzero,
            "projectively_reduced": rank_reduced,
        },
        "kernel": {
            "dimension": len(nullspace),
            "basis": [encode_vector(vector) for vector in nullspace],
        },
        "variables": variables,
        "raw_row_metadata": row_metadata,
        "nonzero_raw_indices": nonzero_raw_indices,
        "projective_representative_raw_indices": projective_indices,
        "projective_duplicate_map": duplicate_map,
        "jacobian_shape": [jacobian.rows, jacobian.cols],
        "jacobian_sparse": [
            [row, col, encode_expr(jacobian[row, col])]
            for row in range(jacobian.rows)
            for col in range(jacobian.cols)
            if sp.simplify(jacobian[row, col]) != 0
        ],
        "jacobian_projectively_reduced_sparse": [
            [reduced_row, col, encode_expr(jacobian[raw_row, col])]
            for reduced_row, raw_row in enumerate(projective_indices)
            for col in range(jacobian.cols)
            if sp.simplify(jacobian[raw_row, col]) != 0
        ],
        "independent_audit": audit,
        "claim_status": "Z3_KERNEL_COMPUTED_GAUGE_QUOTIENT_OPEN",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--fusion", type=Path, required=True)
    parser.add_argument("--baseline", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = build(args.fusion, args.baseline)
    dump(args.output, result)
    summary = {
        "status": result["status"],
        **result["counts"],
        "rank": result["rank"]["raw"],
        "kernel_dimension": result["kernel"]["dimension"],
        "independent_audit": result["independent_audit"]["verified"],
    }
    print(json.dumps(summary, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
