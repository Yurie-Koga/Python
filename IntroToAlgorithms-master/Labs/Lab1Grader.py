import unittest
from Labs.Lab1 import *


class Grader(unittest.TestCase):
    def test_hello_name(self):
        cases = [
            ("Bob", "Hello Bob!"),
            ("X", "Hello X!"),
            ("Derrick", "Hello Derrick!"),
            ("Alpha", "Hello Alpha!"),
            ("Van couver", "Hello Van couver!"),
            ("xyz!", "Hello xyz!!"),
        ]
        for i, (arg, expected) in enumerate(cases):
            with self.subTest(test=i):
                self.assertEqual(hello_name(arg), expected)

    def test_make_tags(self):
        cases = [
            ("i", "Yay", "<i>Yay</i>"),
            ("p", "Hello", "<p>Hello</p>"),
            ("img", "here", "<img>here</img>"),
            ("body", "Heart", "<body>Heart</body>"),
            ("h1", "", "<h1></h1>"),
            ("a", "a", "<a>a</a>"),
        ]
        for i, (arg1, arg2, expected) in enumerate(cases):
            with self.subTest(test=i):
                self.assertEqual(make_tags(arg1, arg2), expected)

    def test_first_two(self):
        cases = [
            ("Hello", "He"),
            ("abcdefg", "ab"),
            ("a bcd", "a "),
            ("a", "a"),
            ("", ""),
            ("hi", "hi"),
        ]
        for i, (arg, expected) in enumerate(cases):
            with self.subTest(test=i):
                self.assertEqual(first_two(arg), expected)

    def test_first_half(self):
        cases = [
            ("WooHoo", "Woo"),
            ("HelloThere", "Hello"),
            ("ab", "a"),
            ("", ""),
            ("0123456789", "01234"),
            ("abcd", "ab"),
        ]
        for i, (arg, expected) in enumerate(cases):
            with self.subTest(test=i):
                self.assertEqual(first_half(arg), expected)

    def test_without_end(self):
        cases = [
            ("Hello", "ell"),
            ("java", "av"),
            ("coding", "odin"),
            ("code", "od"),
            ("ab", ""),
            ("Yeah!", "eah"),
        ]
        for i, (arg, expected) in enumerate(cases):
            with self.subTest(test=i):
                self.assertEqual(without_end(arg), expected)

    def test_non_start(self):
        cases = [
            ("Hello", "There", "ellohere"),
            ("Python", "Code", "ythonode"),
            ("ab", "xy", "by"),
            ("ab", "x", "b"),
            ("x", "ac", "c"),
            ("a", "x", ""),
        ]
        for i, (arg1, arg2, expected) in enumerate(cases):
            with self.subTest(test=i):
                self.assertEqual(non_start(arg1, arg2), expected)

    def test_left2(self):
        cases = [
            ("Hello", "lloHe"),
            ("Hi", "Hi"),
            ("python", "thonpy"),
            ("cat", "tca"),
            ("12345", "34512"),
            ("bricks", "icksbr"),
        ]
        for i, (arg, expected) in enumerate(cases):
            with self.subTest(test=i):
                self.assertEqual(left2(arg), expected)


if __name__ == '__main__':
    unittest.main()
