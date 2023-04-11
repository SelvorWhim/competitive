# stars act as backspaces. Go through the string left-to-right and build a stack of letters, removing one for every star encountered.
class Solution:
    def removeStars(self, s: str) -> str:
        letterstack = []
        for c in s:
            if c == '*':
                letterstack.pop()
            else:
                letterstack.append(c)
        return ''.join(letterstack)
