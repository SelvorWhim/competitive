# idea: find how many times the number is divisible by 10
# for every increase by 10 in n, it gains one 10 factor, one other 5 factor and several 2 factors, so effectively 2 factors
# since 2 factors always come in first, for any positive integer the answer is simply div 5
# but also past 25 you gain 2 5-factors (and enough 2-factors to make them 10's), etc.
# this is essentially the sum of digits in base 5 (except the 1's digit), but there's no builtin base 5 conversion, and this is simple enough to do manually

def zeros(n):
    sum = 0
    while n > 5:
        sum += n//5
        n = n//5
    return sum
