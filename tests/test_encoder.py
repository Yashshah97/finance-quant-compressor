import unittest
from finance_quant_compressor import encoder


class TestDomainTunedEncoder(unittest.TestCase):

    def test_log(self):
        self.assertAlmostEqual(encoder._log(1), 0)
        self.assertAlmostEqual(encoder._log(10), 2.302585092994046)

    def test_fit_transform(self):
        X = [[1, 2], [3, 4]]
        encoder = encoder.DomainTunedEncoder(2)
        encoder.fit(X)
        encoded_X = encoder.transform(X)
        self.assertEqual(len(encoded_X), len(X))
        for x in encoded_X:
            self.assertAlmostEqual(sum(x), 0)

    def test_encoder_ratio_benchmark(self):
        X = [[1, 2], [3, 4]]
        ratio = encoder.encoder_ratio_benchmark(X)
        self.assertGreaterEqual(ratio, 0)


if __name__ == '__main__':
    unittest.main()
