import unittest

class MergeSortTest(unittest.TestCase):

    def setUp(self):
        self.list = [8, 5, 9, 2, 4, 1, 7, 10, 6]

    # Complexity: O(log(n * log(n)))
    def test_merge_sort(self):
        n = len(self.list)
        self.list = self.merge_two_lists(self.list[:n/2], self.list[n/2:])

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
        n = len(self.list)
        for index in range(1, n):
            self.assertLess(self.list[index - 1], self.list[index])

if __name__ == '__main__':
    unittest.main()
