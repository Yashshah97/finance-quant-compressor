"""
Utility functions for finance quant data processing and compression.

This module contains utility functions used by the finance quant compressor.
"""

def is_increasing(data):
    """
    Check if a list of numbers is increasing.

    Args:
        data (list): A list of numbers.

    Returns:
        bool: True if the list is increasing, False otherwise.
    """
    return all(x <= y for x, y in zip(data, data[1:]))

def is_decreasing(data):
    """
    Check if a list of numbers is decreasing.

    Args:
        data (list): A list of numbers.

    Returns:
        bool: True if the list is decreasing, False otherwise.
    """
    return all(x >= y for x, y in zip(data, data[1:]))

def calculate_ratio(a, b):
    """
    Calculate the ratio of two lists.

    Args:
        a (list): The first list.
        b (list): The second list.

    Returns:
        float: The ratio of the two lists.
    """
    return sum(a) / sum(b)

def normalize_data(data, min_val=None, max_val=None):
    """
    Normalize data to a specified range.

    Args:
        data (list): The data to be normalized.
        min_val (float, optional): The minimum value. Defaults to 0.
        max_val (float, optional): The maximum value. Defaults to 1.

    Returns:
        list: The normalized data.
    """
    if min_val is None or max_val is None:
        raise ValueError("Both min_val and max_val must be specified")
    return [(x - min(data)) / (max(data) - min(data)) * (max_val - min_val) + min_val for x in data]

def calculate_percentile(data, percentile):
    """
    Calculate the percentile of a list.

    Args:
        data (list): The data to be calculated.
        percentile (float): The percentile to be calculated.

    Returns:
        float: The percentile of the data.
    """
    return np.percentile(data, percentile)
