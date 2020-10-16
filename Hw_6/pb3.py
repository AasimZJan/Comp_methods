#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 12:23:13 2020

@author: aj3008
"""

#%%
import numpy as np
import math
import matplotlib.pyplot as plt
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
    Av=3.1*data[i][6]
    Al=0.271*Av  #J band
    Y.append(data[i][3]-5*math.log((10**3)*data[i][1],10)+5-Al)
    
    
    
#-------------------------------------Parameter estimation-------------------------------------
Y=np.array(Y)
Xt=np.transpose(X)
A=np.matmul(Xt,Y)
B=np.matmul(Xt,X)
C=np.linalg.inv(B)
Para=np.matmul(C,A)
errors=[[0.1*np.sqrt(C[i][i])]for i in range(len(C))]

#-----------------------------------Printing----------------------------
print("Alpha =",Para[0], "error=",errors[0])
print("Beta=",Para[1],"error=",errors[1])
print("Gamma=", Para[2], "error=",errors[2])
