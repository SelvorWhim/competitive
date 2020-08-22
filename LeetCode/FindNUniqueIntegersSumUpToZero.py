# idea: use numbers up to n/2 and their negative counterparts to cancel each other out, plus 0 when n is odd
class Solution:
    def sumZero(self, n: int) -> List[int]:
        return [i for i in range(1, n//2 + 1)] + [-i for i in range(1, n//2 + 1)] + ([0] if n%2 == 1 else [])
