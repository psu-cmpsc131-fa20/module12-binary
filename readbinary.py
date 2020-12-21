from sys import argv
with open(argv[1], 'rb') as f:
  data = f.read(4)
  while data != b'':
    i = int.from_bytes(data, 'little', signed = True)
    print(i)
    data = f.read(4)
