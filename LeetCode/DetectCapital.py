class Solution:
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return ((word == word.upper()) or (len(word) > 0 and word[1:] == word[1:].lower()))
