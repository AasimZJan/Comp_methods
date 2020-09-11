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
c=35
v_2=160*u.km/u.s
r_2=230*u.kiloparsec
G=(4.3*10**(-3))*(u.parsec*u.km**2)/(u.Msun*u.s**2)
###
###Function returns V_c**2(where V_c is circular velocity)
def y(r,c,r_2,v_2): #v==vc**2                  #Arguments(Radial distance=r, concentration factor=c, 
                                               #Virial radius=r_2, Speed at r_2=v_2 )
    x=r/r_2
    num=math.log(1+c*x)-((c*x)/(1+c*x))
    den=math.log(1+c)-(c/(1+c))
    v=(((v_2)**2)/x)*(num/den)                   #the equation for v_c**2
    return(v)
###
###function returns Mass enclosed              #Arguments(Radial distance=r, V_c=v, Gravitational constant=G)
def Menc(r,v,G):                               #gives a value
    num=r*v
    return(num/G)

def Menc_1(v,G):                               #Gives a function in terms of r
    v=v*((1*u.s**2)/(1*u.km**2))
    G=G/(1*(u.parsec*u.km**2)/(u.Msun*u.s**2))
    def y(x):
        return(x*v/G)
    return(y)
###finding mass enclosed at different r(this part is self contained except it doesn't have constants)
r=10*u.kiloparsec                              #initialising to get Menc and V_c values at different r and plotting them
a=10*u.kiloparsec                              #increments in r(adding it to r in a loop and getting Menc)
r_m=[]
v_m=[]
Me_m=[]
for i in range(1000):                          #change range to plot for different ranges
    r_m.append(r/(1*u.kiloparsec))             #had to make them dimensionless to make a plot
    v=y(r,c,r_2,v_2)
    v_m.append(v/(1*u.km**2/u.s**2))
    Men=Menc(r,v,G)
    Me_m.append(Men/(1*u.Msun))
    r=r+a
plt.title("Variation of Mass enclosed with distance")
plt.xlabel("Radial distance in kiloparsec")
plt.ylabel("Mass enclosed in Msun")
plt.plot(r_m,Me_m)
plt.savefig("/Users/aj3008/Desktop/MS_3rd_Sem/Comp_methods_in_AST/Comp_methods/HW_2/Images/pb2plot1")
###
###Total mass of the  halo
r=300*u.kiloparsec                            #I was informed to calculate at that point
v=y(r,c,r_2,v_2)
M=Menc(r,v,G)
print("The mass of the Halo is",M)
###
###Amount of mass in a little shell(using midpoint)(just to test if the approximation is good)
Del_r=0.5*u.kiloparsec                          #take whatever you want
r=250*u.kiloparsec                            #point at which you wanna calculate, I took it to be 250kpc
a=(r-Del_r)/(1*u.kiloparsec)                  #inner boundary of shell
b=(r+Del_r)/(1*u.kiloparsec)                  #outer boundary of shell
v=y(r,c,r_2,v_2)
M_r=midpoint(Menc_1(v,G),a,b,2)
###
###Amount of mass in a little shell
Del_r=0.5*u.kiloparsec                        #half of the thickness of shell
r=300*u.kiloparsec                          #location of shell
M_r1=Menc(r+Del_r,y(r+Del_r,c,r_2,v_2),G)-Menc(r-Del_r,y(r-Del_r,c,r_2,v_2),G)
print("Mass in a little shell",M_r1)
###dM/dr
def df(r,h,c,v_2):
    Del_r=0.5*u.kiloparsec
    r_2=230*u.kiloparsec
    G=(4.3*10**(-3))*(u.parsec*u.km**2)/(u.Msun*u.s**2)
    M1=Menc(r+Del_r,y(r+Del_r,c,r_2,v_2),G)-Menc(r-Del_r,y(r-Del_r,c,r_2,v_2),G)
    M2=Menc(r+h+Del_r,y(r+h+Del_r,c,r_2,v_2),G)-Menc(r+h-Del_r,y(r+h-Del_r,c,r_2,v_2),G)
    return((M2-M1)/h)
h=0.00001*u.kiloparsec
print("the value of dM(r)/dr at",r,"is",df(r,h,c,v_2))
print("value of v_200 and c is",v_2,c)




