
def readFile (filename):

	# filename passed as a string from main
	# open file for reading
	# readfile into script
	file = open(filename,'r')
	text = file.read()
	file.close()
	return(text)

def encrypt (text, encryptionMethod):

	# text read in from file passed in
	# int passed in that specifies which encryption method

	if (encryptionMethod == 1):
		# do morse code encryption
		# use a dictionary to map letters to dots/dashes?
		x = 1

	elif (encryptionMethod == 2):

		# constants list
		lowerVowelsList = ['a', 'e', 'i', 'o', 'u', 'w']
		upperVowelsList = ['A', 'E', 'I', 'O', 'U', 'W']

		# holding lists
		encryptedTextList = []
		convTextList = text.split()

		# convert to each word into pig latin
		for word in convTextList:
			# check if first is vowel
			if (word[0] in lowerVowelsList) or (word[0] in upperVowelsList):
				# YES: add way to end 
				pigWord = word + 'way'
			else:
				# NO: check if second is vowel
				if (word[1] in lowerVowelsList) or (word[1] in upperVowelsList):
					# YES: get first letter, add to end + 'ay' 
					pigWord = word[1:] + word[0] + 'ay'
				else:
					# NO: get both letters, add to end + 'ay'
					pigWord = word[2:] + word[0:2] + 'ay'
			# add new word to new list
			encryptedTextList.append(pigWord)

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

		# constant lists
		lowerConsonantClustersList = ['bl', 'br', 'ch', 'cl', 'cr', 'dr', 'fl', 'fr', 'gh', 'gl', 'gr', 'ph', 'pl', 'pr', 'sc', 'sh', 'sk', 'sl', 'sm', 'sn', 'sp', 'st', 'sw', 'th', 'tr', 'tw', 'wh', 'wr']
		upperConsonantClustersList = ['Bl', 'Br', 'Ch', 'Cl', 'Cr', 'Dr', 'Fl', 'Fr', 'Gh', 'Gl', 'Gr', 'Ph', 'Pl', 'Pr', 'Sc', 'Sh', 'Sk', 'Sl', 'Sm', 'Sn', 'Sp', 'St', 'Sw', 'Th', 'Tr', 'Tw', 'Wh', 'Wr']

		# holding lists
		decryptedTextList = []
		revTextList = text.split()

		# convert each word back to normal english
		for word in revTextList:
			# IF | check if 4th and 3rd to last characters are in cluster
			if (word[-4:-2] in lowerConsonantClustersList) or (word[-4:-2] in upperConsonantClustersList):
				# YES: remove 'ay' & move cluster to front
				normWord = word[-4:-2] + word[:-4]
			# ELSE | 
			else:
				# IF | check if 3rd to last character is w
				if (word[-3] == 'w'):
					# check if 4th to last character is also w
					if (word[-4] == 'w' or word[-4] == 'W'):
						# YES: remove 'way' and move letter to front
						normWord = word[-4] + word[:-4]
					else:
						# NO: remove 'way'
						normWord = word[:-3]
				# remove 'ay' & move letter to front
				normWord = word[-3] + word[:-3]
			# add new word to list
			decryptedTextList.append(normWord)

		# join list with spaces in btw.
		decryptedText = ' '.join(decryptedTextList)

		x = 1

	return(decryptedText)

def writeFile (Text):

	# encrypted or decrypted text passed in
	# open a NEW file for writing
	# write text to new file
	f = open("encrypted_file.txt","w+")
	f.write(Text)
	f.close()

def main():
	
	encryptDecrypt = int(input("Would you like to encrypt or decrypt a file?\n(1) for encrypt, (2) for decrypt: "))

	if (encryptDecrypt == 1):
		filename = input("Enter the name of the file you'd like to encrypt: ")
		encryptionMethod = int(input("Which encyrption method would you like to use?\n(1) for morse code, (2) for pig latin: "))
		text = readFile(filename)
		encryptedText = encrypt(text, encryptionMethod)
		writeFile(encryptedText)
	elif (encryptDecrypt == 2):
		filename = input("Enter the name of the file you'd like to decrypt: ")
		decryptionMethod = int(input("Which decyrption method would you like to use?\n(1) for morse code, (2) for pig latin: "))
		text = readFile(filename)
		decryptedText = decrypt(text, decryptionMethod)
		writeFile(decryptedText)

main()

