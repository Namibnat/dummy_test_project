import unittest
import main


class TestThis(unittest.TestCase):
    def test_this(self):
        self.assertEqual(1, 1)

    def test_random_number(self):
        self.assertGreaterEqual(main.gen_number(), 1)
        self.assertLess(main.gen_number(), 100)
