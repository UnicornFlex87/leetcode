import unittest
from snail import snail

class TestSnail(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(snail([]), [])

    def test_array_with_empty_inner_list(self):
        self.assertEqual(snail([[]]), [])

    def test_1x1_array(self):
        self.assertEqual(snail([[1]]), [1])

    def test_3x3_array(self):
        self.assertEqual(snail([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [1, 2, 3, 6, 9, 8, 7, 4, 5])

    def test_4x4_array(self):
        self.assertEqual(snail([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]), [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10])

    def test_2x2_array(self):
        self.assertEqual(snail([[1, 2], [3, 4]]), [1, 2, 4, 3])

if __name__ == '__main__':
    unittest.main()
