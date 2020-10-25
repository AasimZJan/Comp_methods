#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 09:23:15 2020

@author: aj3008
"""

#%%
#-------------------------------------------libraries--------------------------------------------
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import math

#-----------------------------------------Extracting data----------------------------------------
data=np.loadtxt("lightcurve_data.txt")
t=[data[i][0]-2454953.538373 for i in range(len(data))]
I=data[:,1]
tn=[] 


#---------------------------------------------Folding--------------------------------------------
for i in range(len(data)):
    tn.append(t[i]%3.5485)

    
#-----------------------------------------Finding t ref and tau graphically-------------------------------------
plt.axis([2.261,2.4625,0.991,1.002])
plt.plot(tn,I,"x")
plt.show()


#--------------------------------------Defining the BOX function---------------------------------------
def Box(delI,tn,tref=2.271,T=0.190):
    '''
    

    Parameters
    ----------
    tref : the beginning of dip
    T : the time for which dip lasts
    delI : the depth of dip.
    tn : time(x) axis.

    Returns
    -------
    The data which resembles a Box when plotted

    '''
    f=[]
    for i in range(len(tn)):
        if tn[i] <= tref or tn[i] >= (tref+T):
            f.append(1)
        else:
            f.append(1-delI)
            
    return(f)


#-----------------------------------Defining the likelihood function-----------------------------------
def Like(I,s):
    sum=0
    for i in range(len(I)):
#        sum =sum+(1/(np.sqrt(2*3.14)))*np.exp(-0.5*(I[i]-s[i])**2)
        sum=sum+math.log(1/(np.sqrt(2*3.14)))-0.5*(I[i]-s[i])**2
    return(sum)
        

#-----------------------------------------------MCMC------------------------------------------------------
i=0
xt=0.05
distd=[]
while i<1000:
    print(i)
    y=np.random.normal(xt)
    while y>1 or y<-1:
        y=np.random.normal(xt)
    num=Like(I,Box(y,tn))
    den=Like(I,Box(xt,tn))
    r=math.exp(num-den)
    if r>=1:
        xt=y
    else:
        u=np.random.uniform(0,1)
        if u<=r:
            xt=y
            
        else:
            xt=xt
    i=i+1
    distd.append(xt)
    
prob=[]
sum=0
for i in range(len(distd)):
    print(i)
    a=sp.exp(Like(I,Box(distd[i],tn)))
    sum=sum+a
    prob.append(a)
prob=[prob[i]/sum for i in range(len(prob))]
ind=prob.index(max(prob))
print("the depth is",distd[ind])


b=distd[ind]
#-------------------------------------marginalised distribution-----------------------------------------
plt.plot(distd,prob,"x")
plt.show()
    

#------------------------------------------------Plotting-----------------------------------------------------
plt.axis([2.1,2.6,0.991,1.002])
plt.plot(tn,I,"x")
box=Box(b,tn)
plt.plot(tn,box,"x")

#-----------------------------------------------error-------------------------------
sum=0
for i in range(len(distd)):
    sum=sum+distd[i]
avg=sum/len(distd)
dev=0
for i in range(len(distd)):
    dev=dev+(distd[i]-avg)**2
dev=np.sqrt(dev)/len(distd)



#----------------------------------------------Calculating Radius---------------------------------------------
print("radius=",b*1.79**2,"times radius of sun with error(1*sigma)=", dev)


#%%
j=0
for i in range(len(distd)):
    if 0.004<= distd[i] <=0.009:
        j=j+1
        print(distd[i],prob[i])
        
    






    