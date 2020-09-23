
"""
Created on Mon Sep 21 13:55:10 2020

@author: aj3008
"""

#%%
import math
import pb3
import matplotlib.pyplot as plt
def f(b,c):                                #defining the f(t,y(t)) function
    def y(x,y,t):
        return([y,-b*y-c*math.sin(x)])
    return(y)
    
b=0.25
c=5
y_0=0                           #(initial values)
x_0=math.pi/2
h=math.pi/200
k=400
l,m,j=pb3.euler(x_0,y_0,f(b,c),h,k)
x,y,j=pb3.rk(x_0,y_0,f(b,c),h,k)
q,w,j=pb3.heun(x_0,y_0,f(b,c),h,k)
plt.plot(j,l,"o")
plt.plot(j,m,"o")
plt.plot(j,x)
plt.plot(j,y)
plt.plot(j,q,"o")
plt.plot(j,w,"o")