import unittest

class MoveZeroesTest(unittest.TestCase):

    def test_zeroes_moved(self):
        self.assertEqual(self.move_zeroes([]), [])
        self.assertEqual(self.move_zeroes([0,1,5,9]), [1,5,9,0])
        self.assertEqual(self.move_zeroes([0,0,3,7,9,0]), [3,7,9,0,0,0])
        self.assertEqual(self.move_zeroes([1,5,0,9,2,0,5]), [1,5,9,2,5,0,0])
        self.assertEqual(self.move_zeroes([0,0,0]), [0,0,0])

    def move_zeroes(self, nums):
        non_zeroes = [n for n in nums if n != 0]
        return non_zeroes + [0] * (len(nums) - len(non_zeroes))

if __name__ == '__main__':
    unittest.main()
