from collections import Counter

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k > len(s):
            return False
        odds = 0
        even_pairs = 0
        for _, count in Counter(s).items():
            even_pairs += count // 2
            if count % 2 == 1:
                odds += 1
        print(odds, even_pairs)
        if odds > k:
            return False
        return odds + 2*even_pairs >= k
