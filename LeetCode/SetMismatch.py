class Solution:
    # O(n) time, O(n) space solution using set; based on LeetCode tests/statistics, it's the single fastest Python 3 solution!
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        S_expected = n*(n+1)//2
        S_set = sum(set(nums))
        S_total = sum(nums)
        return [S_total-S_set, S_expected-S_set]
