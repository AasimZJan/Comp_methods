# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#%%

import math                                #libraries
import matplotlib.pyplot as plt
def euler(x_0,y_0,f,h,k):
    y=[]
    x=[]
    j=[]
    t=10**(-9)
    for i in range(k):                       #loop to find values at different points
        j.append(t)
        x.append(x_0)
        y.append(y_0)
        x_0=x_0+h*f(x_0,y_0,t)[0]
        y_1=y_0+h*f(x_0,y_0,t)[1]
        y_0=y_1
        t=t+h
    return(x,y,j)
def heun(x_0,y_0,f,h,k,p=10):
    yh=[]
    xh=[]
    j=[]
    t=10**(-9)
    for i in range(k):
        j.append(t)
        yh.append(y_0)
        xh.append(x_0)
        x_1=x_0+h*f(x_0,y_0,t)[0]
        y_1=y_0+h*f(x_0,y_0,t)[1]
        for i in range(p):
            y_1=y_0+0.5*h*(f(x_0,y_0,t)[1]+f(x_1,y_1,t)[1])
            x_1=x_0+0.5*h*(f(x_0,y_0,t)[0]+f(x_1,y_1,t)[0])
        x_0=x_1
        y_0=y_1
        t=t+h
    return(xh,yh,j)
def rk(x_0,y_0,f,h,k):
    yr=[]
    xr=[]
    j=[]
    t=10**(-9)
    for i in range(k):
        j.append(t)
        yr.append(y_0)
        xr.append(x_0)
        k1=h*f(x_0,y_0,t)[1]
        k1x=h*f(x_0,y_0,t)[0]
        k2=h*f(x_0+k1x/2,y_0+k1/2,t+h/2)[1]
        k2x=h*f(x_0+k1x/2,y_0+k1/2,t+h/2)[0]
        k3=h*f(x_0+k2x/2,y_0+k2/2,t+h/2)[1]
        k3x=h*f(x_0+k2x/2,y_0+k2/2,t+h/2)[0]
        k4=h*f(x_0+k3x,y_0+k3,t+h)[1]
        k4x=h*f(x_0+k3x,y_0+k3,t+h)[0]
        y_1=y_0+(1.0/6)*(k1+2*k2+2*k3+k4)
        x_1=x_0+(1.0/6)*(k1x+2*k2x+2*k3x+k4x)
        x_0=x_1
        y_0=y_1
        t=t+h
    return(xr,yr,j)
