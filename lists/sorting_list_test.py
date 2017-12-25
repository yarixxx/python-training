import unittest

class SortingListTest(unittest.TestCase):

    def setUp(self):
        self.s_list = [8, 5, 9, 2, 4, 1, 7]

    # Complexity: O(n*n)
    def test_selection_sort(self):
        n = len(self.s_list)
        for i in range(0, n):
            min_index = -1
            for j in range(i, n):
                if self.s_list[j] < self.s_list[min_index]:
                    min_index = j
            if i != min_index:
                self.swap_elements(i, min_index)

    # Complexity: O(< n*n)
    def test_insertion_sort(self):
        n = len(self.s_list)
        for i in range(1, n):
            cursor1 = i
            cursor2 = i - 1
            while self.s_list[cursor1] < self.s_list[cursor2]:
                self.swap_elements(cursor1, cursor2)
                cursor1 = cursor1 - 1 if cursor1 > 0 else 0
                cursor2 = cursor2 - 1 if cursor2 > 0 else 0

    def tearDown(self):
        n = len(self.s_list)
        for index in range(1, n):
            self.assertLess(self.s_list[index - 1], self.s_list[index])

    def swap_elements(self, index1, index2):
        self.s_list[index1], self.s_list[index2] = self.s_list[index2], self.s_list[index1]

if __name__ == '__main__':
    unittest.main()
