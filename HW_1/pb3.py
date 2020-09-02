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
def f(xp,c):     #lens equation
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
c=(L**2)*r*N*D/(pi*(a**2))    #the constant next to the exponential
x=[]
x1=[]
for n in range(12):
    xp= 1 + 1*math.cos(n*pi/6)    #coordinates of the observer
    x1.append(xp)
    k,q=pb1.bisection(0,2,f(xp,c))
    x.append(k)                  #getinng the values of the points where it hits the lens
print(x)
print(x1)
plt.clf()
plt.gca().axes.get_yaxis().set_visible(False)
plt.xlabel("Distance of observer in AU")
for i in range(12):
    plt.plot([x1[i],x[i],0],[-2,0,2])    
plt.savefig("HW_1_pb3.png")

    
    
    