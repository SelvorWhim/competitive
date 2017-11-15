class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        kmod = k%len(nums) # nums[-0:] == nums, same for indexes out of range, creating duplicates in this case for the otherwise neat solution. Rotation by n leaves array unchanged, hence mod
        if kmod != 0:
            nums[:] = nums[-kmod:] + nums[:len(nums)-kmod] # TIL [:] necessary to change python list in place...
