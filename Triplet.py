# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 11:50:54 2017

@author: rmaskus
"""

for a in range (1, 333):
    for b in range(a+1, 500):
        c = 1000 -(a + b)
        
        if (a**2 + b**2) == c**2:
            print("solved", a, b, c)
            print("abc product is:", a * b * c)
            break