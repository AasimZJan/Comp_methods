#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 22:01:25 2020

@author: aj3008
"""

#%%
#importing packages
from astropy import units as u                 #for units
from astropy import constants as const         #for Gravitational constant
import math                                    #for the log function
import matplotlib.pyplot as plt                #for plotting


c=15
v_2=160*(10**3)*u.m/u.s
r_2=230*u.kiloparsec
r_2=r_2.to(u.m)
G=const.G




def y(r,c,r_2,v_2): #v==vc**2
    x=r/r_2
    num=math.log(1+c*x)-(c*x/(1+c*x))
    den=math.log(1+c)-c/(1+c)
    v=(((v_2)**2)/x)*num/den
    return(v)
def Menc(r,v,G):
    num=r*v
    return(num/G)
    
r=10*u.kiloparsec
r=r.to(u.m)
a=10*u.kiloparsec
a=a.to(u.m)
r_m=[]
v_m=[]
Me_m=[]
for i in range(1000):
    r_m.append(r/(1*u.m))
    print(r/(1*u.m))
    v=y(r,c,r_2,v_2)
    print(v/(1*u.m**2/u.s**2))
    v_m.append(v/(1*u.m**2/u.s**2))
    Men=Menc(r,v,G)
    print(Men/(1*u.kg))
    Me_m.append(Men/(1*u.kg))
    r=r+a
plt.plot(r_m,Me_m)

    
    
    




#%%
def v(c,r_2,v_2): 
    def y(r,c,r_2,v_2):
        x=float(r)/r_2
        v=(((v_2)**2)/x)*((math.log(1+c*x)-(c*x/(z+c*x)))/(math.log(1+c)-c/(1+c)))
        return(v)
    return(y)