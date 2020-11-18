# pattern seems to be multiplying every pair of digits from different numbers and adding them up

from itertools import product

def test_it(a, b):
    return sum(int(d1)*int(d2) for d1,d2 in product(str(a), str(b)))
