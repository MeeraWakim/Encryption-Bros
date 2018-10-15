import unittest
import piglatin

class TestStringMethods(unittest.TestCase):

    def test_encryption(self):
        self.assertEqual(piglatin.encrypt('ACL was great and ODESZA was amazing', 1), '')

    def test_decryption(self):
        self.assertEqual(piglatin.decrpyt('Next is Astroworld Fest', 1),'')

    def test_encryption(self):
        self.assertEqual(piglatin.encrypt('Texas Fight', 2), 'exasTay ightFay')

    def test_decryption(self):
        self.assertEqual(piglatin.decrypt('OUway ucksSay',2), 'OU Sucks')


if __name__ == '__main__':
    unittest.main()
