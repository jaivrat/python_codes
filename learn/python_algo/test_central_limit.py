import math

def cumulative_normal(x, mu, sigma):
    return 0.5 * (1.0 + math.erf((x - mu)/(sigma * math.sqrt(2.0))))

if __name__ == '__main__':
    max_weight = float(input().rstrip().lstrip())
    n = int(input().rstrip().lstrip())
    mu = float(input().rstrip().lstrip())
    sigma = float(input().rstrip().lstrip())
    #
    #
    mean_sum = n*mu
    sd_sum = math.sqrt(n*math.pow(sigma,2))
    safe_prob = cumulative_normal(max_weight, mean_sum, sd_sum)
    print(round(safe_prob,4))
