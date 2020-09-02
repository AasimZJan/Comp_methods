#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 11:01:28 2020

@author: aj3008
"""

#%%
#problem 6
import matplotlib.pyplot as plt
import numpy as np
#importing interpolator from problem 5
from pb5 import interpolator     
#extracting data
data = np.loadtxt('lens_density.txt',delimiter=',',skiprows=1)   #make sure to check the file path
x=data[:,0]
y=data[:,1]
#generating the points we are interested in
xp=[]
for i in range(len(x)-1):
    xp.append(0.5*(x[i]+x[i+1]))
#calling the interpolator
yp=interpolator(x,y,xp)
print(yp)
#plotting
plt.xlabel("interested x values")
plt.ylabel("Corresponding y valuesls")
plt.title("Interpolated points")
plt.plot(xp,yp,marker='o')
plt.savefig("HW_1_pb6.png")



    
