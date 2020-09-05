# idea: order by size and take largest elements until the sum becomes > sum of remaining
# but keep track of original order so subsequence can be returned in original order
class Solution:
    def minSubsequenceInOriginalOrder(self, nums: List[int]) -> List[int]:
        total_sum = sum(nums)
        sorted_nums = sorted(enumerate(nums), key=lambda x: x[1], reverse=True) # preserving original order in 1st index
        running_sum = 0
        subseq_len = 0 # how many biggest members we'll need to take before sum is greater than the rest
        for t in sorted_nums:
            running_sum += t[1]
            subseq_len += 1
            if running_sum > (total_sum - running_sum):
                break
        subseq_indexes = sorted([t[0] for t in sorted_nums[:subseq_len]])
        return [nums[i] for i in subseq_indexes]
