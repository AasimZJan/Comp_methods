#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 08:32:38 2020

@author: aj3008
"""

#%%
#bisection method
from pb2 import f
from pb2 import h
def bisection(a,b,t=0.000001):
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
    print('the number of iterations is', i)
    print("the value of x is",x2)
def secant(a,b,t=0.00001):
    x0=a
    x1=b
    y0=f(x0)
    y1=f(x1)
    x2=x1-(float(x1-x0)/(y1-y0))*y1
    y2=f(x2)
    i=1
    while ((x2-x1)/x1)>t or ((x2-x1)/x1)< -t:
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
    print("the number of iterations is ",i)
    print("the value of x is",x2)
def  newton(a,t=0.000001):
    x1=a-h(a)
    i=1
    while (x1-a)/a >t or (x1-a)/a<-t:
        a=x1
        x1=a-h(a)
        i=i+1
    print('the number of iterations is', i)
    print("the value of x is",x1)
    