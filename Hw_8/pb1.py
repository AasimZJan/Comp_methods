#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 22:56:54 2020

@author: aj3008
"""

#%%\#%%
#---------------------------------------importing libraries-------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt 

data=np.load("strain.npy")#data each a minute apart
time=np.array([i/(60*24) for i in range(len(data))])#time for each data point 
#-------------------------------------plotting data----------------------------------------------
plt.title("Strain Curve")
plt.xlabel("Time(days)")
plt.ylabel("Strain")
plt.plot(time,data)
plt.savefig("Images/data")
plt.show()



#---------------------------------------defining functions---------------------------------------

#Discrete Fourier Transform
def DFT(x):
    """
    This is the generic fourier transform

    Parameters
    ----------
    x : data(in time space).

    Returns
    -------
    data in frequency space

    """
    N=len(x)
    n=np.arange(N)
    k=n.reshape((N,1))
    M=np.exp(-2j*3.14*k*n/N)
    return(np.dot(M, x))



#Fast Fourier Transform
def FFT(x):
    """
    This is the Fast Fourier Transform based on Cooley Tukey method

    Parameters
    ----------
    x : data (in time space).

    Returns
    -------
    data in frequency space.

    """
    N = len(x)
    if N <= 128:
        return(DFT(x))
    else:
        X_even=FFT(x[::2])
        X_odd=FFT(x[1::2])
        factor=np.exp(-2j*np.pi*np.arange(N)/N)
        return(np.concatenate([X_even + factor[:N // 2] * X_odd, X_even + factor[N // 2:] * X_odd]))


#Calculating frequency    
def freq(time):
	samp_time=np.mean(np.diff(time))
	samp_freq=1/(samp_time*3600*24)    #express in seconds
	fre = [i*samp_freq/len(time) for i in range(int(len(time)/2))]
	return(fre)

#-----------------------------Finding Fourier Transform and calculatind amplitude

f=np.array(FFT(data))
Amp=[(np.abs(f[i])) for i in range(int(len(data)/2))]
time1=freq(time)
plt.title("Fourier Transform of strain")
plt.yscale('log')
plt.xscale('log')
plt.xlabel("Freqency in Hertz")
plt.ylabel("Amplitude of Strain")
plt.plot(time1,Amp)

#-----------------------------------------Find the peak values----------------------------------------------
for i in range(len(Amp)):
    if 10**(-3)<time1[i]<10**(-2) and Amp[i]>10**(-16):    #range found by looking at the graph
        Fre=time1[i]                                       #frequency GW
        h=Amp[i]                                           #h GW
        
plt.plot(Fre,h,"rx",label="peak") 
plt.legend()
plt.savefig("Images/Pb1")                                   #confirming the point is the peak
hz=h*2/len(data)


#------------------------------------------Calculations for M and R----------------------------------------
A=2.6*10**(-21)*12**(-1)
B=10**(-4)
R=(((B**4)*hz)/(A*Fre**4))**(0.2)#relation obtained by eliminating m from the two equations
m=((hz*R)/A)**(0.5)#using R to find M
print("h=",hz,"f_Gw=",Fre,"Hertz")
print("R is",R,"radius of sun")
print("M is",m,"mass of sun")
        
