import json
import pickle
from sys import argv
with open(argv[1], 'rb') as f:
  data = pickle.load(f)
  print(data)
with open(argv[2], 'w') as output:
  json.dump(data, output)