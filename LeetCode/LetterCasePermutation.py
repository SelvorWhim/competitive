'''
note: also tried a variant where concatenation was to lists of chars
rather than strings (since strings are immutable),
but for some reason it ended up slower
'''

class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        ret = ['']
        for c in S:
            if c.isalpha():
                ret = [perm + c.lower() for perm in ret] + [perm + c.upper() for perm in ret]
            else:
                ret = [perm + c for perm in ret]
        return ret
