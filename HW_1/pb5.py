#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 11:00:53 2020

@author: aj3008
"""

#%%
#interpolator
def interpolator(x,y,a):
    #calculationg slope since it is linear interpolation
    yp=[]
    for i in range(len(x)-1):
        m=(y[i+1]-y[i])/(x[i+1]-x[i])              
        yp.append(m*(a[i]-x[i])+y[i])
    #When you call this function you get a function when inputted a point gives you the interpolated y values
    return(yp)                     
    

    
    