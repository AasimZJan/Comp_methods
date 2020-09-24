#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 20:48:22 2020

@author: aj3008
"""

#%%
#---------------------------------importing-------------------------------------------------------

import unittest
import numpy as np
from scipy.linalg import lu
import sys
import pb2                                   #from hw_2 for matrix class

#-----------------------------------testing-------------------------------------------------------


class TestMatrix(unittest.TestCase):
    """My unit_test"""
    def test_add(self):
        """testing addition of matrices"""
        a=[[1,2,33],[54,18,6],[27,8,19]]
        b=[[4,5,6],[8,19,10],[77,66,30]]
        m1=pb2.matrix(a)
        m2=pb2.matrix(b)
        for i in range(len(a)):
            for j in range(len(a[0])):
                self.assertAlmostEqual(m1.add(m2)[i][j],np.add(a,b)[i][j])
    def test_mult(self):
        """testing multiplication of matrices"""
        a=[[1,2,33],[54,18,6],[27,8,19]]
        b=[[4,5,6],[8,19,10],[77,66,30]]
        m1=pb2.matrix(a)
        m2=pb2.matrix(b)
        for i in range(len(a)):
            for j in range(len(a[0])):
                self.assertAlmostEqual(m1.mult(m2)[i][j],np.dot(a,b)[i][j])
    def test_tran(self):
        """testing transpose of matrix class"""
        a=[[1,2,33],[54,18,6],[27,8,19]]
        m1=pb2.matrix(a)
        for i in range(len(a)):
            for j in range(len(a[0])):
                self.assertAlmostEqual(m1.tran()[i][j],np.transpose(a)[i][j])
    def test_trace(self):
        """testing trace of the matrix class"""
        a=[[1,2,33],[54,18,6],[27,8,19]]
        m1=pb2.matrix(a)
        for i in range(len(a)):
            for j in range(len(a[0])):
                self.assertAlmostEqual(m1.trace(),np.trace(a))
    def test_Det(self):
        """tesing Determinant of matrix class """
        a=[[1,2,33],[54,18,6],[27,8,19]]
        m1=pb2.matrix(a)
        for i in range(len(a)):
            for j in range(len(a[0])):
                self.assertAlmostEqual(m1.Det(),np.linalg.det(a))
    def test_Inv(self):
        """tesing Inverse of the matrix class"""
        a=[[1,2,33],[54,18,6],[27,8,19]]
        m1=pb2.matrix(a)
        for i in range(len(a)):
            for j in range(len(a[0])):
                self.assertAlmostEqual(m1.Inv()[i][j],np.linalg.inv(a)[i][j])
    def test_LU(self):
        """testing LU decomp of matrix class"""
        a=[[1,2,33],[54,18,6],[27,8,19]]
        m1=pb2.matrix(a)
        h,q=m1.LU()
        print(h,q)
        m2=pb2.matrix(h)
        m3=pb2.matrix(q)
        for i in range(len(a)):
            for j in range(len(a[0])):
                self.assertAlmostEqual(m2.mult(m3)[i][j],a[i][j])        #the product of LU should be equal to original matric
                if i<j:
                    self.assertAlmostEqual(h[i][j],0)                    #testing if lower triangular matrix
                if j<i:
                    self.assertAlmostEqual(q[i][j],0)                    #testig if upper triangular matrix
if __name__ == '__main__':
    unittest.main()