from collections import Counter

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        if len(arr) == 0:
            return 0
        c = Counter(arr)
        min_set_size = 0
        min_set_count = 0
        for _, count in c.most_common():
            min_set_size += 1
            min_set_count += count
            if min_set_count >= len(arr)/2:
                return min_set_size
        # shouldn't reach here :)
