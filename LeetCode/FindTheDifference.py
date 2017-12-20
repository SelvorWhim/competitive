from collections import Counter

class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        cs = Counter(s)
        ct = Counter(t)
        for l in ct:
            if ct[l] > cs[l]: # extra letter will have higher count in t (including 0 count if cs didn't have it)
                return l
        # if input is as described, shouldn't reach here
