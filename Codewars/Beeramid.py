# given the number of levels, the number of cans needed is the sum of squares up to L, which simplifies to (L^3)/3 + (L^2)/2 + L/6
# this can be inverted, but the result is a complicated formula
# instead I'll do an estimate based on the leading term and go down until it matches

from math import floor

def beeramid(bonus, price):
    max_C = bonus//price
    if max_C <= 0:
        return 0
    L = floor((3 * max_C)**(1/3)) # upper estimate based on leading term
    while (L**3)/3 + (L**2)/2 + L/6 > max_C: # shouldn't take too many iterations, but... possible optimization: test if binary search performs better (search between 1 and upper bound)
        L -= 1
    return L
