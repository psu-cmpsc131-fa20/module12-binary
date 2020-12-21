import json
import pickle
from sys import argv
with open(argv[1]) as f:
  data = json.load(f)
  print(data)
with open(argv[2], 'wb') as output:
  pickle.dump(data, output)