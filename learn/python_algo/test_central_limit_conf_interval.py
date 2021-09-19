import math

def cumulative_normal(x, mu, sigma):
    return 0.5 * (1.0 + math.erf((x - mu)/(sigma * math.sqrt(2.0))))

if __name__ == '__main__':
    size = int(input().rstrip().lstrip())
    mu = float(input().rstrip().lstrip())
    sigma = float(input().rstrip().lstrip())
    prob = float(input().rstrip().lstrip())
    z = float(input().rstrip().lstrip())
    
    stat_mean= mu
    stat_sd = math.sqrt(sigma * sigma/size)
    
    #-z< (x-mu)/stat_sd <= z
    B = mu + z * stat_sd
    A = mu - z * stat_sd
    print(round(A,2))
    print(round(B,2))
    