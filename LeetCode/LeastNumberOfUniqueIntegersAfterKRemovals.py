# remove going from least common to most common to leave the fewest different

from collections import Counter

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counts = Counter(arr)
        remaining_removals = k
        remaining_unique = len(counts)
        for _, count in counts.most_common()[::-1]:  # from least to most common
            remaining_removals -= count
            if remaining_removals >= 0:
                remaining_unique -= 1
            if remaining_removals <= 0:
                break
        return remaining_unique
