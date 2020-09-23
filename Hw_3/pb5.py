
"""
Created on Mon Sep 21 13:51:32 2020

@author: aj3008
"""

#%%
import pb3
import math                                #libraries
import matplotlib.pyplot as plt
def f(l):                                #defining the f(t,y(t)) function
    def y(x,y,t):
        return([1,-l*y+l*math.cos(x)])
    return(y)
y_0=10**(-12)                             #(initial values)
x_0=10**(-12)
h=0.1                                      #step size
k=100                                      #number of times
l=10.0                                     #lamda
y_actual=[]
x_actual=[]
for i in range(k):
    m=(l**2)/(1+l**2)
    y_1=-m*math.exp(-l*x_0)+(m/l)*math.sin(x_0)+m*math.cos(x_0)
    y_actual.append(y_1)
    x_actual.append(x_0)
    x_0=x_0+h
y_0=10**(-12)                             #(initial values)
x_0=10**(-12)
h=0.1                                      #step size
k=100                                      #number of times
l=10.0                                     #lamda
x,y,j=pb3.euler(x_0,y_0,f(l),h,k)
xr,yr,j=pb3.rk(x_0,y_0,f(l),h,k)
xh,yh,j=pb3.heun(x_0,y_0,f(l),h,k)
plt.title("Difference between analytical solution and Euler method")
plt.xlabel("t")
plt.ylabel("y(t)")
plt.plot(x_actual,y_actual)
plt.scatter(x,y,color="red")
plt.show()
plt.clf()
plt.title("Difference between analytical solution and RK-4 method")
plt.xlabel("t")
plt.ylabel("y(t)")
plt.plot(x_actual,y_actual)
plt.scatter(xr,yr,color="black")
plt.show()
plt.clf()
plt.title("Difference between analytical solution and Heun's method")
plt.xlabel("t")
plt.ylabel("y(t)")
plt.plot(x_actual,y_actual)
plt.scatter(xh,yh,color="blue")
plt.show()

    