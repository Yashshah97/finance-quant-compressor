"""Smoke tests for encoder."""
import unittest

from finance_quant_compressor import encoder


class TestModule(unittest.TestCase):
    def test_module_loads(self):
        self.assertTrue(hasattr(encoder, '__doc__'))

    def test_public_api_exists(self):
        public = [n for n in dir(encoder) if not n.startswith('_')]
        self.assertTrue(public)


if __name__ == "__main__":
    unittest.main()
