class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        ret = ''
        open_levels = 0 # inc for every level of parentheses we've opened, dec for every one closed
        primitive_start = 0 # index where current primitive parentheses string starts
        for i in range(len(S)):
            if S[i] == '(':
                open_levels += 1
            else:
                open_levels -= 1
            if open_levels == 0:
                # add primitive string that just ended not including outermost parentheses
                ret += S[primitive_start + 1 : i]
                primitive_start = i + 1
        return ret
