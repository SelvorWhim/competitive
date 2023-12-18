# no negatives, so we want the product of the 2 biggest numbers minus the product of the 2 smallest
# there's more efficient ways to get those but this is the simplest

class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        return nums[-1] * nums[-2] - nums[0] * nums[1]
