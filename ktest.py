__author__ = 'karlp'

import usbtmc
import struct

data = [65,66,67,68]
packed = struct.pack(">%dh" % len(data), *data)
x = usbtmc.pack_ieee4882(packed)
z = [ord(y) for y in x]
print(z)
print(len(x))
print(x)
