class Solution:
    # could probably be done in one pass, but O(n) either way and this is simpler
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
        move_to = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                if move_to != i:
                    nums[move_to] = nums[i]
                    nums[i] = 0
                move_to += 1
        return nums
