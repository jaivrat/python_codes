import math
import numpy as np
import random

def MC_solution(trials):
    vars = np.random.random((trials,2))
    return sum(np.apply_along_axis(lambda coeff: coeff[0]*coeff[0] - 4.0*coeff[1] >0, 1, vars))/trials

def analytic_solution(a):
    # x^2 + ax + b where a,b are unif 0-1
    return (1.0/12)

if __name__ == "__main__":
   print(MC_solution(10000000))
   print(1.0/12)
