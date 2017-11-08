class Solution(object):
    # 344. Reverse String
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]
    
    # 541. Reverse String II
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        (in the description, don't you mean greater than k? Doesn't really matter)
        """
        slices = [s[i:i+k] for i in range(0, len(s), k)] # every other slice, starting with the first, must be reversed
        for i in range(0,len(slices),2):
            slices[i] = slices[i][::-1] # reverse all the even-indexed slices
        return "".join(slices)
    
    # 557. Reverse Words in a String III
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split() # split words by whitespace
        words = [s[::-1] for s in words] # reverse each word
        return " ".join(words)
