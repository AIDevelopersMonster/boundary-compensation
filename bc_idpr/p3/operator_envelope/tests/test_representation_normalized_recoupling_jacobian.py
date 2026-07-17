#!/usr/bin/env python3
from __future__ import annotations
import importlib.util
from pathlib import Path
import unittest

SRC=Path(__file__).resolve().parents[1]/'src'/'representation_normalized_recoupling_jacobian.py'
spec=importlib.util.spec_from_file_location('m6',SRC)
if spec is None or spec.loader is None: raise RuntimeError(SRC)
m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)

class M6Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls): cls.out=m.build(65)
    def test_status(self): self.assertEqual(self.out['status'],'RECOUPLING_JACOBIAN_FACTORIZATION_CERTIFIED_SCALAR_NORMALIZATION_INSUFFICIENT')
    def test_five_carriers(self): self.assertEqual(len(self.out['atlas']),5)
    def test_two_channels(self):
        for r in self.out['atlas'].values(): self.assertEqual((len(r['channels_e_doubled']),len(r['channels_f_doubled'])),(2,2))
    def test_orthogonality(self):
        for r in self.out['atlas'].values(): self.assertLess(r['maximum_orthogonality_residual'],1e-12)
    def test_skew_generator(self):
        for r in self.out['atlas'].values(): self.assertLess(r['maximum_generator_skew_residual'],2e-7)
    def test_operator_factorization(self):
        for r in self.out['atlas'].values(): self.assertLess(r['maximum_operator_factorization_relative_residual'],2e-7)
    def test_raw_variation(self): self.assertGreater(self.out['scalar_normalization_audit']['raw_anchor_speed_cv'],0.5)
    def test_simple_scalar_normalizations_fail(self):
        self.assertGreater(self.out['scalar_normalization_audit']['product_gap_normalized_cv'],0.10)
        self.assertFalse(self.out['scalar_normalization_audit']['passed'])
    def test_shape_collapse_fails(self):
        self.assertGreater(self.out['anchor_normalized_shape_audit']['maximum_pairwise_abs_difference'],0.10)
        self.assertFalse(self.out['anchor_normalized_shape_audit']['passed'])
    def test_gate(self): self.assertEqual(self.out['gates']['new_cross_carrier_pilot'],'BLOCKED_PENDING_RICHER_REPRESENTATION_MAP')

if __name__=='__main__': unittest.main()
