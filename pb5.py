#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 11:00:53 2020

@author: aj3008
"""

#%%
#interpolator
def interpolator(x0,y0,x1,y1):
    m=(y1-y0)/(x1-x0)             #calculationg slope since it is linear interpolation 
    def f(x):
        return(m*(x-x0)+y0)
    return(f)
    
    
    
    