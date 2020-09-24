#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 16:53:45 2020

@author: aj3008
"""

#%%
#libraries
import RK
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
###
D=[10**14,5*10**14,10**15,5*10**15,10**16] #Density array
G=6.6743*10**(-8)                          #constants
c=3*10**10
l=5.4*10**9
for i in range(len(D)):                    #Loop for different densities
    P=l*(D[i]**(5.0/3))
    y_0=10**(-6)                           #initial values(y_0=mass enclosed=0)
    x_0=P                                  #x_0=Initial Pressure
    h=10**4                                #step size
    k=2*10**2                              #number of points
    p,m,r,rh,mh=RK.rk(x_0,y_0,func(G,c,l),h,k)  #calling the function and RK-4 and storing the outputs in p,m,r
    ###plotting
    plt.title("Variation of P with r, (D="+ str(D[i]/10**15) +" *10**15g/cm**3)")
    plt.xlabel("r in cm")
    plt.ylabel("P in CGS units")
    plt.plot(r,p,"red")
    plt.savefig("/Users/aj3008/Desktop/MS_3rd_Sem/Comp_methods_in_AST/Comp_methods/Hw_4/Images/Pr_pb2_"+str(i))
    plt.show()
    plt.clf()
    plt.title("Variation of Menc with r (D="+str(D[i]/10**15)+" *10**15g/cm**3)")
    plt.xlabel("r in cm")
    plt.ylabel("M in terms of mass of the sun")
    plt.plot(r,m,"blue")
    plt.savefig("/Users/aj3008/Desktop/MS_3rd_Sem/Comp_methods_in_AST/Comp_methods/Hw_4/Images/Mr_pb2_"+str(i))
    plt.show()
d=[x*10**14 for x in range(1,100,3)]
rh_=[]
mh_=[]
for i in range(len(d)):                    #loop for different densities
    P=l*(d[i]**(5.0/3))
    y_0=10**(-6)                           #initial values(y_0=mass enclosed=0)
    x_0=P                                  #x_0=Initial Pressure
    h=10**4                                #step size
    k=2*10**2                              #number of points
    p,m,r,rh,mh=RK.rk(x_0,y_0,func(G,c,l),h,k)  #calling the function and RK-4 and storing the outputs in p,m,r
    rh_.append(rh)
    mh_.append(mh)
plt.title("Variation of mass enclosed with radii" )
plt.xlabel("Radius of the Neutron star")
plt.ylabel("Mass of the Neutron Star")
plt.plot(rh_,mh_,"ko")
plt.savefig("/Users/aj3008/Desktop/MS_3rd_Sem/Comp_methods_in_AST/Comp_methods/Hw_4/Images/Mr_pb2h")
plt.show()   
    