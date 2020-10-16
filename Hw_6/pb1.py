#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 22:07:30 2020

@author: aj3008
"""

#%%
#--------------------------------------------libraries---------------------------------------------
import numpy as np
import math


#---------------------Opening file and removing first column which contained string(names)----------------------


#removing first column
with open("cepheid_data.txt") as f:
    ncols = len(f.readline().split(','))
    

#Period(days), Distance(kpc), V(mag), J(mag), H(mag), K(mag), E(mag), Z([Fe/H])
data=np.loadtxt("cepheid_data.txt",delimiter=',',skiprows=0,usecols=range(1,ncols))

#Design matrix
#Period(days), J(mag), Z([Fe/H])
X=np.array([[1,math.log(data[i][0],10),data[i][7]]for i in range(len(data))])
Y=[]


#-------------------------------calculating absolute magnitude, band taken is J-----------------------
for i in range(len(data)):
    Av=3.1*data[i][6]    #relation 6 from HW
    Al=0.271*Av  #J band   
    Y.append(data[i][3]-5*math.log((10**3)*data[i][1],10)+5-Al)   #relation 4 from Hw
    
    
    
#-------------------------------------Parameter estimation-------------------------------------
Y=np.array(Y)
Xt=np.transpose(X)
A=np.matmul(Xt,Y)
B=np.matmul(Xt,X)
C=np.linalg.inv(B)
Para=np.matmul(C,A)    #equation from lecture notes for parameter vector calculation
errors=[[np.sqrt(C[i][i])]for i in range(len(C))]


#-----------------------------------Printing----------------------------
print("Alpha =",Para[0], "error=",errors[0])
print("Beta=",Para[1],"error=",errors[1])
print("Gamma=", Para[2], "error=",errors[2])









