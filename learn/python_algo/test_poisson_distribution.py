import math

if __name__ == '__main__':
    lambda_val  = float(input().rstrip().lstrip())
    k = int(input().rstrip().lstrip())
    prob  = math.exp(-lambda_val) * math.pow(lambda_val, k)/math.factorial(k)
    print(round(prob,3))