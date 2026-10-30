"""
Unit tests for the finance quant compressor's encoder implementation.

This module contains unit tests to ensure the correctness of the encoder class.
"""

import unittest
from io import StringIO
import sys

class TestEncoder(unittest.TestCase):

    def test_encoder(self):
        """
        Test that the encoder can compress and decompress a sample time series.
        """
        from finance_quant_compressor.encoder import Encoder
        encoder = Encoder()
        data = [1, 2, 3, 4, 5]
        compressed_data = encoder.encode(data)
        decompressed_data = encoder.decode(compressed_data)
        self.assertEqual(decompressed_data, data)

    def test_encoder_ratio(self):
        """
        Test that the encoder's compression ratio is reasonable.
        """
        from finance_quant_compressor.encoder import Encoder
        encoder = Encoder()
        data = [1] * 1000
        compressed_data = encoder.encode(data)
        self.assertLess(len(compressed_data), len(data))

    def test_encoder_empty(self):
        """
        Test that the encoder can handle empty input.
        """
        from finance_quant_compressor.encoder import Encoder
        encoder = Encoder()
        data = []
        compressed_data = encoder.encode(data)
        decompressed_data = encoder.decode(compressed_data)
        self.assertEqual(decompressed_data, [])

    def test_encoder_invalid_input(self):
        """
        Test that the encoder raises an error for invalid input.
        """
        from finance_quant_compressor.encoder import Encoder
        encoder = Encoder()
        data = 'not a list'
        with self.assertRaises(TypeError):
            encoder.encode(data)

if __name__ == '__main__':
    unittest.main()
