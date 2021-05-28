class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left_i = 0
        seen = set()
        curr_sum = 0
        max_sum = 0
        for i in range(len(nums)):
            if nums[i] not in seen: # expand current subarray to the right
                seen.add(nums[i])
                curr_sum += nums[i]
                max_sum = max(max_sum, curr_sum)
            else: # shrink subarray from the left until we find the number causing expansion to right to be non-unique. Since so far everything was unique, there should only be one.
                while nums[left_i] != nums[i]:
                    seen.remove(nums[left_i])
                    curr_sum -= nums[left_i]
                    left_i += 1
                left_i += 1
        return max_sum
