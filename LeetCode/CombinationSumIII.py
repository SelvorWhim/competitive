# maximum number of combinations of 9 digits is for k=4 or k=5, and it's only 126
# so assuming itertools.combinations is implemented efficiently enough, this can be brute-forced

from itertools import combinations

digits = range(1,10)

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        return [combo for combo in combinations(digits, k) if sum(combo) == n]
