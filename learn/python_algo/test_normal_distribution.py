import math

def cumulative_normal(mu, sigma, xval):
    return 0.5 * ( 1 + math.erf((xval-mu)/(math.sqrt(2) * sigma)))
    
        
if __name__ == '__main__':
    mean_sd  = input().rstrip().lstrip().split()
    mean = float(mean_sd[0])
    sd = float(mean_sd[1])
    #
    #
    less_than = float(input().rstrip().lstrip())
    between = [float(x) for x in input().rstrip().lstrip().split()]
    x1 = between[0]
    x2 = between[1]
    
    prob_til  = cumulative_normal(mean, sd, less_than)
    prob_bwt  = cumulative_normal(mean, sd, x2) - cumulative_normal(mean, sd, x1)
    print(round(prob_til,3))
    print(round(prob_bwt,3))

    #
    