from sys import argv
import random
with open(argv[1], 'wb') as f:
  f.write(b'\x01\x02\x03\x04\x05\xf0\xf1\xf2')
