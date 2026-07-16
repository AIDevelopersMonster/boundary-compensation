import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from protocol_relative_separation import build

class TestProtocolRelativeSeparation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.out = build()

    def test_status(self):
        self.assertEqual(self.out['status'], 'SEPARATION_NOT_CERTIFIED')

    def test_response_nonzero(self):
        self.assertGreater(self.out['decision']['max_response'], 0)

    def test_net_margin_negative(self):
        self.assertLess(self.out['decision']['maximum_net_margin'], 0)

    def test_p1_blocked(self):
        self.assertEqual(self.out['decision']['p1_gate'], 'BLOCKED')

    def test_protocol_family_size(self):
        self.assertEqual(len(self.out['protocol_family']), 4)

    def test_wall_margin_declared(self):
        self.assertEqual(self.out['domain']['wall_margin'], 'pi/20')

if __name__ == '__main__':
    unittest.main()
