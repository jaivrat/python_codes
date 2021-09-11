#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 19:40:31 2019

@author: jvsingh
"""

def square_root(a):
    guess = 2.0 * (a + 0.1) #to make it non zero
    while(1):
        x_next = 0.5 * (guess + a/guess)
        if(abs(x_next - guess) < 1e-16):
            return(guess)
        guess = x_next
    return(-1)
    
    
ans = square_root(-250)
print(ans)