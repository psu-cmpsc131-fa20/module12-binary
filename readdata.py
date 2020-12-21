from sys import argv
import json
with open(argv[1]) as f:
  t = json.load(f)
  print(t)
