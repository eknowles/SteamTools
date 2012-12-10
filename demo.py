#!/usr/bin/python
import os
import re
import struct
import binascii
import codecs


#packed_data = binascii.unhexlify(dem)
#struct.unpack_from(dem)

f = codecs.open("demo.dem", "rb", "hex")
for LINE in f.read():
    print LINE
f.close()
        