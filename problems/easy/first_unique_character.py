import unittest

class FirstUniqueCharacterTest(unittest.TestCase):

    def test_assert_something(self):
        self.assertEqual(self.find_first_unique_character('aabcd'), 'b')
        self.assertEqual(self.find_first_unique_character('abcd'), 'a')
        self.assertEqual(self.find_first_unique_character('aabbdd'), None)

    def find_first_unique_character(self, text):
        frequencies = dict()
        for index, letter in enumerate(text):
            if letter not in text[index+1:] and not frequencies.get(letter):
                return letter
            else:
                frequencies[letter] = frequencies.get(letter, 0) + 1            
        return None
                
        

if __name__ == '__main__':
    unittest.main()
