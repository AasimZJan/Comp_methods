#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 16:48:21 2020

@author: aj3008
"""

#%%
class matrix:
    '''This is my matrix class. It does almost all matrix stuff.'''            #docstring
    ###initialising
    def __init__(self,a):        
        self.g=a                                                               #a=the matrix in array form
        self.row=len(a)                                                        #number of rows
        self.column=len(a[0])                                                  #number of columns
    ###
    ###Addition
    def add(self,other):
        if self.row==other.row and self.column==other.column:                  #checking if addition exists
            m=[]                                                               #m will be the sum of two matrices
            for j in range(self.row):                                          #loop to get all the rows
                l=[]
                for i in range(self.column):                                   #getting one rows m
                    l.append(self.g[j][i]+other.g[j][i])
                m.append(l)
            print('the sum is',m)
        else:
            print("addition not defined")
    ###
    ###Multiplication
    def mult(self,other):
        if self.column==other.row:                                             #checking if multiplication is possible
            n=[]                                                               #n will be the multiplication of two matrices
            for j in range(self.row):                                          #loop to get all the rows
                m=[]
                for i in range(other.column):                                  #loop to get one row
                    sum=0
                    for k in range(self.column):                               #loop to get one term
                        sum=sum+(self.g[j][k]*other.g[k][i])
                    m.append(sum)
                n.append(m)
            print('The product is',n)
        
        else:
            print("multiplication not defined")
        return(n)
    ###
    ###Transpose
    def tran(self):                                                            #I will make my columns into rows
        n=[]                                                                   #n will be the transposed matrix
        for k in range(self.column):                                           #loop to make columns into rows
            r=[]
            for i in range(self.row):                                          #loop to make a column into a row
                r.append(self.g[i][k])    
            n.append(r)
        print('the transpose is',n)
    ###
    ###Trace of a function
    def trace(self):
        sum=0
        if self.row==self.column:                                              #defining trace if only sqaure matrix
            for i in range(self.row):
                sum = sum+self.g[i][i]
        else:
            print('Trace not defined')
        print('The trace is',sum)
    ###
    ###Determinant
    def Det(self):
        a=self.g
        def mm(a,i,j):
            return [row[:j] + row[j+1:] for row in (a[:i]+a[i+1:])]            #creates the minor matrix
        def det(a):
            if len(a) == 2:
                return a[0][0]*a[1][1]-a[0][1]*a[1][0]

            summ = 0
            for i in range(len(a)):                                            #keeps on going till it becomes a 2*2 matrix and does it till you get the determinant
                summ= summ+((-1)**i)*a[0][i]*det(mm(a,0,i))
            return(summ)
        print('The determinant is',det(a))
    ###
    ###Inverse of a matrix
    def Inv(self):
        m=self.g
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
            print(l)
        a=inv(m)
    ###   
    ###LU decomposition 
    def LU(self):        
        a=self.g                                                               #a will contain the matrix 
        def lu(a):
            n=len(a)
            if len(a) != len(a[0]):                                            #to stop incase a non square matrix is inputted
                print("Input a square matrix")
                pass
            #creating two zero matrixes of size n*n
            l= [[0 for x in range(n)] for y in range(n)]                       #Creating two zero matrices of size n*n (n*n is the size of input matrix)
            u= [[0 for x in range(n)] for y in range(n)]
            for k in range(n):                                                 
                for i in range(n):
                    if i<k:                                                    #too keep the u as upper matrix and l as lower matrix
                        pass

                    if i==k:                                                   #a special case because l[i][i]=1
                        l[i][i]=1

                        sum =0
                        for j in range(k):
                            sum=sum+l[k][j]*u[j][k]
                        u[k][i]=a[i][k]-sum
                    
                    if i>k:                                                    #to find non zero elements fo u and l(and non diagonal too)
                        sum=0
                        for m in range(k):                                     #first find l[i[k]
                            sum=sum+l[i][m]*u[m][k]
                        l[i][k]=(a[i][k]-sum)/u[k][k]
                        sum=0
                        for m in range(k):                                     #use the l[i][k] to find u[i][k]
                            sum=sum+l[k][m]*u[m][i]
                        u[k][i]=a[k][i]-sum
            return(l,u)
        l,u=lu(a)
        print('lower Traingular matrix',l)
        print('upper Triangular matrix',u)        

            



        
#test
o=[[2,3],[5,6]]
m1=matrix(o)
m1.Inv()
m1.LU()
m1.Det()

#test
