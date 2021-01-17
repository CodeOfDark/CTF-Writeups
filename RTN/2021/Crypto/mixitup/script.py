from PIL import Image

def mixitup():
	firstImage = Image.open("image1.bmp")
	secondImage = Image.open("image2.bmp")

	(width, height) = firstImage.size

	resultImage = Image.new( 'RGB', (width, height)) 
	resultImagePixels = resultImage.load()

	firstImagePixels = firstImage.load()
	secondImagePixels = secondImage.load()

	for width in range(0, width):
		for height in range(0, height):
			r = firstImagePixels[width, height][0] ^ secondImagePixels[width, height][0]
			g = firstImagePixels[width, height][1] ^ secondImagePixels[width, height][1]
			b = firstImagePixels[width, height][2] ^ secondImagePixels[width, height][2]
			resultImagePixels[width, height] = (r, g, b)

	return resultImage


mixitup().save("result.bmp", "bmp")