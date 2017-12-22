class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        mod9 = num % 9
        return (9 if (num != 0 and mod9 == 0) else mod9)
