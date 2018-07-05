from PIL import Image
from colorama import Fore, init
init()
import argparse
parser = argparse.ArgumentParser(description='script to turn images into ASCII-art')
parser.add_argument("filename")
parser.add_argument("-c","--color", help="ASCII art in glorious color", action='store_true')
parser.add_argument("-i","--invert", help="invert all the brightnesses", action='store_true')
parser.add_argument("-m","--map",type=int, choices=[0,1,2], help="brightness mappings: 0 for average, 1 for lightness, 2 for luminosity", default=0)
parser.add_argument("-ws","--width",type=int, help="width of the screen", default=210) # change the default values once you figure out 
parser.add_argument("-hs","--height",type=int, help="height of the screen",default=108)# the apt width and height for your terminal
args = parser.parse_args()

# RGB mappings

def Average(RGB):
	return (RGB[0]+RGB[1]+RGB[2])/3

def Lightness(RGB):
	return (max(RGB)+min(RGB))/2

def Luminosity(RGB):
	return 0.21*RGB[0] + 0.72*RGB[1] + 0.07*RGB[2]

def brightnessMapping(RGB, m):
	if m==0:
		return Average(RGB)
	elif m==1:
		return Lightness(RGB)
	else:
		return Luminosity(RGB)

# map Brightness(0,255) to custom ASCII(0,64)
def toASCII(b):
	chars =  "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
	slope = 64/255
	return chars[round(slope*b)]

# invert brightness
def invert(b):
	return 255-b

# reduce color by considering only the MSB
def reduceColor(RGB):
	i = RGB[0] >> 7
	j = RGB[1] >> 7
	k = RGB[2] >> 7
	return str(i)+str(j)+str(k)

def getReducedPixelColor(s):
	if s == "000":
		return Fore.BLACK
	elif s == "100":
		return Fore.RED 
	elif s == "010":
		return Fore.GREEN
	elif s == "110":
		return Fore.YELLOW
	elif s == "001":
		return Fore.BLUE
	elif s == "101":
		return Fore.MAGENTA
	elif s == "011":
		return Fore.CYAN
	else:
		return Fore.WHITE

im = Image.open(args.filename)

# rs > ri ? (wi * hs/hi, hs) : (ws, hi * ws/wi)
CMD_size = args.width,args.height
wi, hi = im.size

rs = args.width/args.height
ri = wi/hi
#fit image to screen retaining aspect ratio
new_size = (int(wi* args.height/hi), args.height) if rs > ri else (args.width, int(hi * args.width/wi))

r_im = im.resize(new_size, Image.ANTIALIAS)

if r_im != None:
	## Load your image’s pixel data into a 2-dimensional array

	pix = r_im.load()
	width, height = r_im.size
	#print(r_im.size)
	
	## Convert the RGB tuples of your pixels into single brightness numbers

	bright = [None]*(width*height)
	pixColor = [None]*(width*height)
	for col in range(width):
		for row in range(height):
			bright[width*row + col] = invert(brightnessMapping(pix[col,row], args.map)) if args.invert else brightnessMapping(pix[col,row], args.map)
			pixColor[width*row + col] = reduceColor(pix[col,row])
	
	## Convert brightness numbers to ASCII characters

	asciiMatrix = [None]*(width*height)
	for col in range(width):
		for row in range(height):
			asciiMatrix[width*row + col] = toASCII((bright[width*row + col]))

	## Print image

	for row in range(height):
		for col in range(width):
			for i in range(3): #image looks squahed: so printing each character 3 times
				print((getReducedPixelColor(pixColor[width*row + col]) if args.color else '') + str(asciiMatrix[width*row + col]),end="")
		print("")