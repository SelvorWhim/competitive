# gotta have a 1 at the end to make it odd, the rest of the 1's should be as far left as possible to maximize

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        n_ones = s.count('1')
        n_zeroes = len(s) - n_ones  # under assumption
        return (n_ones - 1) * '1' + n_zeroes * '0' + '1'
