import unittest
from Lab6 import *


class Grader(unittest.TestCase):
    def test_is_prime(self):
        cases = [
            (1, False),
            (2, True),
            (67, True),
            (89, True),
            (100, False),
            (120, False),
            (157, True),
            (179, True),
        ]
        for i, (arg, expected) in enumerate(cases):
            with self.subTest(test=i):
                self.assertEqual(is_prime(arg), expected)

    def test_gcd(self):
        cases = [
            (24, 18, 6),
            (4, 14, 2),
            (48, 180, 12),
            (42, 56, 14),
            (9, 28, 1),
        ]
        for i, (arg1, arg2, expected) in enumerate(cases):
            with self.subTest(test=i):
                self.assertEqual(gcd(arg1, arg2), expected)

    def test_lcm(self):
        cases = [
            (24, 8, 24),
            (4, 14, 28),
            (48, 180, 720),
            (42, 56, 168),
            (9, 28, 252),
        ]
        for i, (arg1, arg2, expected) in enumerate(cases):
            with self.subTest(test=i):
                self.assertEqual(lcm(arg1, arg2), expected)

    def test_generate_primes(self):
        cases = [
            (100, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]),
            (50, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]),
        ]
        for i, (arg, expected) in enumerate(cases):
            with self.subTest(test=i):
                self.assertEqual(generate_primes(arg), expected)