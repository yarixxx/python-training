import unittest

class ReverseWordsTest(unittest.TestCase):

    def test_reversed(self):
        self.assertEqual(self.reverse_words('What is this?'), 'this? is What')
        self.assertEqual(self.reverse_words(''), '')
        self.assertEqual(self.reverse_words('a b c'), 'c b a')

    def reverse_words(self, sentence):
        words = sentence.split()
        words.reverse()
        return ' '.join(words)

if __name__ == '__main__':
    unittest.main()
