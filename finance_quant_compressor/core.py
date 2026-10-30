"""
Finance Quant Compression Tool - Main Domain Logic and Public Entry Points.

This module contains the core functionality of the finance quant compression tool.
It defines a domain-tuned encoder with ratio benchmarks for compressing market time series and risk metrics.
"""

import math
from typing import List, Tuple

def encode_ratio_benchmark(time_series: List[float], benchmark_value: float) -> Tuple[List[int], float]:
    """
    Encode time series using a ratio-based benchmark.

    Args:
        time_series (List[float]): Time series to be encoded.
        benchmark_value (float): Benchmark value for encoding.

    Returns:
        Tuple[List[int], float]: Encoded time series and the compression ratio.
    """
    encoded_time_series = [math.floor(value / benchmark_value) for value in time_series]
    compression_ratio = sum(encoded_time_series) / len(time_series)
    return encoded_time_series, compression_ratio

def encode_domain_tuned(time_series: List[float], domain_tuned_params: Tuple[float, float]) -> Tuple[List[int], float]:
    """
    Encode time series using a domain-tuned encoder.

    Args:
        time_series (List[float]): Time series to be encoded.
        domain_tuned_params (Tuple[float, float]): Domain-tuned parameters for encoding.

    Returns:
        Tuple[List[int], float]: Encoded time series and the compression ratio.
    """
    min_value, max_value = domain_tuned_params
    encoded_time_series = [math.floor((value - min_value) / (max_value - min_value) * 255) for value in time_series]
    compression_ratio = sum(encoded_time_series) / len(time_series)
    return encoded_time_series, compression_ratio

def compress_market_data(market_data: List[List[float]]) -> Tuple[List[int], float]:
    """
    Compress market data using a ratio-based benchmark.

    Args:
        market_data (List[List[float]]): Market data to be compressed.

    Returns:
        Tuple[List[int], float]: Compressed market data and the compression ratio.
    """
    encoded_market_data = []
    for time_series in market_data:
        _, compression_ratio = encode_ratio_benchmark(time_series, 1.0)
        encoded_time_series, _ = encode_domain_tuned(time_series, (time_series[0], time_series[-1]))
        encoded_market_data.append(encoded_time_series)
    return encoded_market_data, compression_ratio
