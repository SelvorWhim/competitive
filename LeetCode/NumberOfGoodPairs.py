# don't need to show the pairs, so the order doesn't matter
# just need to find how many times each number appears and count the pairs

from collections import Counter

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counts = Counter(nums)
        return sum(count * (count - 1) // 2 for count in counts.values()) # n*(n-1)/2 = number of pairs in n items
