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

    @patch('client.get_json')
    @patch.object(
            GithubOrgClient, '_public_repos_url', new_callable=PropertyMock)
    def test_public_repos(self, mocked_prop, mocked_get_json):
        """Test case for public_repos method"""
        mocked_prop.return_value = "https://github.com/Ajibose/alx-backend.git"
        mocked_get_json.return_value = [
            {"name": "test"},
            {"name": "dart"}
        ]

        instance = GithubOrgClient("https://api.github.com/orgs/google")
        public_repos = instance.public_repos()
        self.assertEqual(["test", "dart"], public_repos)

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected_output):
        """Test case for has_license method"""
        res = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(res, expected_output)


if __name__ == '__main__':
    unittest.main()
