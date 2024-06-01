def scoreOfTwoLetters(c1: str, c2: str):
    return abs(ord(c1) - ord(c2))

class Solution:
    def scoreOfString(self, s: str) -> int:
        return sum(scoreOfTwoLetters(s[i], s[i-1]) for i in range(1, len(s)))
