from PIL import Image


def image(original_image_directory,max_side_length,resized_image_destination):
	"""
	a function to resize images.
	Args (img/path , img_size_in_px , destination/path)
	returns: a thumbnail (squared-resized) version of the given image to the specified destination
	"""
	# ~ #plug the image directory in here
	# ~ original_image_directory = ''
	
	# ~ #max side length in PIXELS
	# ~ max_side_length =
	
	# ~ #saving destination of the resized image
	# ~ resized_image_destination = ''
	#______________________________________________________________
	#open the image
	image = Image.open(original_image_directory)
	
	#reseize the image to the max side length
	image.thumbnail((max_side_length, max_side_length))
	
	#save the resized image to its proper directory
	image.save(resized_image_destination)
	

if __name__=="__main__":
	image("images/1.jpg",100,"images/resized_1.jpg")
	image("images/2.jpg",100,"images/resized_2.jpg")
	image("images/3.jpg",100,"images/resized_3.jpg")


