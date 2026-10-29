"""
Ratio benchmarks and comparison functions.

This module provides ratio-based benchmarks for evaluating the effectiveness of
the finance quant compressor. It also includes functions for comparing compressed
values to their original values.
"""

def ratio(original, compressed):
    """
    Calculate the compression ratio between two values.

    Args:
        original (float): The original value.
        compressed (float): The compressed value.

    Returns:
        float: The compression ratio.
    """
    if original == 0:
        return float('inf')  # Avoid division by zero
    return abs(original) / abs(compressed)


def compare_ratio(original, compressed):
    """
    Compare the compression ratio to a threshold (1.05 by default).

    Args:
        original (float): The original value.
        compressed (float): The compressed value.

    Returns:
        bool: Whether the compression ratio is within the threshold.
    """
    return ratio(original, compressed) <= 1.05


def compare_ratio_percent_change(original, compressed):
    """
    Compare the percentage change in the compression ratio to a threshold (-5% by default).

    Args:
        original (float): The original value.
        compressed (float): The compressed value.

    Returns:
        bool: Whether the percentage change is within the threshold.
    """
    if original == 0 or abs(compressed) < 1e-6:  # Avoid division by zero
        return True
    return ((ratio(original, compressed) - 1) / ratio(original, compressed)) * 100 <= -5


# Example usage:
if __name__ == "__main__":
    original_value = 10.0
    compressed_value = 9.99

    print(ratio(original_value, compressed_value))
    print(compare_ratio(original_value, compressed_value))
    print(compare_ratio_percent_change(original_value, compressed_value))
