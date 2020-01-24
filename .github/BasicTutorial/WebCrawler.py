# This one needs work.

import requests
from bs4 import BeautifulSoup


# I imported beautifulsoup4

# Make core spider

def trade_spider(max_pages):
    page = 120
    while page < max_pages:
        url = 'https://sfbay.craigslist.org/search/apa?s=' + str(page) # When page changes, so does the website.
        source_code = requests.get(url) # Gets the stuff on the page
        plain_text = source_code.text # Gets the text from the stuff.
        soup = BeautifulSoup(plain_text) # Turns the text into a soup object (more managable).
        for link in soup.findAll('a', {'class': 'data_id'}): #Item name was a class. Gets all the item-names.
            href = link.get('href')
            print(href)
        page += 120

trade_spider(240)