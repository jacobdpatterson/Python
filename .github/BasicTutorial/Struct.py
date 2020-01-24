# -  Can convert data to bytes. Useful for networking.

# - Imports the structs functionality.
from struct import *

# - Store data as bytes

packed_data = pack('iif', 6, 19, 4.73) # - storing two integers and a float. Type of data and data itself.
print(packed_data) # - Printing out in Byte format. This is what it looks like over the network.

# - File types and what it takes to send them.

print(calcsize('i')) # - One integer
print(calcsize('f')) # - One integer
print(calcsize('iif')) # - Two integers, one float

# - Convert byte data into readable form

original_data = unpack('iif', packed_data) # - What to unpack, the packed data
print(original_data)

# - Can also do it this way with the raw data.

print(unpack('iif', b'\x06\x00\x00\x00\x13\x00\x00\x00)\\\x97@'))