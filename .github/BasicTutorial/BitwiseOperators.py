# -------- BINARY AND --------------

a = 50 #110010
b = 25 #011001
# - 010000 - Only ones on both sides are ones. all the rest zeroes. this is 16.
c = a & b
print(c)

#---------- BINARY RIGHT SHIFT ----------

x = 240 # 11110000
y = x >> 2 # shifts every bit two spots to the right #00111100. That's 60.

