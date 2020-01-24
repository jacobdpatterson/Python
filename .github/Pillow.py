#imported Pillow

from PIL import Image

img = Image.open("th.jpg") # - Opens and converts to pillow object.


print(img.size)
print(img.format)
img.show() # - This displays your image with your default program. Won't display in Command Prompt. Creates temp image.

# - Cropping Images

area = (100, 100, 200, 170) # - Don't crop outside main image area.
cropped_img = img.crop(area) # - This takes a four-digit touple.
cropped_img.show()


# - Combining images together

flower = Image.open("Th.jpg")
rock = Image.open("Th-1.jpg")

print(flower.size)
print(rock.size)

area = (100,100,332,274) # - The last two minus the first two has to equal the picture pasting to (232,174)
rock.paste(flower, area) # Rock crop will be pasted on top of flower.

rock.show() # - Shows the rock

# - Breaking up images into channels (Red, Green, Blue)

print(rock.mode) # Is this three channels or four?
r, g, b = rock.split() #Stores red green and blue channels.

r.show() # - Red channel (or band)
g.show() # - Green channel (or band)
b.show() # - Blue Channel (or band)

new_img = Image.merge("RGB", (b,r,g)) # - RGB is mode, red, then green, then blue
new_img.show()

# - You can mix and match two images

r1, g1, b1 = flower.split() # Split channels for flower

new_img2 = Image.merge("RGB", (b1,r1,g1)) # - RGB is mode, red, then green, then blue
new_img2.show()

# - Technically you can merge two images, but you have to be careful about their sizes.

# new_img = Image.merge("RGB", (b,r1,g)) # - RGB is mode, red, then green, then blue
# new_img.show()

