"""
Array order doesn't matter, just the number of elements of any given value (counter).
We can solve the problem separately for every element value and sum them.
There's no solution when one of the elements appears once, otherwise you can always get the number using 2's and 3's.
Minimum operations will be when you remove 3 as much as possible (without leaving a 1) then remove 2 if necessary.
That works out to just be the number divided by 3 rounded up (unless the number is 1).
"""

from collections import Counter

def minOperationsForOneValue(count: int) -> int:
    """Returns minimum number of 2's and 3's that sum up to the number, or -1 if impossible."""
    if count == 1 or count < 0:
        return -1
    return ceil(count / 3)

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        c = Counter(nums)
        total_operations = 0
        for _, count in c.items():
            operations_for_value = minOperationsForOneValue(count)
            if operations_for_value == -1:
                return -1
            total_operations += operations_for_value
        return total_operations
