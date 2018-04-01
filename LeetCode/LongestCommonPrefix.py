# idea: sort alphabetically and compare the first and last strings pairwise. Whatever they have in common, everything in between them should have in common too, right? Don't know if it's the most efficient method, but it's simple
# complexity: not sure if sorting strings is O(nlogn) - should be nlogn*efficiency of string comparison, which might be proportional to the length of the shorter string.

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        if len(strs) == 1: # optimization in case there's one long string in the array
            return strs[0]
        strs = sorted(strs)
        s1 = strs[0]
        s2 = strs[-1]
        for i in range(min(len(s1), len(s2))):
            if s1[i] != s2[i]:
                return s1[:i]
        return s1 if len(s1) < len(s2) else s2
