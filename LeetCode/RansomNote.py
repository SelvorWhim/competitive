from collections import Counter as c

class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        cr = c(ransomNote)
        cm = c(magazine)
        for l in cr:
            if cr[l] > cm[l]:
                return False
        return True
