import unittest

class SlicingListTest(unittest.TestCase):

    def setUp(self):
	self.hetero_list = range(0,5)

    def test_sub_list(self):
	self.assertEqual(len(self.hetero_list), 5)
	sub_list = self.hetero_list[2:4]
	self.assertEqual(len(sub_list), 2)
	self.assertEqual(sub_list[0], 2)
	self.assertEqual(sub_list[1], 3)

    def test_sub_list_without_start(self):
	sub_list = self.hetero_list[:4]
	self.assertEqual(len(sub_list), 4)
	self.assertEqual(sub_list[0], 0)
	self.assertEqual(sub_list[3], 3)

    def test_sub_list_withou_end(self):
	sub_list = self.hetero_list[2:]
	self.assertEqual(len(sub_list), 3)
	self.assertEqual(sub_list[0], 2)

    def test_replace_slice_and_insert(self):
	self.hetero_list[2:4] = [9,4,7]
	self.assertEqual(self.hetero_list[2], 9)
	self.assertEqual(self.hetero_list[3], 4)
	self.assertEqual(self.hetero_list[0], 0)
	self.assertEqual(len(self.hetero_list), 6)

    def test_sub_list_negative(self):
	sub_list = self.hetero_list[-1:-3]
	print(sub_list)

if __name__ == '__main__':
    unittest.main()
