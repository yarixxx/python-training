import unittest

class QuickSortTest(unittest.TestCase):

    def setUp(self):
        self.list = [8, 5, 9, 2, 4, 1, 7, 3, 10, 6, 22]

    def test_quick_sort(self):
        self.list = self.divide_and_swap(self.list)

    def divide_and_swap(self, elements):
        if not elements:
            return []
        left_list = []
        right_list = []
        pivot = elements.pop()
        while elements:
            element = elements.pop()
            if element > pivot:
                right_list.append(element)
            else:
                left_list.append(element)
        return self.divide_and_swap(left_list) + [pivot] + self.divide_and_swap(right_list)

    def tearDown(self):
        n = len(self.list)
        for index in range(1, n):
            self.assertLess(self.list[index - 1], self.list[index])

if __name__ == '__main__':
    unittest.main()
