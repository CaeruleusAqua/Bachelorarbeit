#!/usr/bin/env python
import csv
import numpy as np
from optparse import OptionParser 
parser = OptionParser()

(optionen, args) = parser.parse_args()
data=np.genfromtxt(args[0] , delimiter=' ', dtype='int')

voltage=data[:,1]
distance=data[:,2]-data[:,1]
time=data[:,3]-data[:,2]
infrared=data[:,4]-data[:,3]
motor=data[:,5]-data[:,4]
imu=data[:,0]-data[:,5]
gesammt=(data[:,0])

#np.savetxt("voltage.csv",voltage, delimiter=",",fmt="%i")
#np.savetxt("distance.csv",distance, delimiter=",",fmt="%i")
#np.savetxt("ucTime.csv",time, delimiter=",",fmt="%i")
#np.savetxt("Infrared.csv",infrared, delimiter=",",fmt="%i")
#np.savetxt("motor.csv",motor, delimiter=",",fmt="%i")
#np.savetxt("imu.csv",imu, delimiter=",",fmt="%i")
#np.savetxt("gesammt.csv",gesammt, delimiter=",",fmt="%i")
print "Voltage Min: %s. Max %s Mean: %s Std: %s" % (min(voltage), max(voltage),voltage.mean(),voltage.std())
print "Distance Min: %s. Max %s Mean: %s Std: %s" % (min(distance), max(distance),distance.mean(),distance.std())
print "time Min: %s. Max %s Mean: %s Std: %s" % (min(time), max(time),time.mean(),time.std())
print "Infrared Min: %s. Max %s Mean: %s Std: %s" % (min(infrared), max(infrared),infrared.mean(),infrared.std())
print "motor Min: %s. Max %s Mean: %s Std: %s" % (min(motor), max(motor),motor.mean(),motor.std())
print "imu Min: %s. Max %s Mean: %s Std: %s" % (min(imu), max(imu),imu.mean(),imu.std())
print "gesammt Min: %s. Max %s Mean: %s Std: %s" % (min(gesammt), max(gesammt),gesammt.mean(),gesammt.std())

