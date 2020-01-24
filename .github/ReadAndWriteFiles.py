fw = open('sample.txt', 'w') # This means open (or create) a file and write to it
fw.write('Writing some stuff in my text file.\n\n')
fw.write('Lah de dah.')
fw.close()

# - This creates a text file for you.

fr = open('sample.txt', 'r')
text = fr.read()
print(text)
fr.close()