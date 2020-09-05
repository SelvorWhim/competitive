# idea: order by size and take largest elements until the sum becomes > sum of remaining
class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums = sorted(nums, reverse=True)
        total_sum = sum(nums)
        running_sum = 0
        subseq_len = 0 # how many biggest members we'll need to take before sum is greater than the rest
        for x in nums:
            running_sum += x
            subseq_len += 1
            if running_sum > (total_sum - running_sum):
                break
        return nums[:subseq_len]

    # in this variant (not relevant for the problem as described) we keep track of original order so subsequence can be returned in original order
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
