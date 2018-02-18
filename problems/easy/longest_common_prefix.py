import unittest

class LongestCommonPrefix(unittest.TestCase):

    def test_some_prefix(self):
        self.assertEqual(self.find_prefix(['asdf', 'asdr']), 'asd')
        self.assertEqual(self.find_prefix([]), '')
        self.assertEqual(self.find_prefix(['1234', '1435']), '1')
        self.assertEqual(self.find_prefix(['Hello', 'Help', 'Hem']), 'He')
    
    def find_prefix(self, strs):
        if len(strs) == 0:
            return ''
        if len(strs) == 1:
            return strs[0]        
        prefix = self.common_prefix(strs[0], strs[1])
        if (len(strs) == 2):
            return prefix
        for s in strs[1:]:
            prefix = self.common_prefix(prefix, s)
        return prefix
    
    def common_prefix(self, s1, s2):
        prefix = list()
        min_length = len(s1) if len(s1) < len(s2) else len(s2)
        for i in range(0, min_length):
            if s1[i] == s2[i]:
                prefix.append(s1[i])
            else:
                return ''.join(prefix)
        return ''.join(prefix)

if __name__ == '__main__':
    unittest.main()
