from PIL import Image

# - Assign image to pillow format

flower = Image.open("th.jpg")
mountain = Image.open("th-1.jpg")

# - Shows image

flower.show()

#- Re-sizes image

square_flower = flower.resize((250,250))

# - Image is now resized.

square_flower.show()

# - Here's how you flip (or transpose) left to right

flip_square_flower = square_flower.transpose(Image.FLIP_LEFT_RIGHT)
flip_square_flower.show()

# - And again top to bottom

flip_square_flower = square_flower.transpose(Image.FLIP_TOP_BOTTOM)
flip_square_flower.show()

# - Rotating

spin_square_flower = square_flower.transpose(Image.ROTATE_90)
spin_square_flower.show()
spin_square_flower = square_flower.transpose(Image.ROTATE_180)
spin_square_flower.show()
spin_square_flower = square_flower.transpose(Image.ROTATE_270)
spin_square_flower.show()