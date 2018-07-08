# idea: the simple approach is to check the sum, I opted for XOR (with reduce) because it works even if the sum doesn't fit in the largest integer type. Even if the integer representation is unlimited, XOR keeps the numbers no bigger than the maximum, so it should be faster than summation for larger inputs

from functools import reduce
from operator import xor

def oddOrEven(arr):
    return {0:'even', 1:'odd'}[reduce(xor,arr) % 2]
