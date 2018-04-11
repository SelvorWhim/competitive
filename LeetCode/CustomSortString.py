from collections import Counter

class Solution:
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        ct = Counter(T)
        known_order = [c*ct[c] for c in S]
        unknown_order = [c for c in T if c not in S]
        return "".join(known_order + unknown_order)
