class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        consistent_strings = 0
        for word in words:
            consistent = True
            for c in word:
                if c not in allowed:
                    consistent = False
                    break
            if consistent:
                consistent_strings += 1
        return consistent_strings
