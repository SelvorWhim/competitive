"""
given half of them are even and half are odd and internal order between odd and even indexes doesn't matter,
we can scan odd and even indexes until we find a pair that need to be swapped and swap that.
Under the assumptions everything can be put in place with swaps like that.
"""

class Solution:
    # in-place implementation - original list is modified
    # note: this looks like a double loop, but due to the next_odd_index update it's actually linear
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        next_odd_index = 1
        for i in range(0, len(nums), 2):
            if nums[i] % 2 == 1: # odd number in even index
                for j in range(next_odd_index, len(nums), 2):
                    if nums[j] % 2 == 0: # even number in odd index - swap them
                        temp = nums[i]
                        nums[i] = nums[j]
                        nums[j] = temp
                        next_odd_index = j + 2
                        break
        return nums
