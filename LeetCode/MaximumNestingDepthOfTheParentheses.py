class Solution:
    def maxDepth(self, s: str) -> int:
        nesting_depth = 0
        max_nesting_depth = 0
        for c in s:
            if c == '(':
                nesting_depth += 1
                max_nesting_depth = max(max_nesting_depth, nesting_depth)
            elif c == ')':
                nesting_depth -= 1
                assert nesting_depth >= 0 # given s represents a VPS
        assert nesting_depth == 0 # given s represents a VPS
        return max_nesting_depth
