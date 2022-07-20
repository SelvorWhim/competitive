"""
Naive solution counting matches was too slow (O(sum # letters in words)).
Sped it up just enough by preventing recalculation on duplicate words.
"""

from collections import Counter

def is_subsequence(subs, s):
    if len(subs) == 0:
        return True
    if len(subs) > len(s):
        return False
    i = 0 # index within subs we're trying to find in s
    for j in range(len(s)): # index within s
        if subs[i] == s[j]:
            i += 1
            if i >= len(subs):
                return True
    return False

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        c_words = Counter(words)
        return sum(c_words[word] for word in c_words.keys() if is_subsequence(word, s))
