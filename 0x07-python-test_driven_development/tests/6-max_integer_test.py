#!/usr/bin/python3
"""
    Unitest module for the max_integer function
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInt(unittest.TestCase):
    """
        A class that runs all the unit teste cases\
        for the function max_integer
    """

    def test_with_ints(self):
        """ Tests case for list with a set of regular integers\
        and returns the max number."""
        lis_t = [1, 2, 3, 4, 5]
        max_num = max_integer(lis_t)
        self.assertEqual(max_num, 5)

    def test_with_letters(self):
        """ Tests case for list with some letters\n
        and returns Error"""
        lis_t = [1, 2, 'a', 4, 5]
        self.assertRaises(TypeError, max_integer, lis_t)

    def test_with_floats(self):
        """ Tests case for list with floats."""
        lis_t = [1.1, 2.4, 3, 5]
        max_num = max_integer(lis_t)
        self.assertEqual(max_num, 5)

    def test_with_negative(self):
        """Test case for negative numbers."""
        lis_t = [-1, -2, -3, -7]
        max_num = max_integer(lis_t)
        self.assertEqual(max_num, -1)

    def test_with_empty(self):
        """Test case for list that is empty"""
        lis_t = []
        max_num = max_integer(lis_t)
        self.assertEqual(max_num, None)

    def test_with_none(self):
        """Test case for no parameter passed and\
        raise a TypeError"""
        self.assertRaises(TypeError, max_integer, None)

    def test_with_not_list(self):
        """Test case for a parameter passed not as a list"""
        lis_t = 1
        self.assertRaises(TypeError, max_integer, lis_t)

    def test_with_identical(self):
        """ Test case for elements with identical elements\
        returns one of the elements."""
        lis_t = [3, 3, 3, 3, 3, 3]
        max_num = max_integer(lis_t)
        self.assertEqual(max_num, 3)

    def test_with_one_elem(self):
        """Test case for one element list"""
        lis_t = [12]
        max_num = max_integer(lis_t)
        self.assertEqual(max_num, 12)


if __name__ == '__main__':
    unittest.main()
