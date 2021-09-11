
import math
import os
import random
import re
import sys

#

def subset_sum(values, target):
    def helper(values, target, idx):
        if idx == len(values) and target == 0:
            return 1
        if idx == len(values) and target != 0:
            return 0

        # print(f"{values} :::: {target} ::::: {idx}")
        include = helper(values, target - values[idx],  idx + 1)
        exclude = helper(values, target,  idx + 1)
        return include + exclude 
    #res = helper(values, target,0)

    def helper_table(values, target):
        # first we create a table
        t = []
        for i in range(len(values) + 1):
            t.append([-1]*(target+1))
        # please note to access values we need to subtract the index by one.
        # table index runs faster
        # initial conditions
        for j in range(len(t[0])):
            t[0][j] = 0
        for i in range(len(t)):
            t[i][0] = 1

        targets = range(0,target+1)
        for i in range(1, len(t), 1):
            for j in range(1, len(t[0]), 1):
                # include
                include = 0
                value = values[i-1]
                if targets[j] - value >= 0: #Then only we can include
                    tgt_idx = targets[j] - value
                    include = t[i][tgt_idx]
                # exclude: then target value remains same as above
                exclude = t[i-1][j]
                t[i][j] = include + exclude
        return t[len(t)-1][len(t[0])-1]
        
    res = helper_table(values, target)
    return res

if __name__ == '__main__':
    val = [2,3,5,6,8,10]
    target = 10
    #val = [2,3,5,6,8,10,11,14,6,7,8,9,10,12,76,89,4,5,7,8,9,3,56,7,4,32,76,9]
    #target = 36
    ret = subset_sum(val, target)
    print(f"Res {ret}")
