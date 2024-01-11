#!/usr/bin/env python3
"""gets a value from dictionary"""
from typing import Any, Mapping, Union, TypeVar


V = TypeVar('V')
ret = Union[Any, V]
args = Union[V, None]


def safely_get_value(dct: Mapping, key: Any, default: args = None) -> ret:
    """gets a value from dictionary"""
    if key in dct:
        return dct[key]
    else:
        return default