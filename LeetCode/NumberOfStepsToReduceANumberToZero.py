'''
can be implemented more efficiently with bitwise operations, but the idea is
the steps work on a numbers bits from right to left until finish them all (get 0)
when rightmost bit is 0, it is removed (divide even by 2)
when rightmost bit is 1, it is turned into a 0 (subtract 1 from odd)
so when a number is in binary form with leftmost digit being 1,
every 0 bit will add 1 step, and every 1 bit will add 2 steps,
except the leftmost which will add only 1.
#steps = #0 + 2*#1 - 1
'''

class Solution:
    def numberOfSteps (self, num: int) -> int:
        if num == 0:
            return 0
        bin_str = bin(num)[2:]
        n_0 = bin_str.count('0')
        n_1 = bin_str.count('1')
        return n_0 + 2*n_1 - 1
