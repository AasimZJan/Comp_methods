
"""
Created on Mon Sep 21 13:55:10 2020

@author: aj3008
"""

#%%
###libraries
import math
import pb3
import matplotlib.pyplot as plt

def f(b,c):
    
    """This function takes two arguments, b= coefficient of y, c= coefficient of g(x,t).
    This function returns an array where the first element gives d(theta)/dt and the second element returns d(omega)/dt"""                                   
    def y(x,y,t):
        return([y,-b*y-c*math.sin(x)])
    return(y)
#defining constants based on the example   
b=0.25
c=5
y_0=0                              #initial angular velocity. The pendulum is vertical so the velocity is zero
x_0=math.pi/2                      #initial angle. The pendulum is horizontal
h=0.1                              #stepsize
k=200
###calling the methods
l,m,j=pb3.euler(x_0,y_0,f(b,c),h,k)
x,y,j=pb3.rk(x_0,y_0,f(b,c),h,k)
q,w,j=pb3.heun(x_0,y_0,f(b,c),h,k)
###plotting
plt.title("Solving the pendulum using different numberical methods")
plt.xlabel("time")
plt.plot(j,l,"o",label="Euler theta")
plt.plot(j,m,"bo",label="Euler Omega")
plt.plot(j,x,"orange",label="RK-4 theta")
plt.plot(j,y,"red",label="RK-4 Omega")
plt.plot(j,q,"kx",label="Heun theta")
plt.plot(j,w,"rx",label="Heun Omega")
plt.savefig("/Users/aj3008/Desktop/MS_3rd_Sem/Comp_methods_in_AST/Comp_methods/Hw_3/Images/pb4_1")
plt.legend()