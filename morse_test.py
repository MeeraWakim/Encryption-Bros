import unittest
import morse

class TestStringMethods(unittest.TestCase):

    def test_encryption(self):
        self.assertEqual(morse.encrypt('Texas Fight', 2), 'exasTay ightFay')

    def test_decryption(self):
        self.assertEqual(morse.decrypt('OUway ucksSay',2), 'OU Sucks')


if __name__ == '__main__':
    unittest.main()
