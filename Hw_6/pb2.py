#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 00:36:44 2020

@author: aj3008
"""

#%%
#--------------------------------------------libraries---------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
import pb1


#------------------------------------------Finding the fit values of absolute magnitude---------
Para= pb1.Para
X=pb1.X
Y=pb1.Y
fit=[]
for i in range(len(X)):
    fit.append(Para[0]+Para[1]*X[i][1]+Para[2]*X[i][2])
fit=np.array(fit)



#------------------------------------Plotting-------------------------------------
plt.title("log(Period)")
plt.xlabel("log(Period)")
plt.ylabel("M/Fit")
plt.plot(X[:,1],Y,"o",label="Data")
plt.plot(X[:,1],fit,"rx",label="fit")
plt.legend()
plt.savefig("Images/pb2_p")
plt.show()


plt.title("Z")
plt.xlabel("Z)")
plt.ylabel("M/Fit")
plt.plot(X[:,2],Y,"o",label="data")
plt.plot(X[:,2],fit,"rx",label="fit")
plt.legend()
plt.savefig("Images/pb2_z")
plt.show()

a=[-40,0]
b=[-40,0]
plt.xlabel("Fit")
plt.ylabel("M")
plt.title("Fit V/s M")
plt.plot(fit,Y,"rx",label="Results")
plt.plot(a,b,label="Expected")
plt.legend()
plt.savefig("Images/pb2_fm")
plt.show()

ax = plt.axes(projection='3d')
ax.set_xlabel("log(Period)")
ax.set_ylabel("Z")
ax.set_zlabel("M/fit")
ax.scatter3D(X[:,1],X[:,2],Y[:],"gray",label="data")
ax.plot3D(X[:,1],X[:,2],fit[:],"ro",label="fit")
plt.legend()
plt.savefig("Images/pb2_3d")
plt.show()


