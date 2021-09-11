
def mean_median_mode(n, x):
    x = sorted(x)
    mean = sum(x)/n
    median = None
    if n == 1:
        median = x[0]
    elif n%2 == 0:
        median = 0.5 * (x[int(n/2)] + x[int(n/2)-1])
    else:
        median = x[int(n/2)]
    mode = None
    dct = dict([(f, x.count(f)) for f in set(x)])
    max_val = max(dct.values())
    modes = [(k,v) for k,v in dct.items() if v ==  max_val]
    if len(modes) == 1:
        mode = modes[0][0]
    else:
        # sorts inplace
        modes.sort(key = lambda x: x[0])
        mode = modes[0][0]
    return mean, median, mode
    
    

if __name__ == "__main__":
    n = int(input().lstrip().rstrip())
    numbers = [float(i) for i in input().lstrip().rstrip().split()]
    mean, median, mode = mean_median_mode(n,numbers)
    print(mean)
    print(median)
    print(mode)