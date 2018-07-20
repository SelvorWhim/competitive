def gps(s, x):
    max_delta = max((x[i] - x[i-1] for i in range(1,len(x))), default=0)
    return ((3600 * max_delta) / s)//1
