class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # check pattern length matches sentence length:
        s_words = s.split()
        if len(s_words) != len(pattern):
            return False
        
        # check every letter in the pattern is mapped to the same word each time:
        pattern_map = {}
        for i in range(len(pattern)):
            c = pattern[i]
            word = s_words[i]
            if c in pattern_map:
                if pattern_map[c] != word:
                    return False
            else:
                pattern_map[c] = word
        
        # check there aren't 2 pattern letters mapped to the same word:
        return len(set(pattern)) == len(set(s_words))
