# idea: sort alphabetically and compare the first and last strings pairwise. Whatever they have in common, everything in between them should have in common too, right? Don't know if it's the most efficient method, but it's simple
# complexity: not sure if sorting strings is O(nlogn) - should be nlogn*efficiency of string comparison, which might be proportional to the length of the shorter string.
# optimization: if sort works on a list of strings, so does min/max, and they're linear (or linear proportionally to string comparison). We only need min and max here.

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        s1 = min(strs)
        s2 = max(strs)
        for i in range(min(len(s1), len(s2))):
            if s1[i] != s2[i]:
                return s1[:i]
        return s1 # one is a substring of the other, and the substring comes earlier in lexicographic sort
