# NOTE: this solution failed because I should have used something closer to a simple factorial rather than a combinatorical combination

from math import factorial

# an unsafe and possibly inefficient implementation in general, but in this usage n,k <= 9 which fits well within integer range, should be fine
def nChooseK(n,k):
    return (factorial(n) / factorial(k)) / factorial(n-k)

def countNumbersWithKUniqueDigits(k):
    if k > 10 or k < 1:
        return 0
    if k == 1: # special case because we can have a "leading" zero
        return 1
    return 9*(nChooseK(9, k-1)) # 9 because leading digit should not be a 0, choose k-1 remaining digits out of 9 remaining options (all the digits including 0 but not including the leding one)

class Solution:
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        return sum([countNumbersWithKUniqueDigits(i) for i in range(1,min(n,10)+1)])
