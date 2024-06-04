# idea: for a palindrome with rearrangements, all unique letter counts will be even with one possible exception

from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        longest_len = 0
        has_odd_count = False
        for _, count in Counter(s).items():
            if count % 2 == 0:
                longest_len += count
            else:
                longest_len += count - 1
                has_odd_count = True
        if has_odd_count:
            longest_len += 1
        return longest_len
