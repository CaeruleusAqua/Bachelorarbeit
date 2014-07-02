#!/usr/bin/env python2.7
import math

#Common
R5=1000.
R6=47000.
C2=82.0*(10**-9)
C4=82.0*(10**-9)
f=100
R1=2700
R3=150000

## Butterorth
Q=0.707
O=1.

A=1+(R6/R5)

w=2*math.pi*f

tmp=1/(2*w*O*Q)

print "C2: " + str(C2)
print "C4: " + str(C4)
print "R1: " + str(R1)

print "R3: " + str(R3)

Q=math.sqrt(R1*R3*C2*C4)/( C4*(R1+R3)+(R1*C2*(1-A) ))
O=1/(w*math.sqrt(R1*R3*C2*C4))


print "Omega_p: " + str(O)
print "Q: " + str(Q)
