import base64
import time

def readFile (filename):

	# filename passed as a string from main
	# open file for reading
	errorFlag = 1
	while errorFlag == 1:
		try:
			file = open(filename, 'r')
		except FileNotFoundError:
			filename = input("File not found. Please try entering filename/path again: ")
			continue
		errorFlag = 0
	# readfile into script
	#if you want a list of characters uncomment this

	text = file.read()
	words = text.split(' ')
	file.close()
	return(words)


def encrypt (textList, encryptionMethod):

	# text read in from file passed in
	# int passed in that specifies which encryption method

	characters = []
	for word in textList:
		for letter in word:
			characters.append(letter)
		characters.append(' ')

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
    	'9': '----.',  ' ': ''
    	}

		encryptedTextList = []

		for char in characters:
			if (char.upper() in morseDict.keys()):
				encryptedTextList.append(morseDict[char.upper()])
			else:
				encryptedTextList.append('(' + char + ')')		# put parenthesis around characters that aren't alphanumeric

		encryptedText = ' '.join(encryptedTextList)

	elif (encryptionMethod == 2):
		# do other method encryption
		new_string = ''
		for words in textList:
			for letter in words:
				new_string = new_string + letter
			new_string = new_string + ' '
		

		encryptedText = vig_cypher(new_string,'a key','e')

	return(encryptedText)

def decrypt (textList, decryptionMethod):

	# text read in from file passed in
	# int passed in that specifies which decryption method

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
		'--...': '7',  '---..': '8',  '----.': '9',  '': ' '}

		decryptedTextList = []

		for word in textList:
			if (word in englishDict.keys()):
				decryptedTextList.append(englishDict[word])
			else:
				word = word[1:len(word)-1]
				decryptedTextList.append(word)

		decryptedText = ''.join(decryptedTextList)

	elif (decryptionMethod == 2):
		new_string = ''
		for words in textList:
			for letter in words:
				new_string = new_string + letter
			new_string = new_string + ' '
		new_string = new_string[:-2]

		decryptedText = vig_cypher(new_string,'a key','d')

	return(decryptedText)

def vig_cypher(txt='', key='', typ='d'):
	if not txt:
		print ('Needs text')
		return
	if not key:
		print ('Needs key')
		return
	if typ not in ('d', 'e'):
		print ('Type must be "d" or "e"')
		return

	k_len = len(key)
	k_ints = [ord(i) for i in key]
	txt_ints = [ord(i) for i in txt]
	ret_txt = ''
	for i in range(len(txt_ints)):
		adder = k_ints[i % k_len]
		if typ == 'd':
			adder *= -1

		if txt_ints[i] == 10:
			ret_txt += chr(10)
		else:
			v = (txt_ints[i] - 32 + adder) % 95

			ret_txt += chr(v + 32)

	return ret_txt

def writeFile (Text, name):
	file_name = name + '.txt'
	f = open(file_name, "w+")
	f.write(Text)
	f.close()

def main():

	errorFlag = 1
	while errorFlag == 1:
		try:
			encryptDecrypt = int(input("Would you like to encrypt or decrypt a file?\n(1) for encrypt, (2) for decrypt: "))
			while(encryptDecrypt != 1 and encryptDecrypt != 2):
				encryptDecrypt = int(input("That was an incorrect value. Please try again\n(1) for encrypt, (2) for decrypt: "))
		except ValueError:
			print("That was an incorrect value. Please try again")
			continue
		errorFlag = 0

	if (encryptDecrypt == 1):
		function = "Encryption"
		filename = input("Enter the name of the file you'd like to encrypt: ")
		errorFlag = 1
		while errorFlag == 1:
			try:
				encryptionMethod = int(input("Which encyrption method would you like to use?\n(1) for morse code, (2) for Vigenere Cypher: "))
				while(encryptionMethod != 1 and encryptionMethod != 2):
					encryptionMethod = int(input("That was an incorrect value. Please try again\n(1) for morse code, (2) for Vigenere Cypher: "))
			except ValueError:
				print("That was an incorrect value. Please try again")
				continue
			errorFlag = 0
		if(encryptionMethod == 1):
			method = "Morse Code"
		else:
			method = "Vigenere Cypher"
		text = readFile(filename)
		encrypt_name = input("Enter name for encrypted file: ")
		t1 = time.time()
		encryptedText = encrypt(text,encryptionMethod)
		writeFile(encryptedText, encrypt_name)
		t2 = time.time()
		t = t2 - t1
	elif (encryptDecrypt == 2):
		function = "Decryption"
		filename = input("Enter the name of the file you'd like to decrypt: ")
		errorFlag = 1
		while errorFlag == 1:
			try:
				decryptionMethod = int(input("Which decyrption method would you like to use?\n(1) for morse code, (2) for Vigenere Cypher: "))
				while(decryptionMethod != 1 and decryptionMethod != 2):
					decryptionMethod = int(input("That was an incorrect value. Please try again\n(1) for morse code, (2) for Vigenere Cypher: "))
			except ValueError:
				print("That was an incorrect value. Please try again")
				continue
			errorFlag = 0
		if(decryptionMethod == 1):
			method = "Morse Code"
		else:
			method = "Vigenere Cypher"
		text = readFile(filename)
		encrypt_name = input("Enter name for decrypted file: ")
		t1 = time.time()
		decryptedText = decrypt(text,decryptionMethod)
		writeFile(decryptedText, encrypt_name)
		t2 = time.time()
		t = t2 - t1

	print("\nReport\n-----------\n%s\nMethod: %s\nRuntime: %f s\nFile Encrypted: %s\nFile Created: %s.txt\n" % (function,method,t,filename,encrypt_name))

main()







