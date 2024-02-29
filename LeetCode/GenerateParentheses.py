class Solution:

    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []
        self.generateParenthesisUtil(n, n, "")
        return self.res

    def generateParenthesisUtil(self, n: int, openings_left: int, substr_so_far: str) -> List[str]:
        if len(substr_so_far) >= n * 2:
            self.res.append(substr_so_far)
            return
        if openings_left > 0:
            self.generateParenthesisUtil(n, openings_left - 1, substr_so_far + "(")
        openings_done = n - openings_left
        closes_done = len(substr_so_far) - openings_done
        if openings_done > closes_done:
            self.generateParenthesisUtil(n, openings_left, substr_so_far + ")")
