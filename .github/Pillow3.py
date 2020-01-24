from PIL import Image
from PIL import ImageFilter #Some filters for images

# - Assign image to pillow format

flower = Image.open("th.jpg")
mountain = Image.open("th-1.jpg")

# This changes the mode from RGB to Black and White

black_white = flower.convert("L") # L is Black and White
black_white.show() # - The mode is changed from RGB to Black and White. No more RGB channels.

blur = flower.filter(ImageFilter.BLUR) # - This blurs the image using the imported filter
blur.show()

detail = flower.filter(ImageFilter.DETAIL) # - This gets the detail of the image.
detail.show()

edges = flower.filter(ImageFilter.FIND_EDGES) # - Finds the edges and highlights.
edges.show()