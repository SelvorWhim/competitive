'''
idea: if they keep doing this,
the situation is equivalent
to an infinite queue of the form:
1234511223344551111222233334444555511111111....
I guess there's a closed formula for that
but I'll do this iteratively with powers for now, should be log(n)
'''

def whoIsNext(names, n):
    power = 1
    k = len(names)
    cycle_len = k
    while n > cycle_len:
        n -= cycle_len
        power *= 2
        cycle_len = k * power
    i = (n-1) // power
    return names[i]
