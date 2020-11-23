#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 20:26:34 2020

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

# Data: decimal year, sunspot number
decyear, ssn = np.loadtxt("SN_m_tot_V2.0.txt", unpack=True, usecols=(2, 3))
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
    if len(theta)==5:
        c=theta[0]
        phi=theta[1]
        phi1=theta[2]
        phi2=theta[3]
        sigma=theta[4]
    if len(theta)==4:
        c=theta[0]
        phi=theta[1]
        phi1=theta[2]
        phi2=0
        sigma=theta[3]
    if len(theta)==3:
        c=theta[0]
        phi=theta[1]
        phi1=0
        phi2=0
        sigma=theta[2]
    x=[]
    N=len(data)
    for i in range(132,N):
        xi=c+phi*data[i]+phi1*data[i-12]+phi2*data[i-132]+np.random.normal(0,abs(sigma))
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








#---------------------------------------MODEL 1--------------------------------------------------
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
c,phi,phi1,phi2,sigma=[np.mean(samples[:,0]),np.mean(samples[:,1]),np.mean(samples[:,2]),np.mean(samples[:,3]),np.mean(samples[:,4])]
theta1=[c,phi,phi1,phi2,sigma]
AIC1=10-2*lnlike(theta1,ssn)











#---------------------------------------MODEL 2--------------------------------------------------
# Number of walkers to search through parameter space
nwalkers = 10
# Number of iterations to run the sampler for
niter = 100
# Initial guess of parameters
pinit = np.array([1,0.5,0.5,0.1])
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
c,phi,phi1,sigma=[np.mean(samples[:,0]),np.mean(samples[:,1]),np.mean(samples[:,2]),np.mean(samples[:,3])]
theta2=[c,phi,phi1,sigma]
AIC2=8-2*lnlike(theta2,ssn)












#---------------------------------------MODEL 3--------------------------------------------------
# Number of walkers to search through parameter space
nwalkers = 10
# Number of iterations to run the sampler for
niter = 100
# Initial guess of parameters
pinit = np.array([1,0.5,0.1])
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
c,phi,sigma=[np.mean(samples[:,0]),np.mean(samples[:,1]),np.mean(samples[:,2])]
theta3=[c,phi,sigma]
AIC3=6-2*lnlike(theta3,ssn)




print("model 1 and 2 comparison",AIC1/AIC2)
print("model 1 and 3 comparison",AIC1/AIC3)
print("model 2 and 3 comparison",AIC2/AIC3)




