#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 10:34:46 2020

@author: aj3008
"""

#%%
#-----------------------------------------libraries and font
import numpy as np
import matplotlib.pyplot as plt
import emcee
import corner
import math


#--------------------------------------------Functions----------------------------------------------------------

def lnprior(theta):
    """
    Parameters
    ----------
    theta : np.ndarray
        Array of parameters.

    Returns
    -------
    Value of log-prior.
    """
    for i in range(1,4):
        if theta[i] >1 or theta[i]<-1:
            return(0)
        else: 
            return(0.25)
    pass


def lnlike(theta,data):
    '''
    Parameters
    ----------
    theta : Array of parameters
    data : data
    Returns
    -------
    Log Likelihood of the given model

    '''
    c=theta[0]
    phi=theta[1]
    phi1=theta[2]
    phi2=theta[3]
    sigma=theta[4]
    x=[]
    N=len(data)
    for i in range(132,N):
        xi=c+phi*data[i-1]+phi1*data[i-12]+phi2*data[i-132]+np.random.normal(0,abs(sigma))
        x.append(xi)
    s=x       #model 
    I=data       #priors(useless)
    sum=0
    for i in range(len(s)):
        sum=sum+math.log(1./(np.sqrt(2*3.14)))-0.5*(I[i+132]-s[i])**2
    return(sum)


def lnprob(theta, data):
    lp = lnprior(theta)
    return lp+ lnlike(theta,data)


#--------------------------------------plotting data------------------------------------------------------
# Data: decimal year, sunspot number
decyear, ssn = np.loadtxt("SN_m_tot_V2.0.txt", unpack=True, usecols=(2, 3))
plt.plot(decyear, ssn, 'k.')
plt.xlabel("year")
plt.ylabel('Sunspot Number')
plt.savefig("Images/data")
plt.show()

#---------------------------------------MC sampler--------------------------------------------------
# Number of walkers to search through parameter space
nwalkers = 10
# Number of iterations to run the sampler for
niter = 5000
# Initial guess of parameters
pinit = np.array([1,0.5,0.5,0.5,0.1])
# Number of dimensions of parameter space
ndim = len(pinit)
# Perturbed set of initial guesses. Have your walkers all start out at
# *slightly* different starting values
p0 = [pinit + 1e-4*pinit*np.random.randn(ndim) for i in range(nwalkers)]


#----------------------------------setting up the sampler------------------------------------------------------
# Number of CPU threads to use. 
nthreads = 2
# Set up the sampler
sampler = emcee.EnsembleSampler(nwalkers, ndim, lnprob, args=[ssn], threads=nthreads)
sampler.run_mcmc(p0, niter, progress=True)
# Burn-in value = 1/4th the number of iterations. Feel free to change!
burn = int(0.25*niter)
# Reshape the chains for input to corner.corner()
samples = sampler.chain[:, burn:, :].reshape((-1, ndim))












#%%----------------------------------------plotting the model +noise values---------------------------------



N=len(ssn)
year=[decyear[i] for i in range(132,N)]    #not including first 132 values since they will be used as initial values
ssnnew=[]
x=[]
xmodel=[]
noise=[]
#average of all the parameter values MCMC goes through (excluding the burnt ones)
c,phi,phi1,phi2,sigma=[np.mean(samples[:,0]),np.mean(samples[:,1]),np.mean(samples[:,2]),np.mean(samples[:,3]),np.mean(samples[:,4])]
print("c=",c,"phi=",phi,"phi12=",phi1,"phi132=",phi2,"sigmaz=",sigma)
for i in range(132,N):
    m=c+phi*ssn[i]+phi1*ssn[i-12]+phi2*ssn[i-132]#model
    n=np.random.normal(0,abs(sigma))#noise
    xmodel.append(m)
    noise.append(n)
    x.append(m+n)#AR model
    ssnnew.append(ssn[i])
plt.title("AR and data V/s year")
plt.xlabel("year")
plt.ylabel("Sunspot number")
plt.plot(year,x,"k.",label="AR model")
plt.plot(year,ssnnew,"b.",label="data")
plt.legend()
plt.savefig("Images/AR")
plt.show()

plt.title("noise V/s year")
plt.xlabel("year")
plt.ylabel("noise")
plt.plot(year,noise)
plt.savefig("Images/noise1")
plt.show()
plt.figure()
plt.plot(ssnnew,noise,".")
plt.title("noise V/s data")
plt.xlabel("data")
plt.ylabel("noise")
plt.savefig("Images/noise2")
plt.show()
plt.figure()

plt.title("model V/s year")
plt.xlabel("year")
plt.ylabel("model")
plt.plot(year,xmodel,"k.")
plt.savefig("Images/model1")
plt.show()
plt.figure()
plt.title("model V/s data")
plt.xlabel("data")
plt.ylabel("model")
plt.plot(ssnnew,xmodel,".")
plt.savefig("Images/model2")
plt.show()













#---------------------------------------plotting corner plots---------------------
labels = [r"c",r"$\phi_1$",r"$\phi_{12}$", r"$\phi_{132}$",r"$\sigma_z$"]
fig = corner.corner(samples, bins=50, color='C0', smooth=0.5, plot_datapoints=True, plot_density=True, \
                    plot_contours=True, fill_contour=False, show_titles=True, labels=labels)

fig.savefig("corner.png")
plt.savefig("Images/corner")
plt.show()













#--------------------------------------plotting spectrum earlier method----------------------------------------
def freq(time):
	samp_time=np.mean(np.diff(time))
	samp_freq=1/(samp_time*3600*24*30)    #express in seconds
	fre = [i*samp_freq/len(time) for i in range(int(len(time)/2))]
	return(fre)

f=np.fft.fft(xmodel)
Amp=[(np.abs(f[i])) for i in range(int(len(xmodel)/2))]
time1=freq(year)
plt.title("Fourier Transform of data")
plt.yscale('log')
plt.xscale('log')
plt.xlabel("Freqency in Hertz")
plt.ylabel("Amplitude")
plt.plot(time1,Amp)
plt.savefig("Images/spectrum")
plt.show()

#--------------------------------------------plotting spectrum-----------------------------------------------------
def frequ():
    """
    This gives the frequencies from 10^−10 to 10^2.
    Parameters:none
    Returns:frequency in Hertz.
    """
    j=10**(-10)
    fre=[10**(-10)]
    while j<=100:
        j=1.25*j
        fre.append(j)
    return(fre)
S=[]
fre=frequ()
#finding spectrun
for i in range(len(fre)):
    num=sigma**2
    den=(abs(1-phi*np.exp(-2j*np.pi*1*fre[i])-phi1*np.exp(-2j*np.pi*12*fre[i])-phi2*np.exp(-2j*np.pi*132*fre[i])))**2
    a=num/den
    S.append(a)
plt.title("Power spectrum")
plt.yscale('log')
plt.xscale('log')
plt.xlabel("Freqency in Hertz")
plt.ylabel("Spectrum amplitude")
plt.plot(fre,S)
plt.savefig("Images/spectrum2")
plt.show()










#-----------------------------------predicting to 2050---------------------------------------------------
N=len(ssn)
year=[decyear[i] for i in range(132,N)]
j=11#starting from November 2020
#adding more months till 2050 end
for i in range(N,N+360):
    year.append(2020+j/12)
    j=j+1
for i in range(360):
    a=len(x)
    x.append(c+phi*x[a-1]+phi1*x[a-12]+phi2*x[a-132]+noise[i])
plt.figure()
plt.title("AR 2050 V/s year")
plt.xlabel("year")
plt.ylabel("Sunspot number")
plt.plot(year,x,"k.")
plt.savefig("Images/ARp")
plt.show()
plt.figure()



