"""Smoke tests for benchmarks."""
import unittest

from finance_quant_compressor import benchmarks


class TestModule(unittest.TestCase):
    def test_module_loads(self):
        self.assertTrue(hasattr(benchmarks, '__doc__'))

    def test_public_api_exists(self):
        public = [n for n in dir(benchmarks) if not n.startswith('_')]
        self.assertTrue(public)


if __name__ == "__main__":
    unittest.main()
