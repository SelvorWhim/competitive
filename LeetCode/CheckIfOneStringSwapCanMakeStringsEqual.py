from collections import Counter

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        unequal_char_count = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                unequal_char_count += 1
            if unequal_char_count > 2:
                return False
        return Counter(s1) == Counter(s2)
