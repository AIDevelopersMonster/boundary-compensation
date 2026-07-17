import math
import sys
import unittest
from pathlib import Path

HERE=Path(__file__).resolve()
sys.path.insert(0,str(HERE.parents[1]/'src'))
import coherent_symbol_bridge as m

class CoherentSymbolBridgeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.r=m.build(samples=33,dps=80)

    def test_status(self):
        self.assertEqual(self.r['status'],'EUCLIDEAN_COHERENT_SYMBOL_BRIDGE_CERTIFIED')

    def test_invariant_basis(self):
        self.assertLess(self.r['carrier']['basis_gram_residual'],1e-14)

    def test_geometry_closure(self):
        self.assertLess(self.r['geometries']['regular']['closure_norm'],1e-14)
        self.assertLess(self.r['geometries']['holdout_anisotropic_equifacial']['closure_norm'],1e-14)

    def test_holdout_is_anisotropic(self):
        self.assertGreater(self.r['geometries']['holdout_anisotropic_equifacial']['edge_spread'],1.0)

    def test_anchor_calibration_is_exact_for_regular_geometry(self):
        self.assertLess(self.r['anchor']['regular_mismatch_norm'],1e-14)

    def test_holdout_mismatch_is_finite_and_reported(self):
        self.assertGreater(self.r['anchor']['holdout_mismatch_norm'],0)
        self.assertLess(self.r['anchor']['holdout_mismatch_norm'],0.25)

    def test_nonzero_q_response(self):
        self.assertGreater(abs(self.r['anchor']['regular_symbol_derivative'][1]),1e-3)
        self.assertGreater(abs(self.r['anchor']['holdout_symbol_derivative'][1]),1e-3)

    def test_compact_grid_bounds(self):
        self.assertLess(self.r['grid_summary']['max_regular_mismatch_norm'],0.02)
        self.assertLess(self.r['grid_summary']['max_holdout_mismatch_norm'],0.16)
        self.assertLess(self.r['grid_summary']['regular_second_channel_derivative_range'][1],0)
        self.assertGreater(self.r['grid_summary']['holdout_second_channel_derivative_range'][0],0)

if __name__=='__main__':
    unittest.main()
