import os
import imghdr as img
from PIL import Image as im
from numpy import*
from random import shuffle

#Code that takes an image directory and finds the image after checking whether or not the supplied directory exists
locationOfDirectory = raw_input("Please enter the location of the directory that contains the image(s) that you would like to encrypt: ")
isADirectory = os.path.isdir(locationOfDirectory)
while not isADirectory:
    print("ERROR: Inputted location not a directory! Please enter a valid location.")
    locationOfDirectory = raw_input("Please enter the location of the directory that contains the image(s) that you would like to encrypt: ")
    isADirectory = os.path.isdir(locationOfDirectory)
os.chdir(locationOfDirectory)
#Ensures that the path can be found in python
if locationOfDirectory[-1:] != "/":
    locationOfDirectory += "/"

#Finds and loads the images 
selectedImage = raw_input("\nPlease enter the file name of the image that you would like to encrypt. The file must be either a PNG or JPEG file. Enter it here: ")
while True:
    try:
        isAnImage = img.what(locationOfDirectory + selectedImage)
        break
    except IOError:
        print("ERROR: Selected file is not either a PNG or JPEG file. Please try again.")
        selectedImage = raw_input("Please enter the file name of the image that you would like to encrypt. The file must be either a PNG or JPEG file. Enter it here: ")
while isAnImage != "png" and isAnImage != "jpeg":
    print("ERROR: Selected file is not either a PNG or JPEG file. Please try again.")
    selectedImage = raw_input("Please enter the file name of the image that you would like to encrypt. The file must be either a PNG or JPEG file. Enter it here: ")
    while True:
        try:
            isAnImage = img.what(locationOfDirectory + selectedImage)
            break
        except IOError:
            print("ERROR: Selected file is not either a PNG or JPEG file. Please try again.")
            selectedImage = raw_input("Please enter the file name of the image that you would like to encrypt. The file must be either a PNG or JPEG file. Enter it here: ")

enOrDe = raw_input("Would you like to encrypt or decrypt your selected image? Enter \"encrypt\" or \"decrypt\" (NOT case-sensitive): ")
while True:
    if enOrDe.lower() == "encrypt" or enOrDe.lower() == "decrypt":
        break
    else:
        print("ERROR: Invalid option inputted.")
        enOrDe = raw_input("Would you like to encrypt or decrypt your selected image? Enter \"encrypt\" or \"decrypt\" (NOT case-sensitive): ")

if enOrDe.lower() == "encrypt":
    theImage = im.open(selectedImage)
    theImage.show()
    print("Picture selected and shown. What would you like to do with this picture?\n1. Swap pixels around randomly.\n2. Swap the red and blue values of each pixel.\n")
    choice = raw_input("Please choose from the available options by entering the number: ")
    while True:
        if choice.find(".") >= 0 or choice.find("-") >= 0:
            choice = raw_input("You didn't type in a positive integer. Please try again: ")
        else:
            try:
                choice = int(choice)
                dummyNum = 2/choice
                if choice == 1 or choice == 2:
                    break
                else:
                    choice = raw_input("You didn't type either \"1\" or \"2\". Please try again: ")
            except ValueError:
                choice = raw_input("You didn't type in a positive integer. Please try again: ")
            except ArithmeticError:
                choice = raw_input("You didn't type in a positive integer. Please try again: ")
    print("")

    choice = int(choice)
    rgb_image = theImage.load()
    if choice == 1:
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
    else:
        for x in range(theImage.size[0]):
            for y in range(theImage.size[1]):
                rgb_image[x,y] = (rgb_image[x,y][2], rgb_image[x,y][1], rgb_image[x,y][0])
        theImage.show()
        theImage.save("EncryptedImage.png")
        print("Swapped the red and blue color values for each pixel. The encrypted image is called \"EncryptedImage.png\" and has been saved to the directory where your original image is.")
else:
    theImage = im.open(selectedImage)
    theImage.show()
    print("Picture selected and shown. What would you like to do with this picture?\n1. Swap pixels around to their original positions.\n2. Swap the red and blue values of each pixel.\n")
    choice = raw_input("Please choose from the available options by entering the number: ")
    while True:
        if choice.find(".") >= 0 or choice.find("-") >= 0:
            choice = raw_input("You didn't type in a positive integer. Please try again: ")
        else:
            try:
                choice = int(choice)
                dummyNum = 2/choice
                if choice == 1 or choice == 2:
                    break
                else:
                    choice = raw_input("You didn't type either \"1\" or \"2\". Please try again: ")
            except ValueError:
                choice = raw_input("You didn't type in a positive integer. Please try again: ")
            except ArithmeticError:
                choice = raw_input("You didn't type in a positive integer. Please try again: ")
    print("")

    choice = int(choice)
    rgb_image = theImage.load()
    theKey = []
    if choice == 1:
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
    else:
        for x in range(theImage.size[0]):
            for y in range(theImage.size[1]):
                rgb_image[x,y] = (rgb_image[x,y][2], rgb_image[x,y][1], rgb_image[x,y][0])
        theImage.show()
        theImage.save("DecryptedImage.png")
        print("Swapped the red and blue color values for each pixel. The decrypted image is called \"DecryptedImage.png\" and has been saved to the directory where your encrypted image is.")