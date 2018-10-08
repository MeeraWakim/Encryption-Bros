import unittest
import EncryptImage
import os
import imghdr as img
from PIL import Image as im
from PIL import ImageChops as ImCh
from numpy import*
from random import shuffle
selectedImage = 
class TestImageMethods(unittest.TestCase):
	def test_encrypt_shuffle(self):
		rgb_image = im.open
		rgb_shuffled_image = encrypt_shuffle(selectedimage, rgb_image)
		for x in range(theImage.size[0]):
			for y in range(theImage.size[1]):
				self.AssertNotEqual(rgb_image[x,y][0], rgb_shuffled_image[x,y][2])


	def test_encrypt_swap(self):
		rgb_image = im.open(selectedImage)
		rgb_switched_image = encrypt_swap(selected image, rgb_image)
		for x in range(theImage.size[0]):
			for y in range(theImage.size[1]):
				self.AssertEqual(rgb_image[x,y][0], rgb_switched_image[x,y][2])
				self.AssertEqual(rgb_image[x,y][1], rgb_switched_image[x,y][1])
				self.AssertEqual(rgb_image[x,y][2], rgb_switched_image[x,y][0])


	def test_decrypt_shuffle(self):
		im1 = im.open("file1.jpg")
		im2 = im.open("DecryptedImage.png")

		self.AssertEqual(ImageChops.difference(im2, im1).getbbox(), 0)



	def test_decrypt_swap(self):
		im1 = im.open("file1.jpg")
		im2 = im.open("DecryptedImage.png")

		self.AssertEqual(ImageChops.difference(im2, im1).getbbox(), 0)
		


if __name__ == '__main__':
	unittest.main()


