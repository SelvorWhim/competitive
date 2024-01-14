# swaps preserve letter counts, and the 2nd operation swaps letter counts
# so 2 strings are close if they are made of the same set of characters, with the same counts but possibly reordered

from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # for some reason comparing set(word1) and set(word2) isn't working on LeetCode, so comparing counter keys instead
        c1 = Counter(word1)
        c2 = Counter(word2)
        if c1.keys() != c2.keys():
            return False
        sorted_counts1 = sorted(list(c1.values()))
        sorted_counts2 = sorted(list(c2.values()))
        return sorted_counts1 == sorted_counts2
