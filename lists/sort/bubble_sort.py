import unittest

class BubbleSortTest(unittest.TestCase):

    def setUp(self):
        self.list = [8, 5, 9, 2, 4, 1, 7, 3, 10, 6]

    # Complexity: O(n*n)
    def test_bubble_sort(self):
        is_sorted = False
        while not is_sorted:
            is_sorted = True
            for i in range(1, len(self.list)):
                if self.list[i] < self.list[i - 1]:
                    self.swap_elements(i, i - 1)
                    is_sorted = False

    def tearDown(self):
        n = len(self.list)
        for i in range(1, n):
            self.assertGreater(self.list[i], self.list[i - 1])

    def swap_elements(self, i1, i2):
        self.list[i1], self.list[i2] = self.list[i2], self.list[i1]

if __name__ == '__main__':
    unittest.main()
