from heapq import nsmallest
from math import sqrt

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        return nsmallest(K, points, key=lambda p: sqrt(p[0]*p[0]+p[1]*p[1]))
