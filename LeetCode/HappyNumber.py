class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = set()
        curr = n
        while curr not in seen:
            seen ^= {curr}
            digits = [int(c) for c in str(curr)]
            squares = [d*d for d in digits]
            curr = sum(squares)
            if curr == 1:
                return True
        return False
