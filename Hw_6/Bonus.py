#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 14:10:54 2020

@author: aj3008
"""

#%%
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy import stats
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
errors=[[np.sqrt(C[i][i])]for i in range(len(C))]

fit=[]
for i in range(len(X)):
    fit.append(Para[0]+Para[1]*X[i][1]+Para[2]*X[i][2])
fit=np.array(fit)

Xn=np.array([[1,math.log(data[i][0],10)]for i in range(len(data))])
Yn=np.array(Y)
Xtn=np.transpose(Xn)
An=np.matmul(Xtn,Yn)
Bn=np.matmul(Xtn,Xn)
Cn=np.linalg.inv(Bn)
Paran=np.matmul(Cn,An)
errorsn=[[0.1*np.sqrt(C[i][i])]for i in range(len(C))]

fitn=[]
for i in range(len(X)):
    fitn.append(Paran[0]+Paran[1]*Xn[i][1])
fitn=np.array(fitn)

X2=0
X2n=0
for i in range(len(data)-len(Para)):
    X2=X2+((Y[i]-fit[i])**2)/(fitn[i])
    
for i in range(len(data)-len(Paran)):
    X2n=X2n+((Yn[i]-fitn[i])**2)/(fitn[i])
v=len(data)-len(Para)
vn=len(data)-len(Paran)

Num=(X2n-X2)/(v-vn)
Den=X2/(len(data)-v)
Num1=X2n/vn
Den1=X2/v
F=Num/Den
F1=Num1/Den1
return_value=stats.f.cdf(F1,Num1,Den1)
