import unittest
from finance_quant_compressor import benchmarks

class TestRatioFunctions(unittest.TestCase):
    def test_ratio(self):
        self.assertEqual(benchmarks.ratio(10, 9), 1.111111111111111)
        self.assertEqual(benchmarks.ratio(-10, -9), 1.111111111111111)

    def test_compare_ratio(self):
        self.assertTrue(benchmarks.compare_ratio(10, 9))
        self.assertFalse(benchmarks.compare_ratio(1000, 999))

    def test_compare_ratio_percent_change(self):
        self.assertTrue(benchmarks.compare_ratio_percent_change(10, 9))
        self.assertFalse(benchmarks.compare_ratio_percent_change(1000, 999))

if __name__ == "__main__":
    unittest.main()
