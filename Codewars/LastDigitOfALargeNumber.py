# taking advantage of mathematical properties, we can get a constant time (and space) solution that's also fairly simple
# last digits of the power of a single-digit number cycle. Same cycle for any number ending in that digit. Here they all are in base 10:
cycles = {0:[0], 1:[1], 2:[2,4,8,6], 3:[3,9,7,1], 4:[4,6], 5:[5], 6:[6], 7:[7,9,3,1], 8:[8,4,2,6], 9:[9,1]}

def last_digit(n1, n2):
    if n2 == 0:
        return 1
    d1 = n1 % 10
    c1 = cycles[d1]
    return c1[(n2-1) % len(c1)]
