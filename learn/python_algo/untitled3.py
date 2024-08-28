#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 20:14:38 2019

@author: jvsingh
"""

def f(x):
    def g(y, z):
        if(z == 0):
            return y
        return g(x+y+z, z - 1)
    return lambda p,q:g(0,x+p+q)

foo = f(3)
print(foo(100,200))
