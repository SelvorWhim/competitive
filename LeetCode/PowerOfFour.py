from re import match

class Solution:
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return bool(re.match("0b1(00)*$", bin(num))) # matches even number of 0s after the first 1
