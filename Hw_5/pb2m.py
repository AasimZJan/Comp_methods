#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 12:37:44 2020

@author: aj3008
"""

#%%
#https://jakevdp.github.io/PythonDataScienceHandbook/04.04-density-and-contour-plots.html



#------------------------------------------libraries----------------------------------

import numpy as np
import matplotlib.pyplot as plt
import math



#---------------------------------------Functions---------------------------------------

def poten(point1,point2):
    '''
    This function calulates potential due to point2 on point1

    Parameters
    ----------
    point1 : the point where potential is being found (x,y).
    point2 : potential due to a point (x,y,n) where n is the number of galazies in that disk.

    Returns
    -------
    Potential in (km/s)**2.

    '''
    G=4.3*10**(-9)                                                                      #Mpc⋅M⊙^–1⋅(km/s)^2
    dist=(3.086*10**19)*((np.sqrt((point1[0]-point2[0])**2+(point1[1]-point2[1])**2)))  #in km
    return(-(3.086*10**19)*G*point2[2]*(10**12)/dist)                                   #in (km/s)**2, 10**12 is mass of one galaxy, point2[2] will give the number of galaxies in disk



#------------------------------------Mesh creation-----------------------------------------


#step size here is 10/100=0.1. It is a regular mesh
x = np.linspace(0, 10, 100)
y = np.linspace(0, 10, 100)

X, Y = np.meshgrid(x, y)
p=np.array([[0 for i in range(100)]for j in range(100)])





#location of each disk
g1=[7,7,400]
g2=[8,2,255]



#-------------------------------Loops to calculate potential at each point-----------------------


for i in range(len(Y)): #y coordinate jump
    for j in range(len(X)):#x coordinate jump
    
    
        x=X[0][j]
        y=Y[i][0]
        p1=[x,y]   # the point in consideration
        a=(x-7)**2+(y-7)**2
        b=(x-8)**2+(y-2)**2
        
        
        
        #if statments to check where the point lies and finding the potential accordingly
        if a<=9:
            #this statement checks if it is inside the disk at (7,7) and finds potential if it is
            print("inside circle at 7,7")
            density=400/(math.pi*9)
            num=density*(math.pi*a)
            p2=[7,7,num]
            Potential=poten(p1,p2)+poten(p1,g2)
            p[i][j]=Potential
        if b<=4:            
            #this statement checks if it is inside the disk at (8,2) and finds potential if it is
            print("inside circle at 8,2")
            density=255/(math.pi*4)
            num=density*(math.pi*b)
            p2=[8,2,num]
            Potential=poten(p1,p2)+poten(p1,g1)
            p[i][j]=Potential
            
        if a>9 and b >4:
            #this statement checks if the point is outside the two disks and finds potential if it is
            print("outside")
            Potential=poten(p1,g1)+poten(p1,g2)
            p[i][j]=Potential



#enforcing boundary condition
for i in (0,99):
    for j in range(100):
        p[i][j]=0
        p[j][i]=0
#-------------------------------------Plotting--------------------------------------------------------
#plt.contour(X, Y, p, colors='black');


plt.contourf(X, Y, p, 20, cmap='RdGy')
cbar=plt.colorbar();
cbar.set_label("Potenial")

plt.xlabel("X coordinate in Mpc")
plt.ylabel("Y coordinate in Mpc")
plt.savefig("Images/Pb2")

           
           
           
           
           
           
           