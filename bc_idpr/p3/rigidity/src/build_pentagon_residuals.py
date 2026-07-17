#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
from pathlib import Path
from typing import Any
import sympy as sp


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, obj: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def outs(rules: dict[str, list[str]], a: str, b: str) -> list[str]:
    return rules[f"{a},{b}"]


def parse_expr(value: str) -> sp.Expr:
    return sp.sympify(value, locals={"sqrt": sp.sqrt})


def f_table(fusion: dict[str, Any], baseline: dict[str, Any]) -> dict[tuple[str, ...], sp.Expr]:
    objs, rules = fusion["objects"], fusion["fusion_rules"]
    default = parse_expr(baseline["default_rule"]["value"])
    overrides: dict[tuple[str, ...], sp.Expr] = {}
    for item in baseline.get("overrides", []):
        if item["type"] == "scalar":
            overrides[(item["a"], item["b"], item["c"], item["d"], item["e"], item["f"])] = parse_expr(item["value"])
        else:
            for i, e in enumerate(item["left_channels"]):
                for j, f in enumerate(item["right_channels"]):
                    overrides[(item["a"], item["b"], item["c"], item["d"], e, f)] = parse_expr(item["entries"][i][j])
    table: dict[tuple[str, ...], sp.Expr] = {}
    for a in objs:
        for b in objs:
            for c in objs:
                for d in objs:
                    left = [e for e in outs(rules, a, b) if d in outs(rules, e, c)]
                    right = [f for f in outs(rules, b, c) if d in outs(rules, a, f)]
                    if len(left) != len(right):
                        raise ValueError(f"Associativity mismatch {(a, b, c, d)}")
                    for e in left:
                        for f in right:
                            table[(a, b, c, d, e, f)] = overrides.get((a, b, c, d, e, f), default)
    unused = set(overrides) - set(table)
    if unused:
        raise ValueError(f"Overrides address inadmissible entries: {sorted(unused)}")
    return table


def bases(rules: dict[str, list[str]], a: str, b: str, c: str, d: str, z: str):
    t0, t1, t2, t3, t4 = [], [], [], [], []
    for x in outs(rules, a, b):
        for y in outs(rules, x, c):
            if z in outs(rules, y, d): t0.append((x, y))
    for u in outs(rules, b, c):
        for y in outs(rules, a, u):
            if z in outs(rules, y, d): t1.append((u, y))
    for u in outs(rules, b, c):
        for v in outs(rules, u, d):
            if z in outs(rules, a, v): t2.append((u, v))
    for w in outs(rules, c, d):
        for v in outs(rules, b, w):
            if z in outs(rules, a, v): t3.append((w, v))
    for x in outs(rules, a, b):
        for w in outs(rules, c, d):
            if z in outs(rules, x, w): t4.append((x, w))
    return t0, t1, t2, t3, t4


def matrix(rows, cols, coefficient):
    return sp.Matrix([[sp.simplify(coefficient(r, q)) for q in cols] for r in rows])


def instance(fusion, F, a, b, c, d, z):
    rules = fusion["fusion_rules"]
    t0, t1, t2, t3, t4 = bases(rules, a, b, c, d, z)
    if not t0:
        return None
    if len({len(x) for x in (t0, t1, t2, t3, t4)}) != 1:
        raise ValueError(f"Four-object basis mismatch {(a, b, c, d, z)}")
    a01 = matrix(t1, t0, lambda r, q: F[(a, b, c, r[1], q[0], r[0])] if q[1] == r[1] else 0)
    a12 = matrix(t2, t1, lambda r, q: F[(a, q[0], d, z, q[1], r[1])] if q[0] == r[0] else 0)
    a23 = matrix(t3, t2, lambda r, q: F[(b, c, d, r[1], q[0], r[0])] if q[1] == r[1] else 0)
    a04 = matrix(t4, t0, lambda r, q: F[(q[0], c, d, z, q[1], r[1])] if q[0] == r[0] else 0)
    a43 = matrix(t3, t4, lambda r, q: F[(a, b, q[1], z, q[0], r[1])] if q[1] == r[0] else 0)
    path_three = sp.simplify(a23 * a12 * a01)
    path_two = sp.simplify(a43 * a04)
    return path_three, path_two, sp.simplify(path_three - path_two)


def encode_matrix(m: sp.Matrix):
    return [[sp.sstr(sp.simplify(m[i, j])) for j in range(m.cols)] for i in range(m.rows)]


def build(fusion, baseline):
    F, objs = f_table(fusion, baseline), fusion["objects"]
    instances, failures, n_scalar = [], [], 0
    for a in objs:
        for b in objs:
            for c in objs:
                for d in objs:
                    for z in objs:
                        result = instance(fusion, F, a, b, c, d, z)
                        if result is None:
                            continue
                        p3, p2, residual = result
                        n_scalar += residual.rows * residual.cols
                        nonzero = []
                        for i in range(residual.rows):
                            for j in range(residual.cols):
                                value = sp.simplify(residual[i, j])
                                if value != 0:
                                    nonzero.append({"row": i, "col": j, "value": sp.sstr(value)})
                        if nonzero:
                            failures.append({"external": [a, b, c, d], "total": z, "entries": nonzero})
                        instances.append({"external": [a, b, c, d], "total": z, "dimension": residual.rows, "path_three": encode_matrix(p3), "path_two": encode_matrix(p2), "residual": encode_matrix(residual)})
    return {
        "status": "BASELINE_PENTAGON_VERIFIED" if not failures else "BASELINE_PENTAGON_FAILURE",
        "n_instances": len(instances),
        "n_scalar_residuals": n_scalar,
        "n_nonzero_residuals": sum(len(x["entries"]) for x in failures),
        "failures": failures,
        "instances": instances
    }


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--fusion", type=Path, required=True)
    p.add_argument("--baseline", type=Path, required=True)
    p.add_argument("--output", type=Path, required=True)
    args = p.parse_args()
    result = build(load(args.fusion), load(args.baseline))
    dump(args.output, result)
    print(json.dumps({k: result[k] for k in ("status", "n_instances", "n_scalar_residuals", "n_nonzero_residuals")}, sort_keys=True))
    return 0 if result["n_nonzero_residuals"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
