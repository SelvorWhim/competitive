# 4 digits, only 24 permutations. Brute force is much more straightforward than tailored code to construct the max time.

from itertools import permutations

def is_valid_time(A):
    return 10*A[0]+A[1] <= 23 and 10*A[2]+A[3] <= 59

def format_time(A):
    return "{}{}:{}{}".format(*A)

class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        return max((format_time(perm_A) for perm_A in permutations(A) if is_valid_time(perm_A)), default="")
