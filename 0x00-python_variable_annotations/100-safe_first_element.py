#!/usr/bin/env python3
"""function that returns the first element of iterable if it exists"""

from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Returns the first element of the iterable if it exists"""
    if lst:
        return lst[0]
    else:
        return None
