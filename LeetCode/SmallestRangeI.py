"""
for each number in the array, add to it any number between -K and K
what's the smallest possible range of values in A after doing this?
well, take the current biggest and smallest values in A:
if we can get them as close as possible to each other
we can get any other number in A within that range too
if they're at most 2K apart, then the difference can be made 0.
If they're more than 2K apart, then the difference is the current difference minus 2K
"""

class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        A_min = min(A)
        A_max = max(A)
        return max((A_max - A_min) - (2*K), 0)
