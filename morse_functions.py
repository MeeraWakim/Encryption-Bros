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
		x = 1

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
		# do other method decryption
		x = 1

	return(decryptedText)

def writeFile (Text):

	f = open("encrypted_file.txt", "w+")
	f.write(Text)
	f.close()


