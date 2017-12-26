import unittest

class SortingListTest(unittest.TestCase):

    def setUp(self):
        self.list = [8, 5, 9, 2, 4, 1, 7, 3, 10, 6]

    # Complexity: O(n*n)
    def test_selection_sort(self):
        n = len(self.list)
        for i in range(0, n):
            min_index = -1
            for j in range(i, n):
                if self.list[j] < self.list[min_index]:
                    min_index = j
            if i != min_index:
                self.swap_elements(i, min_index)

    def tearDown(self):
        n = len(self.list)
        for index in range(1, n):
            self.assertLess(self.list[index - 1], self.list[index])

    def swap_elements(self, index1, index2):
        self.list[index1], self.list[index2] = self.list[index2], self.list[index1]

if __name__ == '__main__':
    unittest.main()
