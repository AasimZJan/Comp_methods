#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 15:13:08 2020

@author: aj3008
"""

#%%

#importing libraries
import math                                  #for test cosine and sine function
####
####
def midpoint(f,a,b,n):                       #arguments(f=the function, a=the starting point,
                                             #b=the ending point,n the number of divisions)               
    h=float(b-a)/n                           #width
    x0=a                                     #initialising
    x1=x0+h
    first=f((x0+x1)*0.5)*h                   #area of first rectangle
    for i in range(n-1):                     #area of subsequent rectangles
        x0=x1 
        x1=x0+h 
        first=first+f((x0+x1)*0.5)*h         #used recursion
    print('The value from midpoint rule is', first)
    return(first)
####    

####
def trapezoid(f,a,b,n):                      #arguments(f=the function, a=the starting point,
                                             #b=the ending point,n the number of divisions)  
    h=float(b-a)/n                           
    x0=a
    first=(f(x0))*h*0.5                      #area of first rectangle
    for i in range(n-1):                     #area of subsequent rectangles
        x1=x0+h
        first=first+(f(x1))*h                #used recursion
        x0=x1
    end=first+f(b)*h*0.5                     #in the formula the last term had no coefficient so I took it out of the loop       
    print('The value from trapezoid rule is', end)
####
####
def simpson(f,a,b,n):                        #arguments(f=the function, a=the starting point,
                                             #b=the ending point,n the number of divisions)
    h=float(b-a)/n
    x0=a
    first=f(x0)*h*(float(1)/3)               #area of first rectangle
    for i in range(n-1):                     #area of subsequent rectangles except last
        if (i+1)%2==0:                       #f(x2),f(x4),f(x6)...terms had 2 as their coefficient and f(x1),f(x3),f(x5)....terms
                                             # had 4 as their coefficient so I made if statements for that
            x1=x0+h
            first=first+(2*f(x1)*h*float(1)/3)
            x0=x1
        else:
            x1=x0+h
            first=first+(4*f(x1)*h*float(1)/3)
            x0=x1
    end=first+f(b)*h*(1/3)                  #area of last rectangle added to total
    print('The value from simpson rule is', end)
####
####
def diff(f,a,h=0.000001):                   #arguments(f=the function, a=the point of evaluation,h=step size(smaller the better)(careful to not make it too small))
    d=(f(a+h)-f(a))/h                       #basic definition
#    print(a,f(a))
    print('The result of differentiation is',d)
#testing
####
#test function
def g():                                        
    def y(x):
        return(math.sin(x))
    return(y)
####
diff(g(),math.pi)
simpson(g(),0,math.pi,1000)
midpoint(g(),0,math.pi,1000)
trapezoid(g(),0,math.pi,1000)
    