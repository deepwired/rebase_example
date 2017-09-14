__author__ = 'deepsinghbaweja'
import unittest
from activecheck import find_between, get_active_three

class TestActiveCheck(unittest.TestCase):
    """
    basic unit tests for activecheck.py
    """

    def test_find_between(self):
        """
        unit tests for find_between function
        """
        s = "My name is Deep Singh Baweja"
        first = 's '
        last = ' B'
        actual = find_between(s, first, last)
        expected = "Deep Singh"
        self.assertEqual(actual, expected)

        s = "<Deep>: Hello world"
        first = '<'
        last = '>'
        actual = find_between(s, first, last)
        expected = "Deep"
        self.assertEqual(actual, expected)

        s = "<Deep>: <Singh>"
        first = '<'
        last = '>'
        actual = find_between(s, first, last)
        expected = "Deep"
        self.assertEqual(actual, expected)

        s = ""
        first = '<'
        last = '>'
        actual = find_between(s, first, last)
        expected = ""
        self.assertEqual(actual, expected)

    def test_get_active_three(self):
        """
        unit tests for get_active_three function
        """
        data = {'A': [2, 3], 'B': [4, 1], 'C': [1, 7], 'D': [2, 1]}
        actual = get_active_three(data)
        expected = ['B', 'C', 'D']
        self.assertEqual(actual, expected)

        data = {'A': [2, 3], 'B': [4, 1], 'C': [1, 20], 'D': [2, 17]}
        actual = get_active_three(data)
        expected = ['D', 'C', 'B']
        self.assertEqual(actual, expected)

        data = {'A': [1, 0], 'B': [4, 0], 'C': [2, 0], 'D': [7, 0]}
        actual = get_active_three(data)
        expected = ['D', 'B', 'C']
        self.assertEqual(actual, expected)

        data = {'A': [1, 0], 'B': [1, 0], 'C': [1, 0], 'D': [1, 0]}
        actual = get_active_three(data)
        expected = ['D', 'B', 'C']
        self.assertEqual(actual, expected)

        data = {'A': [5, 0], 'B': [4, 0], 'C': [4, 0], 'D': [1, 0]}
        actual = get_active_three(data)
        expected = ['A', 'B', 'C']
        self.assertEqual(actual, expected)

        data = {'A': [1, 0], 'B': [4, 0], 'C': [4, 0], 'D': [1, 0]}
        actual = get_active_three(data)
        expected = ['B', 'C', 'A']
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
