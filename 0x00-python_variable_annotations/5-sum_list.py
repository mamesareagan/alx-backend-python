#!/usr/bin/env python3
"""sumation of floats"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """gets the sum of floats in a list

    Args:
        input_list (list[float]): list of floats

    Returns:
        float: sum
    """
    if input_list is None:
        return 0
    else:
        return sum(input_list)
