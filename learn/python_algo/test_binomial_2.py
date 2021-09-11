import math

# Piston problem = number of rejects etc.
if __name__ == '__main__':
    list_in = input().rstrip().lstrip().split()
    reject_pct = int(list_in[0])
    n = int(list_in[1])
    p_reject = reject_pct/100.00

    res = 0.0
    prob_max_2_rejects = 0

    for i in range(0,3):
        prob_max_2_rejects += math.pow(p_reject, i) *\
                              math.pow(1- p_reject, n-i) * \
                              math.factorial(n)/( math.factorial(i)*math.factorial(n-i))

    print(round(prob_max_2_rejects,3))
    # at least two rejects => 1 - max 1 reject
    prob_max_1_rejects = 0
    for i in range(0,2):
        prob_max_1_rejects += math.pow(p_reject, i) *\
                              math.pow(1- p_reject, n-i) * \
                              math.factorial(n)/( math.factorial(i)*math.factorial(n-i))
    

    print(round(1- prob_max_1_rejects,3))