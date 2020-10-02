import unittest
# from Labs.Lab3 import *    #this did not work on my lap
from Lab3 import *


# print(f"sys.path: {sys.path}")
print("Hellow")


class Grader(unittest.TestCase):
    def test_count_hi(self):
        cases = [
            ("abc hi ho", 1),
            ("ABChi hi", 2),
            ("hihi", 2),
            ("hiHIhi", 2),
            ("", 0),
            ("h", 0),
            ("hi", 1),
            ("Hi is no HI on ahI", 0),
            ("hiho not HOHIhi", 2),
        ]
        for i, (arg, expected) in enumerate(cases):
            with self.subTest(test=i):
                self.assertEqual(count_hi(arg), expected)

    def test_cat_dog(self):
        cases = [
            ("catdog", True),
            ("catcat", False),
            ("1cat1cadodog", True),
            ("catxxdogxxxdog", False),
            ("catxdogxdogxcat", True),
            ("catxdogxdogxca", False),
            ("dogdogcat", False),
            ("dogogcat", True),
            ("dog", False),
            ("cat", False),
            ("ca", True),
            ("c", True),
            ("", True),

        ]
        for i, (arg, expected) in enumerate(cases):
            with self.subTest(test=i):
                self.assertEqual(cat_dog(arg), expected)

    def test_count_code(self):
        cases = [
            ("aaacodebbb", 1),
            ("codexxcode", 2),
            ("cozexxcope", 2),
            ("cozfxxcope", 1),
            ("xxcozeyycop", 1),
            ("cozcop", 0),
            ("abcxyz", 0),
            ("code", 1),
            ("ode", 0),
            ("c", 0),
            ("", 0),
            ("AAcodeBBcoleCCccoreDD", 3),
            ("AAcodeBBcoleCCccorfDD", 2),
            ("coAcodeBcoleccoreDD", 3),
        ]
        for i, (arg, expected) in enumerate(cases):
            with self.subTest(test=i):
                self.assertEqual(count_code(arg), expected)

    def test_end_other(self):
        cases = [
            ('Hiabc', 'abc', True),
            ('AbC', 'HiaBc', True),
            ('abc', 'abXabc', True),
            ('Hiabc', 'abcd', False),
            ('Hiabc', 'bc', True),
            ('Hiabcx', 'bc', False),
            ('abc', 'abc', True),
            ('xyz', '12xyz', True),
            ('yz', '12xz', False),
            ('Z', '12xz', True),
            ('12', '12', True),
            ('abcXYZ', 'abcDEF', False),
            ('ab', 'ab12', False),
            ('ab', '12ab', True),
        ]
        for i, (arg1, arg2, expected) in enumerate(cases):
            with self.subTest(test=i):
                self.assertEqual(end_other(arg1, arg2), expected)

    def test_count_evens(self):
        cases = [
            ([2, 1, 2, 3, 4], 3),
            ([2, 2, 0], 3),
            ([1, 3, 5], 0),
            ([], 0),
            ([11, 9, 0, 1], 1),
            ([2, 11, 9, 0], 2),
            ([2], 1),
            ([2, 5, 12], 2),
        ]
        for i, (arg, expected) in enumerate(cases):
            with self.subTest(test=i):
                self.assertEqual(count_evens(arg), expected)

    def test_big_diff(self):
        cases = [
            ([10, 3, 5, 6], 7),
            ([7, 2, 10, 9], 8),
            ([2, 10, 7, 2], 8),
            ([2, 10], 8),
            ([10, 2], 8),
            ([10, 0], 10),
            ([2, 3], 1),
            ([2, 2], 0),
            ([2], 0),
            ([5, 1, 6, 1, 9, 9], 8),
            ([7, 6, 8, 5], 3),
            ([7, 7, 6, 8, 5, 5, 6], 3),
        ]
        for i, (arg, expected) in enumerate(cases):
            with self.subTest(test=i):
                self.assertEqual(big_diff(arg), expected)

    def test_sum13(self):
        cases = [
            ([1, 2, 2, 1], 6),
            ([1, 1], 2),
            ([1, 2, 2, 1, 13], 6),
            ([1, 2, 13, 2, 1, 13], 4),
            ([13, 1, 2, 13, 2, 1, 13], 3),
            ([], 0),
            ([13], 0),
            ([13, 13], 0),
            ([13, 0, 13], 0),
            ([13, 1, 13], 0),
            ([5, 7, 2], 14),
            ([5, 13, 2], 5),
            ([0], 0),
            ([13, 0], 0),
        ]
        for i, (arg, expected) in enumerate(cases):
            with self.subTest(test=i):
                self.assertEqual(sum13(arg), expected)

    def test_sum67(self):
        cases = [
            ([1, 2, 2], 5),
            ([1, 2, 2, 6, 99, 99, 7], 5),
            ([1, 1, 6, 7, 2], 4),
            ([1, 6, 2, 2, 7, 1, 6, 99, 99, 7], 2),
            ([1, 6, 2, 6, 2, 7, 1, 6, 99, 99, 7], 2),
            ([2, 7, 6, 2, 6, 7, 2, 7], 18),
            ([2, 7, 6, 2, 6, 2, 7], 9),
            ([1, 6, 7, 7], 8),
            ([6, 7, 1, 6, 7, 7], 8),
            ([6, 8, 1, 6, 7], 0),
            ([], 0),
            ([6, 7, 11], 11),
            ([11, 6, 7, 11], 22),
            ([2, 2, 6, 7, 7], 11),
        ]
        for i, (arg, expected) in enumerate(cases):
            with self.subTest(test=i):
                self.assertEqual(sum67(arg), expected)

    def test_has22(self):
        cases = [
            ([1, 2, 2], True),
            ([1, 2, 1, 2], False),
            ([2, 1, 2], False),
            ([2, 2, 1, 2], True),
            ([1, 3, 2], False),
            ([1, 3, 2, 2], True),
            ([2, 3, 2, 2], True),
            ([4, 2, 4, 2, 2, 5], True),
            ([1, 2], False),
            ([2, 2], True),
            ([2], False),
            ([], False),
            ([3, 3, 2, 2], True),
            ([5, 2, 5, 2], False),
        ]
        for i, (arg, expected) in enumerate(cases):
            with self.subTest(test=i):
                self.assertEqual(has22(arg), expected)
