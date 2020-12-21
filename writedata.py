from sys import argv
import json

with open(argv[1], 'w') as f:
  t = [1,2,3,4]
  d = {'a':1, 'b':2, 'c':[3,4,5]}
  json.dump(t,f)
  json.dump(d,f)

