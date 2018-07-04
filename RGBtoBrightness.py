from PIL import Image

# RGB mappings

def Average(RGB):
	return (RGB[0]+RGB[1]+RGB[2])/3

def Lightness(RGB):
	return (max(RGB)+min(RGB))/2

def Luminosity(RGB):
	return 0.21*RGB[0] + 0.72*RGB[1] + 0.07*RGB[2]

im = Image.open("ascii-pineapple.jpg")

if im != None:
	pix = im.load()
	width, height = im.size
	bright = [None]*(width*height)
	print(width)
	for col in range(width):
		for row in range(height):
			bright[width*row + col] = Average(pix[col,row])

	print("Successfully constructed brightness matrix!")
	print("Brightness matrix size: %d x %d "%(im.size[0],im.size[1]))
	print("Iterating through pixel brightness:")
	for row in range(height):
		for col in range(width):
			print(bright[width*row + col])
