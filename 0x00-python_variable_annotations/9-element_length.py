#!/usr/bin/env python3
""" function that returns list of tuples"""

from typing import List, Tuple


def element_length(lst: List) -> List[Tuple[str, int]]:
    """function that returns list of tuples"""
    return [(i, len(i)) for i in lst]
