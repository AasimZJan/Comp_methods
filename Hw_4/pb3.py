#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 17:45:26 2020

@author: aj3008
"""

#%%
import math
import matplotlib.pyplot as plt
def secant(a,b,f,t=0.000001):
    x0=a
    x1=b
    y0=f(x0)
    y1=f(x1)
    print(x0,x1)
    print(y0,y1)
    x2=x1-(float(x1-x0)/(y1-y0))*y1
    y2=f(x2)
    i=1
    while ((x2-x1)/x1)>t or ((x2-x1)/x1)< -t:
        print(x0,x1,x2)
        print(y0,y1,y2)
        if y2*y1<0:
            x0=x1
            x1=x2
            y0=f(x0)
            y1=f(x1)
            x2=x1-(float(x1-x0)/(y1-y0))*y1
            y2=f(x2)
            i=i+1
        else:
            x0=x0
            x1=x2
            y0=f(x0)
            y1=f(x1)
            x2=x1-(float(x1-x0)/(y1-y0))*y1
            y2=f(x2)
            i=i+1
    return(x2,i)
def bisection(a,b,f,t=0.000001):
    x0=a
    x1=b
#    print(x0,x1,f(a),f(b))    sanity check
    x2=(x1+x0)*0.5
    y0=f(x0)
    y1=f(x1)
    y2=f(x2)
    i=1
    while ((x2-x1)/x1)>t or ((x2-x1)/x1)< -t:
        if y2*y0<0:
            x0=x0
            x1=x2
            x2=(x1+x0)*0.5
            y0=f(x0)
            y1=f(x1)
            y2=f(x2)
            i=i+1
        else:
            x0=x2
            x1=x1
            x2=(x1+x0)*0.5
            y0=f(x0)
            y1=f(x1)
            y2=f(x2)
            i=i+1
    return(x2,i)
 #   print('the number of iterations is', i)
 #   print("the value of x is",x2)
def func(G,c,l,p,r):
    def y(m):
        return(10**(-12)+(-G*m*p**(3.0/5)/(l**(3.0/5)*(r**2)))*(1+p**(2.0/5)*l**(3/5)/c**(2))*(1+4*math.pi*r**(3)*p/(m*c**(2)))*(1-2*G*m/(r*c**2))**(-1))
    return(y)
def fun(G,c,l,p,r):
    def y(m):
        return(-G*m*p**(3.0/5)/(l**(3.0/5)*(r**2)))
    return(y)
G=6.6743*10**(-8)
c=3*10**10
l=5.4*10**9
p=10**-(34)
r=13.02*10**5
print(secant(1**33,4*10**33,func(G, c, l, p, r)))
