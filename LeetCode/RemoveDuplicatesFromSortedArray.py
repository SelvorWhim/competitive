class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last = "NaN"
        uniques = 0
        i = 0
        while i < len(nums): # len must be evaluated at every step for this to work
            if nums[i] == last:
                del nums[i]
            else:
                uniques += 1
                last = nums[i]
                i += 1
        return uniques
