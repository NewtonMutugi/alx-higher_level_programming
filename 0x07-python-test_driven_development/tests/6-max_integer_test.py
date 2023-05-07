"""
unit test that tests module max_integer
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    class that inherits from unittest.TestCase
    """

    def test_max_integer(self):
        """tests max_integer function"""

        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 2, 4, 3]), 4)
        self.assertEqual(max_integer([4, 2, 3, 1]), 4)
        self.assertEqual(max_integer([4]), 4)
        self.assertEqual(max_integer([1, 2, 3, 4, 3, 2, 1]), 4)

    def test_empty_list(self):
        """tests empty list"""

        self.assertEqual(max_integer([]), None)

    def test_no_args(self):
        """tests no arguments"""

        self.assertEqual(max_integer(), None)

    def test_one_arg(self):
        """tests one argument"""

        self.assertEqual(max_integer([1]), 1)

    def test_floats(self):
        """tests floats"""

        self.assertEqual(max_integer([1.2, 1.3, 1.4]), 1.4)

    def test_strings(self):
        """tests strings"""

        self.assertEqual(max_integer(["a", "b", "c"]), "c")

    def test_mixed(self):
        """tests mixed types"""

        with self.assertRaises(TypeError):
            max_integer([1, "a", 2])

    def test_none(self):
        """tests None"""

        with self.assertRaises(TypeError):
            max_integer(None)

    def test_inf(self):
        """tests inf"""

        self.assertEqual(max_integer([float('inf'), 1]), float('inf'))

    def test_neg_inf(self):
        """tests -inf"""

        self.assertEqual(max_integer([float('-inf'), 1]), 1)

    def test_nan(self):
        """tests nan"""

        self.assertNotEqual(max_integer([float('nan'), 1]), 1)

    def test_dict(self):
        """tests dict"""

        with self.assertRaises(KeyError):
            max_integer({1: "a", 2: "b"})

    def test_tuple(self):
        """tests tuple"""

        self.assertEqual(max_integer((1, 2, 3)), 3)

    # def test_set(self):
    #    """tests set"""

    #    self.assertEqual(max_integer({1, 2, 3}), 3)

    def test_list_of_lists(self):
        """tests list of lists"""

        self.assertEqual(max_integer([[1, 2], [3, 4]]), [3, 4])

    def test_list_of_tuples(self):
        """tests list of tuples"""

        self.assertEqual(max_integer([(1, 2), (3, 4)]), (3, 4))

    # def test_list_of_sets(self):
    #    """tests list of sets"""

    #   self.assertEqual(max_integer([{1, 2}, {3, 4}]), {3, 4})

    def test_list_of_dicts(self):
        """tests list of dicts"""

        with self.assertRaises(TypeError):
            max_integer([{1: "a"}, {2: "b"}])

    def test_list_of_strings(self):
        """tests list of strings"""

        self.assertEqual(max_integer(["abc", "def"]), "def")

    def test_list_of_floats(self):
        """tests list of floats"""

        self.assertEqual(max_integer([1.2, 1.3, 1.4]), 1.4)

    def test_list_of_mixed(self):
        """tests list of mixed types"""

        with self.assertRaises(TypeError):
            max_integer([1, "a", 2])

    def test_list_of_none(self):
        """tests list of None"""

        with self.assertRaises(TypeError):
            max_integer([None, 1])

    def test_list_of_inf(self):
        """tests list of inf"""

        self.assertEqual(max_integer([float('inf'), 1]), float('inf'))

    def test_list_of_neg_inf(self):
        """tests list of -inf"""

        self.assertEqual(max_integer([float('-inf'), 1]), 1)

    def test_list_of_nan(self):
        """tests list of nan"""

        self.assertNotEqual(max_integer([float('nan'), 1]), 1)

    def test_list_of_list_of_lists(self):
        """tests list of list of lists"""

        self.assertEqual(max_integer([[[1, 2], [3, 4]], [[5, 6], [7, 8]]]),
                         [[5, 6], [7, 8]])


if __name__ == '__main__':
    unittest.main()
