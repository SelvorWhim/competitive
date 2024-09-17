class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        uncommon_words = set()
        common_words = set()
        for word in (s1.split() + s2.split()):
            if word in common_words:
                continue
            elif word in uncommon_words:
                uncommon_words.remove(word)
                common_words.add(word)
            else:
                uncommon_words.add(word)
        return list(uncommon_words)
