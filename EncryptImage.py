import os
import imghdr as img
from PIL import Image as im
from numpy import*
import numpy
from random import shuffle, randint
from math import floor
	#Code that takes an image directory and finds the image after checking whether or not the supplied directory exists
	locationOfDirectory = input("Please enter the location of the directory that contains the image(s) that you would like to encrypt or decrypt: ")
	isADirectory = os.path.isdir(locationOfDirectory)
	while not isADirectory:
		print("ERROR: Inputted location not a directory! Please enter a valid location.")
		locationOfDirectory = input("Please enter the location of the directory that contains the image(s) that you would like to encrypt or decrypt: ")
		isADirectory = os.path.isdir(locationOfDirectory)
	os.chdir(locationOfDirectory)
	#Ensures that the path can be found in python
	if locationOfDirectory[-1:] != "/":
		locationOfDirectory += "/"

	#Finds and loads the images
	selectedImage = input("\nPlease enter the file name of the image that you would like to encrypt or decrypt. The file must be either a PNG or JPEG file. Enter it here: ")
	print()
	while True:
		try:
			isAnImage = img.what(locationOfDirectory + selectedImage)
			break
		except IOError:
			print("ERROR: Selected file is not either a PNG or JPEG file. Please try again.")
			selectedImage = input("Please enter the file name of the image that you would like to encrypt or decrypt. The file must be either a PNG or JPEG file. Enter it here: ")
			print()
	while isAnImage != "png" and isAnImage != "jpeg":
		print("ERROR: Selected file is not either a PNG or JPEG file. Please try again.")
		selectedImage = input("Please enter the file name of the image that you would like to encrypt or decrypt. The file must be either a PNG or JPEG file. Enter it here: ")
		print()
		while True:
			try:
				isAnImage = img.what(locationOfDirectory + selectedImage)
				break
			except IOError:
				print("ERROR: Selected file is not either a PNG or JPEG file. Please try again.")
				selectedImage = input("Please enter the file name of the image that you would like to encrypt or decrypt. The file must be either a PNG or JPEG file. Enter it here: ")
				print()
	return selectedImage

def choose():

	print("Picture selected and shown. What would you like to do with this picture?\n1. Swap pixels around randomly.\n2. Swap the red and blue values of each pixel.\n3. Manipulate the image with a mathematical function.\n4. Encrypt an image based on a user-given key.\n")
	choice = input("Please choose from the available options by entering the number: ")
	print()
	while True:
		if choice.find(".") >= 0 or choice.find("-") >= 0:
			choice = input("You didn't type in a positive integer. Please try again: ")
			print()
		else:
			try:
				choice = int(choice)
				dummyNum = 2/choice
				if choice == 1 or choice == 2 or choice == 3 or choice == 4:
					break
				else:
					choice = input("You didn't type either \"1\", \"2\", \"3\", or \"4\". Please try again: ")
				if choice == 1 or choice == 2 or choice == 3:
					break
				else:
					choice = input("You didn't type either \"1\", \"2\" or \"3\". Please try again: ")
				if choice == 1 or choice == 2 or choice == 3 or choice == 4:
					break
				else:
					choice = input("You didn't type either \"1\", \"2\", \"3\", or \"4\". Please try again: ")
					print()
			except ValueError:
				choice = input("You didn't type in a positive integer. Please try again: ")
				print()
			except ArithmeticError:
				choice = input("You didn't type in a positive integer. Please try again: ")
				print()
	return int(choice)
#######################################################################################################################################
#Encryption methods

#######################################################################################################################################
#Encryption methods

def encrypt_shuffle(theImage, rgb_image):
	oldImage = []
	newImage = []
	for x in range(theImage.size[0]):
		for y in range(theImage.size[1]):
			oldImage.append((rgb_image[x,y][0], rgb_image[x,y][1], rgb_image[x,y][2]))
			newImage.append((rgb_image[x,y][0], rgb_image[x,y][1], rgb_image[x,y][2]))
	shuffle(newImage)
	index = 0
	for x in range(theImage.size[0]):
		for y in range(theImage.size[1]):
			rgb_image[x,y] = (newImage[index][0], newImage[index][1], newImage[index][2])
			index += 1
	filename = input("What would you like to name your encrypted image?")
	try:
		doesExist = img.what(locationOfDirectory + filename + "_Key.txt")
		open(filename + "_Key.txt", "w").close()
		keyFile = open(filename + "_Key.txt", "w")
	except IOError:
		keyFile = open(filename + "_Key.txt", "w")
	for anotherIndex in range(len(oldImage)):
		keyFile.write(str(newImage[anotherIndex]))
		keyFile.write("=")
		keyFile.write(str(oldImage[anotherIndex]))
		keyFile.write("\n")
	keyFile.close()
	theImage.show()
	theImage.save(filename + ".png")
	print("Shuffled the pixels of the original image. The encrypted image is called " + filename + ".png and has been saved to the directory where your original image is.")
	print("Encryption key saved as " + filename + ".txt and has been saved to the directory where your original image is.")

