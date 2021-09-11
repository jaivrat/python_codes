#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 18:57:03 2019

@author: jvsingh
"""

def swap(A, i, j):
    tmp = A[i]
    A[i] = A[j]
    A[j] = tmp
    
def InsertionSort(A):
    if(len(A) == 1):
        return(A)
    print(A)
    for i in range(1,len(A)):
        j = i #Sorted till i-1
        while(A[j] < A[j-1] and j >= 1):
            swap(A,j,j-1)
            print(A)
            j = j - 1
    return(A)
        

input = [8, 3, 9, 15, 29, 7, 10]

InsertionSort(input)

print(input)