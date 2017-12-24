import unittest

class SortingListTest(unittest.TestCase):

    def test_selection_sort(self):
	s_list = [8,4,9,2,5,3,1]
	n = len(s_list)
	for i in range(0, n):
	    min_index = -1
	    for j in range(i, n):
		if s_list[j] < s_list[min_index]:
		    min_index = j
	    if i != min_index:
		s_list[i], s_list[min_index] = s_list[min_index], s_list[i]
	
	for index in range(1, n): 
	    self.assertLess(s_list[index - 1], s_list[index])
	

if __name__ == '__main__':
    unittest.main()
