from collections import Counter

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        max_frequency = 0
        max_frequency_total = 0
        for _, count in Counter(nums).most_common():
            if count >= max_frequency:
                max_frequency = count
                max_frequency_total += count
            else:
                break
        return max_frequency_total

