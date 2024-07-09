#!/usr/bin/env python3
"""
    Test suite for utils module
"""
import unittest
from unittest.mock import patch, MagicMock
import requests
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """Test cases for access_nested_map"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """TestCase for get_json"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        mock_get.return_value.json = MagicMock(return_value=test_payload)
        json_resp = get_json(test_url)
        mock_get.assert_called_once()
        self.assertEqual(json_resp, test_payload)


class TestMemoize(unittest.TestCase):
    """TestCase for utils.memoize decorator"""
    def test_memoize(self):
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as mocked_method:
            instance = TestClass()
            val = instance.a_property
            self.assertEqual(val, 42)
            instance.a_property
            self.assertEqual(val, 42)
            mocked_method.assert_called_once()


if __name__ == '__main__':
    unittest.main()
