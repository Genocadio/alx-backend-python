#!/usr/bin/env python3
""" function to return sum of mixed list with annotations"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """_function to sum a list of numbers"""
    return sum(mxd_lst)
