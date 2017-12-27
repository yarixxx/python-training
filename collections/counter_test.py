import unittest
from collections import Counter

class CounterTest(unittest.TestCase):

    def test_use_counter_with_list(self):
        my_list = [1,3,4,5,1,6,3,8,9,11]
        counter = Counter(my_list)
        self.assertEqual(2, counter[1])
        self.assertEqual(1, counter[11])
        self.assertEqual(0, counter[55])

    # Combine all values from both counters and sum
    def test_combine_count(self):
        counter1 = Counter([3,4,5,6,3])
        counter2 = Counter([4,5,7,9])
        sum_counter = counter1 + counter2
        self.assertEqual(2, sum_counter[4])
        self.assertEqual(1, sum_counter[6])
        self.assertEqual(0, sum_counter[8])

    # Take only what is unique
    def test_subtraction(self):
        counter1 = Counter([3,4,5,6])
        counter2 = Counter([4,5])
        sub_counter = counter1 - counter2
        self.assertEqual(1, sub_counter[3])
        self.assertEqual(0, sub_counter[5])

    # Take only what appears in both counters
    def test_intersection(self):
        counter1 = Counter([3,4,5,6,7])
        counter2 = Counter([3,4])
        inter_counter = counter1 & counter2
        self.assertEqual(1, inter_counter[3])
        self.assertEqual(0, inter_counter[6])

    # Take only maximum
    def test_union(self):
        counter1 = Counter([2,2,2,3,3,5,6])
        counter2 = Counter([2,3,5,5,6])
        union_counter = counter1 | counter2
        self.assertEqual(3, union_counter[2])
        self.assertEqual(2, union_counter[5])
        self.assertEqual(1, union_counter[6])

if __name__ == '__main__':
    unittest.main()
