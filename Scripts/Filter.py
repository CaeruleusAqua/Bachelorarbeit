#!/usr/bin/env python2.7
import math

#Common
R5=1000.
R6=47000.
C2=82.0*(10**-9)
f=100

## Butterorth
Q=0.707
O=1.

A=1+(R6/R5)

tmp2=(C2*(1+(4*Q*Q*(A-1))))/(4*Q*Q)
print "C4 < " + str(tmp2)
print "C4 != " + str(C2*(A-1))
C4=82.0*(10**-9)
#C4=tmp2/2
#C4=100.0*(10**-9)
print "C4: " + str(C4)

## kreisfrequenz berechnen
w=2*math.pi*f

tmp=1/(2*w*O*Q)


R1=tmp*((C2+math.sqrt(C2*C2-4*Q*Q*C2*(C4+C2*(1-A))))/(C2*(C4-C2*(A-1))))
if R1 < 0:
  R1=tmp*((C2-math.sqrt(C2*C2-4*Q*Q*C2*(C4+C2*(1-A))))/(C2*(C4-C2*(A-1))))
  

R3=tmp*((C2+math.sqrt(C2*C2-4*Q*Q*C2*(C4+C2*(1-A))))/(C4*C2))
if R3 < 0:
  R3=tmp*((C2-math.sqrt(C2*C2-4*Q*Q*C2*(C4+C2*(1-A))))/(C4*C2))


print "C2: " + str(C2)
print "R1: " + str(R1)
print "R3: " + str(R3)

Q=math.sqrt(R1*R3*C2*C4)/( C4*(R1+R3)+(R1*C2*(1-A) ))

print "Q: " + str(Q)
