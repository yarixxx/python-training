import unittest

class SimpleListTest(unittest.TestCase):

    def setUp(self):
        self.raw_numbers_list = [3, 2, 5]
        self.obj_strings_list = list(['cat', 'dog', 'mouse'])
	self.hetero_list = ['a', 1, True]

    def test_list_item_by_index(self):
        self.assertEqual(self.raw_numbers_list[0], 3)
	self.assertEqual(self.obj_strings_list[0], 'cat')

    def test_list_length(self):
	self.assertEqual(len(self.raw_numbers_list), 3)

    def test_hetero_list(self):
	self.assertEqual(self.hetero_list[0], 'a')
	self.assertEqual(self.hetero_list[1], 1)
	self.assertTrue(self.hetero_list[2])

    def test_for_in_list(self):
	for s in self.obj_strings_list:
	    self.assertNotEqual(s, 'b')

    def test_range(self):
	r = range(1, 4)
	self.assertEqual(len(r), 3)	


if __name__ == '__main__':
    unittest.main()
