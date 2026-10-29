"""
Domain-tuned encoder for market time series and risk metrics.

This module provides a domain-specific encoder that leverages the characteristics of
financial time series to reduce dimensionality while preserving relevant information.
"""

from typing import Tuple
import math


def _log(x: float) -> float:
    """Compute natural logarithm, avoiding log(0)."""
    return 1e-10 if x == 0 else math.log(x)


class DomainTunedEncoder:
    """
    Domain-tuned encoder for market time series and risk metrics.

    Attributes:
        num_features (int): Number of features to encode.
        scale_factors (list[float]): Scale factors for each feature.
    """

    def __init__(self, num_features: int):
        self.num_features = num_features
        self.scale_factors = [1.0] * num_features

    def fit(self, X: list[list[float]]) -> None:
        """
        Fit the encoder to the given data.

        Args:
            X (list[list[float]]): Market time series or risk metrics.
        """
        for i in range(self.num_features):
            feature = [x[i] for x in X]
            self.scale_factors[i] = max(_log(max(feature)) - _log(min(feature)), 1e-10)

    def transform(self, X: list[list[float]]) -> list[list[float]]:
        """
        Apply the domain-tuned encoder to the given data.

        Args:
            X (list[list[float]]): Market time series or risk metrics.

        Returns:
            list[list[float]]: Encoded market time series or risk metrics.
        """
        encoded_X = []
        for x in X:
            encoded_x = [_log(x[i] / self.scale_factors[i]) for i in range(self.num_features)]
            encoded_X.append(encoded_x)
        return encoded_X


def encoder_ratio_benchmark(X: list[list[float]]) -> float:
    """
    Compute the ratio of variance explained by the domain-tuned encoder.

    Args:
        X (list[list[float]]): Market time series or risk metrics.

    Returns:
        float: Ratio of variance explained.
    """
    encoder = DomainTunedEncoder(len(X[0]))
    encoder.fit(X)
    encoded_X = encoder.transform(X)
    # Compute ratio of variance explained using the L2 norm
    ratio = sum(sum(x**2 for x in y) for y in X) / sum(sum(x**2 for x in y) for y in encoded_X)
    return 1 - (ratio / len(X[0]))
