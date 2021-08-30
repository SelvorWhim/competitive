"""
initialized with 0's and all the additions (of non-empty rectangles) include the top left corner,
so that will necessarily become a max integer, and the question is how big the smallest range
that includes the top left corner is. It might be an intersection of ranges,
e.g. intersection of [2,3] and [3,2] is [2,2]
in the general case, I think it's just the minimum along each axis...
"""

class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if len(ops) == 0:
            return m*n
        return min(op[0] for op in ops) * min(op[1] for op in ops)
