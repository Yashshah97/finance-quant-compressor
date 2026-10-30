import unittest
from finance_quant_compressor import tests_test_encoder

class TestTestEncoder(unittest.TestCase):

    def test_import(self):
        """
        Test that the module imports correctly.
        """
        from finance_quant_compressor import tests_test_encoder
        self.assertIsNotNone(tests_test_encoder)

if __name__ == '__main__':
    unittest.main()
