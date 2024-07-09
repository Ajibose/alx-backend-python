#!/usr/bin/env python3
"""Test Suite for client module"""
from client import GithubOrgClient, get_json
from parameterized import parameterized
from unittest.mock import patch
import unittest


class TestGithubOrgClient(unittest.TestCase):
    """TestCase for GithubOrgClient class"""
    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json')
    def test_org(self, name, mocked_func):
        """Test case for org method"""
        instance = GithubOrgClient(name)
        instance.org
        mocked_func.assert_called_once_with(
                f"https://api.github.com/orgs/{name}")


if __name__ == '__main__':
    unittest.main()
