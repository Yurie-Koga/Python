import unittest
from recurPractice import *

class Grader(unittest.TestCase):
    def test_print_stars_loop(self):
        cases = [
            (3, "***"),
            (10, "**********"),
            (9, "*********"),
            (0, ""),
            (-1, ""),
            (7, "*******"),
        ]
        for i, (arg, expected) in enumerate(cases):
            with self.subTest(test=i):
                self.assertEqual(print_stars_loop(arg), expected)

    def test_print_stars_recur(self):
        cases = [
            (3, "***"),
            (10, "**********"),
            (9, "*********"),
            (0, ""),
            (-1, ""),
            (7, "*******"),
        ]
        for i, (arg, expected) in enumerate(cases):
            with self.subTest(test=i):
                self.assertEqual(print_stars_recur(arg), expected)