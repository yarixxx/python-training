import unittest

class MyFirstTest(unittest.TestCase):

    def test_assert_something(self):
        self.assertEqual(1, 1)
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
