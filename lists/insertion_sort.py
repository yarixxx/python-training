import unittest

class InsertionSortTest(unittest.TestCase):

    def setUp(self):
        self.list = [8, 5, 9, 2, 4, 1, 7, 3, 10, 6]

    # Complexity: O(< n*n)
    def test_insertion_sort(self):
        n = len(self.list)
        for i in range(1, n):
            cursor1, cursor2 = i, i - 1
            while self.list[cursor1] < self.list[cursor2]:
                self.swap_elements(cursor1, cursor2)
                cursor1 -= 1
                cursor2 = 0 if cursor2 < 1 else cursor2 - 1

    def tearDown(self):
        n = len(self.list)
        for index in range(1, n):
            self.assertLess(self.list[index - 1], self.list[index])

    def swap_elements(self, index1, index2):
        self.list[index1], self.list[index2] = self.list[index2], self.list[index1]

if __name__ == '__main__':
    unittest.main()
