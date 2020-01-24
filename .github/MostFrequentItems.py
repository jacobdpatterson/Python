from collections import Counter

text = "This is cool. Whatever. La la la. I'm up late AF on Wednesday. Woohoo! Lego! Lego my eggo!"

# - Need to convert words into list

words = text.split() # This is the list split into words.
print(words)


# - Prints out three most common words

counter = Counter(words)
top_three = counter.most_common(3)
print(top_three)