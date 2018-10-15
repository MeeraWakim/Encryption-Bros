import unittest
import piglatin

class TestStringMethods(unittest.TestCase):

    def test_encryption(self):
        self.assertEqual(piglatin.encrypt('ACL was great and ODESZA was amazing', 1), '3498 3606 4092 . 6414 5226 6198 . 5550 6144 5442 5226 6252 . 5226 5928 5388 . 4254 3660 3714 4470 4848 3498 . 6414 5226 6198 . 5226 5874 5226 6576 5658 5928 5550 ')

    def test_decryption(self):
        self.assertEqual(piglatin.decrpyt('4200 5442 6468 6252 . 5658 6198 . 3498 6198 6252 6144 5982 6414 5982 6144 5820 5388 . 3768 5442 6198 6252 . 6414 5658 6252 5604 . 4524 6144 5226 6360 5658 6198 . 4470 5334 5982 6252 6252 ', 1),'Next is Astroworld Fest with Travis Scott')

    def test_encryption(self):
        self.assertEqual(piglatin.encrypt('Texas Fight', 2), 'exasTay ightFay')

    def test_decryption(self):
        self.assertEqual(piglatin.decrypt('OUway ucksSay',2), 'OU Sucks')


if __name__ == '__main__':
    unittest.main()
