"""
note you can remove subsequences, not just substrings
so you can always remove all the a's in one go and then all the b's
so either the string is empty, then the answer is 0
or it's already a palindrome and the answer is 1
or you can remove each letter type, and with 2 letters, the answer is 2
"""

class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if s == s[::-1]:
            return 1
        return 2
