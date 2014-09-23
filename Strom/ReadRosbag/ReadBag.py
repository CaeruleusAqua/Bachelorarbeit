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

ges_current_list=list()
current_list=list()
time=list()
starttime=None

for topic, msg, t in rosbag.Bag('voltage.bag').read_messages():
    # This also replaces tf timestamps under the assumption 
    # that all transforms in the message share the same timestamp
    #print ges_current
   # print topic
    if topic=="/ges_current":
        counter+=1
        ges_current+=msg.data
    elif topic=="/sensors/voltage":
        accu_voltage=msg.data
    else:        
        if counter!=0:
            if starttime is None:
                starttime=t.to_sec()
                
            t=(t.to_sec()-starttime)
            current_list.append((t,msg.data*accu_voltage))

            ges_current_=(((((float(ges_current)/counter)/1024.)*ref_voltage)/gain)/shunt_res)*accu_voltage
            ges_current_list.append((t, ges_current_))
            counter=0
            ges_current=0

ges_current_list=np.array(ges_current_list)
current_list=np.array(current_list)

np.save("ges_current_list.npy", ges_current_list)
np.save("current_list.npy", current_list)



        
        