import unittest

import main


class Basic(unittest.TestCase):

    def test_add(self):
        self.assertEqual(main.add(1, 2), 3)

    def test_add_str(self):
        self.assertEqual(main.add("a", "b"), "ab")

    def test_add_fixed(self):
        self.assertEqual(main.add("a", ""), "a")


