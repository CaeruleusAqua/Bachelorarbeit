#!/usr/bin/env python2.7
import math

C2=100*(10**-9)
f=150

A=47
Q=0.707
O=1
C1=(C2*(1+(4*Q*Q*(A-1))))/(4*Q*Q)
tmp2=(C2*(1+(4*Q*Q*(A-1))))/(4*Q*Q)
print "C1 < " + str(tmp2)
C1=2*(10**-6)
w=2*math.pi*f
tmp=1/(2*w*O*Q)
R1=tmp*(C2+math.sqrt(C2*C2-4*Q*Q*C2*(C1+C2*(1-A)))/(C2*(C1-C2*(A-1))))
if R1 < 0:
  R1=tmp*(C2-math.sqrt(C2*C2-4*Q*Q*C2*(C1+C2*(1-A)))/(C2*(C1-C2*(A-1))))
R2=tmp*(C2+math.sqrt(C2*C2-4*Q*Q*C2*(C1+C2*(1-A)))/(C1*C2))
if R2 < 0:
  R2=tmp*(C2-math.sqrt(C2*C2-4*Q*Q*C2*(C1+C2*(1-A)))/(C1*C2))

print "C1: " + str(C1)
print "C2: " + str(C2)
print "R1: " + str(R1)
print "R2: " + str(R2)
