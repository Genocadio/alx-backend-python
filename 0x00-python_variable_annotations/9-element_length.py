#!/usr/bin/env python3
""" function that returns list of tuples"""

from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """function that returns list of tuples"""
    return [(i, len(i)) for i in lst]
