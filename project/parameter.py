#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 13:56:39 2020

@author: aj3008
"""

#---------------
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

cc=7.424*10**(-28)     #(m/kg)convert mass into distance

msun=2*10**30*cc #mm

m1=35*msun
m2=35*msun

r=100*10**3 #m radius of both blackholes
Ri=1000*10**3 # initial separation


M=m1+m2
u=m1*m2/M

noise=np.random.normal(0,0.001)
dt=10000
h=[]
R=[]
t=[]
i=0
while i<=70000:
    print(Ri)
    hi=u*M/(r*Ri)+noise
    h.append(hi)
    R.append(Ri)
    Ri=Ri-dt*(u*M**2)/Ri**3    #forward difference
    i=i+1
    
    #-----------------------------------Defining the likelihood function-----------------------------------------
def Like(data,mod):
    h=mod[0]
    R=mod[1]
    sum=0
    for i in range(len(data)):
        sum=sum-0.5*(data[i]-h[i])**2
    return(sum+np.log(1/(np.sqrt(2*3.14))))

def model(y):
    cc=7.424*10**(-28)     #(m/kg)convert mass into distance

    msun=2*10**30*cc #mm
    
    m1=y[0]*msun
    m2=y[0]*msun
    
    r=100*10**3#m radius of both blackholes
    Ri=1000*10**3 # initial separation
    
    
    M=m1+m2
    u=m1*m2/M
    
    noise=np.random.normal(0,abs(y[1]))
    dt=10000
    h=[]
    i=0
    while i<=70000:
        hi=u*M/(r*Ri)+noise
        h.append(hi)
        R.append(Ri)
        Ri=Ri-dt*(u*M**2)/Ri**3    #forward difference
        i=i+1
    return(h,R)
    
    

#-----------------------------------------------MCMC----------------------------------------------------------
i=0
xt=[40,0.003]      #best initial guess
distd=[]                  #to store the parameters
y=[40,0.003]       #defined twice
while i<1000:
    print(i)
    y[0]=np.random.normal(xt[0],1)
    num=Like(h,model(y))
    den=Like(h,model(xt))
    r=sp.exp(num-den)
    if r>=1:
        xt[0]=y[0]
    else:
        u=np.random.uniform(0,1)
        if u<=r:
            xt[0]=y[0]
            
        else:
            xt[0]=xt[0]
    # y[1]=np.random.normal(xt[1],1)
    # num=Like(h,model(y))
    # den=Like(h,model(xt))
    # r=sp.exp(num-den)
    # if r>=1:
    #     xt[1]=y[1]
    # else:
    #     u=np.random.uniform(0,1)
    #     if u<=r:
    #         xt[1]=y[1]
            
    #     else:
    #         xt[1]=xt[1]
    y[1]=abs(np.random.normal(xt[1],0.001))
    num=Like(h,model(y))
    den=Like(h,model(xt))
    r=sp.exp(num-den)
    if r>=1:
        xt[1]=y[1]
    else:
        u=np.random.uniform(0,1)
        if u<=r:
            xt[1]=y[1]
            
        else:
            xt[1]=xt[1]
    i=i+1
    xt=list(xt)
    distd.append(xt)

print("done")
    

#-------------------------------------------Finding probability for parameters--------------------------------
prob=[]
sum=0
for i in range(len(distd)):
    print(i)
    a=sp.exp(Like(h,model(distd[i])))
    sum=sum+a
    prob.append(a)
prob=[prob[i]/sum for i in range(len(prob))]    #normalising 
ind=prob.index(max(prob))                       #finding max probability
print("the value of parameters is",distd[ind])
    
