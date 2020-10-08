import unittest
from final_version3 import *


class FinalGrader(unittest.TestCase):
    def test_is_anagram(self):
        cases = [
            ("anagram", "nagaram", True),
            ("rat", "car", False),
            ("listen", "silent", True),
            ("carr", "car", False),
            ("", "", True),
            ("h", "e", False),
        ]
        for i, (arg1, arg2, expected) in enumerate(cases):
            with self.subTest(test=i):
                self.assertEqual(is_anagram(arg1, arg2), expected)

    def test_remove_vowels(self):
        cases = [
            ("hello", "hll"),
            ("world", "wrld"),
            ("what", "wht"),
            ("", ""),
            ("a", ""),
        ]
        for i, (arg, expected) in enumerate(cases):
            with self.subTest(test=i):
                self.assertEqual(remove_vowels(arg), expected)

