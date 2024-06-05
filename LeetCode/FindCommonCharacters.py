from collections import Counter

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        counts = Counter(words[0])
        for word in words[1:]:
            counts = counts & Counter(word) # Counter intersection includes duplicates
        return ''.join(count*c for c, count in counts.items())
