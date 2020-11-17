import csv
with open('comma.csv', newline='') as f:
  csvreader = csv.reader(f)
  for row in csvreader:
    print(row)