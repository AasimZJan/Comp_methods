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


#-------------------------------calculating absolute magnitude, band taken is J---------------------------------
for i in range(len(data)):
    Av=3.1*data[i][6]
    Al=0.271*Av  #J band
    Y.append(data[i][3]-5*math.log((10**3)*data[i][1],10)+5-Al)
    
    
    
#-------------------------------------Parameter estimation for full model-------------------------------------
#n added to a variable means nested value, X is full models design matrix and Xn is nested models design matrix

Y=np.array(Y)
Xt=np.transpose(X)
A=np.matmul(Xt,Y)
B=np.matmul(Xt,X)
C=np.linalg.inv(B)
Para=np.matmul(C,A)    #equation from lecture notes for parameter vector calculation
errors=[[np.sqrt(C[i][i])]for i in range(len(C))] #equation from lecture notes for parameter vector calculation

fit=[]
for i in range(len(X)):
    fit.append(Para[0]+Para[1]*X[i][1]+Para[2]*X[i][2]) #PLZ relation
fit=np.array(fit)



#----------------------------------Parameter estimation of nested model------------------------------------
Xn=np.array([[1,math.log(data[i][0],10)]for i in range(len(data))])
Yn=np.array(Y)
Xtn=np.transpose(Xn)
An=np.matmul(Xtn,Yn)
Bn=np.matmul(Xtn,Xn)
Cn=np.linalg.inv(Bn)
Paran=np.matmul(Cn,An)
errorsn=[[0.1*np.sqrt(Cn[i][i])]for i in range(len(Cn))]
print("For nested model")
print("Alpha =",Paran[0], "error=",errorsn[0])
print("Beta=",Paran[1],"error=",errorsn[1])

fitn=[]
for i in range(len(X)):
    fitn.append(Paran[0]+Paran[1]*Xn[i][1])         #nested relation
fitn=np.array(fitn)

#---------------------------------------------Chisquare-----------------------------------------------------------------
X2,p=stats.chisquare(Y,fit)
X2n,pn=stats.chisquare(Y,fitn)
v=len(data)-len(Para)     #full dof
vn=len(data)-len(Paran)   #nested dof
Num=(X2n-X2)/(v-vn)
Den=X2/(v)
F=Num/Den                 #relation given in the problem
return_value=stats.f.cdf(F,v-vn,v)
print("full model dof=",v,"nested model dof=",vn)
print("F statisic based on the given equation=",F)

print()