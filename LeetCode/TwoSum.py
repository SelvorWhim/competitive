# brute force version
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(0,i):
                if nums[i]+nums[j] == target:
                    return [j,i]
