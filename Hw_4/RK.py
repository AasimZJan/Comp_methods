#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 17:04:26 2020

@author: aj3008
"""

#%%
def rk(x_0,y_0,f,h,k):
    """ This function call RK-4 method for solving ODE. The arguments are:
        x_0=initial x value
        y_0=initial y value
        f=function of x,y,t
        h=step size
        k=number of times
        It returns x,y,t values in that order
    Note: Dont't set initial value to 0 but to something close to 0"""
    yr=[]
    xr=[]
    j=[]
    t=10**(-9)
    for i in range(k):
        if isinstance(x_0,float): 
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
            b=y_0
            x_0=x_1
            y_0=y_1
            t=t+h
            c=i
        else:
            j.append(t)
            xr.append(10**(-6))
            yr.append(b)
            t=t+h
    return(xr,yr,j,j[c],yr[c])