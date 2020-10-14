#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 22:07:30 2020

@author: aj3008
"""

#%%
import numpy as np
import matrix
import math
with open("cepheid_data.txt") as f:
    ncols = len(f.readline().split(','))
#Period(days), Distance(kpc), V(mag), J(mag), H(mag), K(mag), E(mag), Z([Fe/H])

data=np.loadtxt("cepheid_data.txt",delimiter=',',skiprows=0,usecols=range(1,ncols))
X=np.array([[1,math.log(data[i][0]),data[i][7]]for i in range(len(data))]) #independent variables
Y=np.array([[data[i][2]]for i in range(len(data))])                        #Dependent variables

# Xt=matrix.tran(X)
# A=matrix.mult(Xt,Y)
# B=matrix.mult(Xt,X)
# C=matrix.inv(B)
# Para=matrix.mult(C,A)
Xt=np.transpose(X)
A=np.dot(Xt,Y)
B=np.dot(Xt,X)
C=np.linalg.inv(B)
Para=np.dot(C,A)
errors=[[np.sqrt(C[i][i])]for i in range(len(C))]