# idea: unique sort and use 2 iterators to find all pairs
# except in k=0 case where we can't use unique but need to know how many nums appear more than once

from collections import Counter

class Solution:
    def findPairs0(self, nums: List[int]):
        return sum(1 for count in Counter(nums).values() if count > 1)
    
    def findPairs(self, nums: List[int], k: int) -> int:
        # special case for k=0 - don't want to lose count information, and can be solved more efficiently
        if k == 0:
            return self.findPairs0(nums)
        
        nums = sorted(set(nums)) # sorted unique
        i1, i2 = 0, 1
        pairs_found = 0
        while i2 < len(nums):
            if nums[i1] + k < nums[i2]:
                # gap too wide, narrow it:
                i1 += 1
                # but not too much:
                if i1 == i2:
                    i2 += 1
            elif nums[i1] + k > nums[i2]:
                # gap too narrow, widen it:
                i2 += 1
            else: # nums[i1] + k == nums[i2]:
                pairs_found += 1
                # nums are unique now, so there can't be another k-diff pair without incrementing both iterators
                i1 += 1
                i2 += 1
        return pairs_found
