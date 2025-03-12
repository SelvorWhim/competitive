class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        # according to LeetCode, significantly faster than a straightforward loop to find both at once
        pos_count = sum(1 for num in nums if num > 0)
        neg_count = sum(1 for num in nums if num < 0)
        return max(pos_count, neg_count)
