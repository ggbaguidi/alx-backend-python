#!/usr/bin/env python3
""" unit test for utils package
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Test Class for Access nested map function
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Parameterize a unit test
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), ("a",)),
        ({"a": 1}, ("a", "b"), ("b",))
    ])
    def test_access_nested_map_exception(
        self,
        nested_map,
        path,
        expected_message
    ):
        """Parameterize a unit test with exception raised
        """
        with self.assertRaises(KeyError, msg='a') as cm:
            access_nested_map(nested_map, path)
        self.assertEqual(cm.exception.args, expected_message)


if __name__ == '__main__':
    unittest.main()
