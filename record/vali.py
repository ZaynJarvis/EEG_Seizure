import sys
import csv
s = set()
c = 0
with open(f'./{sys.argv[1]}/manifest.csv', 'r+') as f:
    r = csv.DictReader(f)
    for row in r:
        s.add((row['originalFreq'], row['fileID'], row['patientID'],
               row['sessionID']))
        c += 1
    d = {}
    for i in s:
        d[i[0]] = d.get(i[0], 0) + 1
    from functools import reduce
    a = d
    print(a)
    print(reduce(lambda x, p: x + p, a.values(), 0))