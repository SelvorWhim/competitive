"""
idea: to check if words in A are universal relative to B,
we can construct a word (B_max) which has as many instances of each letter in B
as the word in B with the most instances, and check which words in A have B_max as a "subset"
"""

from collections import Counter

class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        A_counters = [Counter(word) for word in A]
        B_max_counter = Counter()
        for word in B:
            word_counter = Counter(word)
            for letter in word_counter:
                B_max_counter[letter] = max(B_max_counter[letter], word_counter[letter])
        ret = []
        for i in range(len(A_counters)):
            word_counter_A = A_counters[i]
            if any(B_max_counter[letter] > word_counter_A[letter] for letter in B_max_counter):
                continue
            ret.append(A[i])
        return ret
