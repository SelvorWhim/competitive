from collections import Counter
from math import ceil

class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        c = Counter(tasks)
        rounds = 0
        for difficulty, count in c.items():
            if count == 1:
                return -1
            # If the count divides by 3, all rounds will have 3.
            # If it is 2 mod 3, all rounds can have 3 except the last with 2.
            # If it is 1 mod 3, all rounds can have 3 except the last 2 with 2 - this works as long as the count isn't exactly 1.
            rounds += ceil(count / 3)
        return rounds
