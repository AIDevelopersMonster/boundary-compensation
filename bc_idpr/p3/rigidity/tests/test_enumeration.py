#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "src" / "enumerate_fusion_trees.py"
SPEC = importlib.util.spec_from_file_location("enumerate_fusion_trees", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class IsingEnumerationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fusion = MODULE.load(ROOT / "data" / "ising_fusion_rules.json")
        cls.baseline = MODULE.load(ROOT / "data" / "ising_F_baseline.json")
        MODULE.validate(cls.fusion)
        cls.blocks = MODULE.enumerate_blocks(cls.fusion)
        cls.expanded = MODULE.expand(cls.fusion, cls.baseline, cls.blocks)

    def test_all_associator_dimensions_match(self) -> None:
        self.assertEqual(len(self.blocks), 33)
        for block in self.blocks:
            self.assertEqual(len(block["left_channels"]), len(block["right_channels"]))

    def test_sigma_sigma_sigma_block(self) -> None:
        block = next(
            b for b in self.expanded
            if (b["a"], b["b"], b["c"], b["d"])
            == ("sigma", "sigma", "sigma", "sigma")
        )
        self.assertEqual(block["dimension"], 2)
        self.assertEqual(block["left_channels"], ["1", "psi"])
        values = {(e["e"], e["f"]): e["value"] for e in block["entries"]}
        self.assertEqual(values[("1", "1")], "1/sqrt(2)")
        self.assertEqual(values[("psi", "psi")], "-1/sqrt(2)")

    def test_scalar_minus_one_overrides(self) -> None:
        lookup = {}
        for block in self.expanded:
            for entry in block["entries"]:
                lookup[(block["a"], block["b"], block["c"], block["d"], entry["e"], entry["f"])] = entry["value"]
        self.assertEqual(lookup[("sigma", "psi", "sigma", "psi", "sigma", "sigma")], "-1")
        self.assertEqual(lookup[("psi", "sigma", "psi", "sigma", "sigma", "sigma")], "-1")

    def test_variable_registry(self) -> None:
        registry = MODULE.variables(self.fusion, self.expanded)
        self.assertEqual(len(registry), 14)
        self.assertTrue(all("variable_id" in item for item in registry))


if __name__ == "__main__":
    unittest.main()
