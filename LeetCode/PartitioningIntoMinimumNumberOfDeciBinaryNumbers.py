""" a convoluted way of describing finding the biggest decimal digit :D """

class Solution:
    def minPartitions(self, n: str) -> int:
        return max(int(d) for d in str(n))
