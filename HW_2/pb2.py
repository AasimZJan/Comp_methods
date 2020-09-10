#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 16:48:21 2020

@author: aj3008
"""

#%%
class matrix:
    "This is my matrix class"
    def __init__(self,a):
        self.g=a
        self.row=len(a)
        self.column=len(a[0])
    def add(self,other):
        if self.row==other.row and self.column==other.column:
            m=[]
            for j in range(self.row):
                l=[]
                for i in range(self.column):
                    l.append(self.g[j][i]+other.g[j][i])
                m.append(l)
            return(m)
        else:
            print("addition not defined")
    def mult(self,other):
        if self.column==other.row:
            n=[]
            for j in range(self.row):
                m=[]
                for i in range(other.column):
                    sum=0
                    for k in range(self.column):
                        sum=sum+(self.g[j][k]*other.g[k][i])
                    m.append(sum)
                n.append(m)
            return(n)
    def tran(self):
        n=[]
        for k in range(self.column):
            r=[]
            for i in range(self.row):
                r.append(self.g[i][k])
            n.append(r)
        return(n)
    def trace(self):
        sum=0
        if self.row==self.column:
            for i in range(self.row):
                sum = sum+self.g[i][i]
        else:
            print('Trace not defined')
        return(sum)

    def mm(self,i,j):
        return [row[:j] + row[j+1:] for row in (self.g[:i]+self.g[i+1:])]
    
    def Det(self):
        a=self.g
        def mm(a,i,j):
            return [row[:j] + row[j+1:] for row in (self.g[:i]+self.g[i+1:])]
        def det(a):
            if len(a) == 2:
                return a[0][0]*a[1][1]-a[0][1]*a[1][0]

            summ = 0
            for i in range(len(a)):
                summ= summ+((-1)**i)*a[0][i]*det(mm(a,0,i))
            return(summ)
        return(det(a))



        
#test
a=[[1,2,10],[5,3,45]]
m1=matrix(a)
b=[[2,2],[3,3]]
m2=matrix(b)
print(m1.mult(m2))
print(m1.tran())
c=[[1,2,3],[2,3,4],[4,5,6]]
m3=matrix(c)
print(m3.trace())
print(m2.trace())
print(m1.trace())
d=[[1,2,3,4],[2,3,4,5],[3,4,5,6]]
m4=matrix(d)
print(m4.mm(2,2))
print(m1.Det())