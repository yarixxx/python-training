import unittest

class IntersectListTest(unittest.TestCase):

    def test_assert_intersection(self):
        self.assertEqual(self.intersection([], []), [])
        self.assertEqual(self.intersection([1,2,3], [2]), [2])
        self.assertEqual(self.intersection(['a', 'b', 'z', 't'], ['t', 'b', 'a','r']), ['a', 'b', 't'])
        self.assertEqual(self.intersection([], [5,7,8,9]), [])

    def intersection(self, list1, list2):
        return [e for e in list1 if e in list2]

if __name__ == '__main__':
    unittest.main()
