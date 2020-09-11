#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 22:01:25 2020

@author: aj3008
"""

#%%
#importing packages
from astropy import units as u                 #for units
from pb_1 import midpoint                       #integrator
import math                                    #for the log function
import matplotlib.pyplot as plt                #for plotting

#defining constants
c=15
v_2=160*u.km/u.s
r_2=230*u.kiloparsec
G=(4.3*10**(-3))*(u.parsec*u.km**2)/(u.Msun*u.s**2)
###
###Function returns V_c**2(where V_c is circular velocity)
def y(r,c,r_2,v_2): #v==vc**2                  #Arguments(Radial distance=r, concentration factor=c, 
                                               #Virial radius=r_2, Speed at r_2=v_2 )
    x=r/r_2
    num=math.log(1+c*x)-(c*x/(1+c*x))
    den=math.log(1+c)-c/(1+c)
    v=(((v_2)**2)/x)*num/den                   #the equation
    return(v)
###
###function returns Mass enclosed              #Arguments(Radial distance=r, V_c=v, Gravitational constant=G)
def Menc(r,v,G):
    num=r*v
    return(num/G)

def Menc_1(v,G):
    v=v*((1*u.s**2)/(1*u.km**2))
    G=G/(1*(u.parsec*u.km**2)/(u.Msun*u.s**2))
    def y(x):
        return(x*v/G)
    return(y)
    
r=10*u.kiloparsec                              #initialising to get Menc and V_c values at different r and plotting them
a=10*u.kiloparsec                              #increments in r
r_m=[]
v_m=[]
Me_m=[]
for i in range(10):                          #change range r to plot for different values
    r_m.append(r/(1*u.kiloparsec))
    v=y(r,c,r_2,v_2)
    v_m.append(v/(1*u.km**2/u.s**2))
    Men=Menc(r,v,G)
    Me_m.append(Men/(1*u.Msun))
    r=r+a
plt.plot(r_m,Me_m)
###
###Total mass of the  halo
r=300*u.kiloparsec
v=y(r,c,r_2,v_2)
M=Menc(r,v,G)
print("The mass of the Halo is",M_H)
###
###Amount of mass in a little shell
Del_r=5*u.kiloparsec                           #take whatever you want
r=10*u.kiloparsec                              #point at which you wann calculate
a=(r-Del_r)/(1*u.kiloparsec)
b=(r+Del_r)/(1*u.kiloparsec)
v=y(r,c,r_2,v_2)
M_r=midpoint(Menc_1(v,G),a,b,2)
###
###Amount of mass in a little shell
Del_r=5*u.kiloparsec 
r=10*u.kiloparsec  
M_r1=Menc(r+Del_r,y(r+Del_r,c,r_2,v_2),G)-Menc(r-Del_r,y(r-Del_r,c,r_2,v_2),G)
###dM/dr
def df(r,h):
    Del_r=5*u.kiloparsec
    c=15
    v_2=160*u.km/u.s
    r_2=230*u.kiloparsec
    G=(4.3*10**(-3))*(u.parsec*u.km**2)/(u.Msun*u.s**2)
    M1=Menc(r+Del_r,y(r,c,r_2,v_2),G)-Menc(r-Del_r,y(r,c,r_2,v_2),G)
    M2=Menc(r+h+Del_r,y(r+h+Del_r,c,r_2,v_2),G)-Menc(r+h-Del_r,y(r+h-Del_r,c,r_2,v_2),G)
    print(M2)
    return((M2-M1)/h)
h=0.00001*u.kiloparsec
print(df(r,h))




#%%
def v(c,r_2,v_2): 
    def y(r,c,r_2,v_2):
        x=float(r)/r_2
        v=(((v_2)**2)/x)*((math.log(1+c*x)-(c*x/(z+c*x)))/(math.log(1+c)-c/(1+c)))
        return(v)
    return(y)