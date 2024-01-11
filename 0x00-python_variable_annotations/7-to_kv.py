#!/usr/bin/env python3
"""function to return a tuple from str and number"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """function to return a tuple from str and number"""
    return (k, float(v ** 2))
