# another one in the <1ms bucket according to LeetCode

class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        if sentence[0] != sentence[-1]:
            return False
        prev_word = sentence.split()[0]
        for word in sentence.split()[1:]:
            if word[0] != prev_word[-1]:
                return False
            prev_word = word
        return True
