# Equivalent to minimum amount of changes to make letter counts equal.
# Find highest common letter count, everything else is a difference, divided by 2 is the number of swaps you need
# Alternatively, count all the letter instances one string has the other doesn't, that should be equivalent

from collections import Counter

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_count = Counter(s)
        t_count = Counter(t)
        swap_count = 0
        for c in s_count.keys():
            count_diff = s_count[c] - t_count[c]
            if count_diff > 0:
                swap_count += count_diff
        return swap_count
