#!/usr/bin/env python3
'''unitest file'''
import unittest
from parameterized import parameterized
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
    Callable,
    Tuple,
    Union,
)
from utils import (
    access_nested_map,
    get_json,
    memoize,
)


class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
        self,
        nested_map: Dict,
        path: Tuple[str],
        expected: Union[Dict, int]
    ) -> None:
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(
        self,
        nested_map: Dict,
        path: Tuple[str],
        exception: Exception,
    ) -> None:
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)

class TestGetJson(unittest.TestCase):
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(
        self,
        test_url: str,
        test_payload: Dict,
    ) -> None:
        with unittest.mock.patch('requests.get') as mock_request:
            mock_request.return_value.json.return_value = test_payload
            self.assertEqual(get_json(test_url), test_payload)
            mock_request.assert_called_once_with(test_url)
            mock_request.return_value.json.assert_called_once_with()
            mock_request.return_value.raise_for_status.assert_not_called()
            mock_request.return_value.raise_for_status.assert_called_once_with()
            mock_request.return_value.close.assert_not_called()
            mock_request.return_value.close.assert_called_once_with()
