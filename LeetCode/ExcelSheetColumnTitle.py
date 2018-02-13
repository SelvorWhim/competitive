# idea: a variation on conversion to base 26

class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        out = ""
        while n > 0:
            out = chr(ord('A') + (n-1)%26) + out
            n = (n-1)//26
        return out