def encrypt_swap(theImage, rgb_image):
	for x in range(theImage.size[0]):
		for y in range(theImage.size[1]):
			rgb_image[x,y] = (rgb_image[x,y][2], rgb_image[x,y][1], rgb_image[x,y][0])
	theImage.show()
	theImage.save("EncryptedImage.png")
	print("Swapped the red and blue color values for each pixel. The encrypted image is called " + filename + ".png and has been saved to the directory where your original image is.")

	theImage.show()
	theImage.save("EncryptedImage.png")
	print("Your image has been jumbled all around. The encrypted image is called \"EncryptedImage.png\" and has been saved to the directory where your original image is.")

def encrypt_keyHash(theImage, rgb_image):
	userKey = input("Please enter any kind of sentence to act as your encryption key. Your chosen picture will be scrambled based on your choice of key. Your key cannot contain any \"\\\" (backslash) symbols: ")

	charList = []
	for index in range(len(userKey)):
		charAsInt = ord(userKey[index]) #Gets the ASCII value of a character within userKey
		charList.append(charAsInt)


	#Caesar cipher based on userKey
	shiftedImage = rgb_image #shiftedImage will represent the final encrypted image - but first set it to the original image
	inProgressImage = im.new("RGB", (theImage.size[0], theImage.size[1])) #Image in between shifts
	randomCoords = []
	for index in range(len(charList)):
		numShift = charList[index]
		randomCoord = []
		randomX = randint(0, theImage.size[0]-1)
		randomY = randint(0, theImage.size[1]-1)
		randomCoord.append(randomX)
		randomCoord.append(randomY)
		randomCoords.append(randomCoord)
		for x in range(theImage.size[0]):
			for y in range(theImage.size[1]):
				xCoord = (numShift + x + randomX)%theImage.size[0]
				yCoord = (y + randomY + floor((x + randomX + numShift)/theImage.size[0]))%theImage.size[1]
				inProgressImage[x][y] = shiftedImage[xCoord][yCoord]
		shiftedImage = inProgressImage
		inProgressImage = im.new("RGB", (theImage.size[0], theImage.size[1])) #Image in between shifts
	shiftedImage.show()
	shiftedImage.save("EncryptedImage.png")

	try:
		doesExist = img.what(locationOfDirectory + "YourKey.txt")
		open("YourKey.txt", "w").close()
		keyFile = open("YourKey.txt", "w")
	except IOError:
		keyFile = open("YourKey.txt", "w")
	keyFile.write(str(userKey) + "\n")
	for index in range(len(randomCoords)):
		keyFile.write(str(randomCoords[index][0]) + "," + str(randomCoords[index][1]) + "!\n")
	keyFile.close()
	print("Employed a modified Caesar cipher based on your key. The encrypted image is called \"EncryptedImage.png\" and has been saved to the directory where your original image is.")
#######################################################################################################################################

def encrypt_function(theImage, rgb_image):
	new_image = []
	for x in range(theImage.size[0]):
		for y in range(theImage.size[1]):
			calc1 = int(ceil(rgb_image[x,y][0] ** 3))
			calc2 = int(ceil(rgb_image[x,y][1] ** 3))
			calc3 = int(ceil(rgb_image[x,y][2] ** 3))
			line = str(calc1) + ' ' + str(calc2) + ' ' + str(calc3) + '\n'
			new_image.append(line)
			rgb_image[x,y] = ((rgb_image[x,y][0] ** 3), (rgb_image[x,y][1] ** 3), (rgb_image[x,y][2] ** 3))

	filename = input("Please enter the name you would like to give your file: ")
	try:
		doesExist = img.what(locationOfDirectory + filename + "_Key.txt")
		open(filename + "_Key.txt", "w").close()
		keyFile = open(filename + "_Key.txt", "w")
	except IOError:
		keyFile = open(filename + "_Key.txt", "w")
	for i in range(len(new_image)):
		keyFile.write(str(new_image[i]))
	keyFile.close()
	theImage.show()
	theImage.save(filename + ".png")
	print("Manipulated the image using a mathematical function. The encrypted image is called " + filename + ".png and has been saved to the directory where your original image is.")
	print("Encryption key saved as " + filename + ".txt and has been saved to the directory where your original image is.")

