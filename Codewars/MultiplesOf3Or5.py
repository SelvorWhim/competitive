# I like this version FizzBuzz better than the standard :P

# sum of first "n" multiples of "d" (limited case of arithmetic series sum)
def sum_of_n_muls(d, n):
    # (2*a1+(n-1)*d)*n/2 = (2*d+(n-1)*d)*n/2 = ((n+1)*d)*n/2
    return (n+1)*d*n/2

# sum of all multiples of "d" below positive integer "number"
def sum_muls_below(d, number):
    return sum_of_n_muls(d, (number-1)//d)

def solution(number):
    return sum_muls_below(3, number) + sum_muls_below(5, number) - sum_muls_below(15, number)
