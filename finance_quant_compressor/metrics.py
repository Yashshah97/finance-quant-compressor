"""
Module for risk metric calculations and aggregation.

This module provides functions to calculate various risk metrics such as Value-at-Risk (VaR),
Conditional Value-at-Risk (CVaR), and Expected Shortfall (ES) for a given time series data.
"""

def var(data, confidence=0.95):
    """
    Calculate the Value-at-Risk (VaR) of a given time series data.

    Args:
        data (list): Time series data.
        confidence (float, optional): Confidence level. Defaults to 0.95.

    Returns:
        float: VaR value.
    """
    import numpy as np
    sorted_data = np.sort(data)
    index = int((1 - confidence) * len(sorted_data))
    return sorted_data[index]

def cva(data, confidence=0.95):
    """
    Calculate the Conditional Value-at-Risk (CVaR) of a given time series data.

    Args:
        data (list): Time series data.
        confidence (float, optional): Confidence level. Defaults to 0.95.

    Returns:
        float: CVaR value.
    """
    var_value = var(data, confidence)
    return np.mean([x for x in data if x > var_value])

def es(data, confidence=0.95):
    """
    Calculate the Expected Shortfall (ES) of a given time series data.

    Args:
        data (list): Time series data.
        confidence (float, optional): Confidence level. Defaults to 0.95.

    Returns:
        float: ES value.
    """
    return cva(data, confidence)

def aggregate_risk_metrics(data):
    """
    Aggregate risk metrics for a given time series data.

    Args:
        data (list): Time series data.

    Returns:
        dict: Aggregated risk metrics.
    """
    var_value = var(data)
    cvar_value = cva(data)
    es_value = es(data)
    return {
        'var': var_value,
        'cvar': cvar_value,
        'es': es_value
    }
