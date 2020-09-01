#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 11:01:28 2020

@author: aj3008
"""

#%%
#problem 6
from pb5 import interpolator
x=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
y=[0.0,0.0,0.001,0.008,0.030,0.065,0.103,0.130,0.140,0.132,0.113,0.089,0.066,0.0460,.030,0.019,0.012,0.007,0.004,0.002,0.001]
xp=[0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5,10.5,11.5,12.5,13.5,14.5,15.5,16.5,17.5,18.5,19.5]
yp=[]
for i in range(len(xp)):
    l=interpolator(x[i+1],y[i+1],x[i],y[i])
    yp.append(l(xp[i]))
print(yp)

    
#%%
#trying out interpolator
from pb5 import interpolator
y=interpolator(0,5,1,10)
x=[1,2,0.5]

    
    
