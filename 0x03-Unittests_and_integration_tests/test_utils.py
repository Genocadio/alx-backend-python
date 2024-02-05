#!/usr/bin/env python3
'''unitest file'''
import unittest
from parameterized import parameterized
from unittest.mock import Mock, patch
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
        atrbs = {'json.return_value': test_payload}
        with patch("requests.get", return_value=Mock(**atrbs)) as req_get:
            self.assertEqual(get_json(test_url), test_payload)
            req_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    def test_memoize(self) -> None:
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as mock:
            test = TestClass()
            self.assertEqual(test.a_property, 42)
            self.assertEqual(test.a_property, 42)
            mock.assert_called_once()
            mock.reset_mock()
            test.a_property = 98
            self.assertEqual(test.a_property, 98)
            mock.assert_not_called()
            mock.reset_mock()
            test.a_method = 98
            self.assertEqual(test.a_method, 98)
            mock.assert_not_called()
