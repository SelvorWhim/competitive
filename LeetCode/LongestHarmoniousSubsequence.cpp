from collections import Counter

class Solution:
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = Counter(nums) # c[n] counts the number of apperances of n
        lhs = 0
        for n in c:
            if c[n+1] > 0:
                lhs = max(lhs, c[n] + c[n+1])
        return lhs
