# greedy solution - since each character is part of a contiguous string, go left to right, cutting as soon as the string is balanced.

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balanced_count = 0
        balance = 0 # +1 for R, -1 for L (number line)
        for c in s:
            if c == 'R':
                balance += 1
            else:
                balance -= 1
            if balance == 0:
                balanced_count += 1
        return balanced_count
