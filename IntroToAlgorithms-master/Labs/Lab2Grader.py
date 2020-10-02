import unittest
#from Labs.Lab2 import *
from Lab2Sol import *

class Grader(unittest.TestCase):
    def test_first_last6(self):
        cases = [
            ([1, 2, 6], True),
            ([6, 1, 2, 3], True),
            ([13, 6, 1, 2, 3], False),
            ([3, 2, 1], False),
            ([6], True),
            ([3], False),
            ([5, 6], True),
            ([5, 5], False),
        ]
        for i, (arg, expected) in enumerate(cases):
            with self.subTest(test=i):
                self.assertEqual(first_last6(arg), expected)

    def test_same_first_last(self):
        cases = [
            ([1, 2, 3], False),
            ([1, 2, 3, 1], True),
            ([7], True),
            ([], False),
            ([7, 7], True),
            ([1, 2, 3, 4, 5, 1], True),
            ([1, 2, 3, 4, 5, 13], False),
        ]
        for i, (arg, expected) in enumerate(cases):
            with self.subTest(test=i):
                self.assertEqual(same_first_last(arg), expected)

    def test_common_end(self):
        cases = [
            ([1, 2, 3], [7, 3], True),
            ([1, 2, 3], [7, 3, 2], False),
            ([1, 2, 3], [1, 3], True),
            ([1, 2, 3], [1], True),
            ([1, 2, 3], [2], False),
        ]
        for i, (arg1, arg2, expected) in enumerate(cases):
            with self.subTest(test=i):
                self.assertEqual(common_end(arg1, arg2), expected)

    def test_sum3(self):
        cases = [
            ([1, 2, 3], 6),
            ([5, 11, 2], 18),
            ([7, 0, 0], 7),
            ([1, 2, 1], 4),
            ([1, 1, 1], 3),
            ([2, 7, 2], 11),
        ]
        for i, (arg, expected) in enumerate(cases):
            with self.subTest(test=i):
                self.assertEqual(sum3(arg), expected)

    def test_rotate_left3(self):
        cases = [
            ([1, 2, 3], [2, 3, 1]),
            ([5, 11, 9], [11, 9, 5]),
            ([7, 0, 0], [0, 0, 7]),
            ([1, 2, 1], [2, 1, 1]),
            ([0, 0, 1], [0, 1, 0]),
        ]
        for i, (arg, expected) in enumerate(cases):
            with self.subTest(test=i):
                self.assertEqual(rotate_left3(arg), expected)

    def test_reverse3(self):
        cases = [
            ([1, 2, 3], [3, 2, 1]),
            ([7, 0, 0], [0, 0, 7]),
            ([2, 1, 2], [2, 1, 2]),
            ([2, 11, 3], [3, 11, 2]),
            ([0, 6, 5], [5, 6, 0]),
            ([7, 2, 3], [3, 2, 7]),
        ]
        for i, (arg, expected) in enumerate(cases):
            with self.subTest(test=i):
                self.assertEqual(reverse3(arg), expected)

    def test_max_ends3(self):
        cases = [
            ([1, 2, 3], [3, 3, 3]),
            ([11, 5, 9], [11, 11, 11]),
            ([2, 11, 3], [3, 3, 3]),
            ([3, 11, 11], [11, 11, 11]),
            ([2, 11, 2], [2, 2, 2]),
            ([0, 0, 1], [1, 1, 1]),
        ]
        for i, (arg, expected) in enumerate(cases):
            with self.subTest(test=i):
                self.assertEqual(max_ends3(arg), expected)

    def test_make_ends(self):
        cases = [
            ([1, 2, 3], [1, 3]),
            ([1, 2, 3, 4], [1, 4]),
            ([1, 2, 2, 2, 2, 2, 2, 3], [1, 3]),
            ([7, 4], [7, 4]),
            ([7], [7, 7]),
            ([5, 2, 9], [5, 9]),
            ([2, 3, 4, 1], [2, 1]),
        ]
        for i, (arg, expected) in enumerate(cases):
            with self.subTest(test=i):
                self.assertEqual(make_ends(arg), expected)

    def test_has23(self):
        cases = [
            ([2, 5], True),
            ([5, 2], True),
            ([2, 3], True),
            ([4, 3], True),
            ([4, 5], False),
            ([3, 3], True),
            ([7, 7], False),
        ]
        for i, (arg, expected) in enumerate(cases):
            with self.subTest(test=i):
                self.assertEqual(has23(arg), expected)


if __name__ == '__main__':
    unittest.main()
