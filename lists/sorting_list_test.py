import unittest

class SortingListTest(unittest.TestCase):

    def setUp(self):
        self.s_list = [8, 5, 9, 2, 4, 1, 7, 3, 10, 6]

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
            cursor1, cursor2 = i, i - 1
            while self.s_list[cursor1] < self.s_list[cursor2]:
                self.swap_elements(cursor1, cursor2)
                cursor1 -= 1
                cursor2 = 0 if cursor2 < 1 else cursor2 - 1

    # Complexity: O(log(n * log(n)))
    def test_merge_sort(self):
        n = len(self.s_list)
        self.s_list = self.merge_two_lists(self.s_list[:n/2], self.s_list[n/2:])

    def merge_two_lists(self, left_list, right_list):
        merged_list = []
        if left_list and right_list:
            left_n = len(left_list)
            right_n = len(right_list)
            new_left_list = self.merge_two_lists(left_list[:left_n/2], left_list[left_n/2:])
            new_right_list = self.merge_two_lists(right_list[:right_n/2], right_list[right_n/2:])
            while new_left_list and new_right_list:
                if new_right_list[0] < new_left_list[0]:
                    merged_list.append(new_right_list.pop(0))
                else:
                    merged_list.append(new_left_list.pop(0))
            merged_list += new_left_list
            merged_list += new_right_list
        else:
            merged_list += left_list
            merged_list += right_list
        return merged_list

    def tearDown(self):
        n = len(self.s_list)
        for index in range(1, n):
            self.assertLess(self.s_list[index - 1], self.s_list[index])

    def swap_elements(self, index1, index2):
        self.s_list[index1], self.s_list[index2] = self.s_list[index2], self.s_list[index1]

if __name__ == '__main__':
    unittest.main()
