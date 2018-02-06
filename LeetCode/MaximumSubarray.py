class Solution:
    # returns sum of contiguous non-empty subarray with greatest sum
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sumCurr = 0
        sumMax = -math.inf
        for i in range(len(nums)):
            sumCurr += nums[i]
            if sumCurr > sumMax: # this is checked before negativity in case entire array is negative - in that case the one with the least absolute value will be returned
                sumMax = sumCurr
            if sumCurr < 0:
                sumCurr = 0
        return sumMax
