import math
import os
import random
import re
import sys

#
# Complete the 'quartiles' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def quartiles(arr):
    # Write your code here
    len_arr = len(arr)
    arr = sorted(arr)
    def median(a):
        if len(a)%2 == 0:
            return 0.5 * (a[int(len(a)/2)] + a[int(len(a)/2)-1] )
        else:
            return a[int(len(a)/2)]
    if len_arr%2 ==0:
        # even
        lower = arr[0:int(len_arr/2)]
        upper = arr[int(len_arr/2):len_arr]
    else:
        # odd
        lower = arr[0:int(len_arr/2)]
        upper = arr[(int(len_arr/2)+1):len_arr]
    
    q1 = median(lower)
    q2 = median(arr)
    q3 = median(upper)
    return [int(q1),int(q2),int(q3)]
        

if __name__ == '__main__':
    fptr = open("outopt_test_quartiles.py", 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    res = quartiles(data)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
