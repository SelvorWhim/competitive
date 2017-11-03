class Solution:
    def get_digit(n, i): # ith digit of integer n (0-indexed)
        return n // 10**i % 10
    
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # if O(n) space was acceptable, easiest way in Python would be using str(x)
        # determine length in digits:
        if x < 0:
            return False
            # by the failed example, apparently negatives are possible, but must return false because the '-' is part of the "string" being evaluated as a palindrome
        xcopy = x # har har
        xlen = 0
        while xcopy > 0:
            xcopy //= 10
            xlen += 1
        for i in range(xlen//2): # checking all but the middle digit, if length is odd
            if Solution.get_digit(x,i) != Solution.get_digit(x,xlen-i-1):
                return False
        return True
