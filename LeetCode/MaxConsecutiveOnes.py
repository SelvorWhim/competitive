class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxrun = 0
        currun = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                currun += 1
            else:
                maxrun = max(maxrun, currun)
                currun = 0
        maxrun = max(maxrun, currun)
        return maxrun
