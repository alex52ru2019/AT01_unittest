import unittest
from dz_main import *

class TestDz(unittest.TestCase):
    def test_ost(self):
        self.assertEqual(ost(4, 2), 0)
        self.assertEqual(ost(20, 6), 2)
        self.assertEqual(ost(6, 5), 1)
        self.assertEqual(ost(21, 6), 3)

    def test_ost_zero(self):
        self.assertRaises(ValueError, ost, 4, 0)


if __name__ == '__main__':
    unittest.main()