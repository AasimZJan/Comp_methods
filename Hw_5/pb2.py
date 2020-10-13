#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 18:14:43 2020

@author: aj3008
"""

#%%
#%%
#https://jakevdp.github.io/PythonDataScienceHandbook/04.04-density-and-contour-plots.html (plots)
#https://my.ece.utah.edu/~ece6340/LECTURES/Feb1/Nagel%202012%20-%20Solving%20the%20Generalized%20Poisson%20Equation%20using%20FDM.pdf
#(theory)

#------------------------------------------libraries----------------------------------

import numpy as np
import matplotlib.pyplot as plt
import math

#------------------------------------Mesh creation-----------------------------------------


#step size here is 10/100=0.1. It is a regular mesh
x = np.linspace(0, 10, 100)
y = np.linspace(0, 10, 100)

X, Y = np.meshgrid(x, y)
p=np.array([[0 for i in range(100)]for j in range(100)])    #p[k]
p1=np.array([[0 for i in range(100)]for j in range(100)])   #p[k+1]
R=np.array([[0 for i in range(100)]for j in range(100)])    #residual





#location of each disk
g1=[7,7,400]
g2=[8,2,255]
G=4.3*10**(-9)        #in Mpc⋅M⊙^–1⋅(km/s)^2



#-------------------------------Loops to calculate potential at each point-----------------------

for k in range(1000):
    print(k)
    for i in range(1,99,1): #y coordinate jump
        for j in range(1,99,1):#x coordinate jump
        
        
            x=X[0][j]+0.05
            y=Y[i][0]+0.05
            a=(x-7)**2+(y-7)**2
            b=(x-8)**2+(y-2)**2
            
            
            
            #if statments to check where the point lies and finding the density accordingly
            if a<=9:
                #this statement checks if it is inside the disk at (7,7) and finds density  if it is
                density=400*(10**12)/(math.pi*9)
            if b<=4:            
                #this statement checks if it is inside the disk at (8,2) and finds density  if it is
                density=255*(10**12)/(math.pi*4)
                
            if a>9 and b >4:
                #this statement checks if the point is outside the two disks and finds density  if it is
                density=0
            #Residual
            R[i][j]=0.25*(p[i+1][j]+p[i-1][j]+p[i][j-1]+p[i][j+1]-(0.1**2)*4*math.pi*G*density)-p[i][j]
            #p[k+1]
            p1[i][j]=R[i][j]+p[i][j]
    p=p1
    
    
    
#---------------------------------------Plotting-------------------------------------------------------------
plt.contourf(X, Y, p, 20, cmap='RdGy')
cbar=plt.colorbar();
cbar.set_label("Potenial")
plt.xlabel("X coordinate in Mpc")
plt.ylabel("Y coordinate in Mpc")
plt.savefig("Images/pb2n")
plt.show()





