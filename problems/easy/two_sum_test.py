import unittest

class TwoSum(unittest.TestCase):

    def test_has_no_two_sum(self):
        self.assertFalse(self.has_two_sum([], 9))
        self.assertFalse(self.has_two_sum([2, 4, 7, 9, 2], 22))
        self.assertFalse(self.has_two_sum([2, 3, 9, 4, 7], 0))

    def test_has_two_sum(self):
        self.assertTrue(self.has_two_sum([3, 2, 6, 1, 9], 15))
        self.assertTrue(self.has_two_sum([6, 1, 5, -2, 2], 0))
        self.assertTrue(self.has_two_sum([1, 2, 4, 3, 7], 10))

    def has_two_sum(self, nums, target):
        for i, n in enumerate(nums):
            for m in nums[i:]:
                if target - n == m:
                    return True
        return False
        

if __name__ == '__main__':
    unittest.main()
