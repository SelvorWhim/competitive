"""
idea: for a monotone bit string, there has to be a point where the string
switches from all 0's to all 1's, possibly at the edge of the string.
Count how many flips of each type we need at one edge, and adjust as we move
along the string going through every possible such point, since the difference
only depends on the character we just passed.
"""
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        left_1s_to_flip = 0
        right_0s_to_flip = s.count('0')
        min_flips = left_1s_to_flip + right_0s_to_flip
        print(left_1s_to_flip, right_0s_to_flip)
        for c in s:
            if c == '0':
                right_0s_to_flip -= 1
            else:
                left_1s_to_flip += 1
            min_flips = min(min_flips, left_1s_to_flip + right_0s_to_flip)
            print(left_1s_to_flip, right_0s_to_flip)
        return min_flips
