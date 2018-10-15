import unittest
import EncryptImage

class TestImageMethods():
	def test_encrypt_shuffle(self):
		selectedImage = im.open("Cat.jpeg")
		rgb_image = selectedImage.load()
		rgb_shuffled_image = encrypt_shuffle(selectedimage, rgb_image)
		for x in range(theImage.size[0]):
			for y in range(theImage.size[1]):
				self.AssertNotEqual(rgb_image[x,y][0], rgb_shuffled_image[x,y][0])
				self.AssertNotEqual(rgb_image[x,y][1], rgb_shuffled_image[x,y][1])
				self.AssertNotEqual(rgb_image[x,y][2], rgb_shuffled_image[x,y][2])

	def test_encrypt_swap(self):
		selectedImage = im.open("Cat.jpeg")
		rgb_image = selectedImage.load()
		rgb_switched_image = encrypt_swap(selectedImage, rgb_image)
		for x in range(theImage.size[0]):
			for y in range(theImage.size[1]):
				self.AssertEqual(rgb_image[x,y][0], rgb_switched_image[x,y][2])
				self.AssertEqual(rgb_image[x,y][1], rgb_switched_image[x,y][1])
				self.AssertEqual(rgb_image[x,y][2], rgb_switched_image[x,y][0])
	
	def test_encrypt_function(self):
		selectedImage = im.open("Curiosity.jpeg")
		rgb_image = selectedImage.load()
		rgb_shuffled_image = encrypt_function(selectedimage, rgb_image)
		for x in range(theImage.size[0]):
			for y in range(theImage.size[1]):
				self.AssertNotEqual(rgb_image[x,y][0], rgb_shuffled_image[x,y][0])
				self.AssertNotEqual(rgb_image[x,y][1], rgb_shuffled_image[x,y][1])
				self.AssertNotEqual(rgb_image[x,y][2], rgb_shuffled_image[x,y][2])

	def test_decrypt_shuffle(self):
		selectedImage = im.open("Shuffled.png")
		rgb_image = selectedImage.load()
		rgb_deshuffled_image = decrypt_shuffle(selectedImage, rgb_image)
		for x in range(theImage.size[0]):
			for y in range(theImage.size[1]):
				self.AssertEqual(rgb_image[x,y][0], rgb_deshuffled_image[x,y][0])
				self.AssertEqual(rgb_image[x,y][1], rgb_deshuffled_image[x,y][1])
				self.AssertEqual(rgb_image[x,y][2], rgb_deshuffled_image[x,y][2])

	def test_decrypt_swap(self):
		selectedImage = im.open("RGB.png")
		rgb_image = selectedImage.load()
		rgb_deswapped_image = decrypt_swap(selectedImage, rgb_image)
		for x in range(theImage.size[0]):
			for y in range(theImage.size[1]):
				self.AssertEqual(rgb_image[x,y][0], rgb_deswapped_image[x,y][0])
				self.AssertEqual(rgb_image[x,y][1], rgb_deswapped_image[x,y][1])
				self.AssertEqual(rgb_image[x,y][2], rgb_deswapped_image[x,y][2])
	
	def test_decrypt_function(self):
		#Image will pass test by final release
		selectedImage = im.open("Function.png")
		rgb_image = selectedImage.load()
		rgb_decrypted_image = decrypt_function(selectedImage, rgb_image)
		for x in range(theImage.size[0]):
			for y in range(theImage.size[1]):
				self.AssertEqual(rgb_image[x,y][0], rgb_decrypted_image[x,y][0])
				self.AssertEqual(rgb_image[x,y][1], rgb_decrypted_image[x,y][1])
				self.AssertEqual(rgb_image[x,y][2], rgb_decrypted_image[x,y][2])


if __name__ == '__main__':
	unittest.main()
