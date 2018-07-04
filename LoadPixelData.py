from PIL import Image

im = Image.open("ascii-pineapple.jpg")

if im != None:
	pix = im.load()
	print("Successfully constructed pixel matrix!")
	print("Pixel matrix size: %d x %d "%(im.size[0],im.size[1]))
	print("Iterating through pixel contents:")
	width, height = im.size
	#for x in range(width):
	#	for y in range(height):
	#		print(pix[x,y])
