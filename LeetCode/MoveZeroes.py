class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        length = len(nums)
        zeros = 0
        while i < length:
            if nums[i] == 0:
                del nums[i]
                zeros += 1
                length -= 1
            else:
                i += 1
        nums += [0]*zeros
