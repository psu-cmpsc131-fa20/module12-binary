from sys import argv
with open(argv[1], encoding=argv[2]) as f:
  text = f.read()
  print(text)