def encrypt_keyHash(theImage, rgb_image):
	userKey = input("Please enter any kind of sentence to act as your encryption key. Your chosen picture will be scrambled based on your choice of key. Your key cannot contain any \"\\\" (backslash) symbols: ")

	charList = []
	for index in range(len(userKey)):
		charAsInt = ord(userKey[index]) #Gets the ASCII value of a character within userKey
		charList.append(charAsInt)

	#Caesar cipher based on userKey
	shiftedImage = rgb_image #shiftedImage will represent the final encrypted image - but first set it to the original image
	inProgressImage = im.new("RGB", (theImage.size[0], theImage.size[1])) #Image in between shifts
	randomCoords = []
	for index in range(len(charList)):
		numShift = charList[index]
		randomCoord = []
		randomX = randint(0, theImage.size[0]-1)
		randomY = randint(0, theImage.size[1]-1)
		randomCoord.append(randomX)
		randomCoord.append(randomY)
		randomCoords.append(randomCoord)
		inProgressImageList = []
		for x in range(theImage.size[0]):
			row = []
			for y in range(theImage.size[1]):
				xCoord = (numShift + x + randomX)%theImage.size[0]
				yCoord = (y + randomY + floor((x + randomX + numShift)/theImage.size[0]))%theImage.size[1]
				row.append((shiftedImage[xCoord, yCoord][0], shiftedImage[xCoord, yCoord][1], shiftedImage[xCoord, yCoord][2]))
			inProgressImageList.append(row)
		inProgressImageList = numpy.array(inProgressImageList, dtype = numpy.uint8)
		if index != len(charList) - 1:
			shiftedImage = im.fromarray(inProgressImageList).load()
		else:
			shiftedImage = im.fromarray(inProgressImageList)
		inProgressImage = im.new("RGB", (theImage.size[0], theImage.size[1])) #Image in between shifts
	shiftedImage.show()


#Decryption methods

def decrypt_shuffle(theImage, rgb_image):

	#Naming and saving the files
	filename = input("Please enter what you would like to name your file: ")
	shiftedImage.save(filename + ".png")

	try:
		doesExist = img.what(locationOfDirectory + filename + "_Key.txt")
		open(filename + "_Key.txt", "w").close()
		keyFile = open(filename + "_Key.txt", "w")
	except IOError:
		keyFile = open(filename + "_Key.txt", "w")
	keyFile.write(str(userKey) + "\n")
	for index in range(len(randomCoords)):
		keyFile.write(str(randomCoords[index][0]) + "," + str(randomCoords[index][1]) + "!\n")
	keyFile.close()
	print("Employed a modified Caesar cipher based on your key. The encrypted image is called " + filename + ".png and has been saved to the directory where your original image is.")
#######################################################################################################################################
#Decryption methods

def decrypt_shuffle(theImage, rgb_image, filename):

	theKey = []
	try:
		doesExist = img.what(locationOfDirectory + filename +"_Key.txt")
		keyFile = open(filename + "_Key.txt", "r")
		for line in keyFile:
			firstRight = line.find(")")
			secondTuple = line[firstRight+2:-1]

			firstComma2nd = secondTuple.find(",")
			secondTupleR = secondTuple[1:firstComma2nd]
			secondComma2nd = secondTuple.find(",", firstComma2nd + 1)
			secondTupleG = secondTuple[firstComma2nd+2:secondComma2nd]
			secondTupleB = secondTuple[secondComma2nd+2:-1]

			secondTuple = (int(secondTupleR), int(secondTupleG), int(secondTupleB))
			theKey.append(secondTuple)

		myIndex = 0
		for x in range(theImage.size[0]):
			for y in range(theImage.size[1]):
				rgb_image[x,y] = (theKey[myIndex][0], theKey[myIndex][1], theKey[myIndex][2])
				myIndex += 1
		theImage.show()
		decryptedname = input("Please enter a name for your decrypted file: ")
		theImage.save(decryptedname + ".png")
		print("Shuffled the pixels of the original image. The decrypted image is called " + decryptedname + ".png and has been saved to the directory where your encrypted image is.")
	except IOError:
		print("ERROR! No encryption key found!")

