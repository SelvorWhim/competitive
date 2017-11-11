class Solution:
    # a trivial solution using existing functions...was accepted by the site
    def mySqrt_trivial(self, x):
        """
        :type x: int
        :rtype: int
        """
        from math import sqrt, floor
        return floor(sqrt(x))
    
    # binary search (log(x)) implementation
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= 1: # and is a non-negative integer
            return x
        lower = 0
        upper = x
        mid = 0
        for i in range(x+2): # or log...should return out of this pretty quickly
            mid = lower + ((upper-lower)//2) # mid remains an integer because the condition checks for integer match
            low_sq = mid*mid
            high_sq = (mid+1)*(mid+1)
            if low_sq <= x and high_sq > x:
                return mid
            elif low_sq > x:
                upper = mid
            else:
                lower = mid
