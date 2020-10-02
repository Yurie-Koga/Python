import unittest
from Lab7 import *


class Grader(unittest.TestCase):
    def test_is_palindrome(self):
        cases = [
            ("", True),  # empty string
            ("a", True),  # single char
            ("aa", True),  # 2 chars, palindrome
            ("ab", False),  # 2 chars, not palindrome
            ("aba", True),  # 3 chars, palindrome
            ("abc", False),  # 3 chars, not palindrome
            ("redder", True),  # longer, even, palindrome
            ("renter", False),  # longer, even, not palindrome
            ("racecar", True),  # longer, odd, palindrome
            ("banana", False),  # longer, odd, not palindrome
        ]
        for i, (arg, expected) in enumerate(cases):
            with self.subTest(test=i):
                self.assertEqual(is_palindrome(arg), expected)