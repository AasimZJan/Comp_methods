#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 20:26:34 2020

@author: aj3008
"""


#%%
import numpy as np
import emcee
import math

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
            return(0)
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
    ssnn=[]
    N=len(data)
    for i in range(132,N):
        xi=c+phi*data[i]+phi1*data[i-12]+phi2*data[i-132]+np.random.normal(0,abs(sigma))
        x.append(xi)
        ssnn.append(data[i])
    s=x       #model 
    I=data       #priors(useless)
    sum=0
    for i in range(len(s)):
        sum=sum+math.log(1./(np.sqrt(2*3.14)))-0.5*(I[i+132]-s[i])**2
#    print(stats.chisquare(ssnn,x))
    return(sum)


def lnprob(theta, data):
    lp = lnprior(theta)
    return lp+ lnlike(theta,data)








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
a1=lnlike(theta1,ssn)
AIC1=14+2*a1












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
a2=lnlike(theta2,ssn)
AIC2=12+2*a2













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
a3=lnlike(theta3,ssn)
AIC3=10+2*a3


#%%
print("model 1 and 2 comparison",np.exp((AIC2-AIC1)/AIC2))
print("model 1 and 3 comparison",np.exp((AIC3-AIC1)/AIC3))





