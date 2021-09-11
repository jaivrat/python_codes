import math

# Russian birth
if __name__ == '__main__':
    list_in = input().rstrip().lstrip().split()
    num = float(list_in[0])
    den = float(list_in[1])
    p_b = num/(num + den)
    p_g =  1.0 - p_b
    res = 0.0
    for i in range(3,6+1):
        res += math.pow(p_b, i) * math.pow(p_g, 6-i) * \
                          math.factorial(6)/( math.factorial(i) * math.factorial(6-i))
    print(round(res, 3))
    