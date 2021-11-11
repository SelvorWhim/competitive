# convoluted description, but seems like you can just calculate the minimum partial sum (left to right), negate and add 1 to that

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        sum_so_far = 0
        min_so_far = 0
        for num in nums:
            sum_so_far += num
            min_so_far = min(min_so_far, sum_so_far)
        return 1 - min_so_far
