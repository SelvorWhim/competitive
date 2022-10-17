# simple solution under assumption sentence only has lowercase English letters
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence)) == 26
