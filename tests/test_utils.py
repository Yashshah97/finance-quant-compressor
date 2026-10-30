import unittest
import numpy as np
from finance_quant_compressor import utils

class TestUtils(unittest.TestCase):
    def test_is_increasing(self):
        self.assertTrue(utils.is_increasing([1, 2, 3]))
        self.assertFalse(utils.is_increasing([3, 2, 1]))

    def test_is_decreasing(self):
        self.assertTrue(utils.is_decreasing([3, 2, 1]))
        self.assertFalse(utils.is_decreasing([1, 2, 3]))

    def test_calculate_ratio(self):
        a = [1, 2, 3]
        b = [4, 5, 6]
        self.assertAlmostEqual(utils.calculate_ratio(a, b), (a[0] + a[1] + a[2]) / (b[0] + b[1] + b[2]))

    def test_normalize_data(self):
        data = [1, 2, 3, 4, 5]
        min_val = 0
        max_val = 1
        self.assertEqual(len(utils.normalize_data(data, min_val, max_val)), len(data))
        self.assertAlmostEqual(min(utils.normalize_data(data, min_val, max_val)), min_val)
        self.assertAlmostEqual(max(utils.normalize_data(data, min_val, max_val)), max_val)

    def test_calculate_percentile(self):
        data = [1, 2, 3, 4, 5]
        percentile = 50
        self.assertAlmostEqual(utils.calculate_percentile(data, percentile), np.percentile(data, percentile))

if __name__ == '__main__':
    unittest.main()
