#!/usr/bin/env python
import csv
import numpy as np
import matplotlib.pyplot as plt
from optparse import OptionParser 
parser = OptionParser()

(optionen, args) = parser.parse_args()
data=np.genfromtxt(args[0] , delimiter=',', dtype='float')
plt.plot(data*15, 'r-')

plt.show()
print data.shape