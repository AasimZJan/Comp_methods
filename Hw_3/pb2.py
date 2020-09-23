#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 21:53:12 2020

@author: aj3008
"""

#%%
import numpy as np
a=np.loadtxt("A_coefficients.dat",delimiter=",",skiprows=0)
l=[[0 for i in range(9)]for j in range(9)]
m=[[0 for i in range(9)]for j in range(8)]
k=0
for i in range(9):
    for j in range(i):
        m[j][i]=a[k][2]
        k=k+1
def a(i,j,m):
    return(m[j][i])
def b(i,j,m):
    c=3*10**10
    h=6.6261*10**(-27)
    v=abs((-13.6*10**15/4.135667696)*((1/(i+1)**2)-(1/(j+1)**2)))
    if i>j:
        return(c**2*a(i,j,m)/(h*2*v**3))
    if i<j:
        return(c**2*a(j,i,m)/(h*2*v**3)*((j+1)/(i+1))**2)
for i in range(9):
    for j in range(9):
        if i==j:
            for k in range(9):
                if i<k:
                    l[i][j]=l[i][j]-b(i,k,m)
                if i>k:
                    l[i][j]=l[i][j]-b(i,k,m)-a(i,k,m)
        if i>j:
            l[i][j]=l[i][j]+b(j,i,m)
        if i<j:
            l[i][j]=l[i][j]+b(j,i,m)+a(j,i,m)


        
