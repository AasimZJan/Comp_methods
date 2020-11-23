#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 10:34:46 2020

@author: aj3008
"""

#%%
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import emcee
import corner
import math
# Make more readable plots
rc('font',**{'size':14})
rc('xtick',**{'labelsize':16})
rc('ytick',**{'labelsize':16})
rc('axes',**{'labelsize':18,'titlesize':18})

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
            return("a")
        else: 
            return(0.25)
    pass


def lnlike(theta,data):
    '''
    Parameters
    ----------
    I : Intensity (observed)
    q : [Intensity(model), prior(useless as of now)]
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
    # if not np.isfinite(lp):
    #     return -np.inf
    return lnlike(theta,data)


#--------------------------------------plotting data------------------------------------------------------
# Data: decimal year, sunspot number
decyear, ssn = np.loadtxt("SN_m_tot_V2.0.txt", unpack=True, usecols=(2, 3))
plt.plot(decyear, ssn, 'k.')
plt.ylabel('Sunspot Number')
plt.show()

#---------------------------------------MC sampler--------------------------------------------------
# Number of walkers to search through parameter space
nwalkers = 10
# Number of iterations to run the sampler for
niter = 100
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
year=[decyear[i] for i in range(132,N)]
ssnnew=[]
x=[]
xmodel=[]
noise=[]
c,phi,phi1,phi2,sigma=[np.mean(samples[:,0]),np.mean(samples[:,1]),np.mean(samples[:,2]),np.mean(samples[:,3]),np.mean(samples[:,4])]
for i in range(132,N):
    m=c+phi*ssn[i]+phi1*ssn[i-12]+phi2*ssn[i-132]
    n=np.random.normal(0,abs(sigma))
    xmodel.append(m)
    noise.append(n)
    x.append(m+n)
    ssnnew.append(ssn[i])
plt.plot(year,x,"k.")
plt.show()
plt.plot(year,ssnnew,"b.")
plt.show()
plt.figure()
plt.plot(year,noise)
plt.show()
plt.figure()
plt.plot(ssnnew,noise,".")
plt.show()
plt.figure()
plt.plot(year,xmodel,"k.")
plt.show()
plt.figure()
plt.plot(ssnnew,xmodel,".")
plt.show()
#%%---------------------------------------plotting noise and model separately---------------------



fig = corner.corner(samples, bins=50, color='C0', smooth=0.5, plot_datapoints=True, plot_density=True, \
                    plot_contours=True, fill_contour=False, show_titles=True)#, labels=labels)
fig.savefig("corner.png")
plt.show()
#%%
N=len(ssn)
year=[decyear[i] for i in range(132,N)]
j=11
for i in range(N,N+360):
    year.append(2020+j/12)
    j=j+1
for i in range(360):
    a=len(x)
    x.append(c+phi*x[a-1]+phi1*x[a-13]+phi2*x[a-133]+np.random.normal(0,abs(sigma)))
plt.plot(year,x,"k.")
#%%
def freq(time):
	samp_time=np.mean(np.diff(time))
	samp_freq=1/(samp_time*3600*24*30)    #express in seconds
	fre = [i*samp_freq/len(time) for i in range(int(len(time)/2))]
	return(fre)


f=np.fft.fft(xmodel)
Amp=[(np.abs(f[i])) for i in range(int(len(xmodel)/2))]
time1=freq(year)
plt.title("Fourier Transform of strain")
plt.yscale('log')
plt.xscale('log')
plt.xlabel("Freqency in Hertz")
plt.ylabel("Amplitude of Strain")
plt.plot(time1,Amp)

