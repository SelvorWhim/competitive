# idea: we're rotating each digit separately, not the number as a whole. Based on the description and examples, a number is good if all its digits are in the group [0,1,2,5,6,8,9], and at least one of its digits is in the group [2,5,6,9].
# simple approach: iterate over the digits of each number from 1 to N, should be O(NlogN), possibly closer to O(N) because a lot of numbers can be discarded after just a few digits
# there's probably a (faster) closed formula based on combinatorics, but the simple programmatic approach was sufficiently fast for the input guarantee (N<=10^5)

allowed = set(['0','1','2','5','6','8','9'])
required = set(['2','5','6','9'])

class Solution:
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        ret = 0
        for n in range(1,N+1):
            req = False
            for d in str(n):
                if d not in allowed:
                    req = False
                    break
                if not req and d in required:
                    req = True
            if req:
                ret += 1
        return ret
