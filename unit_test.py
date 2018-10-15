import unittest
import morse_functions

class TestStringMethods(unittest.TestCase):
    def test_readfile(self):
        self.assertEqual(morse_functions.readFile('text.txt', ), ['This', 'is', 'a', 'text', 'file!\nI', 'hope', 'this', 'works.'])

    def test_encryption(self):
        self.assertEqual(morse_functions.encrypt(['This', 'is', 'a', 'text', 'file!', 'I', 'hope', 'this', 'works.'], 1), '- .... .. ...  .. ...  .-  - . -..- -  ..-. .. .-.. . (!)  ..  .... --- .--. .  - .... .. ...  .-- --- .-. -.- ... (.) ')

    def test_decryption(self):
        self.assertEqual(morse_functions.decrypt(['-', '....', '..', '...', '', '..', '...', '', '.-', '', '-', '.', '-..-', '-', '', '..-.', '..', '.-..', '.', '(!)', '', '..', '', '....', '---', '.--.', '.', '', '-', '....', '..', '...', '', '.--', '---', '.-.', '-.-', '...', '(.)', ''],1), 'THIS IS A TEXT FILE! I HOPE THIS WORKS. ')


if __name__ == '__main__':
    unittest.main()
