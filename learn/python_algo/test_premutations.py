import math
import os
import random
import re
import sys

def solve(n, m):
    # Write your code here
    res = 1.0
    numer = n+m-1
    denom1 = n
    denom2 = m-1
    iters = max(n+m-1,n,m-1)
    for i in range(1,iters+1, 1):
        res = res * (numer if numer >=1 else 1)
        res = res / (denom1 if denom1 >=1 else 1)
        res = res /(denom2 if denom2 >=1 else 1)
        numer = numer - 1
        denom1 = denom1 - 1
        denom2 = denom2 - 1
    # res = (math.factorial(n+m-1)/(math.factorial(n)))/math.factorial(m-1)
    return int(res%int(7 + 1e9))

if __name__ == '__main__':
    #fptr = open("solve_permutation.txt", 'w')
    #t = int(input().strip())
    #for t_itr in range(t):
    #    first_multiple_input = input().rstrip().split()
    #    n = int(first_multiple_input[0])
    #    m = int(first_multiple_input[1])
    #    result = solve(n, m)
    #    fptr.write(str(result) + '\n')
    #fptr.close()
    res  = solve(2, 6)
    print(res)
    
