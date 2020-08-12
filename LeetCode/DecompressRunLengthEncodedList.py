class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ret = []
        for i in range(len(nums)//2):
            ret += nums[2*i]*[nums[2*i+1]]
        return ret
