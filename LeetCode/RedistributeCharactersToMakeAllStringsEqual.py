# for this to be possible, we need the total count of each character among all the strings to be divisible by the number of strings

from collections import Counter

class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        c = Counter()
        for word in words:
            c += Counter(word)
        n = len(words)
        for _, count in c.items():
            if count % n != 0:
                return False
        return True
