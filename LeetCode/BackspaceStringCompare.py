# idea: input with arbitrary backspaces - could do it with a stack, but then I'd have to messily copy it into something more easily comparable
# instead I initialize an array of the maximum length of an input string (since that's pretty small) and remember up to which point I've written into it, overwriting as necessary. Backspace just moves the index marking valid characters back by 1.

max_len = 200

def typed_result(s):
    temp = ['0']*max_len
    i = 0
    for c in s:
        if c == '#':
            if i > 0: # otherwise backspace on an empty current string - ignored
                i -= 1
        else:
            temp[i] = c
            i += 1
    return "".join(temp[:i])

class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        return typed_result(S) == typed_result(T)
