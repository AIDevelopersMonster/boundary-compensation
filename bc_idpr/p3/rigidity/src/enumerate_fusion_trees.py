#!/usr/bin/env python3
"""Enumerate admissible Ising associator blocks and normalized dF variables."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any, Mapping, Sequence


def load(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def dump(path: Path, value: Mapping[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as f:
        json.dump(value, f, indent=2, ensure_ascii=False)
        f.write("\n")


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def outputs(rules: Mapping[str, Sequence[str]], a: str, b: str) -> list[str]:
    key = f"{a},{b}"
    if key not in rules:
        raise KeyError(f"Missing fusion rule {key}")
    return list(rules[key])


def validate(fusion: Mapping[str, Any]) -> None:
    objects = fusion["objects"]
    rules = fusion["fusion_rules"]
    if len(objects) != len(set(objects)):
        raise ValueError("Duplicate object")
    if fusion["tensor_unit"] not in objects:
        raise ValueError("Unknown tensor unit")
    for a in objects:
        for b in objects:
            result = outputs(rules, a, b)
            if not result or len(result) != len(set(result)):
                raise ValueError(f"Invalid multiplicity-free rule {a},{b}")
            if any(c not in objects for c in result):
                raise ValueError(f"Unknown fusion output in {a},{b}")


def enumerate_blocks(fusion: Mapping[str, Any]) -> list[dict[str, Any]]:
    objects = fusion["objects"]
    rules = fusion["fusion_rules"]
    blocks: list[dict[str, Any]] = []
    for a in objects:
        for b in objects:
            for c in objects:
                for d in objects:
                    left = [e for e in outputs(rules, a, b) if d in outputs(rules, e, c)]
                    right = [f for f in outputs(rules, b, c) if d in outputs(rules, a, f)]
                    if len(left) != len(right):
                        raise ValueError(f"Associativity mismatch {a},{b},{c}->{d}")
                    if left:
                        blocks.append({
                            "block_id": f"F[{a},{b},{c}->{d}]",
                            "a": a, "b": b, "c": c, "d": d,
                            "left_channels": left,
                            "right_channels": right,
                            "dimension": len(left),
                            "n_entries": len(left) * len(right)
                        })
    return blocks


def override_index(baseline: Mapping[str, Any]) -> dict[tuple[str, ...], str]:
    index: dict[tuple[str, ...], str] = {}
    for item in baseline.get("overrides", []):
        prefix = (item["a"], item["b"], item["c"], item["d"])
        if item["type"] == "scalar":
            index[prefix + (item["e"], item["f"])] = item["value"]
        elif item["type"] == "matrix":
            rows, cols, entries = item["left_channels"], item["right_channels"], item["entries"]
            if len(entries) != len(rows) or any(len(row) != len(cols) for row in entries):
                raise ValueError(f"Malformed matrix override {prefix}")
            for i, e in enumerate(rows):
                for j, f in enumerate(cols):
                    index[prefix + (e, f)] = entries[i][j]
        else:
            raise ValueError(f"Unknown override type {item['type']}")
    return index


def expand(fusion: Mapping[str, Any], baseline: Mapping[str, Any], blocks: Sequence[Mapping[str, Any]]) -> list[dict[str, Any]]:
    default = baseline["default_rule"]["value"]
    overrides = override_index(baseline)
    used: set[tuple[str, ...]] = set()
    result: list[dict[str, Any]] = []
    for block in blocks:
        entries = []
        for e in block["left_channels"]:
            for f in block["right_channels"]:
                key = (block["a"], block["b"], block["c"], block["d"], e, f)
                value = overrides.get(key, default)
                if key in overrides:
                    used.add(key)
                entries.append({"e": e, "f": f, "value": value})
        result.append({**block, "unit_normalized": fusion["tensor_unit"] in (block["a"], block["b"], block["c"]), "entries": entries})
    unused = sorted(set(overrides) - used)
    if unused:
        raise ValueError(f"Overrides address inadmissible entries: {unused}")
    return result


def variables(fusion: Mapping[str, Any], blocks: Sequence[Mapping[str, Any]]) -> list[dict[str, Any]]:
    unit = fusion["tensor_unit"]
    registry = []
    for block in blocks:
        if unit in (block["a"], block["b"], block["c"]):
            continue
        for entry in block["entries"]:
            registry.append({
                "index": len(registry),
                "variable_id": f"dF[{block['a']},{block['b']},{block['c']}->{block['d']};{entry['e']}->{entry['f']}]",
                "block_id": block["block_id"],
                "a": block["a"], "b": block["b"], "c": block["c"], "d": block["d"],
                "e": entry["e"], "f": entry["f"],
                "baseline_value": entry["value"]
            })
    return registry


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--fusion", type=Path, required=True)
    p.add_argument("--baseline", type=Path, required=True)
    p.add_argument("--output-dir", type=Path, required=True)
    args = p.parse_args()
    fusion, baseline = load(args.fusion), load(args.baseline)
    validate(fusion)
    if fusion["category_id"] != baseline["category_id"]:
        raise ValueError("Category IDs differ")
    blocks = enumerate_blocks(fusion)
    expanded = expand(fusion, baseline, blocks)
    vars_ = variables(fusion, expanded)
    provenance = {"fusion_datum_sha256": sha256(args.fusion), "baseline_F_sha256": sha256(args.baseline)}
    common = {"schema_version": "1.0", "contract": fusion["contract"], "category_id": fusion["category_id"], "provenance": provenance}
    dump(args.output_dir / "fusion_trees_registry.json", {**common, "n_blocks": len(blocks), "blocks": blocks})
    dump(args.output_dir / "baseline_F_registry.json", {**common, "gauge_id": baseline["gauge_id"], "n_blocks": len(expanded), "blocks": expanded})
    dump(args.output_dir / "variable_registry.json", {**common, "normalization": "unit-normalized associators excluded", "n_variables": len(vars_), "variables": vars_})
    print(json.dumps({"status": "OK", "category_id": fusion["category_id"], "n_blocks": len(blocks), "n_variables": len(vars_), "output_dir": str(args.output_dir)}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
