#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 00:36:44 2020

@author: aj3008
"""

#%%
import numpy as np
import matplotlib.pyplot as plt
import pb1
import math
Para= pb1.Para
X=pb1.X
Y=pb1.Y
fit=[]
for i in range(len(X)):
    a=Para[0]+Para[1]*X[i][1]+Para[2]*X[i][2]
    fit.append(a)

plt.plot(X[:,1],Y,"x",label="data")
plt.plot(X[:,1],fit,"o",label="fit")
plt.legend()

