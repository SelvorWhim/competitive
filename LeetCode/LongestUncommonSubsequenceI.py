# idea: the setup sounds complicated but actually reduces to a trivial problem. If the strings are not identical, the longer of the two strings can't be a subsequence of the other (or either one if they are the same length but not identical), and if they are identical, there is no uncommon subsequence

class Solution:
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        return -1 if (a == b) else max(len(a), len(b))
