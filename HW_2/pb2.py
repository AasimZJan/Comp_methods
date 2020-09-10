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
            return [row[:j] + row[j+1:] for row in (a[:i]+a[i+1:])]
        def det(a):
            if len(a) == 2:
                return a[0][0]*a[1][1]-a[0][1]*a[1][0]

            summ = 0
            for i in range(len(a)):
                summ= summ+((-1)**i)*a[0][i]*det(mm(a,0,i))
            return(summ)
        return(det(a))
    
    def Inv(self):
        m=self.g
        def tran(m):
            n=[]
            for k in range(len(m[0])):
                r=[]
                for i in range(len(m)):
                    r.append(m[i][k])
                n.append(r)
            return(n)
        def mm(a,i,j):
            return [row[:j] + row[j+1:] for row in (a[:i]+a[i+1:])]
        def det(a):
            if len(a) == 2:
                return a[0][0]*a[1][1]-a[0][1]*a[1][0]

            summ = 0
            for i in range(len(a)):
                summ= summ+((-1)**i)*a[0][i]*det(mm(a,0,i))
            return(summ)
        def inv(m):
            determinant = det(m)
            #special case for 2x2 matrix:
            if len(m) == 2:
                return [[m[1][1]/determinant, -1*m[0][1]/determinant],[-1*m[1][0]/determinant, m[0][0]/determinant]]
                        

            #find matrix of cofactors
            cofactors = []
            for r in range(len(m)):
                cofactorRow = []
                for c in range(len(m)):
                    minor = mm(m,r,c)
                    cofactorRow.append(((-1)**(r+c)) * det(minor))
                cofactors.append(cofactorRow)
            cofactors = tran(cofactors)
            for r in range(len(cofactors)):
                for c in range(len(cofactors)):
                    cofactors[r][c] = cofactors[r][c]/determinant
            return cofactors
        return(inv(m))
    def LU(self):
        a=self.g            #now "a"will be the matrix  
        def lu(a):
            n=len(a)
            if len(a) != len(a[0]):
                print("Input a square matrix")
                pass
            #creating two zero matrixes of size n*n
            l= [[0 for x in range(n)] for y in range(n)]
            u= [[0 for x in range(n)] for y in range(n)]
            for k in range(n):
                for i in range(n):
                    if i<k:
                        pass

                    if i==k:
                        l[i][i]=1

                        sum =0
                        for j in range(k):
                            sum=sum+l[k][j]*u[j][k]
                        u[k][i]=a[i][k]-sum
                    
                    if i>k:
                        sum=0
                        for m in range(k):
                            sum=sum+l[i][m]*u[m][k]
                        l[i][k]=(a[i][k]-sum)/u[k][k]
                        sum=0
                        for m in range(k):
                            sum=sum+l[k][m]*u[m][i]
                        u[k][i]=a[k][i]-sum
            return(l,u)
        l,u=lu(a)
        print(l)
        print(u)
            



        
#test
x=[[1,2,3],[2,5,4],[3,15,5]]
m1=matrix(x)
#m1.LU()
#m1.Det()
m1.Inv()
