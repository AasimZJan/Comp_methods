#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 21:53:12 2020

@author: aj3008
"""

#%%
#importing libraries. Mattrix file is to get the inverse and Product. Copied from Hw_2. I have kept it in Hw_3 folder to avoid path issues
import matrix
import numpy as np
import matplotlib.pyplot as plt

#----------------------------------extracting data----------------------------------


a=np.loadtxt("A_coefficients.dat",delimiter=",",skiprows=0)

###n is the the number of states we are interested in.
n=9

###making a zero matrix for the coefficient matrix
l=[[0 for i in range(n)]for j in range(n)]  


 #---------------------------------begin extracting ---------------------------------
 
 
###to extract data I am creating a zero matrix of shape n*n-1. n-1 because (u>l). Aul=m[l][j] since the rows represent l and columns represent u (u>l)                                 
m=[[0 for i in range(n)]for j in range(n-1)]

#begin from zeroth row
k=0
x=[]
###loop to get all the points. a[k][2] becasue data is in 3rd column.
for i in range(n):                    #works
    for j in range(i):
        m[j][i]=a[k][2]
        k=k+1
        
        
#--------------------------------temperature range-------------------------------------


#Ti=[10**i for i in range(1,10)]
Ti=[273,1000,4000,8000,10000,30000,50000,60000]

#--------------------------------defining functions------------------------------------


def a(i,j,m):                                 #works
    """this function gives Aul as output where i=u, j=l, m is the data matrix"""
    #print(m[j][i])
    return(m[j][i])
def p(i,j):                                   #works, sign an issue
    """this function gives the variable part which depends on state in the frequency emitted or absored. i=final state j= initial state (hope this is right!)"""
    #print(((1/(i+1))**2)-(1/(j+1))**2)
    return(((1/(i+1))**2)-(1/(j+1))**2)
def b(i,j,m,T):
    """This function gives Bul and Blu. i and j are the subscripts in order. m is data matrix and T is the temperate. I have multiplied with J already."""
    E=13.6*p(i,j)                             #gives energy in ev
    #v=(-13.6*(10**(15))/4.135667696)*p(i,j)   #frequency(works)
    #print(i,j,v)
    k=8.617*10**(-5)                           #in ev
    d=(np.exp(E/(k*T))-1)
    if i>j:                                   #for Bul, i>j since u>l
        return(a(i,j,m)/d)
    if i<j:                                   #for Blu, j>i since u>l
        return(-a(j,i,m)/d*(((j+1)/(i+1))**2))
    

#------------------------------begin loop to find n values at different temperature---------------------


for u in range(len(Ti)):
    #print(Ti[u])
    T=Ti[u]
    for i in range(n):
        print("EQUATION",i)
                                           #All this is based on pattern observed. I hace added print statements to make sure it works the way it should and I tested it for 2,3 and 4 state systems.
        for j in range(n):
            print("state",j)
            if i==(n-1):                   #the final row in coefficient matrix should be ones since that represents that sum of n's should be 1
                print("1")
                l[i][j]=1       
            if i==j and i !=(n-1):         
                for k in range(n):
                    if i<k:
                        print("-b",i,k)
                        l[i][j]=l[i][j]-b(i,k,m,T) #negative because we bring them to the right side of the equation making the left side 0 and introducing a negative sign.
                        
                    if i>k:
                        print("-b-a",i,k)
                        l[i][j]=l[i][j]-b(i,k,m,T)-a(i,k,m)
            if i>j and i !=(n-1):
                print("b",j,i)
                l[i][j]=l[i][j]+b(j,i,m,T)
            if i<j:
                print("b+a",j,i)
                l[i][j]=l[i][j]+b(j,i,m,T)+a(j,i,m)
                
                
#--------------------------------------finding solution at a given temperature---------------------------


    q=matrix.inv(l)                      #first inverse and then multiply by the column matrix which will be the RHS of the system of equations.      
    h=[[0] for x in range(len(l)-1)]     #RHS of system of equations. Last line represents the sum of n's = 1 equation
    h.append(   [1])
    t=matrix.multi(q,h)
    t=[t[i][j] for i in range(len(t)) for j in range(len(t[0]))] #t came put a column matrix. Needed in roqw form to plot
    t=np.array(t)
    x.append(t)                          #append
    
#-------------------------------------plotting for a 9 system case----------------------------

n=[0 for i in range(9)]
n[8]=[x[i][0] for i in range(len(Ti))]
n[7]=[x[i][1] for i in range(len(Ti))]
n[6]=[x[i][2] for i in range(len(Ti))]
n[5]=[x[i][3] for i in range(len(Ti))]
n[4]=[x[i][4] for i in range(len(Ti))]
n[3]=[x[i][5] for i in range(len(Ti))]
n[2]=[x[i][6] for i in range(len(Ti))]
n[1]=[x[i][7] for i in range(len(Ti))]
n[0]=[x[i][8] for i in range(len(Ti))]
plt.title("Variation of densities with temperature")
plt.xlabel("Temperature in Kelvin")
plt.ylabel("Number densities in g/cm^3")
for i in range(9):
      plt.plot(Ti,n[i],"x",label="N"+str(i+1))
plt.legend(bbox_to_anchor=(1.05, 1),loc='upper center')
plt.savefig("/Users/aj3008/Desktop/MS_3rd_Sem/Comp_methods_in_AST/Comp_methods/Hw_3/Latex/Images/pb2")
        
