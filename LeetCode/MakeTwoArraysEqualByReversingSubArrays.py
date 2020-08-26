"""
don't need to return a sequence or number of steps, just the possibility
with an arbitrary number of steps, we can reorder the array any way we like, like bubble sort
but if the arrays have different multisets of members, they will never be equal because flips don't change the members
so all we need to do is check whether the arrays have the same members in different orders
"""
from collections import Counter
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return Counter(target) == Counter(arr)
        # TODO: add alternative implementations:
        # 1. make one counter and dec it for every member of 2nd array - less space
        # 2. order both arrays for no extra space but higher time complexity
