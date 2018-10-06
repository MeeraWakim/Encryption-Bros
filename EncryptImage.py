import os
import imghdr as img
from PIL import Image as im
from numpy import*
from random import shuffle

def get_image_info():
  #Code that takes an image directory and finds the image after checking whether or not the supplied directory exists
  locationOfDirectory = input("Please enter the location of the directory that contains the image(s) that you would like to encrypt: ")

  isADirectory = os.path.isdir(locationOfDirectory)
  #Loop to ensure that the user enters a valid dictionary before continuing-- throws error if not
  while not isADirectory:
    print("ERROR: Inputted location not a directory! Please enter a valid location.")
    locationOfDirectory = input("Please enter the location of the directory that contains the image(s) that you would like to encrypt: ")
    isADirectory = os.path.isdir(locationOfDirectory)
  
  os.chdir(locationOfDirectory)
  if locationOfDirectory[-1:] != "/":
    locationOfDirectory += "/"

  #Finds and loads the images 
  selectedImage = input("\nPlease enter the file name of the image that you would like to encrypt. The file must be either a PNG or JPEG file. Enter it here: ")
  while True:
    try:
      isAnImage = img.what(locationOfDirectory + selectedImage)
      return selectedImage
    except IOError:
      print("ERROR: Selected file is not either a PNG or JPEG file. Please try again.")
      selectedImage = input("Please enter the file name of the image that you would like to encrypt. The file must be either a PNG or JPEG file. Enter it here: ")
  while isAnImage != "png" and isAnImage != "jpeg":
    print("ERROR: Selected file is not either a PNG or JPEG file. Please try again.")
    selectedImage = input("Please enter the file name of the image that you would like to encrypt. The file must be either a PNG or JPEG file. Enter it here: ")
    while True:
      try:
        isAnImage = img.what(locationOfDirectory + selectedImage)
        return selectedImage
      except IOError:
        print("ERROR: Selected file is not either a PNG or JPEG file. Please try again.")
        selectedImage = input("Please enter the file name of the image that you would like to encrypt. The file must be either a PNG or JPEG file. Enter it here: ")

def encrypt_or_decrypt():
  #User decides whether to encrypt or decrypt
  decision = input("Would you like to encrypt or decrypt your selected image? Enter \"encrypt\" or \"decrypt\" (NOT case-sensitive): ")
  while True:
      if decision.lower() == "encrypt" or decision.lower() == "decrypt":
        return decision
      else:
        print("ERROR: Invalid option inputted.")
        decision = raw_input("Would you like to encrypt or decrypt your selected image? Enter \"encrypt\" or \"decrypt\" (NOT case-sensitive): ")
    
def which_one(selectedImage):
    image = im.open(selectedImage)
    image.show()
    print("Picture selected and shown. What would you like to do with this picture?\n1. Swap pixels around randomly.\n2. Swap the red and blue values of each pixel.\n")
    choice = input("Please choose from the available options by entering the number: ")
    while True:
      if choice.find(".") >= 0 or choice.find("-") >= 0:
        choice = input("You didn't type in a positive integer. Please try again: ")
      else:
        try:
          choice = int(choice)
          dummyNum = 2/choice
          if choice == 1 or choice == 2:
            break
          else:
            choice = input("You didn't type either \"1\" or \"2\". Please try again: ")
        except ValueError:
          choice = input("You didn't type in a positive integer. Please try again: ")
        except ArithmeticError:
          choice = input("You didn't type in a positive integer. Please try again: ")
    print("")
	
	#User selects what option they want: Scramble or swap red/blue values 
    choice = int(choice)
    return choice

def encrypt_shuffle(image):
  #First choice shuffles the pixels randomly
  rgb_image = image.load()
  oldImage = []
  newImage = []
  for x in range(image.size[0]):
    for y in range(image.size[1]):
      oldImage.append((rgb_image[x,y][0], rgb_image[x,y][1], rgb_image[x,y][2]))
      newImage.append((rgb_image[x,y][0], rgb_image[x,y][1], rgb_image[x,y][2]))
  shuffle(newImage)
  index = 0
  for x in range(image.size[0]):
    for y in range(image.size[1]):
      rgb_image[x,y] = (newImage[index][0], newImage[index][1], newImage[index][2])
      index += 1

  try:
    doesExist = img.what(locationOfDirectory + "EncryptionKey.txt")
    open("EncryptionKey.txt", "w").close()
    keyFile = open("EncryptionKey.txt", "w")
  except IOError:
    keyFile = open("EncryptionKey.txt", "w")
  
  for anotherIndex in range(len(oldImage)):
    keyFile.write(str(newImage[anotherIndex]))
    keyFile.write("=")
    keyFile.write(str(oldImage[anotherIndex]))
    keyFile.write("\n")
  keyFile.close()
  theImage.show()
  theImage.save("EncryptedImage.png")
  print("Shuffled the pixels of the original image. The encrypted image is called \"EncryptedImage.png\" and has been saved to the directory where your original image is.")
  print("Encryption key saved as \"EncryptionKey.txt\" and has been saved to the directory where your original image is.")
  return

def encrypt_swap(theImage):
  rgb_image = theImage.load()
  #Choice two swaps the red/blue pixel values 

  for x in range(theImage.size[0]):
    for y in range(theImage.size[1]):
      rgb_image[x,y] = (rgb_image[x,y][2], rgb_image[x,y][1], rgb_image[x,y][0])
  theImage.show()
  theImage.save("EncryptedImage.png")
  print("Swapped the red and blue color values for each pixel. The encrypted image is called \"EncryptedImage.png\" and has been saved to the directory where your original image is.")
  return
  
def decrypt_shuffle(selectedImage):
  rgb_image = theImage.load()
  theKey = []
  try:
    doesExist = img.what(locationOfDirectory + "EncryptionKey.txt")
    keyFile = open("EncryptionKey.txt", "r")
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
    theImage.save("DecryptedImage.png")
    print("Shuffled the pixels of the original image. The decrypted image is called \"DecryptedImage.png\" and has been saved to the directory where your encrypted image is.")
  except IOError:
    print("ERROR! No encryption key found!")
	return

def decrypt_swap(selectedImage):
  rgb_image = selectedImage.load()

  for x in range(selectedImage.size[0]):
    for y in range(selectedImage.size[1]):
      rgb_image[x,y] = (rgb_image[x,y][2], rgb_image[x,y][1], rgb_image[x,y][0])
  selectedImage.show()
  selectedImage.save("DecryptedImage.png")
  print("Swapped the red and blue color values for each pixel. The decrypted image is called \"DecryptedImage.png\" and has been saved to the directory where your encrypted image is.")
  return


def main():
  #User selects image 
  selectedImage = get_image_info()

  #User decides to encrypt or decrypt the image
  decision = encrypt_or_decrypt()

  #Function runs depending on encryption or decryption method
  if decision.lower() == "encrypt":
    #User decides which encryption method they would like to use 
	choice = which_one(selectedImage)
    if choice == 1: 
	  encrypt_shuffle(selectedImage)
	elif choice == 2: 
	  encrypt_swap(selectedImage)
  
  elif decision.lower() == "decrypt":
    #User decides what decryption method they would like to use 
    choice = which_one(selectedImage)
	if choice == 1:
	  decrypt_shuffle(selectedImage)
	elif choice == 2: 
	  decrypt_swap(selectedImage)

main()