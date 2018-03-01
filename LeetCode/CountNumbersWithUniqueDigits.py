from math import factorial

# an unsafe and possibly inefficient implementation in general, but in this usage n,k <= 9 which fits well within integer range, should be fine
def combinationsWithOrder(n,k):
    return factorial(n) // factorial(n-k)

def countNumbersWithKUniqueDigits(k):
    if k > 10 or k < 0:
        return 0
    if k <= 1: # special case because we can have a "leading" zero
        return 9**k # 0 is technically considered part of n=0
    return 9*(combinationsWithOrder(9, k-1)) # 9 because leading digit should not be a 0, then ordered combinations of size k-1 out of 9 remaining digits (all the digits including 0 but not including the leading one)

class Solution:
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        return sum([countNumbersWithKUniqueDigits(i) for i in range(min(n,10) + 1)])
