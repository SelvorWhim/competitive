# idea: keep track of the running sum and calculate averages from that
# all values are positive so Python's regular integer division will truncate to zero as expected (wouldn't work for negatives)

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        ret = [-1] * len(nums)  # efficiently create list of right size and set the edge values
        window_sum = sum(nums[:2*k + 1])
        if len(nums) >= 2*k + 1:
            ret[k] = window_sum // (2*k + 1)
        for i in range(k+1, len(nums) - k):
            window_sum += nums[i+k] - nums[i-k-1]
            ret[i] = window_sum // (2*k + 1)
        return ret
