class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        map1 = {}
        map2 = {} # reverse
        for i in range(len(s)):
            if s[i] in map1:
                if map1[s[i]] != t[i] or map2[t[i]] != s[i]: # doesn't match previously established mapping
                    return False
            elif t[i] in map2: # attempting to map second letter in s to the same letter in t
                return False
            else:
                map1[s[i]] = t[i]
                map2[t[i]] = s[i]
        return True
