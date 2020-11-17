from sys import argv

with open(argv[1],'wb') as f:
  for i in range(1024,1024+10):
    f.write(i.to_bytes(4,'big'))