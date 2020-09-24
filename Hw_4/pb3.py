#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 19:55:05 2020

@author: aj3008
"""

#%%
#libraries
import pb2 
import RK                            #for RK-4 method
import math                                
import matplotlib.pyplot as plt
###
###
def func(G,c,l):
    """Function returns an array where the first element is dP/dr(TOV) and second one is dM/dr. The variables of the returned functions are P, Menc and r.
    The arugments of this function are:
        G= Gravitational constant,
        c= speed of light,
        l= K(the constant multiplied to rho in the relation between P and rho).
        Note: Units given as arguments should be in CGS units.
        """
    def y(p,m,r):
        return([(-G*m*p**(3.0/5)/(l**(3.0/5)*(r**2)))*(1+p**(2.0/5)*l**(3/5)/c**(2))*(1+4*math.pi*r**(3)*p/(m*c**(2)))*(1-2*G*m/(r*c**2))**(-1),4*math.pi*r**(2)*p**(3/5)/l**(3.0/5)])
    return(y)
###
###Assuming density method
D=10**16                                #Density value 
G=6.6743*10**(-8)
c=3*10**10
l=5.4*10**9
P=l*(D**(5.0/3))
y_0=10**(-32)                           #initial values(y_0=mass enclosed=0)
x_0=P                                   #x_0=Initial Pressure
h=10**2                                 #step size in r
k=13020                                 #number of data M/r points I want
p,m,r,rh,mh=RK.rk(x_0,y_0,func(G,c,l),h,k)   #calling the function and RK-4 and storing the outputs in p,m,r
m=[x/(1.989*10**33) for x in m]
###
###plotting
plt.title("Variation of P with r")
plt.xlabel("r in cm")
plt.ylabel("P in CGS units")
plt.plot(r,p,"red")
plt.savefig("/Users/aj3008/Desktop/MS_3rd_Sem/Comp_methods_in_AST/Comp_methods/Hw_4/Pr_pb3")
plt.show()
plt.clf()
plt.title("Variation of Menc with r")
plt.xlabel("r in cm")
plt.ylabel("M in terms of mass of the sun")
plt.plot(r,m,"blue")
plt.savefig("/Users/aj3008/Desktop/MS_3rd_Sem/Comp_methods_in_AST/Comp_methods/Hw_4/Mr_pb3")
plt.show()
print("the mass of the given neutron star is",mh/(1.989*10**33),"times mass of the sun(by the assuming density method")
### interploation method
rh1=[x/(10**5) for x in pb2.rh_]
mh1=[x/(1.989*10**33) for x in pb2.mh_]
#rh1=pb2.rh_
#mh1=pb2.mh_
r=13.02000
for i in range(len(rh1)):
    if i+1 <len(rh1):
        if rh1[i] >13.02000 >rh1[i+1]:           
            a=(mh1[i]-mh1[i+1])/(rh1[i]-rh1[i+1])
            d=13.0200-rh1[i+1]           
            c=(a*(13.0200-rh1[i+1])+mh1[i+1])
            print("The mass of the given neutron star is", c,"times mass of the sun")
            #print("The mass of the given neutron star is", c/(1.989*10**(33)),"times mass of the sun")
    