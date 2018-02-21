from collections import Counter

class Solution:
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = Counter(nums) # c[n] counts the number of apperances of n
        for n,cn in c.most_common():
            if c[n-1] > 0 and c[n-1] >= c[n+1]:
                return cn + c[n-1]
            if c[n+1] > 0:
                return cn + c[n+1]
        return 0
