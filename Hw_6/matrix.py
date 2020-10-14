#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 23:49:03 2020

@author: aj3008
"""

#%%
import numpy as np
def inv(q):
    m=q
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

def tran(a):                                                            #I will make my columns into rows
    n=[]
    c=len(a[0])
    b=len(a)                                                                   #n will be the transposed matrix
    for k in range(c):                                           #loop to make columns into rows
        r=[]
        for i in range(b):                                          #loop to make a column into a row
            r.append(a[i][k])    
        n.append(r)
    return(n)
    ###

def mult(a,b):
    ra=len(a)
    ca=len(a[0])
    rb=len(b)
    cb=len(b[0])
    if ca==rb:                                             #checking if multiplication is possible
        n=[]                                                               #n will be the multiplication of two matrices
        for j in range(ra):                                          #loop to get all the rows
            m=[]
            for i in range(cb):                                  #loop to get one row
                sum=0
                for k in range(ca):                               #loop to get one term
                    sum=sum+(a[j][k]*b[k][i])
                m.append(sum)
            n.append(m)
    
    else:
        print("multiplication not defined")
    return(n)
def add(a,b):
    ra=len(a)
    ca=len(a[0])
    rb=len(b)
    cb=len(b[0])    
    if ra==rb and ca==cb:                  #checking if addition exists
        m=[]                                                               #m will be the sum of two matrices
        for j in range(ra):                                          #loop to get all the rows
            l=[]
            for i in range(ca):                                   #getting one rows m
                l.append(a[j][i]+b[j][i])
            m.append(l)
        print('the sum is',m)
    else:
        print("addition not defined")
    return(m)
    ###
a=[[1,2,4],[6,7,10],[15,17,38]]
b=[[1,24,45],[7,72,14],[17,57,68]]
c=inv(a)
print(c)
print("next")
print(np.add(a,b))
    
    
    
    
    
    
    