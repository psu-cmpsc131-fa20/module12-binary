from sys import argv

with open(argv[1],'wb') as f:
  for i in range(10):
    f.write((-i).to_bytes(4,'little', signed=True))