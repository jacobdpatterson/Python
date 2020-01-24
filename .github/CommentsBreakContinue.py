magicnumber = 26


# Magic numbers are rad!

'''
for n in range(101):
    if n is magicnumber:
        print()
'''

print(9, "Bucky")
# This adds Bucky to 9

for n in range(101):
    if n is magicnumber:
        print(n, " is magic number.")
        break
    else:
        print(n, " is not magic number.")

for n in range(101):
    if (n > 0) and (n % 4 == 0):
        print(n, " is a multiple of 4.")
