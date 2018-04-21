from collections import Counter
from re import sub

class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        return Counter([p_word for p_word in [re.sub("[^a-zA-Z]+", "", word.lower()) for word in paragraph.split()] if p_word not in banned]).most_common(1)[0][0] # process words, then filter, then count and select most common
