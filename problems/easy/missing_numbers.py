import unittest

class MissingNumbersTest(unittest.TestCase):

    def test_assert_something(self):
        self.assertEqual(self.find_missing_numbers(5, [5,4,3,2]), [1])
        self.assertEqual(self.find_missing_numbers(3, [2,1]), [])
        self.assertEqual(self.find_missing_numbers(7, [5,4,2,1]), [3,6])

    def find_missing_numbers(self, number, list_of_numbers):
        numbers = range(1, number)
        result_numbers = list()
        for n in numbers:
           if n not in list_of_numbers:
                result_numbers.append(n) 
        return result_numbers

if __name__ == '__main__':
    unittest.main()
