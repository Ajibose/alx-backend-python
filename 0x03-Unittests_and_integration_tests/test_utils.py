#!/usr/bin/env python3
"""
    Test suite for access_nested_map of utils module
"""
import unittest
from utils import access_nested_map
#from parameterized import parameterized
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """Test cases for access_nested_map"""
    @parameterized.expand([
        {"nested_map": {"a": 1}, "path": ("a",)},
        {"nested_map": {"a": {"b": 2}}, "path": ("a",)},
        {"nested_map": {"a": {"b": 2}}, "path": ("a", "b")}
    ])
    def test_access_nested_map(self):
        assertEqual(access_nested_map(nested_map, path))


if __name__ ==' __main__':
    unittest.main()
