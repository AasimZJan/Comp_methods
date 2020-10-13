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
#data0=np.array([data0[i] for i in range(20)])
data=np.load("galaxies1.npy")
#data=np.array([data[i] for i in range(20)])
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
    new_data=[data[i] for i in k]        #writing the array containing the list of points in the coordinate
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
    n= number of points for which COM is being calculated. I am taking n and not mass since all galaxies have same mass

    '''
    sum_x=0
    sum_y=0
    n=len(data)
    for i in range(n):      #loop to calculate x and y coordinate of COM of given quadrant
        sum_x=sum_x+data[i][0]
        sum_y=sum_y+data[i][1]
    if n !=0:               #to avoid division by 0 when the quadrant is empty
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
    G=4.3*10**(-9)                                           #Mpc⋅M⊙^–1⋅(km/s)^2
    epi=(655)**(-1/3)*(4*3.14*(.23**3)/3)**(1/3)             #Force Smoothing from Dehnen 2001
    dist=(3.086*10**19)*((np.sqrt((point1[0]-point2[0])**2+(point1[1]-point2[1])**2)+epi**2))  #km
    
    #when we aren't finding the acceleration due to COM but due to an individual galaxy, n=1 needs to be added
    if len(point2)==2:                                                         
        point2=np.append(point2,1)
    
    a=(G*point2[2]*10**(12))/((dist)**2)                                       #point2[2]=number of galaxies in that quadrant, so point2[2]*10**12 will give us the mass of COM
    
    
    if (np.sqrt((point1[0]-point2[0])**2+(point1[1]-point2[1])**2)) <0.15:     #if the galaxies come this close they merge
        a=0
    
    
    return([(a*((point2[0]-point1[0])*(3.086*10**19))/dist),((a*(point2[1]-point1[1])*(3.086*10**19))/dist)])





#---------------------------------------Barnes_Hut Algorithm----------------------------------------------------            
#o is the "year", e and f is just a test, h is time step
#r are the points in question
#m saves the COM of quadrants with respect to the point r you keep on dividing the grid up
#ax,ay are the x and y components of acceleration for the given point
            
o=1 
e=[]
f=[]       
while o <11:
    print(40000000*o,"years")
    h=o*3600*24*365*40000000    
    for r in range(len(data)):
        #print("point",r)
        x=data[r][0]
        y=data[r][1]
        limits=[[0,10],
                [0,10]]
        limit=[[0,10],
                [0,10]]
        #i acts as a switch. when it takes a value of 1 it means that the quadrant has only one point and hence move on to next point.
        i=0
        m=[]
        ax=0
        ay=0
        #l acts as a switch to switch to individual force calculation between two galaxies instead of calculating COM
        l=1
        while i!=1:
            l=l+1
            
            #finding the centre of the whole grid in focus
            half_x=(limits[0][0]+limits[0][1])*0.5
            half_y=(limits[1][0]+limits[1][1])*0.5
            
            
            
            #checking if the point is in first quadrant, if it isn't the else statment calculates acceleration due to COM or the individual galaxies depending on the value of l
            if limits[0][0]<=x<half_x and limits[1][0]<=y<half_y:
                limit[0][1]=half_x
                limit[1][1]=half_y
                j,new_data=scan(data,limit)
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
                    
             #checking if the point is in second quadrant, if it isn't the else statment calculates acceleration due to COM or the individual galaxies depending on the value of l   
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
            
               #checking if the point is in third quadrant, if it isn't the else statment calculates acceleration due to COM or the individual galaxies depending on the value of l 
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
             #checking if the point is in fourth quadrant, if it isn't the else statment calculates acceleration due to COM or the individual galaxies depending on the value of l   
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
            
            
            
#-------------------------------------------------Verlet integrator and test stuff-------------------------------------
        data1[r][0]=2*data[r][0]-data0[r][0]+ax*h**2
        data1[r][1]=2*data[r][1]-data0[r][1]+ay*h**2
        
        
        
#moving on to next time snap 
    o=o+1
    data1=np.array(data1)
    data0=np.array(data0)
    data=np.array(data)
    d=[]
#eliminating merged galaxies
    for i in range(len(data1)):
        if data1[i][0]>10.0 or data1[i][0]<0.0 or data1[i][1]>10.0 or data1[i][1]<0.0:
            d.append(data1[i])
    for k in range(len(d)):
        i=np.argwhere(data1==d[k])
        data= np.delete(data,i,0)
        data0=np.delete(data0,i,0)
        data1=np.delete(data1,i,0)
        print(i,data1[i],data0[i])
#test arrays
    f.append(data1[0])
    e.append(data1[1])
#----------------------------------------------------Plotting-------------------------------------------
    xi=data1[:,0]
    yi=data1[:,1]
    plt.title("The system at time ="+ str((o-1))+"*unit time")
    plt.xlabel("X coordinate in Mpc")
    plt.ylabel("Y coordinate in Mpc")
    plt.scatter(xi,yi)
    plt.savefig("Images/pb1_"+str(o-1))
    plt.show()
    data0=data 
    data=data1
       
    
    