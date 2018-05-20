# in a binary string, count the substrings of the form n*0+n*1 and n*1+n*0, including duplicates

from itertools import groupby

# copied from a different solution of mine
def grouped_counter(word):
    return [(l,len(list(group))) for l,group in groupby(word)] # list of tuples, each with character and its count, grouped by consecutive appearances

class Solution:
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        last_group_size = 0
        for i,c in grouped_counter(s):
            res += min(c, last_group_size) # 2 consecutive groups, one of 0's one of 1's (presumably), the minimum size is half the size of the maximum substring of the kind we seek, which also contains a substring like that for each size less by 2
            last_group_size = c
        return res
