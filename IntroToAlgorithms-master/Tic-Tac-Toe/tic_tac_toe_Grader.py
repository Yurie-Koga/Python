import unittest
from tic_tac_toe import *


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
                self.assertEqual(default_def(arg), expected)