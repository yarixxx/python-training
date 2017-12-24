import unittest

class SortingListTest(unittest.TestCase):

    def test_selection_sort(self):
	original_list = [8,4,9,2,5,3,1]
	n = len(original_list)
	for i in range(0, n):
	    min_index = -1
	    for j in range(i, n):
		if original_list[j] < original_list[min_index]:
		    min_index = j
	    if i != min_index:
		original_list[i], original_list[min_index] = original_list[min_index], original_list[i]
	
	for index in range(1, n): 
	    self.assertLess(original_list[index - 1], original_list[index])
	

if __name__ == '__main__':
    unittest.main()
