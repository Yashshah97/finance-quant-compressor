import unittest
from finance_quant_compressor import core

class TestCoreFunctions(unittest.TestCase):
    def test_encode_ratio_benchmark(self):
        time_series = [1.0, 2.0, 3.0]
        benchmark_value = 2.0
        encoded_time_series, compression_ratio = core.encode_ratio_benchmark(time_series, benchmark_value)
        self.assertEqual(encoded_time_series, [0, 1, 1])
        self.assertAlmostEqual(compression_ratio, 0.6666666666666666)

    def test_encode_domain_tuned(self):
        time_series = [10.0, 20.0, 30.0]
        domain_tuned_params = (5.0, 35.0)
        encoded_time_series, compression_ratio = core.encode_domain_tuned(time_series, domain_tuned_params)
        self.assertEqual(encoded_time_series, [2, 7, 12])
        self.assertAlmostEqual(compression_ratio, 6.333333333333334)

    def test_compress_market_data(self):
        market_data = [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]
        encoded_market_data, compression_ratio = core.compress_market_data(market_data)
        self.assertEqual(encoded_market_data, [[0, 1, 1], [1, 2, 2]])
        self.assertAlmostEqual(compression_ratio, 1.3333333333333333)

if __name__ == '__main__':
    unittest.main()
