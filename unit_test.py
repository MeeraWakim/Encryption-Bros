import unittest

class TestStringMethods(unittest.TestCase):

    def test_encryption(self):
        self.assertEqual('AaBCdem', ['.-','.-','-...','-.-.','-..','.','--'])

    def test_decryption(self):
        self.assertEqual(['.-','.-','-...','-.-.','-..','.','--'], ['A','A','B','C','D','E','M'])


if __name__ == '__main__':
    unittest.main()
