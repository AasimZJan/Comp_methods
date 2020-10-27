#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 09:23:15 2020

@author: aj3008
"""

#%%
#-----------------------------------------------libraries--------------------------------------------------
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import math

#---------------------------------------------Extracting data-----------------------------------------------
data=np.loadtxt("lightcurve_data.txt")
t=[data[i][0]-2454953.538373 for i in range(len(data))]     #making initial time to be zero
I=data[:,1]
tn=[]                #to store folded time


#-----------------------------------------------Folding----------------------------------------------------
for i in range(len(data)):
    tn.append(t[i]%3.5485)

    
#-------------------------------------------Plotting Dip-----------------------------------------
plt.title("Dip in intensity KEPLER")
plt.xlabel("time in days")
plt.ylabel("Intensity")
plt.axis([2.261,2.4625,0.991,1.002])
plt.plot(tn,I,"x")
plt.savefig("Images/dip")
plt.show()


#--------------------------------------Defining the BOX function--------------------------------------------
def Box(s,tn):
    '''
    Parameters
    ----------
    s : [dip,tref,width of dip]
    tn: folded time

    Returns
    -------
    The data which resembles a Box when plotted
    g=1 always(I had made this to include priors and we can add a few lines for it to give priors for the posteriors)

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


#-----------------------------------Defining the likelihood function-----------------------------------------
def Like(I,q):
    '''
    Parameters
    ----------
    I : Intensity (observed)
    q : [Intensity(model), prior(useless as of now)]
    Returns
    -------
    Log Likelihood of the given model

    '''
    s=q[0]       #model 
    g=q[1]       #priors(useless)
    sum=0
    for i in range(len(I)):
#        sum =sum+(1/(np.sqrt(2*3.14)))*np.exp(-0.5*(I[i]-s[i])**2)
        sum=sum+math.log(1/(np.sqrt(2*3.14)))-0.5*(I[i]-s[i])**2
    return(sum)
        

#-----------------------------------------------MCMC----------------------------------------------------------
i=0
xt=[0.05,2.27,0.190]      #best initial guess
distd=[]                  #to store the parameters
y=[0.05,2.27,0.190]       #defined twice
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
 
    
#-------------------------------------------Finding probability for parameters--------------------------------
prob=[]
sum=0
for i in range(len(distd)):
    a=sp.exp(Like(I,Box(distd[i],tn)))
    sum=sum+a
    prob.append(a)
prob=[prob[i]/sum for i in range(len(prob))]    #normalising 
ind=prob.index(max(prob))                       #finding max probability
print("the value of parameters is",distd[ind])


b=distd[ind]#parameters associated with max probability
#-------------------------------------------marginalised distribution of dip-----------------------------------------
plt.title("marginalised distribution of dip value")
plt.xlabel("Dip value")
plt.ylabel("Probability")
c=[distd[i][0] for i in range(len(distd))]
plt.axvline(x=b[0])
plt.plot(c,prob,"rx")
plt.savefig("Images/dip_b")  
plt.show()


#------------------------------------------------Plotting-----------------------------------------------------
plt.axis([2.1,2.6,0.991,1.002])
plt.title("Comparison of data and model")
plt.xlabel("time in days")
plt.ylabel("Intensity")
plt.plot(tn,I,"x",label="data" )
box=Box(b,tn)[0]
plt.plot(tn,box,"x", label="model")
plt.legend()
plt.savefig("Images/dip_c")
plt.show()

#-----------------------------------------------corner plots--------------------------------------------------
distd=np.array(distd)
x=distd[:,0]
y=distd[:,1]
z=distd[:,2]
color=prob
plt.title("Corner plot of dip depth and tref")
plt.xlabel("Dip depth")
plt.ylabel("tref")
plt.axvline(x=b[0])
plt.axhline(y=b[1])
plt.scatter(x, y,c=color)
plt.savefig("Images/dip_d")
plt.show()

plt.title("Corner plot of dip depth and dip width")
plt.xlabel("Dip depth")
plt.ylabel("Dip width")
plt.axvline(x=b[0])
plt.axhline(y=b[2])
plt.scatter(x, z,c=color)
plt.savefig("Images/dip_e")
plt.show()

plt.title("Corner plot of tref and dip width")
plt.xlabel("tref")
plt.ylabel("Dip width")
plt.axvline(x=b[1])
plt.axhline(y=b[2])
plt.scatter(y,z,c=color)
plt.savefig("Images/dip_f")
plt.show()


#---------------------------------------------------error------------------------------------------------------
sum=0
for i in range(len(distd)):
    sum=sum+distd[i][0]
avg=sum/len(distd)
dev=0
for i in range(len(distd)):
    dev=dev+(distd[i][0]-avg)**2
dev=np.sqrt((dev)/len(distd))
print("the error associated with dip is =",dev)


#----------------------------------------------Calculating Radius---------------------------------------------
print("radius of the planet is=",np.sqrt(b[0]*1.79**2))


