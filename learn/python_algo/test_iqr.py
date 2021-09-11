
import math
import os
import random
import re
import sys

#

def interQuartile(values, freqs):
    # Print your answer to 1 decimal place within this function
    data = []
    for i in range(len(values)):
        data.extend([values[i]]*freqs[i])
    data.sort()
    #print(data)
    if len(data)%2==0:
        # even
        first_half = data[0:int(len(data)/2)]
        second_half = data[int(len(data)/2):len(data)]
    else:
        # odd
        first_half = data[0:int(len(data)/2)]
        second_half = data[(1 + int(len(data)/2)):len(data)]
    #print("first_half" + str(first_half))
    #print("second_half" + str(second_half))
    def median(arr):
        if len(arr)%2 == 0:
            return 0.5 *  ( arr[int(len(arr)/2)-1]  +  arr[int(len(arr)/2)])
        else:
            return arr[int(len(arr)/2)]
    q1 = median(first_half)
    q3 = median(second_half) 
    print(float(q3- q1))
         
         

if __name__ == '__main__':
    val = [10, 40, 30, 50, 20]
    freq = [1,2,3,4,5]
    interQuartile(val, freq)
    print("exit..")
