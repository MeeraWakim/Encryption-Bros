import unittest

def readFile (filename):

	# filename passed as a string from main
	# open file for reading
	# readfile into script
	x = 1

	return(text)


def encrypt (text, encryptionMethod):

	# text read in from file passed in
	# int passed in that specifies which encryption method

	if (encryptionMethod == 1):
		# do morse code encryption
		# use a dictionary to map letters to dots/dashes?
		morseDict = {'A': '.-',     'B': '-...',   'C': '-.-.',
    	'D': '-..',    'E': '.',      'F': '..-.',
    	'G': '--.',    'H': '....',   'I': '..',
    	'J': '.---',   'K': '-.-',    'L': '.-..',
    	'M': '--',     'N': '-.',     'O': '---',
    	'P': '.--.',   'Q': '--.-',   'R': '.-.',
    	'S': '...',    'T': '-',      'U': '..-',
    	'V': '...-',   'W': '.--',    'X': '-..-',
    	'Y': '-.--',   'Z': '--..',

    	'0': '-----',  '1': '.----',  '2': '..---',
    	'3': '...--',  '4': '....-',  '5': '.....',
    	'6': '-....',  '7': '--...',  '8': '---..',
    	'9': '----.'
    	}

		encryptedTextList = []

		for char in text:
			if (char.upper() in morseDict.keys()):
				encryptedTextList.append(morseDict[char.upper()])

		encryptedText = ' '.join(encryptedTextList)

	elif (encryptionMethod == 2):
		# do other method encryption
		x = 1

	return(encryptedText)

def decrypt (text, decryptionMethod):

	# text read in from file passed in
	# int passed in that specifies which decryption method

	morseList = text.split(' ')
	print(morseList)

	if (decryptionMethod == 1):
		# do morse code decryption
		# use a dictionary to map letters to dots/dashes?
		englishDict = {'.-': 'A',   '-...': 'B',   '-.-.': 'C',
		'-..': 'D',      '.': 'E',   '..-.': 'F',
		'-.': 'G',   '....': 'H',     '..': 'I',  
		'.---': 'J',    '-.-': 'K',   '.-..': 'L',
		'--': 'M',     '-.': 'N',    '---': 'O', 
		'.--.': 'P',   '--.-': 'Q',    '.-.': 'R',
		'...': 'S',      '-': 'T',    '..-': 'U', 
		'...-': 'V',    '.--': 'W',   '-..-': 'X',
		'-.--': 'Y',   '--..': 'Z',  '-----': '0', 
		'.----': '1',  '..---': '2',  '...--': '3',
		'....-': '4',  '.....': '5',  '-....': '6', 
		'--...': '7',  '---..': '8',  '----.': '9'}

		decryptedTextList = []

		for word in morseList:
			if (word in englishDict.keys()):
				decryptedTextList.append(englishDict[word])

		decryptedText = ''.join(decryptedTextList)

	elif (decryptionMethod == 2):
		# do other method decryption
		x = 1

	return(decryptedText)

def writeFile (Text):

	# encrypted or decrypted text passed in
	# open a NEW file for writing
	# write text to new file
	x = 1

def main():
	
	encryptDecrypt = int(input("Would you like to encrypt or decrypt a file?\n(1) for encrypt, (2) for decrypt: "))

	if (encryptDecrypt == 1):
		filename = input("Enter the name of the file you'd like to encrypt: ")
		encryptionMethod = int(input("Which encyrption method would you like to use?\n(1) for morse code, (2) for other: "))
		text = readFile(filename)
		encryptedText = encrypt(text,encryptionMethod)
		writeFile(encryptedText)
	elif (encryptDecrypt == 2):
		filename = input("Enter the name of the file you'd like to decrypt: ")
		decryptionMethod = int(input("Which decyrption method would you like to use?\n(1) for morse code, (2) for other: "))
		text = readFile(filename)
		decryptedText = decrypt(text,decryptionMethod)
		writeFile(decryptedText)

main()

