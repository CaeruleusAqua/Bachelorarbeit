#!/usr/bin/env python
import csv
import numpy as np
from optparse import OptionParser 
parser = OptionParser()
data=list()
(optionen, args) = parser.parse_args()
with open(args[0], 'rb') as csvfile:
  spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
  for row in spamreader:
    data.append(int(row[0]))
data=np.array(data)
print min(data)
print max(data)
print data.std()
print data.mean()