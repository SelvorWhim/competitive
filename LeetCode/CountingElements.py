from collections import Counter

class Solution:
    def countElements(self, arr: List[int]) -> int:
        c = Counter(arr)
        res = 0
        for n,n_count in c.items():
            if n+1 in c:
                res += n_count
        return res
