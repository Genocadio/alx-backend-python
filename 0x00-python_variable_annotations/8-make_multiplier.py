#!/usr/bin/env python3
"""function to return a multiplier function"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """function to return a multiplier"""
    def mult(mul: float) -> float:
        """function to return a value square"""
        return multiplier * mul
    return mult
