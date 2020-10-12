#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 17:30:40 2020

@author: aj3008
"""

#%%
import numpy as np
import matplotlib.pyplot as plt
data=np.load("galaxies0.npy")
x=data[:,0]
y=data[:,1]
plt.scatter(x,y)
#%%
def scan(data,limits):
    j=0
    k=[]
#    data.remove(data[point])
    for i in range(len(data)):
        if limits[0][0]<data[0]<limits[0][1] and limits[1][0]<data[1]<limits[1][1]:
            k.append(i)
            j=j+1
            new_data=[data[i] for i in k]
    return(j,new_data)

def com(data):
    sum_x=0
    sum_y=0
    n=len(data)
    for i in range(n):
        sum_x=sum_x+data[i][0]
        sum_y=sum_y+data[i][1]
    com_x=sum_x/n
    com_y=sum_y/n
    return(com_x,com_y,n)
        
            
            
        
    
    
limits=[[0,10],
        [0,10]]
i=0
m=[]
while i!=1:
    half_x=(limits[0][0]+limits[0][1])*0.5
    half_y=(limits[1][0]+limits[1][1])*0.5
    if limits[0][0]<x<half_x and limits[1][0]<y<half_y:
        limits[0][1]=half_x
        limits[1][1]=half_y
        j,new_data=scan(data,limits)
        if j==1:
            i=1
    else:
        c=[[limits[0][0],half_x],[limits[1][0],half_y]]
        m.append(com(scan(data,c)[1]))
        half_y=(limits[1][0]+limits[1][1])*0.5
        
        
    if half_x<x<limits[0][1] and limits[1][0]<y<half_y:
        limits[0][1]=half_x
        limits[1][1]=half_y
        j,new_data=scan(data,limits)
        if j==1:
            i=1
    else:
        c=[[half_x,limits[0][1]],[limits[1][0],half_y]]
        m.append(com(scan(data,c)[1]))
        half_y=(limits[1][0]+limits[1][1])*0.5
    
        
    if limits[0][0]<x<half_x and half_y<y<limits[1][1]:
        limits[0][1]=half_x
        limits[1][1]=half_y
        j,new_data=scan(data,limits)
        if j==1:
            i=1
    else:
        c=[[limits[0][0],half_x],[half_y,limits[1][1]]]
        m.append(com(scan(data,c)[1]))
        half_y=(limits[1][0]+limits[1][1])*0.5
        
        
    if half_x<x<limits[0][1] and half_y<y<limits[1][1]:
        limits[0][1]=half_x
        limits[1][1]=half_y
        j,new_data=scan(data,limits)
        if j==1:
            i=1
    else:
        c=[[half_x,limits[0][1]],[half_y,limits[1][1]]]
        m.append(com(scan(data,c)[1]))
        
#%%
a=[[1,2],[1,4],[5,6]]     
a.remove(a[2])

    
    