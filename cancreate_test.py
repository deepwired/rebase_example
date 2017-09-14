__author__ = 'deepsinghbaweja'
import unittest
from cancreate import can_create, check_if_word_is_formed

class TestCanCreate(unittest.TestCase):
    """
    basic unit tests for cancreate.py
    """
    def test_can_create(self):
        """
        unit tests for can_create function
        """
        dataStrings = ['back', 'end', 'front', 'tree', 'sparta']
        stringToCheck = 'back'
        actual = can_create(dataStrings, stringToCheck)
        self.assertTrue(actual)

        dataStrings = ['back', 'end', 'front', 'tree', 'sparta']
        stringToCheck = 'backend'
        actual = can_create(dataStrings, stringToCheck)
        self.assertTrue(actual)

        dataStrings = ['back', 'end', 'front', 'tree', 'sparta']
        stringToCheck = 'backendtree'
        actual = can_create(dataStrings, stringToCheck)
        self.assertTrue(actual)

        dataStrings = ['back', 'end', 'front', 'tree', 'sparta']
        stringToCheck = 'spartaback'
        actual = can_create(dataStrings, stringToCheck)
        self.assertTrue(actual)

        dataStrings = ['back', 'end', 'front', 'tree', 'sparta']
        stringToCheck = ''
        actual = can_create(dataStrings, stringToCheck)
        self.assertFalse(actual)

    def test_check_if_word_is_formed(self):
        """
        unit tests for check_if_word_is_formed function
        """
        others = [[4, 6]]
        inputLen = 6
        nextStart = 4
        actual = check_if_word_is_formed(others, inputLen, nextStart)
        self.assertTrue(actual)

        others = [[10, 14], [0, 9]]
        inputLen = 14
        nextStart = 0
        actual = check_if_word_is_formed(others, inputLen, nextStart)
        self.assertTrue(actual)

if __name__ == '__main__':
    unittest.main()
