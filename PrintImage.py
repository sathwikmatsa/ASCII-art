from PIL import Image

# RGB mappings

def Average(RGB):
	return (RGB[0]+RGB[1]+RGB[2])/3

def Lightness(RGB):
	return (max(RGB)+min(RGB))/2

def Luminosity(RGB):
	return 0.21*RGB[0] + 0.72*RGB[1] + 0.07*RGB[2]

# scale down Brightness(0,255) to custom ASCII(0,64)
def toASCII(b):
	chars =  r'`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$'
	slope = 66/255
	return chars[round(slope*b)]

im = Image.open("ascii-pineapple.jpg")

if im != None:
	pix = im.load()
	width, height = im.size
	bright = [None]*(width*height)
	for col in range(width):
		for row in range(height):
			bright[width*row + col] = Average(pix[col,row])

	asciiMatrix = [None]*(width*height)
	for col in range(width):
		for row in range(height):
			asciiMatrix[width*row + col] = toASCII(bright[width*row + col])

	for row in range(height):
		for col in range(width):
			for i in range(3): #problem 1 - image looks squahed: so printing each character 3x
				print(asciiMatrix[width*row + col],end="")
		print("")
