from PIL import Image


def image(original_image_directory,max_side_length,resized_image_destination):
	"""a function to resize images.
	parameters are described below"""
	# ~ #plug the image directory in here
	# ~ original_image_directory = ''
	
	# ~ #max side length
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
	image("images\\email.png",30,"images\\resized_email.png")
	image("images\\twitter.png",27,"images\\resized_twitter.png")
	image("images\\web.jpg",25,"images\\resized_web.jpg")
