#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 16:53:45 2020

@author: aj3008
"""

#%%
import pb3
import math                                #libraries
import matplotlib.pyplot as plt
def func(G,c,l):
    def y(p,m,r):
        return([(-G*m*p**(3.0/5)/(l**(3.0/5)*(r**2)))*(1+p**(2.0/5)*l**(3/5)/c**(2))*(1+4*math.pi*r**(3)*p/(m*c**(2)))*(1-2*G*m/(r*c**2))**(-1),4*math.pi*r**(2)*p**(3/5)/l**(3.0/5)])
    return(y)
D=[10**14,10**15,10**16]
G=6.6743*10**(-8)
c=3*10**10
l=5.4*10**9
for i in range(len(D)):
    P=l*(D[i]**(5.0/3))
    print(P)
    y_0=10**(-6)                           #(initial values)
    x_0=P
    h=10**4
    k=4*10**2
    p,m,r=pb3.rk(x_0,y_0,func(G,c,l),h,k)
    plt.plot(r,p)
    plt.show()
    plt.clf()
    plt.plot(r,m)
    plt.show()
    plt.clf()
    
    