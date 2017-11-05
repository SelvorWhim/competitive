class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        s1 = "{0:b}".format(x)[::-1] # converted into bit strings
        s2 = "{0:b}".format(y)[::-1] # and reversed so their (formerly) rightmost bits match indexes
        count = 0
        if len(s2) > len(s1):
            s1,s2 = s2,s1 # if necessary switch variable names so s1's (bitstring) length is no less than s2's
        for i in range(len(s2)): # indexes iterating shortest bit string
            if s1[i] != s2[i]:
                count += 1
        for i in range(len(s2),len(s1)):
            if s1[i] == '1':
                count += 1
        return count