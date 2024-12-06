# we want as many as possible and can pick each at most once, so just go from small to large, checking against banned
# some optimizations possible, especially more constraints on the banned array, but this is the simplest solution

class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned_set = set(banned)
        curr_sum = 0
        curr_count = 0
        for i in range(1, n+1):
            if i in banned:
                continue
            curr_sum += i
            if curr_sum > maxSum:
                return curr_count
            curr_count += 1
        return curr_count
