from functools import reduce
from operator import mul

def persistence(n):
    return 0 if (n < 10) else (1 + persistence(reduce(mul, [int(d) for d in str(n)])))
