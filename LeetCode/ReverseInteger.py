class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = str(x)
        
        # check for negative and reverse:
        if s[0] == "-":
            rs = "-" + s[1:][::-1] # remove "-" (first char), then reverse
        else:
            rs = s[::-1] # just reverse
        
        # check for overflow (apparently Python stores numbers slightly larger than 2^32 fine (maybe it's long), and reverse of int32 shouldn't be more than 10 times larger than an int32, so this should work fine)
        if abs(int(rs)) > 2147483647: # largest signed int32
            return 0
        else:
            return int(rs)
