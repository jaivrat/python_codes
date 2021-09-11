import math

# First success in nth trial.

def first_success_in_nth_trial():
    list_in = input().rstrip().lstrip().split()
    num = int(list_in[0])
    denom = int(list_in[1])
    n = int(input().rstrip().lstrip())
    p = float(num)/denom
    x = 1
    # (n -1)C(x-1) * p^(x-1)  * (1-p)**(n - x) * p(
    prob  = math.pow(1-p,n-1) * p 
    print(round(prob,3))

def first_defect_in_firstfivetrial():
    list_in = input().rstrip().lstrip().split()
    num = int(list_in[0])
    denom = int(list_in[1])
    n = int(input().rstrip().lstrip())
    p = float(num)/denom
    #1 - prob no defect
    prob  = 1 - math.pow(1-p,n) 
    print(round(prob,3))



if __name__ == '__main__':
    # first_success_in_nth_trial()
    first_defect_in_firstfivetrial()
    