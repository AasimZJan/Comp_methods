#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 15:13:08 2020

@author: aj3008
"""

#%%
import math
def midpoint(f,a,b,n):
    h=float(b-a)/n
    x0=a
    x1=x0+h
    first=f((x0+x1)*0.5)*h
    for i in range(n-1):
        x0=x1
        x1=x0+h
        first=first+f((x0+x1)*0.5)*h
    print('The value from midpoint rule is', first)
def g():
    def y(x):
        return(math.cos(x))
    return(y)
def trapezoid(f,a,b,n):
    h=float(b-a)/n
    x0=a
    first=(f(x0))*h*0.5
    for i in range(n-1):#n+1 points in summation
        x1=x0+h
        first=first+(f(x1))*h
        x0=x1
    end=first+f(b)*h*0.5
    print('The value from trapezoid rule is', end)

def simpson(f,a,b,n):
    h=float(b-a)/n
    x0=a
    first=f(x0)*h*(float(1)/3)
    for i in range(n-1):
        if (i+1)%2==0:
            x1=x0+h
            first=first+(2*f(x1)*h*float(1)/3)
            x0=x1
        else:
            x1=x0+h
            first=first+(4*f(x1)*h*float(1)/3)
            x0=x1
    end=first+f(b)*h*(1/3)
    print('The value from simpson rule is', end)

def diff(f,a,h):
    d=(f(a+h)-f(a))/h
#    print(a,f(a))
    print('The result of differentiation is',d)
    