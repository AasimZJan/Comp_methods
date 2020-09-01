#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 08:27:59 2020

@author: aj3008
"""

#%%
#problem 2
import rf
def h(x):
    return((0.5-((1+x**2)**(-0.5)))/(x*((1+x**2)**1.5)))
def f(x):   #define yout function here
    return(x**2-3)
x0=0
x1=3
#print(x0,x1)
#rf.bisection(0,3)
#rf.secant(0,3)
#rf.newton(1.5)