#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 18:44:47 2020

@author: aj3008
"""

#%%
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
def secant(a,b,f,t=0.000001):
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
    return(x2,i)
#    print("the number of iterations is ",i)
#    print("the value of x is",x2)
def newton(a,f,df,t=0.000001):
    x0=a
    x1=x0-(f(x0)/df(x0))
    i=1
    while ((x1-x0)/x0)>t or ((x1-x0)/x0)< -t:
        x0=x1
        x1=x0-(f(x0)/df(x0))
        i=i+1
    return(x1,i)