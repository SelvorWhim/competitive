# not fast enough for large k, despite optimizations worst case is O(n*k)

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ret = [max(nums[:k])] # given: len(nums) >= 1
        curr_max = ret[0]
        for i in range(1, len(nums) - k + 1):
            if nums[i+k-1] > curr_max: # sliding window moved onto something bigger than previous max
                curr_max = nums[i+k-1]
            elif nums[i-1] == curr_max: # sliding window moved away from previous max, need to recalculate
                curr_max = max(nums[i: i+k])
            ret.append(curr_max)
        return ret
