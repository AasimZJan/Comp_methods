#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 12:37:44 2020

@author: aj3008
"""

#%%
#------------------------------------------libraries----------------------------------


import numpy as np
import matplotlib.pyplot as plt
import math

def poten(point1,point2):
    G=4.3*10**(-9) #Mpc⋅M⊙^–1⋅(km/s)^2
    dist=(3.086*10**19)*((np.sqrt((point1[0]-point2[0])**2+(point1[1]-point2[1])**2)))  #km
    return(-(3.086*10**19)*G*point2[2]*(10**12)/dist)

x=0.1
x_=[]
y=0.1
y_=[]
p=[]
g1=[7,7,400]
g2=[8,2,255]
for i in range(1,101,1): #y coordinate jump
    for j in range(1,101,1): #x coordinate jump
        a=(x-7)**2+(y-7)**2
        b=(x-8)**2+(y-2)**2
        #print(a,b)
        #print(i,j)
        if a<=9:
            print("inside circle at 7,7")
            x_.append(x)
            y_.append(y)
            p1=[x,y]
            density=400/(math.pi*9)
            num=density*(math.pi*a)
            p2=[7,7,num]
            Potential=poten(p1,p2)+poten(p1,g2)
            p.append(Potential)
            x=j*0.1
            y=i*0.1
        if b<=4:
            x_.append(x)
            y_.append(y)
            p1=[x,y]
            print("inside circle at 8,2")
            density=255/(math.pi*4)
            num=density*(math.pi*b)
            p2=[8,2,num]
            Potential=poten(p1,p2)+poten(p1,g1)
            p.append(Potential)
            x=j*0.1
            y=i*0.1
            
        if a>9 and b >4:
            print("outside")
            x_.append(x)
            y_.append(y)
            p1=[x,y]
            Potential=poten(p1,g1)+poten(p1,g2)
            p.append(Potential)
            x=j*0.1
            y=i*0.1
            