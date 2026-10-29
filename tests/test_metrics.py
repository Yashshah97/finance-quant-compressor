import unittest
from finance_quant_compressor import metrics

class TestMetrics(unittest.TestCase):

    def test_var(self):
        data = [1, 2, 3, 4, 5]
        self.assertAlmostEqual(metrics.var(data), 2)

    def test_cva(self):
        data = [1, 2, 3, 4, 5]
        self.assertAlmostEqual(metrics.cva(data), 3)

    def test_es(self):
        data = [1, 2, 3, 4, 5]
        self.assertAlmostEqual(metrics.es(data), 3)

    def test_aggregate_risk_metrics(self):
        data = [1, 2, 3, 4, 5]
        result = metrics.aggregate_risk_metrics(data)
        self.assertIn('var', result)
        self.assertIn('cvar', result)
        self.assertIn('es', result)

if __name__ == '__main__':
    unittest.main()
