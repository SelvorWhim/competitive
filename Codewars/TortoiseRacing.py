# the speeds are given in units per hour, the lead in the same units, and the output must have precison up to seconds

from math import floor

def race(v1, v2, g):
    if v1 >= v2:
        return None
    s_to_catch = floor(3600 * g / (v2-v1)) # based on examples, they're using floor, not ceiling as I expected
    return [s_to_catch//3600, (s_to_catch%3600)//60, s_to_catch%60]
