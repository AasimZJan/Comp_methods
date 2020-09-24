#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 09:53:07 2020

@author: aj3008
"""

#%%
def inv(m):
    n=len(m)
    l= [[0 for x in range(n)] for y in range(n)]                             #creating Identity matrix
    for x in range(n):
        l[x][x]=1  
    for i in range(n):                                                 #starting gaussian elimination(row)                         
        c=m[i][i]      
        for k in range(n):                                             #getting one for [i][i] element which is always the first step one starting a new column
            m[i][k]=float(m[i][k])/c 
            l[i][k]=float(l[i][k])/c                                        
        for j in range(n):                                             #getting zero for [j][i](j!=i) elements
            if j!= i:
                b=m[j][i]
                for q in range(n):
                    m[j][q]=m[j][q]-(b*m[i][q])
                    l[j][q]=l[j][q]-(b*l[i][q])
            
    return(l)
def multi(a,b):
    n=[]                                                               #n will be the multiplication of two matrices
    for j in range(len(a)):                                          #loop to get all the rows
        m=[]
        for i in range(len(b[0])):                                  #loop to get one row
            sum=0
            for k in range(len(a[0])):                               #loop to get one term
                sum=sum+(a[j][k]*b[k][i])
            m.append(sum)
        n.append(m)
    return(n)