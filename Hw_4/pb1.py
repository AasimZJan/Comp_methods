#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 12:43:23 2020

@author: aj3008
"""

#%%
####libraries
import RK
import math                                
import matplotlib.pyplot as plt
D=[10**4,5*10**4,10**5,5*10**5,10**6]                                              #density range

def func(k1,k2):
    """ This function take k1 and k2 as arguments and returns an array where first element is is dP/dr and second one is dM/dr. The variables of the returned functions are P, Menc and r.
    k1=G*u_e/l**3/5
    k2=4*pi*u_e/l**3/5
        G= Gravitational constant,
        c= speed of light,
        l= K(the constant multiplied to rho in the relation between P and rho)
        u_e=2.
    Note: Units given as arguments should be in CGS units.
    """
    def y(p,m,r):
        return([-k1*m*(p**(3.0/5))/(r**2),k2*(r**2)*(p**(3.0/5))])
    return(y)
for i in range(len(D)):                    #loop for different densities
    P=(10**13)*((D[i]/2)**(5.0/3))
    k1=(6.6743*10**(-8))*2*((1.0/10**13)**(3.0/5))
    k2=4*math.pi*2*((1.0/10**13)**(3.0/5))
    y_0=10**(-6)                           #(initial values)(y_0=mass enclosed=0)
    x_0=P                                  #x_0=Initial Pressure
    h=10**6                                #step size
    k=10**4                                #number of points
    p,m,r,rh,mh=RK.rk(x_0,y_0,func(k1,k2),h,k)   ##calling the function and RK-4 and storing the outputs in p,m,r
    ###plotting
    plt.title("Variation of P with r, (D="+ str(D[i]/10**5) +" *10**5g/cm**3)")
    plt.xlabel("r in cm")
    plt.ylabel("P in CGS units")
    plt.plot(r,p,"red")
    plt.savefig("/Users/aj3008/Desktop/MS_3rd_Sem/Comp_methods_in_AST/Comp_methods/Hw_4/Images/Pr_pb1_"+str(i))
    plt.show()
    plt.clf()
    plt.title("Variation of Menc with r (D="+str(D[i]/10**5)+" *10**5g/cm**3)")
    plt.xlabel("r in cm")
    plt.ylabel("M in terms of mass of the sun")
    plt.plot(r,m,"blue")
    plt.savefig("/Users/aj3008/Desktop/MS_3rd_Sem/Comp_methods_in_AST/Comp_methods/Hw_4/Images/Mr_pb1_"+str(i))
    plt.show()
d=[x*10**4 for x in range(1,100,3)]
rh_=[]
mh_=[]
for i in range(len(d)):                    #loop for different densities
    P=(10**13)*((d[i]/2)**(5.0/3))
    k1=(6.6743*10**(-8))*2*((1.0/10**13)**(3.0/5))
    k2=4*math.pi*2*((1.0/10**13)**(3.0/5))
    y_0=10**(-6)                           #(initial values)(y_0=mass enclosed=0)
    x_0=P                                  #x_0=Initial Pressure
    h=10**6                                #step size
    k=10**4                                #number of points
    p,m,r,rh,mh=RK.rk(x_0,y_0,func(k1,k2),h,k)   ##calling the function and RK-4 and storing the outputs in p,m,r
    rh_.append(rh)
    mh_.append(mh)
plt.title("Variation of mass enclosed with radii" )
plt.xlabel("Radius of the White dwarf")
plt.ylabel("Mass of the White dwarf")
plt.plot(rh_,mh_,"bo")
plt.savefig("/Users/aj3008/Desktop/MS_3rd_Sem/Comp_methods_in_AST/Comp_methods/Hw_4/Images/Mr_pb1h")
plt.show()
    
    
    
    
    
    
    
    
    
    
    
    
    
    