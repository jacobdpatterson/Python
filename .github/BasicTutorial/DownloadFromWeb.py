import random
# - For random numbers
import urllib.request
# - For somehow interacting with the internet.

def download_web_image(url):
    name = random.randrange(1, 1000)
    full_name = str(name) + ".jpeg" # - Converts the number to a string
    urllib.request.urlretrieve(url, full_name)

download_web_image("http://picjumbo.com/download?d=IMG-3712.jpg&n=bench-with-the-view-in-austrian-mountains&id=1") # - An image i found on web.

# The above code creates a jpeg file from what's downloaded from the internet. Bit of a work in progress. 