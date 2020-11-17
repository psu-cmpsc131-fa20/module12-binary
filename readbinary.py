from sys import argv

with open(argv[1],'rb') as f:
  data = f.read()
  print(data.decode())