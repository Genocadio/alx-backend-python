#!/usr/bin/env python3
"""gets a value from dictionary"""
from typing import Any, Mapping, Union, TypeVar


V = TypeVar('V')
Res = Union[Any, V]
Def = Union[V, None]


def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Res:
    """gets a value from dictionary"""
    if key in dct:
        return dct[key]
    else:
        return default
