#!/usr/bin/env python 
import numpy as np
import pandas

import json, matplotlib 
s = json.load( open("bmh_matplotlibrc.json") )
matplotlib.rcParams.update(s)

import matplotlib.pyplot as plt

def rolling_window(a, window):
    """Creates an efficient rolling window of a with numpy stride magic.
    @param a
    @param window
    @see http://www.rigtorp.se/2011/01/01/rolling-statistics-numpy.html
    """
    shape = a.shape[:-1] + (a.shape[-1] - window + 1, window)
    strides = a.strides + (a.strides[-1],)
    return np.lib.stride_tricks.as_strided(a, shape=shape, strides=strides)

def rolling_func(func,data, window):
    """Apply func to rolling windows. Deals with end point problem by applying different window sizes.
    @param func - Function to be applied to rolling(/moving/sliding) windows. 
                  Must be applicable to one- and two-dimensional data. 
                  Must have axis parameter that behaves as in np.mean.
                  Must be able to deal with different window sizes.

    @param data - data to which func should be applied
    @param window - size of window
    """
    rolling_mean = func(rolling_window(data, window), axis=1)
    
    # How much items in front and behind of item
    # are part of the rolling window for each element?
    n_front = window//2
    n_behind = window//2 - 1 + window%2
    
    # use different windows for endpoints where no complete window can be applied

    endpoints_front = np.zeros(n_front)
    for i in range(n_front):
        # window as large as possible but with maximal n_behind elements after current element inside window
        endpoints_front[i]=func(data[:1+n_behind+i])
        
    endpoints_behind = np.zeros(n_behind)
    for i in range(n_behind):
        # window as large as possible but with maximal n_front elements in front of current element inside window
        endpoints_behind[-(1+i)]=func(data[-(1+n_front+i):])
    
    # add endpoints
    return np.hstack([endpoints_front,rolling_mean,endpoints_behind])

def rolling_mean(data, window):
    return rolling_func(np.mean,data,window)

def rolling_std(data, window):
    return rolling_func(np.std,data,window)



odom=pandas.read_pickle("merged.pkl")
speed=np.array(odom[["speed"]])
winkel=np.array(odom[["orientation_from_marker"]])
print odom.index.values


mean=rolling_mean(speed[:,0],500)



plt.plot(odom.index.values,speed[:,0], 'g')
plt.plot(odom.index.values,mean, 'b')
plt.plot(odom.index.values,winkel, 'r')
#plt.plot(time[sel],current_list[sel,1] , 'g')
#plt.plot(time[sel],mean[sel] , 'r' ,linewidth=1.0)
#plt.plot(time[sel],mean2[sel] , 'r' ,linewidth=1.0)  
#plt.yticks(np.arange(-10,100,10))
#plt.plot(np.array(ges_current_list[:count])-np.array(current_list[:count]))
plt.show()