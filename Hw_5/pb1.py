#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 17:30:40 2020

@author: aj3008
"""

#%%
#-----------------------------------------------------Libraries--------------------------------------------
import numpy as np
import matplotlib.pyplot as plt



#----------------------------------------------------Extracting Data--------------------------------------------
data0=np.load("galaxies0.npy")
data0=np.array([data0[i] for i in range(20)])
data=np.load("galaxies1.npy")
data=np.array([data[i] for i in range(20)])
data1=[[0,0] for i in range(len(data0))]



#------------------------------------------------------Functions------------------------------------------------------



def scan(data,limits):
    
    '''
    This function scans for the points in the given quadrant.

    Parameters
    ----------
    data : the points you want to get scanned
    limits : Limits of the quadtrant i.e a<x<b nad c<y<d

    Returns
    -------
    j= number of points in the quadtrant
    new_data= the points in the given quadtrant
    '''
    j=0
    k=[]
    for i in range(len(data)):
        if limits[0][0] <= data[i][0]<=limits[0][1] and limits[1][0] <= data[i][1] <= limits[1][1]:
            k.append(i)
            j=j+1
            #print(i)
    new_data=[data[i] for i in k]
    return(j,new_data)




def com(data):
    '''
    This function finds the Centre of mass for the given points

    Parameters
    ----------
    data : Points you want to find centre of mass for. Usually it is an output of scan function

    Returns
    -------
    com_x= x position of COM
    com_y= y position of COM
    n= number of points for which COM is being calculated. I am taking n since all galaxies have same mass

    '''
    sum_x=0
    sum_y=0
    n=len(data)
    for i in range(n):
        sum_x=sum_x+data[i][0]
        sum_y=sum_y+data[i][1]
    if n !=0:
        com_x=sum_x/n
        com_y=sum_y/n
    else:
        com_x=1
        com_y=1
    return(com_x,com_y,n)




        
def accel(point1,point2):
    '''
    This function gives the acceleration on point1 due to point2

    Parameters
    ----------
    point1 : point1 coordinates.
    point2 : point2 coordinates and number of points it representrs if it is a COM.

    Returns
    -------
    X_acceleration, Y_acceleration.

    '''
    G=4.3*10**(-9) #Mpc⋅M⊙^–1⋅(km/s)^2
    #print(point1,point2)
    epi=(655)**(-1/3)*(4*3.14*(.23**3)/3)**(1/3)
    dist=(3.086*10**19)*((np.sqrt((point1[0]-point2[0])**2+(point1[1]-point2[1])**2)))  #km
    smooth=epi*(3.086*10**19)
    #print(dist)
    if len(point2)==2:
        point2=np.append(point2,1)
    a=(G*point2[2]*10**(12))/((dist)**2+smooth**2)
#    print(np.sqrt((point1[0]-point2[0])**2+(point1[1]-point2[1])**2),point2)
    if (np.sqrt((point1[0]-point2[0])**2+(point1[1]-point2[1])**2)) <0.15:
        a=0
#    print([(a*((point2[0]-point1[0])*(3.086*10**19))/dist),((a*(point2[1]-point1[1])*(3.086*10**19))/dist)])
    return([(a*((point2[0]-point1[0])*(3.086*10**19))/dist),((a*(point2[1]-point1[1])*(3.086*10**19))/dist)])





#---------------------------------------Barnes_Hut Algorithm----------------------------------------------------            
#o is the year, e and f is just a test, h is time step
#r are the points in question
#m saves the COM details for a given point as you keep on dividing the grid up
#ax,ay are the x and y components of acceleration for the given point
            
o=1 
e=[]
f=[]       
while o <11:
    print("year",o)
    h=o*3600*24*365*100000000    
    for r in range(len(data)):
        #print("point",r)
        x=data[r][0]
        y=data[r][1]
        limits=[[0,10],
                [0,10]]
        limit=[[0,10],
                [0,10]]
        i=0
        m=[]
        ax=0
        ay=0
        l=1
        while i!=1:
            l=l+1
            #print(limits)
            half_x=(limits[0][0]+limits[0][1])*0.5
            half_y=(limits[1][0]+limits[1][1])*0.5
            if limits[0][0]<=x<half_x and limits[1][0]<=y<half_y:
                #print("quad1")
                limit[0][1]=half_x
                limit[1][1]=half_y
                j,new_data=scan(data,limit)
                #print(j)
                if j==1:
                    i=1
            else:
                if l>=4:
                    c=[[limits[0][0],half_x],[limits[1][0],half_y]]
                    b=scan(data,c)[1]
                    for mi in range (len(b)):
                        ax=ax+accel(data[r],b[mi])[0]
                        ay=ay+accel(data[r],b[mi])[1]
                else:
                    c=[[limits[0][0],half_x],[limits[1][0],half_y]]
                    b=com(scan(data,c)[1])
                    m.append(b)
                    ax=ax+accel(data[r],b)[0]
                    ay=ay+accel(data[r],b)[1]
                    
                
            if half_x<=x<limits[0][1] and limits[1][0]<=y<half_y:
                #print("quad2")
                limit[0][0]=half_x
                limit[1][1]=half_y
                j,new_data=scan(data,limit)
                #print(j)
                if j==1:
                    i=1
            else:
                if l>=4:
                    c=[[half_x,limits[0][1]],[limits[1][0],half_y]]
                    b=scan(data,c)[1]
                    for mi in range (len(b)):
                        ax=ax+accel(data[r],b[mi])[0]
                        ay=ay+accel(data[r],b[mi])[1]
                else:
                    c=[[half_x,limits[0][1]],[limits[1][0],half_y]]
                    b=com(scan(data,c)[1])
                    m.append(b)
                    ax=ax+accel(data[r],b)[0]
                    ay=ay+accel(data[r],b)[1]
            
                
            if limits[0][0]<=x<half_x and half_y<=y<=limits[1][1]:
                #print("quad3")
                limit[0][1]=half_x
                limit[1][0]=half_y
                j,new_data=scan(data,limit)
                #print(j)
                if j==1:
                    i=1
            else:
                if l>=4:
                    c=[[limits[0][0],half_x],[half_y,limits[1][1]]]
                    b=scan(data,c)[1]
                    for mi in range (len(b)):
                        ax=ax+accel(data[r],b[mi])[0]
                        ay=ay+accel(data[r],b[mi])[1]
                else:
                    c=[[limits[0][0],half_x],[half_y,limits[1][1]]]
                    b=com(scan(data,c)[1])
                    m.append(b)
                    ax=ax+accel(data[r],b)[0]
                    ay=ay+accel(data[r],b)[1]
                
            if half_x<=x<limits[0][1] and half_y<=y<=limits[1][1]:
                #print("quad4")
                limit[0][0]=half_x
                limit[1][0]=half_y
                j,new_data=scan(data,limit)
                #print(j)
                if j==1:
                    i=1
            else:
                if l>=4:
                    c=[[half_x,limits[0][1]],[half_y,limits[1][1]]]
                    b=scan(data,c)[1]
                    for mi in range (len(b)):
                        ax=ax+accel(data[r],b[mi])[0]
                        ay=ay+accel(data[r],b[mi])[1]
                else:  
                    c=[[half_x,limits[0][1]],[half_y,limits[1][1]]]
                    b=com(scan(data,c)[1])
                    m.append(b)
                    ax=ax+accel(data[r],b)[0]
                    ay=ay+accel(data[r],b)[1]
            limits=limit
#        print(ax,ay)
#Verlet integrator
        data1[r][0]=2*data[r][0]-data0[r][0]+ax*h**2
        data1[r][1]=2*data[r][1]-data0[r][1]+ay*h**2
    o=o+1
    data1=np.array(data1)
    data0=np.array(data0)
    data=np.array(data)
    d=[]
    for i in range(len(data1)):
        if data1[i][0]>10.0 or data1[i][0]<0.0 or data1[i][1]>10.0 or data1[i][1]<0.0:
            d.append(data1[i])
#            print(i,data1[i],data0[i])
    for k in range(len(d)):
        i=np.argwhere(data1==d[k])
            
        data= np.delete(data,i,0)
        data0=np.delete(data0,i,0)
        data1=np.delete(data1,i,0)
        #print(i,data1[i],data0[i])
    f.append(data1[0])
    e.append(data1[1])
    xi=data1[:,0]
    yi=data1[:,1]
    plt.scatter(xi,yi)
    plt.show()
    data0=data 
    data=data1
       
#%%
a=[[1,2],[1,4],[5,6]]     
a.remove(a[2])
    if dist<=1.6*10**23:
        a=(G*point2[2]*10**(12))/(dist+1.6*10**23)**2
    else:
    
    