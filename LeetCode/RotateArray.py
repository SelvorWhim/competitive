class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if k != 0: # nums[-0:] == nums, creating duplicates in this case for the otherwise neat solution
            kmod = k%len(nums) # same for indexes out of range. Rotation by n leaves array unchanged, hence mod
            nums[:] = nums[-k:] + nums[:len(nums)-k] # TIL [:] necessary to change python list in place...
        