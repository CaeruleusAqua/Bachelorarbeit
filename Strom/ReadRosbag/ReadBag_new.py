#!/usr/bin/env python 
import rosbag
import numpy as np


import json, matplotlib 
s = json.load( open("bmh_matplotlibrc.json") )
matplotlib.rcParams.update(s)

import matplotlib.pyplot as plt


counter=0
ges_current=0

ref_voltage=5.08
gain=5.7
shunt_res=0.2
accu_voltage=1 #14,9

current_list=list()
time=list()
starttime=None

for topic, msg, t in rosbag.Bag('ohneSR.bag').read_messages():
    # This also replaces tf timestamps under the assumption 
    # that all transforms in the message share the same timestamp
    #print ges_current
   # print topic
    if topic=="/sensors/current":
        counter+=1
        ges_current+=msg.data
    elif topic=="/sensors/voltage":
        accu_voltage=msg.data    
        if counter!=0:
            if starttime is None:
                starttime=t.to_sec()
                
            t=(t.to_sec()-starttime)
            current_list.append((t,msg.data*(ges_current/counter)))
            counter=0
            ges_current=0

current_list=np.array(current_list)

np.save("current_nsr.npy", current_list)



        
        