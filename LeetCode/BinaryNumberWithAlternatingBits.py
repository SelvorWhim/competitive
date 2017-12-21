class Solution:
    # log(n) time, no bitwise operators directly invoked
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s = bin(n)[2:] # appears as e.g. 0b01001 before truncation
        for i in range(1, len(s)):
            if s[i] == s[i-1]: # assuming all chars in this representation are 0's or 1's, which they should be
                return False
        return True
