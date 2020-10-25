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
def Box(s,tn):
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
    g=1 always(we can add a few lines for it to give priors for the posteriors)

    '''
    delI=s[0]
    tref=s[1]
    T=s[2]
    f=[]
    g=1
    for i in range(len(tn)):
        if tn[i] <= tref or tn[i] >= (tref+T):
            f.append(1)
        else:
            f.append(1-delI)
            
    return(f,g)


#-----------------------------------Defining the likelihood function-----------------------------------
def Like(I,q):
    s=q[0]
    g=q[1]
    sum=0
    for i in range(len(I)):
#        sum =sum+(1/(np.sqrt(2*3.14)))*np.exp(-0.5*(I[i]-s[i])**2)
        sum=sum+math.log(1/(np.sqrt(2*3.14)))-0.5*(I[i]-s[i])**2
    return(sum)
        

#-----------------------------------------------MCMC------------------------------------------------------
i=0
xt=[0.05,2.27,0.190]
distd=[]
y=[0.05,2.27,0.190]
while i<1000:
    print(i)
    y[0]=np.random.normal(xt[0],.01)
    num=Like(I,Box(y,tn))
    den=Like(I,Box(xt,tn))
    r=sp.exp(num-den)
#    print(xt,y,r)
    if r>=1:
        xt[0]=y[0]
    else:
        u=np.random.uniform(0,1)
        if u<=r:
            xt[0]=y[0]
            
        else:
            xt[0]=xt[0]
    y[1]=np.random.normal(xt[1],0.001)
    num=Like(I,Box(y,tn))
    den=Like(I,Box(xt,tn))
    r=sp.exp(num-den)
#    print(r)
    if r>=1:
        xt[1]=y[1]
    else:
        u=np.random.uniform(0,1)
        if u<=r:
            xt[1]=y[1]
            
        else:
            xt[1]=xt[1]
    y[2]=np.random.normal(xt[2],0.001)
    num=Like(I,Box(y,tn))
    den=Like(I,Box(xt,tn))
    r=sp.exp(num-den)
#    print(r)
    if r>=1:
        xt[2]=y[2]
    else:
        u=np.random.uniform(0,1)
        if u<=r:
            xt[2]=y[2]
            
        else:
            xt[2]=xt[2]
    i=i+1
    xt=list(xt)
    distd.append(xt)
    
prob=[]
sum=0
for i in range(len(distd)):
    a=sp.exp(Like(I,Box(distd[i],tn)))
    sum=sum+a
    prob.append(a)
prob=[prob[i]/sum for i in range(len(prob))]
ind=prob.index(max(prob))
print("the depth is",distd[ind])


b=distd[ind]
#-------------------------------------marginalised distribution-----------------------------------------
c=[distd[i][0] for i in range(len(distd))]
plt.axvline(x=b[0])
plt.plot(c,prob,"rx")
plt.show()
    

#------------------------------------------------Plotting-----------------------------------------------------
plt.axis([2.1,2.6,0.991,1.002])
plt.plot(tn,I,"x")
box=Box(b,tn)[0]
plt.plot(tn,box,"x")
plt.show()
#-----------------------------------------------corner plots--------------------------------------------------
distd=np.array(distd)
x=distd[:,0]
y=distd[:,1]
z=distd[:,2]
color=prob
plt.axvline(x=b[0])
plt.axhline(y=b[1])
plt.scatter(x, y,c=color)
plt.show()
plt.axvline(x=b[0])
plt.axhline(y=b[2])
plt.scatter(x, z,c=color)
plt.show()
plt.axvline(x=b[1])
plt.axhline(y=b[2])
plt.scatter(y,z,c=color)
plt.show()

#-----------------------------------------------error-------------------------------
sum=0
for i in range(len(distd)):
    sum=sum+distd[i][0]
avg=sum/len(distd)
dev=0
for i in range(len(distd)):
    dev=dev+(distd[i][0]-avg)**2
dev=np.sqrt(dev)/len(distd)



#----------------------------------------------Calculating Radius---------------------------------------------
print("radius=",np.sqrt(b[0]*1.79**2),"times radius of sun with error(1*sigma)=", dev)


#%%
j=0
for i in range(len(distd)):
    if 0.004<= distd[i][0] <=0.009:
        j=j+1
        print(distd[i],prob[i])

#%%%
j=[]
k=[]
for i in range(1000):
    j.append(np.random.normal(0.3,1))
    k.append(i)
plt.plot(k,j)
#%%
k=[]
l=[3,4,5]
i=[5,6,7]
k.append(l)
k.append(i)

