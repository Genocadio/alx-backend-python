#!/usr/bin/env python3
"""function that returns the first element of iterable if it exists"""

from typing import Iterable, Optional, Any


def safe_first_element(lst: Iterable[Any]) -> Optional[Any]:
    """Returns the first element of the iterable if it exists"""
    if lst:
        return next(iter(lst))
    return None
