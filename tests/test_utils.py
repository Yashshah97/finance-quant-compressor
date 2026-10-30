"""Smoke tests for utils."""
import unittest

from finance_quant_compressor import utils


class TestModule(unittest.TestCase):
    def test_module_loads(self):
        self.assertTrue(hasattr(utils, '__doc__'))

    def test_public_api_exists(self):
        public = [n for n in dir(utils) if not n.startswith('_')]
        self.assertTrue(public)


if __name__ == "__main__":
    unittest.main()
