class Solution:
    def countSubarraysInContiguous(self, n: int):
        # n subarrays of size 1, n-1 of size 2, etc. - sum from 1 to n
        return n*(n+1)//2

    def zeroFilledSubarray(self, nums: List[int]) -> int:
        total_count = 0
        curr_subarray_len = 0
        for x in nums:
            if x == 0:
                curr_subarray_len += 1
            elif curr_subarray_len > 0:
                total_count += self.countSubarraysInContiguous(curr_subarray_len)
                curr_subarray_len = 0
        total_count += self.countSubarraysInContiguous(curr_subarray_len)
        return total_count
