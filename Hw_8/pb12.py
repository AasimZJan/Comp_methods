#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 08:29:30 2020

@author: aj3008
"""
#%%
#---------------------------------------importing libraries-------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt 

data=np.load("strain.npy")#data each a minute apart
time=[i/(60*24) for i in range(len(data))]#time for each data point 
plt.plot(time,data)
plt.show()
N=len(data)
Nr=int(np.sqrt(N))
f=[0 for i in range(N)]

for k1 in range(Nr):
    k2=0
    print(k1,k2)
    suma=0
    for j2 in range(Nr):
        sum=0
        for j1 in range(Nr):
            factor=(np.exp(2*3.14j*j1*k1/Nr))*data[j1*Nr+j2]
            sum=sum+factor
        suma=suma+(np.exp(2*3.14j*j2*(k2*Nr+k1)/N))*sum
        
        f[k2*Nr+k1]=suma
for k1 in range(Nr):
    for k2 in range(Nr):
        f[k1+k2*Nr]=f[k1]

    