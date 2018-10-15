import unittest
import morse_functions
import vig_cypher_functions

class TestStringMethods(unittest.TestCase):
    def test_readfile(self):
        self.assertEqual(morse_functions.readFile('text.txt', ), ['This', 'is', 'a', 'text', 'file!\nI', 'hope', 'this', 'works.'])

    def test_mores_encryption(self):
        self.assertEqual(morse_functions.encrypt(['This', 'is', 'a', 'text', 'file!', 'I', 'hope', 'this', 'works.'], 1), '- .... .. ...  .. ...  .-  - . -..- -  ..-. .. .-.. . (!)  ..  .... --- .--. .  - .... .. ...  .-- --- .-. -.- ... (.) ')

    def test_morse_decryption(self):
        self.assertEqual(morse_functions.decrypt(['-', '....', '..', '...', '', '..', '...', '', '.-', '', '-', '.', '-..-', '-', '', '..-.', '..', '.-..', '.', '(!)', '', '..', '', '....', '---', '.--.', '.', '', '-', '....', '..', '...', '', '.--', '---', '.-.', '-.-', '...', '(.)', ''],1), 'THIS IS A TEXT FILE! I HOPE THIS WORKS. ')

    def test_vig_encryption(self):
        self.assertEqual(vig_cypher_functions.vig_cypher('This is a text file!', 'a key', 'e'), 'V)uy:k4,g:v&%z:h*xk;')

    def test_vig_decryption(self):
        self.assertEqual(vig_cypher_functions.vig_cypher('V)uy:k4,g:v&%z:h*xk;', 'a key', 'd'), 'This is a text file!')


if __name__ == '__main__':
    unittest.main()