def decrypt_swap(theImage, rgb_image):

	if theImage.filename == "EncryptedImage.png":
		for x in range(theImage.size[0]):
			for y in range(theImage.size[1]):
				rgb_image[x,y] = (rgb_image[x,y][2], rgb_image[x,y][1], rgb_image[x,y][0])
		theImage.show()
		theImage.save("DecryptedImage.png")
		print("Swapped the red and blue color values for each pixel. The decrypted image is called \"DecryptedImage.png\" and has been saved to the directory where your encrypted image is.")
	else:
		print("ERROR! You can't decrypt an image that hasn't been encrypted first!")

def decrypt_function(theImage, rgb_image):
	#Still working out some errors!
	if theImage.filename == "EncryptedImage.png":
		for x in range(theImage.size[0]):
			for y in range(theImage.size[1]):
				print(rgb_image[x,y])
				rgb_image[x,y] = ( (rgb_image[x,y][0] ** (1/3)), (rgb_image[x,y][1] ** (1/3)), (rgb_image[x,y][2] ** (1/3)) )

		theImage.show()
		theImage.save("DecryptedImage.png")
		print("Reversed the equation. The decrypted image is called \"DecryptedImage.png\" and has been saved to the directory where your encrypted image is.")
	else:
		print("ERROR! You can't decrypt an image that hasn't been encrypted first!")

def decrypt_keyHash(theImage, rgb_image):
	try:
		doesExist = img.what(locationOfDirectory + "YourKey.txt")
		keyFile = open("YourKey.txt", "r")
		lineCounter = 0
		userKey = ""
		charAsInt = []
		randomCoords = []
		for line in keyFile:
			randomCoord = []
			if lineCounter == 0:
				userKey = line[:-1]
			else:
				randomCoord.append(int(line[:line.find(",")]))
				randomCoord.append(int(line[line.find(",") + 1:line.find("!")]))
				randomCoords.append(randomCoord)
			lineCounter += 1
		for char in userKey:
			charAsInt.append(ord(char))

		decryptedImage = rgb_image
		inProgressImage = im.new("RGB", (theImage.size[0], theImage.size[1])) #Image in between shifts
		for index in range(len(randomCoords)-1, -1, -1):
			numShift = charAsInt[index]
			randomX = randomCoords[index][0]
			randomY = randomCoords[index][1]
			for x in range(theImage.size[0]):
				for y in range(theImage.size[1]):
					xCoord = (numShift + x + randomX)%theImage.size[0]
					yCoord = (y + randomY + floor((x + randomX + numShift)/theImage.size[0]))%theImage.size[1]
					inProgressImage[xCoord][yCoord] = decryptedImage[x][y]
			decryptedImage = inProgressImage
			inProgressImage = im.new("RGB", (theImage.size[0], theImage.size[1])) #Image in between shifts

def decrypt_function(theImage, rgb_image):
	if theImage.filename == "EncryptedImage.png":

	for x in range(theImage.size[0]):
		for y in range(theImage.size[1]):
			rgb_image[x,y] = (rgb_image[x,y][2], rgb_image[x,y][1], rgb_image[x,y][0])
	theImage.show()
	decryptedname = input("Please enter a name for your decrypted file: ")
	theImage.save(decryptedname + ".png")
	print("Swapped the red and blue color values for each pixel. The decrypted image is called " + decryptedname + ".png and has been saved to the directory where your encrypted image is.")

def decrypt_function(theImage, rgb_image, filename):
		theKey = []
		try:
			doesExist = img.what(locationOfDirectory + filename + "_Key.txt")
			keyFile = open(filename + "_Key.txt", "r")
			for line in keyFile:
				line = line.rstrip("\n")
				line = line.split()
				for item in range(len(line)):
					line[item] = int(line[item])
				theKey.append(line)

			count = 0
			for x in range(theImage.size[0]):
				for y in range(theImage.size[1]):
					rgb_image[x,y] = (int(ceil(theKey[count][0] ** (1/3))), int(ceil(theKey[count][1] ** (1/3))), int(ceil(theKey[count][2] ** (1/3))))
					count += 1

			theImage.show()
			decryptedname = input("Please enter a name for your decrypted file: ")
			theImage.save(decryptedname + ".png")
			print("Reversed the equation. The decrypted image is called " + decryptedname + ".png and has been saved to the directory where your encrypted image is.")
		except IOError:
			print("ERROR! No encryption key found!")


