class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        s1 = ''.join(S.split('-')) # remove dashes
        s2 = ''.join([c.upper() for c in s1]) # upper leaves non alphabetic chars as they are
        len1 = len(s2) % K
        l1 = [] if len1 == 0 else [s2[:len1]] # list initialized to first chunk, or nothing if string divides evenly into chunks
        l2 = [s2[len1+i*K:len1+(i+1)*K] for i in range(len(s2)//K)]
        return '-'.join(l1+l2)
