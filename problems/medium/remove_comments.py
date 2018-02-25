import unittest

class RemoveCommentsTest(unittest.TestCase):

    def test_assert_remove_comments(self):
    	self.assertEqual(self.remove_comments('text /* asdf */ qwer'), 'text  qwer')
        self.assertEqual(self.remove_comments('before /* comment */ after /* comment 2 */ qwer'), 'before  after  qwer')
        self.assertEqual(self.remove_comments('qwer */ text /* comment */ text /* qwer'), ' text  text  qwer')

    def remove_comments(self, text):
        final_text = list()
        parts = text.split('/*')
        for i, part in enumerate(parts):
            subpart = part.split('*/')
            if len(subpart) == 2:
                final_text.append(subpart[1])
            if len(subpart) == 1:
                final_text.append(subpart[0])
        return ''.join(final_text)
                

if __name__ == '__main__':
    unittest.main()
