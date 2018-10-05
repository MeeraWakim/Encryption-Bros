import unittest
import morse

class TestStringMethods(unittest.TestCase):

    def test_encryption(self):
        self.assertEqual(morse.encrypt('AaBCdem', 1), '.- .- -... -.-. -.. . --')

    #def test_decryption(self):
       # self.assertEqual(['.-','.-','-...','-.-.','-..','.','--'], ['A','A','B','C','D','E','M'])


if __name__ == '__main__':
    unittest.main()
