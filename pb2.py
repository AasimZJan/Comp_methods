#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 08:27:59 2020

@author: aj3008
"""

#%%
#problem 2
import pb1
import matplotlib.pyplot as plt
def g():        #the function for pseudo isothermal
    def y(x):
        return(((1+x**2)**(-0.5))-0.5)
    return(y)

def dg():      #the derivate of the function
    def y(x):
        return((-x)/((1+x**2)**(1.5)))
    return(y)
t=[0.001,0.0001,0.00001,0.000001,0.0000001,0.00000001]    #giving it threshold values
#these will store number of iterations for each method with b being for bisection, s for secant, and n for newton
b=[]
s=[]
n=[]
for i in range(len(t)):
    xb,bb=pb1.bisection(0,3,g(),t[i])
    b.append(bb)
    xs,bs=pb1.secant(0,3,g(),t[i])
    s.append(bs)
    xn,bn=pb1.newton(3,g(),dg(),t[i])
    n.append(bn)
plt.xlabel("Threshold values")
plt.ylabel("Number of iterations")
plt.title("Variation in number of iterations as the threshold is changed")
plt.plot(t,b,marker="o",label="Bisection")
plt.plot(t,s,marker="o",label="Secant")
plt.plot(t,n,marker="o",label="Newton's")
plt.legend()
plt.savefig("HW1_pb2")
print(b)
print(s)
print(n)
    
print(pb1.bisection(0,3,g()))
print(pb1.secant(0,3,g()))
print(pb1.newton(3,g(),dg()))