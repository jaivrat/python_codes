
import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER n as parameter.
#
# Pascals triangle
def solve(n):
    # Write your code here
    if n == 0:
        return [1]
    
    prev_row = [1]
    curr_row = None
    # start from second row (n =1 or power 1 ie (x+a)^1)
    for i in range(1, n+1, 1):
        # prepend and append 0 to first row
        prev_row.insert(0, 0)
        prev_row.insert(len(prev_row), 0)
        curr_row = [0]*(i+1)
        for j in range(0,len(curr_row)):
            curr_row[j] = prev_row[j] + prev_row[j+1]
        prev_row = curr_row
    # need to return as per question    
    res = [x%(int(1e9)) for x in curr_row]
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = solve(n)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()