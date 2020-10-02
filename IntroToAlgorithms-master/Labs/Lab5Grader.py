import unittest
from Lab5 import *


class Grader(unittest.TestCase):
    def test_sort_half(self):
        cases = [
            ([5, 2, 4, 7, 9, 3, 1, 6, 8], [2, 4, 5, 7, 9, 8, 6, 3, 1]),
            ([1, 2, 3, 4, 5, 6], [1, 2, 3, 6, 5, 4]),
            ([1], [1]),
            ([], []),
            ([1, 1], [1, 1]),
            ([1, 1, 2], [1, 2, 1]),
            ([5, 4, 6, 2, 1, 3, 8, -1], [2, 4, 5, 6, 8, 3, 1, -1])
        ]
        for i, (arg, expected) in enumerate(cases):
            with self.subTest(test=i):
                self.assertEqual(sort_half(arg), expected)

    def test_merge_two(self):
        cases = [
            ([1, 2, 3], [4, 5, 6], [1, 2, 3, 4, 5, 6]),
            ([1, 3, 5], [2, 4, 6], [1, 2, 3, 4, 5, 6]),
            ([1], [2, 3], [1, 2, 3]),
            ([2, 3], [1], [1, 2, 3]),
            ([], [1], [1]),
            ([2], [], [2]),
            ([], [], []),
            ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]),
        ]
        for i, (arg1, arg2, expected) in enumerate(cases):
            with self.subTest(test=i):
                self.assertEqual(merge_two(arg1, arg2), expected)

    def test_replace_negative(self):
        cases = [
            ([], []),
            ([1, 2, 3, -1], [1, 2, 3, 0]),
            ([2, 5, -1, 3, 7, -2, 8], [2, 5, 0, 3, 7, 0, 8]),
            ([1], [1]),
            ([-1], [0]),
            ([-1, -2, -3, -4, -5], [0, 0, 0, 0, 0]),
            ([1, 2, -3, 4, -5], [1, 2, 0, 4, 0]),
        ]
        for i, (arg, expected) in enumerate(cases):
            with self.subTest(test=i):
                self.assertEqual(replace_negative(arg), expected)