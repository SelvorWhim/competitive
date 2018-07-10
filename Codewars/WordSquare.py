'''
idea:
assuming no limitations on the kind of words the square can contain,
just on the "squareness" of it, we have to know
whether the characters can be arranged into a symmetric matrix.
For that to be the case,
the total number of letters must be a perfect square,
and the counts for identical characters
have to be divisible by 2
except on the diagonal
(all except n have to be arrangeable into pairs),
for symmetry to be possible under at least one arrangement.
A set can be used to keep track of this parity for every unique letter.
'''

from math import sqrt, floor

def is_square(nsq):
    return floor(sqrt(nsq))**2 == nsq

def word_square(s):
    nsq = len(s)
    if not is_square(nsq):
        return False
    unpaired = set()
    for c in s:
        if c in unpaired:
            unpaired.remove(c)
        else:
            unpaired.add(c)
    return len(unpaired) <= sqrt(nsq)