def decrypt_keyHash(theImage, rgb_image, filename):
	try:
		doesExist = img.what(locationOfDirectory + filename + "_Key.txt")
		keyFile = open( filename + "_Key.txt", "r")
		lineCounter = 0
		userKey = ""
		charAsInt = []
		randomCoords = []
		for line in keyFile:
			randomCoord = []
			if lineCounter == 0:
				userKey = line[:-1]
			else:
				randomCoord.append(int(line[:line.find(",")]))
				randomCoord.append(int(line[line.find(",") + 1:line.find("!")]))
				randomCoords.append(randomCoord)
			lineCounter += 1
		for char in userKey:
			charAsInt.append(ord(char))

		decryptedImage = rgb_image
		inProgressImage  = []
		for x in range(theImage.size[0]):
			row = []
			for y in range(theImage.size[1]):
				row.append(0)
			inProgressImage.append(row)
		for index in range(len(randomCoords)-1, -1, -1):
			numShift = charAsInt[index]
			randomX = randomCoords[index][0]
			randomY = randomCoords[index][1]
			for x in range(theImage.size[0]):
				for y in range(theImage.size[1]):
					xCoord = (x + randomX + numShift)%theImage.size[0]
					yCoord = (y + randomY + floor((x + randomX + numShift)/theImage.size[0]))%theImage.size[1]
					inProgressImage[x][y] = (decryptedImage[xCoord, yCoord][0], decryptedImage[xCoord, yCoord][1], decryptedImage[xCoord, yCoord][2])
			inProgressImageList = numpy.array(inProgressImage, dtype = numpy.uint8)
			if index != 0:
				decryptedImage = im.fromarray(inProgressImageList).load()
			else:
				decryptedImage = im.fromarray(inProgressImageList)
			inProgressImage  = [] #Image in between shifts
			for x in range(theImage.size[0]):
				row = []
				for y in range(theImage.size[1]):
					row.append(0)
				inProgressImage.append(row)

		decryptedImage.show()
		decryptedname = input("Please enter a name for your decrypted file: ")
		theImage.save(decryptedname + ".png")
		print("Reversed the Caesar cipher employed on your original image. The decrypted image is called " + decryptedname + ".png and has been saved to the directory where your encrypted image is.")

	except IOError:
		print("ERROR! No user key found!")
#######################################################################################################################################

def main():
	selectedImage = get_info()

	enOrDe = input("Would you like to encrypt or decrypt your selected image? Enter \"encrypt\" or \"decrypt\" (NOT case-sensitive): ")
	print()
	while True:
		if enOrDe.lower() == "encrypt" or enOrDe.lower() == "decrypt":
			break
		else:
			print("ERROR: Invalid option inputted.")
			enOrDe = input("Would you like to encrypt or decrypt your selected image? Enter \"encrypt\" or \"decrypt\" (NOT case-sensitive): ")
			print()

	theImage = im.open(selectedImage)
	theImage.show()
	rgb_image = theImage.load()
	if enOrDe.lower() == "encrypt":
		choice = choose()
		if choice == 1:
			encrypt_shuffle(theImage, rgb_image)
		elif choice == 2:
			encrypt_swap(theImage, rgb_image)
		elif choice == 3:
		    encrypt_function(theImage, rgb_image)

		elif choice == 4:
			encrypt_keyHash(theImage, rgb_image)

		elif choice == 4:
			encrypt_keyHash(theImage, rgb_image)

	else:
		choice = choose()
		if choice == 1:
			filename = input("Please enter the name of your file: ")
			print()
			decrypt_shuffle(theImage, rgb_image, filename)
		elif choice == 2:
			decrypt_swap(theImage, rgb_image)

		elif choice == 3:
			decrypt_function(theImage, rgb_image)
		elif choice == 4:
			decrypt_keyHash(theImage, rgb_image)
		elif choice == 3: 
			decrypt_function(theImage, rgb_image)
			

		elif choice == 3:
			filename = input("Please enter the name of your file: ")
			print()
			decrypt_function(theImage, rgb_image, filename)
		elif choice == 4:
			filename = input("Please enter the name of your file: ")
			print()
			decrypt_keyHash(theImage, rgb_image, filename)

	print("")

main()