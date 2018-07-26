# idea: find the LCM for all the rationals to be their common denominator
# (assumption: the original rationals are in reduced form, or at least reduced enough that the lcm is the same for if they were reduced...then this is more efficient. Or I'm lazy)
# then expand the numerators to match

from fractions import gcd
from functools import reduce

def lcm(a,b):
    return abs(a * b) // gcd(a,b)

def convertFracts(lst):
    common_den = reduce(lcm, (rat[1] for rat in lst)) # lcm of all denominators
    print(lst, common_den)
    return [[rat[0] * (common_den//rat[1]), common_den] for rat in lst]
