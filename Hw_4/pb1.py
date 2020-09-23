#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 12:43:23 2020

@author: aj3008
"""

#%%
import pb3
import math                                #libraries
import matplotlib.pyplot as plt
D=[10**4,10**5,10**6]
def func(k1,k2):
    def y(p,m,r):
        return([-k1*m*(p**(3.0/5))/(r**2),k2*(r**2)*(p**(3.0/5))])
    return(y)
for i in range(len(D)):
    P=(10**13)*((D[i]/2)**(5.0/3))
    k1=(6.6743*10**(-8))*2*((1.0/10**13)**(3.0/5))
    k2=4*math.pi*2*((1.0/10**13)**(3.0/5))
    y_0=10**(-6)                           #(initial values)
    x_0=P
    h=10**6
    k=10*10**3
    x,y,j=pb3.euler(x_0,y_0,func(k1,k2),h,k)
    plt.plot(j,x)
    plt.show()
    plt.clf()
    plt.plot(j,y)
    plt.show()
    plt.clf()