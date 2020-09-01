#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 17:46:08 2020

@author: aj3008
"""

#%%
import pb1
from astropy import units as u
import math
import matplotlib.pyplot as plt
def f(xp):
    c=16.8324
    def y(x):
        return(x*(1+c*math.exp(-x)**2)-xp)
    return(y)
L=21*u.cm
L=L.to(u.AU)
r=2.817*10**(-15)*u.meter
r=r.to(u.AU)
N=0.01*u.parsec*(u.cm)**(-3)
N=N.to(u.AU**(-2))
D=1*u.kiloparsec
D=D.to(u.AU)
pi=3.14
a=1*u.AU
c=16.8324
x=[]
x1=[]
for n in range(12):
    xp= 1 + 1*math.cos(n*pi/6)
    x1.append(xp)
    k,q=test.bisection(0,2,f(xp))
    x.append(k)
print(x)
print(x1)
for i in range(12):
    plt.plot([x1[i],x[i],0],[-2,0,2])
    
    
    