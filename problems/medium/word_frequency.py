import unittest

class WordsFrequencyTest(unittest.TestCase):

    def test_word_frequency(self):
    	self.assertEqual(self.count_frequency('a b a c z b'), {'a':2,'b':2,'c':1,'z':1}) 
        self.assertEqual(self.count_frequency('hello test hi, hello bye say'), {'hello':2,'test':1, 'hi,':1, 'bye':1,'say':1})
        self.assertEqual(self.count_frequency(''), {})
        self.assertEqual(self.count_frequency('aloha'), {'aloha':1})

    def count_frequency(self, text):
        frequency = dict()
        words = text.split()
        for word in words:
            frequency[word] = frequency.get(word, 0) + 1 
        return frequency
            
        

if __name__ == '__main__':
    unittest.main()
