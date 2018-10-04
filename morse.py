
def readFile (filename):

	# filename passed as a string from main
	# open file for reading
	# readfile into script
	x = 1

	return(text)

def pigLatin (text):

	# constants list
	lowerVowelsList = [a, e, i, o, u]
	upperVowelsList = [A, E, I, O, U]

	# holding lists
	convText = []
	pigTextList = []

	convText = text.split()

	# convert to each word into pig latin
	for word in convText:
		pigWord = word
		# check if first is vowel
		if (word[0] in lowerVowelsList) or (word[0] in upperVowelsList):
			# YES: add way to end
		else:
			# NO: check if second is vowel
			if (word[1] in lowerVowelsList) or (word[1] in upperVowelsList):
				# YES: get first letter, add to end + 'ay'
			else:
				# NO: get both letters, add to end + 'ay'
		# add new word to new list
		pigTextList.append(pigWord)

	return (pigTextList)

def encrypt (text, encryptionMethod):

	# text read in from file passed in
	# int passed in that specifies which encryption method

	if (encryptionMethod == 1):
		# do morse code encryption
		# use a dictionary to map letters to dots/dashes?
		x = 1

	elif (encryptionMethod == 2):
		# call pig function
		encryptedTextList = pigLatin(text)

		# join list w/ spaces in btw.
		encryptedText = ' '.join(encryptedTextList)

		x = 1
	return(encryptedText)

def decrypt (text, decryptionMethod):

	# text read in from file passed in
	# int passed in that specifies which decryption method

	if (decryptionMethod == 1):
		# do morse code decryption
		# use a dictionary to map letters to dots/dashes?
		x = 1

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
		encryptedText = encrypt(text)
		writeFile(encryptedText)
	elif (encryptDecrypt == 2):
		filename = input("Enter the name of the file you'd like to decrypt: ")
		decryptionMethod = int(input("Which decyrption method would you like to use?\n(1) for morse code, (2) for other: "))
		text = readFile(filename)
		decryptedText = decrypt(text)
		writeFile(decryptedText)

main()

