class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        open_close = {'(':')','[':']','{':'}'}
        stack = []
        for c in s:
            if c in open_close: # in keys, which are opening brackets
                stack.append(c) # push for openers
            elif stack == []: # prevent pop from empty stack (throws)
                return False
            elif open_close[stack.pop()] != c: # pop for closers
                return False
        return (stack == [])
