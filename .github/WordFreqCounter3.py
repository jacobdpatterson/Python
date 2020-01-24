import requests # - Needed for dealing with web pages.
from bs4 import BeautifulSoup # - Webcrawling tools
import operator

def start(url):
    word_list = []
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code, features="html.parser")
    for post_text in soup.find_all('a', {'class': 'poptip'}): # Get only the class poptip from a href entry.
        content = post_text.string # - Remove HTML
        words = content.split() # - Lower cases and splits a sentence to words by split on space
        for each_word in words: # - Goes through all the words in words.
            word_list.append(each_word) #adds a word to the array made in the beginning.
    clean_up_list(word_list)

def clean_up_list(word_list):
    clean_word_list = []
    for word in word_list:
        symbols = "!@#$%^&*()_+-={}[]:";'?></.,'""
        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], "")
        if len(word) > 0:
            print(word)
            clean_word_list.append(word)
    create_dictionary(clean_word_list)

def create_dictionary(clean_word_list):
    word_count = {}
    for word in clean_word_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    for key, value in sorted(word_count.items(), key=operator.itemgetter(1)):
        print(key, value)



start('https://www.baseball-reference.com/players/f/frazito01.shtml')

#Something here isn't working properly. Troubleshoot.

