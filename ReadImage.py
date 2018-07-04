from PIL import Image

im = Image.open("ascii-pineapple.jpg")

if im != None:
	print("Successfully loaded image!")
	print("Image size: %d x %d "%(im.size[0],im.size[1]))
