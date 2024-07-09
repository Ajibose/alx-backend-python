#!/usr/bin/env python3
"""Test Suite for client module"""
from client import GithubOrgClient, get_json
from parameterized import parameterized
from unittest.mock import patch, PropertyMock
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

    @patch.object(GithubOrgClient, 'org', new_callable=PropertyMock)
    def test_public_repos_url(self, mocked_org):
        """Test the _public_repos_url property"""
        payload = {
            "payload": True,
            "name": "mock",
            "repos_url": "https://github.com/Ajibose/alx-backend.git"
        }
        mocked_org.return_value = payload

        instance = GithubOrgClient("https://api.github.com/orgs/google")
        val = instance._public_repos_url
        self.assertEqual(val, payload["repos_url"])


if __name__ == '__main__':
    unittest.main()
