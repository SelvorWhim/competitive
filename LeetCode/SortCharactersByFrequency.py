from collections import Counter

class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        c = Counter(s)
        l = [] # using list and joining it once instead of directly building string because strings are immutable
        for char, num in c.most_common():
            l += num*[char]
        return "".join(l)
