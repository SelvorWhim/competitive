# sums digits in string, (int(c)) raises error if not all characters are digits
def sum_digits(s):
    return sum(int(c) for c in s)

def luck_check(string):
    # compare sums for first half and last half, excluding middle if length is odd:
    return sum_digits(string[:len(string)//2]) == sum_digits(string[-(len(string)//2):])

# TIL (problem description): someone thought it was a good idea to eat lucky transport tickets
# TIL (debugging): parentheses are important in negative modular division!
